import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CORE_TEXT_SUFFIXES = {".json", ".md", ".py", ".yaml", ".html"}
CORE_DIRS = ["docs", "tools", "schemas"]
UNCERTAIN_STATUSES = {"ai_draft", "needs_review", "needs_human_review", "disputed"}
PLACEHOLDER_SOLUTION_RE = re.compile(r"^\s*решение пока не найдено[.!]?\s*$", re.IGNORECASE)
SOLUTION_RED_FLAGS = [
    ("outline/sketch title", re.compile(r"\b(outline|sketch|plan|summary|compressed)\b", re.IGNORECASE)),
    ("draft Russian marker", re.compile(r"\b(набросок|план|пересказ|сжатый пересказ)\b", re.IGNORECASE)),
    ("external-solution narration", re.compile(r"(официальн\w*\s+решени\w*|автор\w*\s+решени\w*)", re.IGNORECASE)),
    ("handwave marker", re.compile(r"\b(стандартно|легко видеть)\b", re.IGNORECASE)),
    (
        "medium-reasoning incomprehensible marker",
        re.compile(
            r"(требует доработки|нужно доработать|непонятн|неясн|не удалось понять|"
            r"переход не проверен|не довед[её]н|недовед|needs work|unclear)",
            re.IGNORECASE,
        ),
    ),
]
WEAK_RELATION_TEXT_RE = re.compile(
    r"(общ(ая|ей)\s+(метаинформация|тема|цель)|"
    r"общ(ий|им)\s+(мотив|объект|фон)|"
    r"перевод\w*\s+социальн\w*\s+формулировк\w*|"
    r"социально-графов\w*|"
    r"социальн\w*\s+граф|"
    r"social\s+graph|"
    r"story\s+wrapper|"
    r"graph\s+model|"
    r"ВсОШ/российск\w*\s+традиц\w*|"
    r"олимпиадн\w*\s+традиц\w*|"
    r"того\s+же\s+социально-графов\w*\s+язык\w*|"
    r"сюжет\w*\s+о\s+знакомств\w*|"
    r"знакомств\w*/дружб\w*|"
    r"тот\s+же\s+сюжет|"
    r"продолжа\w*\s+тот\s+же\s+сюжет|"
    r"прям\w*\s+усилен\w*\s+сюжет|"
    r"сюжетн\w*\s+оболоч|"
    r"словесн\w*\s+оболоч|"
    r"контекстн\w*\s+связ|"
    r"официальн\w*\s+комментар|"
    r"общ\w*\s+техник\w*\s+моделирован|"
    r"относят\w*\s+к\s+.*олимпиад|"
    r"одн(ого|ой)\s+(блока|олимпиад[ыа]|источник\w*)|"
    r"той\s+же\s+олимпиад[ыа]|"
    r"отмечен[аы]?\s+(тегами|метаданными)|"
    r"помеча[ею]т.*(тег|метаданн)|"
    r"не\s+является\s+прям|не\s+прям(ое|ым)|"
    r"ближайш(ая|ий)\s+классическ|"
    r"естественн(ый|ым)\s+сосед|"
    r"стандартн(ый|ым)\s+эталон|"
    r"классическ(ий|им)\s+ориентир|"
    r"полезн(ая|ый)\s+(карта|сосед)|"
    r"полезно\s+(держать\s+рядом|сравнивать)|"
    r"хорошо\s+рифмуется|"
    r"друг(ой|им)\s+способ\w*\s+графизировать|"
    r"клеточн\w*\s+сюжет\w*|"
    r"объект\s+один\s+и\s+тот\s+же,\s+но|"
    r"графическ\w*\s+инструмент\w*\s+.*совсем\s+друг|"
    r"находится\s+.*территории|"
    r"уровн(е|ем)\s+мотива|"
    r"goal_(exact_)?bound|goal_bound|"
    r"extremal_graph_theory)",
    re.IGNORECASE,
)
PUBLIC_TEXT_KEYS = {"title", "text", "comment", "notes", "basis", "label", "review_notes", "preference_note"}
NON_PUBLIC_TEXT_BRANCHES = {
    "problem_profile",
    "tags",
    "sources",
    "relations",
    "definition_ids",
    "idea_ids",
    "standard_idea_ids",
}
CYRILLIC_RE = re.compile(r"[А-Яа-яЁё]")
ENGLISH_WORD_RE = re.compile(r"\b[A-Za-z]{4,}\b")
URL_OR_PATH_RE = re.compile(r"https?://\S+|[A-Za-z]:[\\/]\S+|%TEMP%[\\/]\S+|audit/[A-Za-z0-9_./-]+")
CODE_SPAN_RE = re.compile(r"`[^`\n]+`")
TEX_MATH_RE = re.compile(r"\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)|\$\$[\s\S]*?\$\$")
TEX_COMMAND_RE = re.compile(r"\\[A-Za-z]+")
MOJIBAKE_RE = (
    r"(?:Рџ|Рќ|РЅ|Рµ|Рё|Рѕ|Р°|Р±|РІ|Рі|Рґ|Р¶|Р·|Р№|Рє|Р»|Рј|Рї|РС|"
    r"СЃ|С‚|СЂ|СЊ|С‹|СЋ|СЏ){3,}"
)
BROKEN_ENCODING_RE = re.compile(r"\?{4,}|\ufffd|" + MOJIBAKE_RE)
ENGLISH_TAIL_RE = re.compile(
    r"\b("
    r"Answer|Construction|Sharpness|Clarification|Complete|Official source present|"
    r"Medium audit|High-reasoning repair|Very-high|public solution|downclassed|"
    r"solution is identified|archive-derived|not downgraded|The agent"
    r")\b",
    re.IGNORECASE,
)
GRAPH_TERMS_RE = re.compile(
    r"(граф|орграф|гиперграф|вершин|реб[её]р|ребро|ребра|смежн|инцидент|"
    r"клик|цикл|путь|дерев|степен|паросочет|сочетан|двудол|связн|компонент|"
    r"гамильтон|эйлер|турнир|ориентац|раскраск[аи]?\s+р[её]бер|разрез)",
    re.IGNORECASE,
)
GRAPH_STORY_RE = re.compile(
    r"(игрок|клет|реш[её]тк|доск|строк|столб|диагон|город|люд|человек|знаком|"
    r"команд|шахмат|ферз|ладь|домино|лягуш|остров|мост|дорог|авиал|метро|"
    r"комнат|провод|ламп|монет|карточ|таблиц|многоугольник|точк|отрез)",
    re.IGNORECASE,
)
GENERIC_GRAPH_TITLE_RE = re.compile(r"^\s*(графовая\s+формулировка|на\s+языке\s+графов)\s*$", re.IGNORECASE)
WORD_RE = re.compile(r"[A-Za-zА-Яа-яЁё0-9]+")
SIMILARITY_STOP_WORDS = {
    "если",
    "или",
    "для",
    "при",
    "что",
    "это",
    "как",
    "так",
    "все",
    "всех",
    "каждый",
    "каждая",
    "каждое",
    "докажите",
    "найдите",
    "может",
    "можно",
    "существует",
    "имеет",
    "имеются",
    "который",
    "которая",
    "которое",
    "которые",
}


def rel(path):
    return str(path.relative_to(ROOT))


def add(report, severity, category, path, message):
    report.append(
        {
            "severity": severity,
            "category": category,
            "path": path,
            "message": message,
        }
    )


def load_json_file(path, report):
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        add(report, "error", "encoding", rel(path), "UTF-8 BOM is not allowed")
        raw = raw[3:]
    try:
        return json.loads(raw.decode("utf-8"))
    except UnicodeDecodeError as exc:
        add(report, "error", "encoding", rel(path), f"not valid UTF-8: {exc}")
    except json.JSONDecodeError as exc:
        hint = ""
        if "Invalid \\escape" in str(exc):
            hint = "; check LaTeX backslashes, use \\\\( ... \\\\) and \\\\le, not \\( ... \\) or \\le"
        add(report, "error", "json", rel(path), f"{exc}{hint}")
    return None


def scrub_for_language_check(text):
    scrubbed = URL_OR_PATH_RE.sub("", text)
    scrubbed = CODE_SPAN_RE.sub("", scrubbed)
    scrubbed = TEX_MATH_RE.sub("", scrubbed)
    scrubbed = TEX_COMMAND_RE.sub("", scrubbed)
    return scrubbed


def is_public_text_path(path_parts):
    if any(part in NON_PUBLIC_TEXT_BRANCHES for part in path_parts):
        return False
    return any(part in PUBLIC_TEXT_KEYS for part in path_parts)


def iter_public_texts(value, path_parts=()):
    if isinstance(value, dict):
        for key, child in value.items():
            yield from iter_public_texts(child, path_parts + (str(key),))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from iter_public_texts(child, path_parts + (str(index),))
    elif isinstance(value, str) and is_public_text_path(path_parts):
        yield path_parts, value


def check_language_policy(problem, path, report):
    if problem.get("language") != "ru":
        return
    for path_parts, text in iter_public_texts(problem):
        if BROKEN_ENCODING_RE.search(text):
            add(
                report,
                "error",
                "broken_encoding",
                rel(path),
                f"Russian card has broken encoding marker at {'.'.join(path_parts)}",
            )
        scrubbed = scrub_for_language_check(text)
        english_words = ENGLISH_WORD_RE.findall(scrubbed)
        cyrillic_chars = CYRILLIC_RE.findall(scrubbed)
        if (len(english_words) >= 6 and len(english_words) > len(cyrillic_chars) / 4) or ENGLISH_TAIL_RE.search(scrubbed):
            add(
                report,
                "error",
                "language_policy",
                rel(path),
                f"Russian card has English-heavy public text at {'.'.join(path_parts)}",
            )


def text_words(text):
    scrubbed = scrub_for_language_check(text).lower().replace("ё", "е")
    words = {word for word in WORD_RE.findall(scrubbed) if len(word) >= 4}
    return words - SIMILARITY_STOP_WORDS


def text_similarity(left, right):
    left_words = text_words(left)
    right_words = text_words(right)
    if not left_words or not right_words:
        return 0.0
    return len(left_words & right_words) / len(left_words | right_words)


def check_graph_theory_quality(problem, path, report):
    statements = problem.get("statements") or {}
    graph_statements = statements.get("graph_theory") or []
    if not graph_statements:
        return
    originals = statements.get("original") or []
    original_texts = [statement.get("text", "") for statement in originals if isinstance(statement, dict)]
    for index, statement in enumerate(graph_statements):
        statement_id = statement.get("id", f"#{index}")
        title = str(statement.get("title", ""))
        text = str(statement.get("text", ""))
        graph_terms = GRAPH_TERMS_RE.findall(text)
        story_terms = GRAPH_STORY_RE.findall(text)
        where = f"graph_theory/{statement_id}"
        if not title.strip():
            add(report, "warning", "graph_theory_quality", rel(path), f"{where} has no title")
        elif GENERIC_GRAPH_TITLE_RE.match(title):
            add(report, "warning", "graph_theory_quality", rel(path), f"{where} has a generic title")
        if not graph_terms:
            add(
                report,
                "warning",
                "graph_theory_quality",
                rel(path),
                f"{where} has no obvious graph-theory vocabulary; check whether it is only a restatement",
            )
        elif len(story_terms) >= 3 and len(story_terms) > len(graph_terms):
            add(
                report,
                "warning",
                "graph_theory_quality",
                rel(path),
                f"{where} still has heavy story vocabulary; check whether graph language really simplifies the statement",
            )
        for original_text in original_texts:
            if len(text) >= 0.85 * len(original_text) and text_similarity(text, original_text) >= 0.72:
                add(
                    report,
                    "warning",
                    "graph_theory_quality",
                    rel(path),
                    f"{where} is close in length and wording to original; prefer removing cosmetic graph restatements",
                )
                break


def check_graph_model_tags(problem, path, report):
    tags = set(problem.get("tags") or [])
    secondary = set((problem.get("kind") or {}).get("secondary") or [])
    statements = problem.get("statements") or {}
    editorial = problem.get("editorial") or {}
    has_graph_statement = bool(statements.get("graph_theory") or statements.get("graph_hint_reformulations"))
    has_absent_reason = bool(editorial.get("graph_theory_absent_reason"))

    if "graph_in_solution" in tags:
        if "graph_in_solution" not in secondary:
            add(
                report,
                "warning",
                "graph_model_tag_consistency",
                rel(path),
                "graph_in_solution tag should be mirrored in kind.secondary",
            )
        if "graph_model" in tags:
            add(
                report,
                "warning",
                "graph_model_tag_consistency",
                rel(path),
                "use either graph_model or graph_in_solution as the top-level model tag, not both",
            )
        if has_graph_statement:
            add(
                report,
                "warning",
                "graph_model_tag_consistency",
                rel(path),
                "graph_in_solution tag is for cards without an independent graph statement",
            )

    if "graph_model" in tags and "graph_in_solution" in secondary and not has_graph_statement and has_absent_reason:
        add(
            report,
            "warning",
            "graph_model_tag_consistency",
            rel(path),
            "graph appears only in the solution; prefer graph_in_solution over graph_model",
        )

    if (
        "graph_model" in tags
        and "graph_in_statement" in secondary
        and editorial.get("graph_theory_duplicate_removed")
        and not has_graph_statement
        and not has_absent_reason
    ):
        add(
            report,
            "warning",
            "graph_model_tag_consistency",
            rel(path),
            "direct graph statement with duplicate graph_theory removed should not keep graph_model only as a topic duplicate",
        )


def iter_problem_files():
    return sorted((DATA / "problems").rglob("*.yaml"))


def iter_relation_files():
    paths = [DATA / "relations" / "relations.yaml"]
    split_dir = DATA / "relations" / "relations.d"
    if split_dir.exists():
        paths.extend(sorted(split_dir.glob("*.yaml")))
    return [path for path in paths if path.exists()]


def check_core_bom(report):
    for dirname in CORE_DIRS:
        root = ROOT / dirname
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            if not path.is_file() or path.suffix.lower() not in CORE_TEXT_SUFFIXES:
                continue
            if path.read_bytes()[:3] == b"\xef\xbb\xbf":
                add(report, "error", "encoding", rel(path), "UTF-8 BOM is not allowed")


def check_problem(problem, path, report):
    check_language_policy(problem, path, report)
    check_graph_theory_quality(problem, path, report)
    check_graph_model_tags(problem, path, report)

    editorial = problem.get("editorial", {})
    solution_classification = editorial.get("solution_classification") or {}
    classification_type = solution_classification.get("type")
    classification_blob = "\n".join(
        str(solution_classification.get(key, ""))
        for key in ["label", "status", "basis", "notes", "audit_source"]
    ).lower()

    if classification_type == "no_solution_hard":
        if problem.get("solutions") or problem.get("ideas"):
            add(
                report,
                "warning",
                "solution_classification",
                rel(path),
                "no_solution_hard must have empty solutions[] and ideas[] after cleanup",
            )
        if not re.search(r"very high|xhigh|очень высок|особо слож|длительн", classification_blob):
            add(
                report,
                "warning",
                "solution_classification",
                rel(path),
                "no_solution_hard must cite the special very-high-reasoning no-solution procedure",
            )

    if classification_type == "official_plan_completed_by_ai":
        if not problem.get("solutions"):
            add(
                report,
                "warning",
                "solution_classification",
                rel(path),
                "official_plan_completed_by_ai requires a completed local solution",
            )
        if not re.search(r"high|высок|довед|completed|провер", classification_blob):
            add(
                report,
                "warning",
                "solution_classification",
                rel(path),
                "official_plan_completed_by_ai must say that a high-reasoning agent completed and checked the official plan",
            )

    if editorial.get("public_ready") is True:
        problems = []
        if editorial.get("review_status") in UNCERTAIN_STATUSES:
            problems.append(f"editorial.review_status={editorial.get('review_status')}")
        for section, statements in problem.get("statements", {}).items():
            for statement in statements:
                statement_id = statement.get("id", "<missing>")
                if statement.get("status") in UNCERTAIN_STATUSES:
                    problems.append(f"{section}/{statement_id}.status={statement.get('status')}")
                self_contained = statement.get("self_contained") or {}
                if self_contained.get("status") in UNCERTAIN_STATUSES:
                    problems.append(f"{section}/{statement_id}.self_contained={self_contained.get('status')}")
        for solution in problem.get("solutions", []):
            if solution.get("status") in UNCERTAIN_STATUSES:
                problems.append(f"solution/{solution.get('id', '<missing>')}.status={solution.get('status')}")
        if problems:
            add(
                report,
                "warning",
                "public_ready",
                rel(path),
                "public_ready=true but local review status is uncertain: " + "; ".join(problems[:6]),
            )

    for solution in problem.get("solutions", []):
        solution_id = solution.get("id", "<missing>")
        text = solution.get("text", "")
        title = solution.get("title", "")
        notes = str(solution.get("review_notes", ""))
        if PLACEHOLDER_SOLUTION_RE.match(text):
            add(
                report,
                "warning",
                "placeholder_solution",
                rel(path),
                f"solution {solution_id} is a placeholder; prefer solutions: [] for new imports",
            )
        if solution.get("status") == "ai_checked":
            haystack = f"{title}\n{text}"
            for label, pattern in SOLUTION_RED_FLAGS:
                if pattern.search(haystack):
                    add(
                        report,
                        "warning",
                        "solution_red_flag",
                        rel(path),
                        f"solution {solution_id} is ai_checked but matches {label}",
                    )
                    break
        if BROKEN_ENCODING_RE.search(notes):
            add(
                report,
                "error",
                "broken_encoding",
                rel(path),
                f"solution {solution_id} review_notes appears to contain replacement question marks",
            )
        for example in solution.get("examples", []):
            if isinstance(example, dict) and example.get("type") == "image":
                asset_path = example.get("path")
                if not asset_path:
                    add(report, "error", "asset", rel(path), f"solution {solution_id} image example has empty path")
                    continue
                if not (DATA / asset_path).exists():
                    add(
                        report,
                        "error",
                        "asset",
                        rel(path),
                        f"solution {solution_id} image asset does not exist: {asset_path}",
                    )


def check_relation(relation, path, report):
    relation_type = relation.get("type")
    status = relation.get("status")
    confidence = relation.get("confidence")
    relation_text = f"{relation.get('forward_text', '')}\n{relation.get('backward_text', '')}"
    same_source_allowed = re.search(
        r"(то\s+же\s+официальн\w*\s+услови\w*|фактическ\w*\s+дубл\w*|"
        r"перепечат|родительск\w*\s+карточк\w*|дочерн\w*\s+карточк\w*|"
        r"выделя\w*\s+(случай|часть|утверждение|конструкцию)|составн\w*\s+родительск\w*)",
        relation_text,
        re.IGNORECASE,
    )
    if relation_type == "same_source" and not same_source_allowed:
        add(
            report,
            "warning",
            "weak_relation_text",
            rel(path),
            f"{relation.get('id')}: same_source should be reserved for a reprint, split case, exact source duplicate, or true version; otherwise name the shared mechanism and use another type",
        )
    if relation_type in {"same_motif", "paired_variant", "solution_transfer", "prerequisite"} and WEAK_RELATION_TEXT_RE.search(
        relation_text
    ):
        add(
            report,
            "warning",
            "weak_relation_text",
            rel(path),
            f"{relation.get('id')}: relation text looks based on a tag/goal/topic/social-wrapper/source tradition; name a shared mechanism or remove it",
        )
    try:
        confidence_value = float(confidence)
    except (TypeError, ValueError):
        return
    if relation_type == "same_motif" and status == "ai_checked" and confidence_value < 0.8:
        add(
            report,
            "warning",
            "low_confidence_relation",
            rel(path),
            f"{relation.get('id')}: same_motif is ai_checked with confidence={confidence}",
        )
    if status == "ai_checked" and confidence_value < 0.65:
        add(
            report,
            "warning",
            "low_confidence_relation",
            rel(path),
            f"{relation.get('id')}: ai_checked relation has very low confidence={confidence}",
        )


def build_report():
    report = []
    check_core_bom(report)

    for path in iter_problem_files():
        problem = load_json_file(path, report)
        if problem is not None:
            check_problem(problem, path, report)

    for path in iter_relation_files():
        payload = load_json_file(path, report)
        if payload is not None:
            for relation in payload.get("relations", []):
                check_relation(relation, path, report)

    return report


def print_report(report, max_items):
    errors = [item for item in report if item["severity"] == "error"]
    warnings = [item for item in report if item["severity"] == "warning"]
    print(f"Audit rules: {len(errors)} errors, {len(warnings)} warnings.")
    if not report:
        return
    by_category = {}
    for item in report:
        by_category.setdefault((item["severity"], item["category"]), []).append(item)
    for (severity, category), items in sorted(by_category.items()):
        print(f"\n{severity.upper()} {category}: {len(items)}")
        for item in items[:max_items]:
            print(f"- {item['path']}: {item['message']}")
        if len(items) > max_items:
            print(f"- ... {len(items) - max_items} more")


def main():
    parser = argparse.ArgumentParser(description="Editorial audit rules for AI database work.")
    parser.add_argument("--json", action="store_true", help="Print full report as JSON.")
    parser.add_argument("--strict", action="store_true", help="Return non-zero on warnings as well as errors.")
    parser.add_argument("--max-items", type=int, default=25, help="Maximum printed examples per category.")
    args = parser.parse_args()

    report = build_report()
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_report(report, args.max_items)

    has_errors = any(item["severity"] == "error" for item in report)
    has_warnings = any(item["severity"] == "warning" for item in report)
    if has_errors or (args.strict and has_warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
