import argparse
import json
import re
import sys
from collections import Counter

from lib import load_comments, load_problems


WORD_RE = re.compile(r"\w+", re.UNICODE)
EXPLICIT_SHORT_MARKERS = [
    "compressed",
    "one-line",
    "short",
    "сжат",
    "наброс",
    "пересказ",
    "план доказ",
]
TEXT_RED_FLAGS = [
    "официальное решение",
    "официальный аргумент",
    "автор решения",
    "легко видеть",
    "стандартно",
    "оставляется читателю",
    "следует из теоремы",
    "требует доработки",
    "нужно доработать",
    "непонятн",
    "неясн",
    "не удалось понять",
    "переход не проверен",
    "не доведен",
    "не доведён",
    "недовед",
    "needs work",
    "unclear",
]
COMMENT_RED_FLAGS = [
    "outline",
    "не самодостаточ",
    "не восстановлено",
    "не содержит",
    "не доказывает",
]


def word_count(text):
    return len(WORD_RE.findall(text or ""))


def folder_of(path):
    parts = str(path).replace("\\", "/").split("/")
    if len(parts) >= 3 and parts[0] == "data" and parts[1] == "problems":
        return parts[2]
    return ""


def comment_targets():
    targets = {}
    for comment in load_comments().values():
        target = comment.get("target", {})
        problem_id = target.get("problem_id")
        if target.get("type") != "problem" or not problem_id:
            continue
        haystack = f"{comment.get('id', '')}\n{comment.get('title', '')}\n{comment.get('text', '')}".lower()
        if any(marker in haystack for marker in COMMENT_RED_FLAGS):
            targets.setdefault(problem_id, []).append(
                {
                    "id": comment.get("id"),
                    "path": comment.get("_path"),
                    "status": comment.get("status"),
                }
            )
    return targets


def solution_reasons(problem, solution, comments, min_ai_checked_words, min_any_words):
    text = solution.get("text", "")
    title = solution.get("title", "")
    solution_id = solution.get("id", "")
    status = solution.get("status")
    repair_status = solution.get("repair_status") or ""
    medium_checked = repair_status.startswith("medium_reasoning_understandable_") or repair_status.startswith(
        "medium_reasoning_minor_repair_"
    )
    repaired_checked = medium_checked or repair_status.startswith("high_reasoning_repaired_") or repair_status.startswith(
        "very_high_repaired_"
    )
    needs_high_repair = repair_status.startswith("needs_high_reasoning_repair_")
    needs_very_high = repair_status.startswith("needs_very_high_no_solution_attempt_")
    words = word_count(text)
    haystack = f"{solution_id}\n{title}\n{text}".lower()
    reasons = []

    if not repaired_checked and status == "ai_checked" and words < min_ai_checked_words:
        reasons.append(f"short_ai_checked:{words}")
    if not repaired_checked and status != "needs_human_review" and words < min_any_words:
        reasons.append(f"very_short:{words}")
    if needs_high_repair:
        reasons.append("needs_high_reasoning_repair")
    if needs_very_high:
        reasons.append("needs_very_high_no_solution_attempt")
    if not repaired_checked and any(marker in haystack for marker in EXPLICIT_SHORT_MARKERS):
        reasons.append("explicit_short_marker")
    matched_text_flag = None if repaired_checked else next((marker for marker in TEXT_RED_FLAGS if marker in haystack), None)
    if matched_text_flag:
        reasons.append(f"text_red_flag:{matched_text_flag}")
    if not repaired_checked and problem["id"] in comments:
        reasons.append("self_containment_comment")

    return words, reasons


def build_report(folders=None, min_ai_checked_words=180, min_any_words=120):
    comments = comment_targets()
    folder_filter = set(folders or [])
    report = []
    for problem in load_problems().values():
        folder = folder_of(problem.get("_path", ""))
        if folder_filter and folder not in folder_filter:
            continue
        for solution in problem.get("solutions", []):
            words, reasons = solution_reasons(
                problem,
                solution,
                comments,
                min_ai_checked_words=min_ai_checked_words,
                min_any_words=min_any_words,
            )
            if not reasons:
                continue
            report.append(
                {
                    "problem_id": problem["id"],
                    "path": problem.get("_path"),
                    "folder": folder,
                    "solution_id": solution.get("id"),
                    "solution_title": solution.get("title"),
                    "solution_status": solution.get("status"),
                    "word_count": words,
                    "public_ready": problem.get("editorial", {}).get("public_ready"),
                    "review_status": problem.get("editorial", {}).get("review_status"),
                    "reasons": reasons,
                    "comments": comments.get(problem["id"], []),
                }
            )
    return sorted(report, key=lambda item: (item["word_count"], item["folder"], item["problem_id"]))


def print_report(report, max_items):
    print(f"Suspicious solutions: {len(report)}")
    by_folder = Counter(item["folder"] for item in report)
    if by_folder:
        print("\nBy folder:")
        for folder, count in by_folder.most_common():
            print(f"- {folder}: {count}")
    print("\nShortest / highest-priority examples:")
    for item in report[:max_items]:
        reasons = ", ".join(item["reasons"])
        print(
            f"- {item['word_count']:>4}w {item['problem_id']} :: {item['solution_id']} "
            f"[{item['solution_status']} public_ready={item['public_ready']}] {reasons}"
        )
        print(f"  {item['path']}")
    if len(report) > max_items:
        print(f"- ... {len(report) - max_items} more")


def main():
    parser = argparse.ArgumentParser(description="Find likely compressed or non-self-contained solutions.")
    parser.add_argument("--folder", action="append", help="Limit to a data/problems subfolder; repeatable.")
    parser.add_argument("--json", action="store_true", help="Print full report as JSON.")
    parser.add_argument("--max-items", type=int, default=40)
    parser.add_argument("--min-ai-checked-words", type=int, default=180)
    parser.add_argument("--min-any-words", type=int, default=120)
    args = parser.parse_args()

    report = build_report(
        folders=args.folder,
        min_ai_checked_words=args.min_ai_checked_words,
        min_any_words=args.min_any_words,
    )
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_report(report, args.max_items)
    return 0


if __name__ == "__main__":
    sys.exit(main())
