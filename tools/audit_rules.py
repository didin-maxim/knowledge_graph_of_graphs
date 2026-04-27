import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CORE_TEXT_SUFFIXES = {".json", ".md", ".py", ".yaml", ".html"}
CORE_DIRS = ["docs", "tools", "schemas"]
UNCERTAIN_STATUSES = {"needs_review", "needs_human_review", "disputed"}
PLACEHOLDER_SOLUTION_RE = re.compile(r"^\s*решение пока не найдено[.!]?\s*$", re.IGNORECASE)
SOLUTION_RED_FLAGS = [
    ("outline/sketch title", re.compile(r"\b(outline|sketch|plan|summary|compressed)\b", re.IGNORECASE)),
    ("draft Russian marker", re.compile(r"\b(набросок|план|пересказ|сжатый пересказ)\b", re.IGNORECASE)),
    ("external-solution narration", re.compile(r"(официальн\w*\s+решени\w*|автор\w*\s+решени\w*)", re.IGNORECASE)),
    ("handwave marker", re.compile(r"\b(аналогично|стандартно|легко видеть)\b", re.IGNORECASE)),
]


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
    editorial = problem.get("editorial", {})
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
