import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from lib import (
    ROOT,
    collect_text,
    extract_problem_year,
    has_real_solution,
    infer_source_key,
    infer_source_label,
    iter_problem_source_ids,
    load_problems,
    load_relations,
    load_sources,
    problem_author_names,
    problem_search_tokens,
    problem_source_labels,
)


PAGES_BASE_URL = "https://didin-maxim.github.io/knowledge_graph_of_graphs"
RAW_BASE_URL = "https://raw.githubusercontent.com/didin-maxim/knowledge_graph_of_graphs/main"
MAX_STATEMENT_CHARS = 2500
RU_TRANSLIT = str.maketrans(
    {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "е": "e",
        "ё": "e",
        "ж": "zh",
        "з": "z",
        "и": "i",
        "й": "y",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "у": "u",
        "ф": "f",
        "х": "h",
        "ц": "ts",
        "ч": "ch",
        "ш": "sh",
        "щ": "sch",
        "ъ": "",
        "ы": "y",
        "ь": "",
        "э": "e",
        "ю": "yu",
        "я": "ya",
    }
)


def compact_whitespace(value):
    return re.sub(r"\s+", " ", str(value or "")).strip()


def truncate(value, limit):
    text = compact_whitespace(value)
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def transliterate_ru(value):
    return str(value or "").lower().translate(RU_TRANSLIT)


def statement_records(problem):
    result = {}
    for group, statements in (problem.get("statements") or {}).items():
        items = []
        for statement in statements:
            items.append(
                {
                    "id": statement.get("id", ""),
                    "title": statement.get("title", ""),
                    "status": statement.get("status", ""),
                    "text": truncate(statement.get("text", ""), MAX_STATEMENT_CHARS),
                    "definition_ids": statement.get("definition_ids", []),
                }
            )
        if items:
            result[group] = items
    return result


def solution_records(problem):
    items = []
    for solution in problem.get("solutions", []):
        items.append(
            {
                "id": solution.get("id", ""),
                "title": solution.get("title", ""),
                "status": solution.get("status", ""),
                "definition_ids": solution.get("definition_ids", []),
                "standard_idea_ids": solution.get("standard_idea_ids", []),
                "tags": solution.get("tags", []),
                "has_text": bool(str(solution.get("text", "")).strip()),
                "text_preview": truncate(solution.get("text", ""), 900),
            }
        )
    return items


def problem_type(problem):
    kind = problem.get("kind") or {}
    if kind.get("primary"):
        return kind["primary"]
    if "classical_theorem" in problem.get("tags", []):
        return "theorem"
    return "olympiad_problem"


def infer_agent_topics(problem):
    tags = set(problem.get("tags", []))
    profile = problem.get("problem_profile", {})
    title = str(problem.get("title", "")).lower()
    statement_text = collect_text(problem.get("statements", {})).lower()
    profile_methods = [str(item).lower() for item in profile.get("methods", [])]
    profile_goal = [str(item).lower() for item in profile.get("goal", [])]
    profile_keywords = [str(item).lower() for item in profile.get("keywords", [])]
    topics = []
    has_strategy_field = any(
        "strategy" in item or "стратег" in item
        for item in [*profile_methods, *profile_goal, *profile_keywords]
    )
    has_game_text = bool(
        re.search(
            r"\bgame\b|\bplayers?\b|\bигра\b|\bиграют\b|\bигрок|\bходы по очереди\b|\bделая ходы\b",
            f"{title}\n{statement_text}",
        )
    )
    if "goal_strategy_game" in tags or has_strategy_field or has_game_text:
        topics.append("game_strategy" if "goal_strategy_game" in tags else "game_strategy_candidate")
    return topics


def relation_index(relations):
    by_problem = defaultdict(list)
    for relation in relations:
        for direction, source_key, target_key in (
            ("forward", "from", "to"),
            ("backward", "to", "from"),
        ):
            problem_id = relation.get(source_key)
            if not problem_id:
                continue
            by_problem[problem_id].append(
                {
                    "id": relation.get("id", ""),
                    "neighbor_id": relation.get(target_key, ""),
                    "direction": direction,
                    "type": relation.get("type", ""),
                    "distance": relation.get("distance", ""),
                    "status": relation.get("status", ""),
                }
            )
    return by_problem


def make_problem_record(problem, sources, relations_by_problem):
    path = problem.get("_path", "")
    source_key = infer_source_key(problem)
    source_label = infer_source_label(problem)
    source_labels = problem_source_labels(problem, sources)
    classification = problem.get("editorial", {}).get("solution_classification", {})
    statements = statement_records(problem)
    solutions = solution_records(problem)
    search_parts = [
        problem.get("id", ""),
        problem.get("title", ""),
        " ".join(problem.get("tags", [])),
        " ".join(problem_search_tokens(problem)),
        " ".join(problem_author_names(problem)),
        " ".join(source_labels),
        collect_text(statements),
        collect_text(problem.get("ideas", [])),
        collect_text(solutions),
    ]
    search_text = "\n".join(search_parts)
    search_text = "\n".join(
        [
            search_text,
            transliterate_ru(search_text),
        ]
    ).lower()
    return {
        "id": problem.get("id", ""),
        "title": problem.get("title", ""),
        "path": path,
        "raw_github_url": f"{RAW_BASE_URL}/{path.replace('\\', '/')}",
        "viewer_url": f"{PAGES_BASE_URL}/#{problem.get('id', '')}",
        "source_key": source_key,
        "source_label": source_label,
        "source_titles": source_labels,
        "year": extract_problem_year(problem),
        "type": problem_type(problem),
        "authors": problem_author_names(problem, include_unknown=False),
        "tags": problem.get("tags", []),
        "agent_topics": infer_agent_topics(problem),
        "difficulty": problem.get("difficulty", {}),
        "review_status": problem.get("editorial", {}).get("review_status", ""),
        "public_ready": problem.get("editorial", {}).get("public_ready", False),
        "solution_state": "with_solution" if has_real_solution(problem) else "without_solution",
        "solution_classification": classification,
        "statements": statements,
        "solutions": solutions,
        "relations": relations_by_problem.get(problem.get("id", ""), []),
        "search_text": compact_whitespace(search_text),
    }


def source_keys_for_problem(problem, known_source_keys):
    primary = infer_source_key(problem)
    result = [primary]
    candidates = sorted(
        (key for key in known_source_keys if key != "misc"),
        key=len,
        reverse=True,
    )
    for source_id in iter_problem_source_ids(problem):
        normalized = str(source_id).lower().removeprefix("src-")
        for key in candidates:
            if normalized == key or normalized.startswith(f"{key}-"):
                if key not in result:
                    result.append(key)
                break
    return result


def make_compact_record(record):
    compact_text = " ".join(
        [
            record["id"],
            record["title"],
            record["source_key"],
            record["source_label"],
            record["year"],
            " ".join(record["tags"]),
            " ".join(record["authors"]),
        ]
    )
    return {
        "id": record["id"],
        "title": record["title"],
        "path": record["path"],
        "raw_github_url": record["raw_github_url"],
        "viewer_url": record["viewer_url"],
        "source_key": record["source_key"],
        "source_keys": record["source_keys"],
        "source_label": record["source_label"],
        "year": record["year"],
        "tags": record["tags"],
        "agent_topics": record["agent_topics"],
        "solution_state": record["solution_state"],
        "solution_classification_type": record["solution_classification"].get("type", ""),
        "search_text": compact_whitespace(f"{compact_text} {transliterate_ru(compact_text)}".lower()),
    }


def write_json(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path, records):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")


def write_markdown_catalog(path, records):
    lines = [
        "# Problem Catalog for Browser Agents",
        "",
        "This is a lightweight, static catalog generated from `data/problems/`.",
        "Use it for discovery. Use the `raw` link for the source-of-truth card.",
        "",
        "| Source | Year | ID | Title | Solution | Raw |",
        "|---|---:|---|---|---|---|",
    ]
    for record in records:
        title = record["title"].replace("|", "\\|")
        lines.append(
            f"| {record['source_key']} | {record['year']} | `{record['id']}` | "
            f"{title} | {record['solution_state']} | [raw]({record['raw_github_url']}) |"
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_topic_html(path, title, records, description):
    items = "\n".join(
        f"""      <li>
        <a href="{record['raw_github_url']}"><strong>{record['id']}</strong></a>
        <span>{record['title']}</span>
        <code>{record['path']}</code>
      </li>"""
        for record in records
    )
    html = f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
    body {{
      margin: 0;
      font: 16px/1.55 system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: #1f2933;
      background: #f7f7f4;
    }}
    main {{
      max-width: 980px;
      margin: 0 auto;
      padding: 32px 20px 56px;
    }}
    a {{ color: #155e75; }}
    code {{
      display: block;
      margin-top: 4px;
      color: #52606d;
      overflow-wrap: anywhere;
    }}
    li {{ margin: 0 0 14px; }}
    .meta {{ color: #52606d; }}
  </style>
</head>
<body>
  <main>
    <p><a href="../index.html">Agent access</a></p>
    <h1>{title}</h1>
    <p class="meta">{description}</p>
    <p class="meta">Count: {len(records)}. Source of truth: linked raw YAML cards.</p>
    <ol>
{items}
    </ol>
  </main>
</body>
</html>
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")


def write_agent_readme(path, source_keys):
    source_list = "\n".join(f"- `problems-by-source/{key}.jsonl`" for key in source_keys)
    text = f"""# External Agent Access

This directory is a browser-agent friendly entry point to the graph problem database.
It is generated from `data/`; it is not the source of truth.

## Rules for Using the Database as Information

1. Treat `data/**/*.yaml` as the source of truth.
2. Do not rely on GitHub code search for completeness. It can miss Cyrillic text, fresh commits, and large YAML files.
3. Do not use the full viewer as the primary machine interface. `../index.html` is for humans and is a large JavaScript page.
4. Use these lightweight files for discovery, then open the `raw_github_url` of the matching card.
5. Never infer that a task is absent from a failed GitHub search. Check `catalog.json`, `problems.jsonl`, or the source-specific JSONL files.
6. When reporting facts, cite the problem `id` and `path`.
7. Do not mutate data unless explicitly asked. For read-only research, use these generated files and raw YAML only.

## Files

- `catalog.json`: compact metadata, counts, source groups, and entry points.
- `problems-compact.jsonl`: small all-problem manifest for first-pass search.
- `problems.jsonl`: one JSON object per problem card. Best for text search.
- `problems.md`: simple Markdown table for browser reading.
- `problems-by-source/*.jsonl`: smaller source-specific chunks for agents that fail on large files.
  A canonical card with several contest sources appears in every relevant source chunk.
- `topics/game-strategy.html`: browser-readable dump of graph game and strategy tasks.
- `topics/game-strategy.jsonl`: tasks curated with `goal_strategy_game`.
- `topics/game-strategy-candidates.jsonl`: wider text/profile matches to audit for missing tags.

## Recommended Browser-Agent Workflow

1. Fetch `catalog.json`.
2. Fetch `problems-compact.jsonl` and search ids, titles, tags, years, and transliterated text.
3. If the query mentions a source, year, or contest family, fetch the relevant source chunk from `problems-by-source/`.
4. For "games", "strategy", "winning strategy", or similar queries, open `topics/game-strategy.html` or fetch `topics/game-strategy.jsonl`; use `topics/game-strategy-candidates.jsonl` only to audit possible missing tags.
5. Use `problems.jsonl` only when source chunks, topic chunks, and the compact manifest are insufficient.
6. Open the matching record's `raw_github_url`.
7. If relations matter, use the record's `relations` list, then fetch neighbor raw cards.

## Useful Search Terms

Russian and English words are mixed in the database. Try both:

- game: `игра`, `стратегия`, `game`, `strategy`
- tournament: `турнир`, `tournament`
- complete graph: `полный граф`, `complete graph`, `complete_graph`
- matching: `паросочетание`, `matching`
- cut: `разрез`, `cut`, `graph_cut`

## Source Chunks

{source_list}
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_agent_index_html(path, source_keys):
    chunk_links = "\n".join(
        f'<li><a href="problems-by-source/{source_key}.jsonl">{source_key}</a></li>'
        for source_key in source_keys
    )
    html = f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Graph DB Agent Access</title>
  <style>
    body {{
      margin: 0;
      font: 16px/1.55 system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: #1f2933;
      background: #f7f7f4;
    }}
    main {{
      max-width: 920px;
      margin: 0 auto;
      padding: 32px 20px 56px;
    }}
    h1, h2 {{
      line-height: 1.2;
    }}
    code {{
      background: #ecebe5;
      padding: 2px 5px;
      border-radius: 4px;
    }}
    a {{
      color: #155e75;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 12px;
      margin: 18px 0;
    }}
    .link-card {{
      display: block;
      padding: 14px;
      border: 1px solid #d7d4c8;
      border-radius: 6px;
      background: white;
      text-decoration: none;
    }}
    .link-card strong {{
      display: block;
      color: #123;
    }}
    .link-card span {{
      display: block;
      color: #52606d;
      margin-top: 4px;
    }}
    ul.columns {{
      columns: 3 180px;
    }}
  </style>
</head>
<body>
  <main>
    <h1>Graph DB Agent Access</h1>
    <p>
      Lightweight entry point for remote browser agents. This layer is generated from
      <code>data/</code>; source-of-truth records remain the raw YAML files.
      The human viewer is still <a href="../index.html">../index.html</a>.
    </p>

    <div class="grid">
      <a class="link-card" href="catalog.json"><strong>catalog.json</strong><span>Counts, entry points, and source chunks.</span></a>
      <a class="link-card" href="problems-compact.jsonl"><strong>problems-compact.jsonl</strong><span>Small all-problem manifest for first-pass search.</span></a>
      <a class="link-card" href="problems.jsonl"><strong>problems.jsonl</strong><span>All problem cards, one JSON object per line.</span></a>
      <a class="link-card" href="problems.md"><strong>problems.md</strong><span>Plain Markdown catalog for quick browsing.</span></a>
      <a class="link-card" href="README.md"><strong>README.md</strong><span>Rules for using the database as an information source.</span></a>
      <a class="link-card" href="topics/game-strategy.html"><strong>topics/game-strategy.html</strong><span>Browser-readable dump of graph game and strategy tasks.</span></a>
      <a class="link-card" href="topics/game-strategy.jsonl"><strong>topics/game-strategy.jsonl</strong><span>Curated graph game and strategy tasks.</span></a>
      <a class="link-card" href="topics/game-strategy-candidates.jsonl"><strong>topics/game-strategy-candidates.jsonl</strong><span>Wider text/profile matches for missing-tag audits.</span></a>
    </div>

    <h2>Rules</h2>
    <ol>
      <li>Use this directory for discovery; cite the problem <code>id</code> and <code>path</code>.</li>
      <li>Source of truth: open a record's <code>raw_github_url</code> for the authoritative YAML card.</li>
      <li>Do not treat GitHub code search or viewer load failures as evidence that a task is absent.</li>
      <li>Start with <code>problems-compact.jsonl</code>; use source chunks when full files are too large for the browser tool.</li>
      <li>For graph games and strategy tasks, use <code>topics/game-strategy.html</code> for browser reading or <code>topics/game-strategy.jsonl</code> for structured data. Use the candidates file only for an audit, not as the final answer.</li>
    </ol>

    <h2>Source Chunks</h2>
    <ul class="columns">
      {chunk_links}
    </ul>
  </main>
</body>
</html>
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")


def main():
    problems = load_problems()
    sources = load_sources()
    relations = load_relations()
    relations_by_problem = relation_index(relations)
    records = [
        make_problem_record(problem, sources, relations_by_problem)
        for problem in sorted(problems.values(), key=lambda item: item["id"])
    ]
    known_source_keys = {record["source_key"] for record in records}
    for record in records:
        problem = problems[record["id"]]
        record["source_keys"] = source_keys_for_problem(problem, known_source_keys)
    out_dir = ROOT / "docs" / "agent"
    by_source = defaultdict(list)
    for record in records:
        for source_key in record["source_keys"]:
            by_source[source_key].append(record)

    source_keys = sorted(by_source)
    write_jsonl(out_dir / "problems.jsonl", records)
    write_jsonl(out_dir / "problems-compact.jsonl", [make_compact_record(record) for record in records])
    write_markdown_catalog(out_dir / "problems.md", records)
    game_strategy_records = [record for record in records if "game_strategy" in record["agent_topics"]]
    game_strategy_candidates = [
        record for record in records if "game_strategy_candidate" in record["agent_topics"]
    ]
    write_topic_html(
        out_dir / "topics" / "game-strategy.html",
        "Graph Games and Strategy Tasks",
        game_strategy_records,
        "Curated tasks tagged with goal_strategy_game. Use this page as a direct dump for browser agents.",
    )
    write_jsonl(out_dir / "topics" / "game-strategy.jsonl", game_strategy_records)
    write_jsonl(out_dir / "topics" / "game-strategy-candidates.jsonl", game_strategy_candidates)
    for source_key in source_keys:
        write_jsonl(out_dir / "problems-by-source" / f"{source_key}.jsonl", by_source[source_key])

    catalog = {
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "source_of_truth": "data/**/*.yaml",
        "problem_count": len(records),
        "relation_count": len(relations),
        "entrypoints": {
            "all_jsonl": "problems.jsonl",
            "compact_jsonl": "problems-compact.jsonl",
            "markdown_catalog": "problems.md",
            "source_chunks_dir": "problems-by-source/",
            "game_strategy_html": "topics/game-strategy.html",
            "game_strategy_topic": "topics/game-strategy.jsonl",
            "game_strategy_candidates": "topics/game-strategy-candidates.jsonl",
            "human_viewer": "../index.html",
        },
        "rules_file": "README.md",
        "source_chunks": [
            {
                "source_key": source_key,
                "path": f"problems-by-source/{source_key}.jsonl",
                "count": len(by_source[source_key]),
            }
            for source_key in source_keys
        ],
    }
    write_json(out_dir / "catalog.json", catalog)
    write_agent_readme(out_dir / "README.md", source_keys)
    write_agent_index_html(out_dir / "index.html", source_keys)
    print(f"Built {out_dir}")
    print(f"Problems: {len(records)}; sources: {len(source_keys)}")


if __name__ == "__main__":
    main()
