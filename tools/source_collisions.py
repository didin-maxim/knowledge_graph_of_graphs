import argparse
import json
from collections import defaultdict
from pathlib import Path

from lib import DATA, ROOT, external_problem_refs, load_problems, load_relations, normalize_external_problem_ref


def relation_pairs():
    return {tuple(sorted((relation["from"], relation["to"]))) for relation in load_relations()}


def problem_ref_index():
    index = defaultdict(list)
    for problem_id, problem in load_problems().items():
        for ref in external_problem_refs(problem):
            index[ref].append(
                {
                    "problem_id": problem_id,
                    "title": problem.get("title", ""),
                    "path": problem.get("_path", ""),
                    "canonical": problem_id.startswith(ref),
                }
            )
    return index


def ref_from_record(record):
    ref = normalize_external_problem_ref(record.get("id", ""))
    if ref:
        return ref
    year = record.get("year")
    code = str(record.get("problem_code", "")).lower().replace("_", "-").replace(" ", "")
    if year and code:
        return normalize_external_problem_ref(f"memo-{year}-{code}")
    return ""


def iter_records(value):
    if isinstance(value, dict):
        if any(key in value for key in ("problem_code", "statement_en", "statement", "solution_text_en")):
            yield value
        for item in value.values():
            yield from iter_records(item)
    elif isinstance(value, list):
        for item in value:
            yield from iter_records(item)


def extracted_ref_index():
    index = defaultdict(list)
    root = DATA / "import_batches" / "extracted"
    if not root.exists():
        return index
    for path in sorted(root.rglob("*.json")):
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        for record in iter_records(payload):
            ref = ref_from_record(record)
            if not ref:
                continue
            index[ref].append(
                {
                    "id": record.get("id"),
                    "problem_code": record.get("problem_code"),
                    "path": str(path.relative_to(ROOT)),
                    "graph_terms": record.get("graph_terms", []),
                    "decision": record.get("combinatorics_decision") or record.get("decision"),
                }
            )
    return index


def build_report(problem_id=None):
    problems_by_ref = problem_ref_index()
    extracted_by_ref = extracted_ref_index()
    pairs = relation_pairs()
    collisions = []
    missing_originals = []

    for ref, items in sorted(problems_by_ref.items()):
        if problem_id and problem_id not in {item["problem_id"] for item in items}:
            continue
        if len(items) > 1:
            linked_pairs = []
            unlinked_pairs = []
            for left_index, left in enumerate(items):
                for right in items[left_index + 1 :]:
                    pair = tuple(sorted((left["problem_id"], right["problem_id"])))
                    target = linked_pairs if pair in pairs else unlinked_pairs
                    target.append(list(pair))
            collisions.append(
                {
                    "external_problem_ref": ref,
                    "cards": items,
                    "linked_pairs": linked_pairs,
                    "unlinked_pairs": unlinked_pairs,
                }
            )

        has_canonical_card = any(item["canonical"] for item in items)
        if extracted_by_ref.get(ref) and not has_canonical_card:
            missing_originals.append(
                {
                    "external_problem_ref": ref,
                    "cards": items,
                    "extracted_records": extracted_by_ref[ref],
                }
            )

    return {"collisions": collisions, "missing_originals": missing_originals}


def print_report(report):
    if not report["collisions"] and not report["missing_originals"]:
        print("No source collisions or missing canonical originals found.")
        return
    for item in report["collisions"]:
        print(f"[collision] {item['external_problem_ref']}")
        for card in item["cards"]:
            marker = "canonical" if card["canonical"] else "reprint"
            print(f"  - {card['problem_id']} ({marker}) :: {card['path']}")
        for pair in item["unlinked_pairs"]:
            print(f"  ! unlinked pair: {pair[0]} <-> {pair[1]}")
        for pair in item["linked_pairs"]:
            print(f"  = linked pair: {pair[0]} <-> {pair[1]}")
    for item in report["missing_originals"]:
        print(f"[missing-original] {item['external_problem_ref']}")
        for card in item["cards"]:
            print(f"  - {card['problem_id']} :: {card['path']}")
        for record in item["extracted_records"][:3]:
            print(f"  extracted: {record['id']} from {record['path']} graph_terms={record['graph_terms']}")


def main():
    parser = argparse.ArgumentParser(description="Find exact-source collisions such as MEMO originals and reprints.")
    parser.add_argument("--problem", help="Only show refs touching this problem id")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    report = build_report(problem_id=args.problem)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_report(report)


if __name__ == "__main__":
    main()
