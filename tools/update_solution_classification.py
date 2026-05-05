import json
import re
from pathlib import Path

from lib import ROOT, load_sources


CLASS_LABELS = {
    "official_complete_or_near_complete": "официальное полное/почти полное",
    "official_outline_needs_work": "официальный план, нужна доработка",
    "unofficial_published": "опубликованное неофициальное",
    "ai_original": "решение ИИ с нуля",
    "ai_heavy_external_theorem": "ИИ/решение с тяжёлыми внешними теоремами",
    "no_solution_hard": "решения нет: сложная задача",
}

MISSING_RE = re.compile(r"^\s*решение пока не найдено[.!]?\s*$", re.IGNORECASE)
PLACEHOLDER_IDS = {"sol-archive-card", "sol-import-note"}
OUTLINE_MARKERS = [
    "compressed",
    "summary",
    "sketch",
    "outline",
    "plan",
    "сжат",
    "наброс",
    "эскиз",
    "план",
]
PUBLISHED_MARKERS = [
    "aops",
    "kedlaya",
    "reviewed",
    "secondary",
    "web",
    "forum",
    "published",
    "archive",
    "официаль",
    "архив",
    "опублик",
]
HEAVY_THEOREM_PATTERNS = [
    (re.compile(r"\b(brooks|brook's)\b|брукс", re.IGNORECASE), "brooks-theorem"),
    (re.compile(r"\bmenger\b|менгер", re.IGNORECASE), "menger-theorem"),
    (re.compile(r"\btur[aá]n\b|туран", re.IGNORECASE), "turan-theorem"),
    (re.compile(r"\bore\b|теорем[аыу] оре", re.IGNORECASE), "ore-theorem"),
    (re.compile(r"\bstiebitz\b|стибиц", re.IGNORECASE), "stiebitz-double-critical-k5"),
    (re.compile(r"\btihany\b|тихани", re.IGNORECASE), "erdos-lovasz-tihany-conjecture"),
    (re.compile(r"\bchen\b|теорем[аыу] чен", re.IGNORECASE), "chen-theorem"),
    (re.compile(r"\bkotzig\b|коциг", re.IGNORECASE), "kotzig-theorem"),
]


def solution_text(solution):
    parts = [
        solution.get("id", ""),
        solution.get("title", ""),
        solution.get("text", ""),
        solution.get("status", ""),
        solution.get("source_id", ""),
        " ".join(solution.get("source_ids", [])),
        " ".join(solution.get("tags", [])),
    ]
    return "\n".join(str(part) for part in parts if part).lower()


def real_solutions(problem):
    items = []
    for solution in problem.get("solutions", []):
        sid = solution.get("id", "")
        text = str(solution.get("text", "")).strip()
        title = str(solution.get("title", "")).strip().lower()
        if sid in PLACEHOLDER_IDS:
            continue
        if not text or MISSING_RE.match(text):
            continue
        if "близк" in title and "решени" in title:
            continue
        items.append(solution)
    return items


def collect_solution_source_ids(problem, solutions):
    source_ids = set()
    for solution in solutions:
        if solution.get("source_id"):
            source_ids.add(solution["source_id"])
        source_ids.update(solution.get("source_ids", []))
    if not source_ids:
        for source in problem.get("sources", []):
            role = str(source.get("role", "")).lower()
            if "solution" in role or "solutions" in role or "реш" in role:
                source_ids.add(source.get("source_id", ""))
    return {item for item in source_ids if item}


def has_official_solution_source(problem, solutions, sources):
    for source_id in collect_solution_source_ids(problem, solutions):
        source = sources.get(source_id, {})
        role = ""
        for local in problem.get("sources", []):
            if local.get("source_id") == source_id:
                role = str(local.get("role", "")).lower()
                break
        if source.get("official") is True and ("solution" in role or "solutions" in role or source_id in collect_solution_source_ids(problem, solutions)):
            return True
        if "official" in role and ("solution" in role or "solutions" in role):
            return True
    return False


def has_unofficial_published_solution(problem, solutions, sources):
    blobs = [solution_text(solution) for solution in solutions]
    for source_id in collect_solution_source_ids(problem, solutions):
        source = sources.get(source_id, {})
        if source and source.get("official") is False:
            return True
        title = str(source.get("title", "")).lower()
        if any(marker in title for marker in ["aops", "kedlaya", "forum", "wiki", "web"]):
            return True
    return any(any(marker in blob for marker in PUBLISHED_MARKERS) for blob in blobs)


def outline_solution(solutions):
    blob = "\n".join(solution_text(solution) for solution in solutions)
    if any(marker in blob for marker in OUTLINE_MARKERS):
        return True
    texts = [str(solution.get("text", "")) for solution in solutions]
    return bool(texts) and max(len(text) for text in texts) < 1200


def heavy_theorems(problem, solutions):
    problem_without_classification = json.loads(json.dumps(problem, ensure_ascii=False))
    problem_without_classification.get("editorial", {}).pop("solution_classification", None)
    blob = json.dumps(problem_without_classification, ensure_ascii=False).lower()
    found = []
    if "external_theorem" in problem.get("tags", []):
        found.append("external_theorem")
    for pattern, theorem_id in HEAVY_THEOREM_PATTERNS:
        if pattern.search(blob) and theorem_id not in found:
            found.append(theorem_id)
    return found


def classify(problem, sources):
    solutions = real_solutions(problem)
    if not solutions:
        return {
            "type": "no_solution_hard",
            "status": "ai_checked",
            "confidence": 0.86,
            "basis": "no real solution object or only placeholder/missing-solution text",
            "notes": "В карточке нет полного решения; это не техническая ошибка импорта, а очередь для отдельной математической доработки.",
        }

    heavy = heavy_theorems(problem, solutions)
    if heavy:
        return {
            "type": "ai_heavy_external_theorem",
            "status": "needs_human_review",
            "confidence": 0.72,
            "basis": "heavy theorem marker in solution/card text",
            "external_theorem_ids": heavy,
            "notes": "Проверьте, что в карточке есть явные ссылки на используемые внешние теоремы или связанные карточки.",
        }

    official = has_official_solution_source(problem, solutions, sources)
    if official and outline_solution(solutions):
        return {
            "type": "official_outline_needs_work",
            "status": "needs_human_review",
            "confidence": 0.78,
            "basis": "official source plus compressed/sketch-like solution marker",
            "notes": "Официальное решение или его краткая версия найдено, но текущий текст похож на план и требует разворачивания.",
        }
    if official:
        return {
            "type": "official_complete_or_near_complete",
            "status": "ai_checked",
            "confidence": 0.82,
            "basis": "official solution source and non-compressed solution text",
            "notes": "Текущий текст основан на официальном источнике и выглядит полным или почти полным.",
        }

    if has_unofficial_published_solution(problem, solutions, sources):
        return {
            "type": "unofficial_published",
            "status": "ai_checked",
            "confidence": 0.78,
            "basis": "non-official published source or published-solution marker",
            "notes": "Решение опубликовано не в официальном архиве; источник надо отличать от официального.",
        }

    return {
        "type": "ai_original",
        "status": "ai_checked",
        "confidence": 0.7,
        "basis": "no official or published solution source detected",
        "notes": "Решение выглядит как восстановленное/написанное ИИ с нуля; желательно выборочно перепроверять математически.",
    }


def main():
    sources = load_sources()
    counts = {key: 0 for key in CLASS_LABELS}
    changed = 0
    for path in sorted((ROOT / "data" / "problems").rglob("*.yaml")):
        problem = json.loads(path.read_text(encoding="utf-8"))
        classification = classify(problem, sources)
        classification["label"] = CLASS_LABELS[classification["type"]]
        editorial = problem.setdefault("editorial", {})
        if editorial.get("solution_classification") != classification:
            editorial["solution_classification"] = classification
            path.write_text(json.dumps(problem, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            changed += 1
        counts[classification["type"]] += 1

    print(f"updated {changed} problem cards")
    for key, count in counts.items():
        print(f"{key}: {count}")


if __name__ == "__main__":
    main()
