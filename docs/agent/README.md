# External Agent Access

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

- `problems-by-source/all.jsonl`
- `problems-by-source/apmo.jsonl`
- `problems-by-source/baltic.jsonl`
- `problems-by-source/bmo.jsonl`
- `problems-by-source/cmo.jsonl`
- `problems-by-source/egmo.jsonl`
- `problems-by-source/flashlight.jsonl`
- `problems-by-source/fyum.jsonl`
- `problems-by-source/hse.jsonl`
- `problems-by-source/imc.jsonl`
- `problems-by-source/imo.jsonl`
- `problems-by-source/inmo.jsonl`
- `problems-by-source/jbmo.jsonl`
- `problems-by-source/k5.jsonl`
- `problems-by-source/kolmogorov.jsonl`
- `problems-by-source/lktg.jsonl`
- `problems-by-source/memo.jsonl`
- `problems-by-source/miklos.jsonl`
- `problems-by-source/misc.jsonl`
- `problems-by-source/mmo.jsonl`
- `problems-by-source/polish.jsonl`
- `problems-by-source/putnam.jsonl`
- `problems-by-source/rmm.jsonl`
- `problems-by-source/school239.jsonl`
- `problems-by-source/simon.jsonl`
- `problems-by-source/spbmo.jsonl`
- `problems-by-source/sums.jsonl`
- `problems-by-source/tc.jsonl`
- `problems-by-source/usa.jsonl`
- `problems-by-source/usajmo.jsonl`
- `problems-by-source/usamo.jsonl`
- `problems-by-source/vjimc.jsonl`
- `problems-by-source/vosh.jsonl`
- `problems-by-source/yumt.jsonl`
