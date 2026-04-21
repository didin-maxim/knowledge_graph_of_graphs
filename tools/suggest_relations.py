import argparse
import json
import math
import re
from collections import Counter

from lib import collect_text, load_problems, load_relations


BROAD_TAGS = {"olympiad_tool", "classical_theorem"}
BROAD_IDEAS = {"induction"}
PROFILE_FIELDS = [
    "objects",
    "methods",
    "transformations",
    "goal",
    "auxiliary_graph_type",
    "invariants",
    "keywords",
]
TOKEN_RE = re.compile(r"[A-Za-zА-Яа-я0-9_]{3,}")


def tokens(text):
    raw = TOKEN_RE.findall(text.lower())
    stop = {
        "the",
        "and",
        "for",
        "with",
        "что",
        "как",
        "или",
        "для",
        "если",
        "при",
        "это",
        "есть",
        "задача",
        "доказать",
        "докажите",
        "граф",
        "вершина",
        "вершины",
    }
    return {token for token in raw if token not in stop}


def solution_ideas(problem):
    result = set()
    by_solution = {}
    for solution in problem.get("solutions", []):
        ideas = set(solution.get("standard_idea_ids", []))
        result.update(ideas)
        by_solution[solution["id"]] = ideas
    return result, by_solution


def local_idea_titles(problem):
    return {idea.get("title", "") for idea in problem.get("ideas", []) if idea.get("title")}


def central_methods(problem):
    item = problem.get("properties", {}).get("central_method", {})
    value = item.get("value", [])
    if isinstance(value, str):
        return {value}
    return set(value)


def profile_values(problem):
    profile = problem.get("problem_profile", {}) or {}
    values = {}
    for field in PROFILE_FIELDS:
        item = profile.get(field, [])
        if isinstance(item, str):
            item = [item]
        values[field] = {str(value).lower() for value in item}
    return values


def best_solution_anchor(left, right):
    _, left_by_solution = solution_ideas(left)
    _, right_by_solution = solution_ideas(right)
    best = (0, None, None, set())
    for left_id, left_ideas in left_by_solution.items():
        for right_id, right_ideas in right_by_solution.items():
            common = (left_ideas & right_ideas) - BROAD_IDEAS
            score = len(common)
            if score > best[0]:
                best = (score, left_id, right_id, common)
    if best[1] and best[2]:
        return best[1], best[2], best[3]
    left_solution = (left.get("solutions") or [{}])[0].get("id")
    right_solution = (right.get("solutions") or [{}])[0].get("id")
    return left_solution, right_solution, set()


def score_pair(left, right):
    left_tags = set(left.get("tags", [])) - BROAD_TAGS
    right_tags = set(right.get("tags", [])) - BROAD_TAGS
    common_tags = left_tags & right_tags

    left_ideas, _ = solution_ideas(left)
    right_ideas, _ = solution_ideas(right)
    common_ideas = (left_ideas & right_ideas) - BROAD_IDEAS

    common_methods = central_methods(left) & central_methods(right)

    left_profile = profile_values(left)
    right_profile = profile_values(right)
    common_profile = {
        field: left_profile[field] & right_profile[field]
        for field in PROFILE_FIELDS
        if left_profile[field] & right_profile[field]
    }

    left_tokens = tokens(collect_text(left.get("statements", {})) + "\n" + collect_text(left.get("ideas", [])))
    right_tokens = tokens(collect_text(right.get("statements", {})) + "\n" + collect_text(right.get("ideas", [])))
    overlap = left_tokens & right_tokens
    token_score = 0
    if left_tokens and right_tokens:
        token_score = 4 * len(overlap) / math.sqrt(len(left_tokens) * len(right_tokens))

    local_overlap = local_idea_titles(left) & local_idea_titles(right)

    score = (
        3.0 * len(common_ideas)
        + 2.0 * len(common_methods)
        + 1.4 * len(common_tags)
        + 2.2 * sum(len(values) for values in common_profile.values())
        + 1.5 * len(local_overlap)
        + token_score
    )

    reasons = []
    if common_ideas:
        reasons.append("standard_ideas=" + ",".join(sorted(common_ideas)))
    if common_methods:
        reasons.append("central_method=" + ",".join(sorted(common_methods)))
    if common_tags:
        reasons.append("tags=" + ",".join(sorted(common_tags)))
    for field, values in common_profile.items():
        reasons.append(f"profile.{field}=" + ",".join(sorted(values)))
    if overlap:
        reasons.append("text=" + ",".join(sorted(list(overlap))[:8]))
    if local_overlap:
        reasons.append("local_ideas=" + ",".join(sorted(local_overlap)))

    return score, reasons, common_ideas, common_tags, common_profile


def suggested_type_and_distance(score, common_ideas, common_tags, common_profile):
    if common_profile.get("transformations") or common_profile.get("methods") or common_ideas:
        relation_type = "same_motif"
    else:
        relation_type = "same_motif"
    if score >= 10:
        distance = 1
    elif score >= 7:
        distance = 2
    elif score >= 4.5:
        distance = 3
    elif score >= 3:
        distance = 4
    else:
        distance = 5
    return relation_type, distance


def make_candidate(left, right, score, reasons, common_ideas, common_tags, common_profile):
    from_solution, to_solution, anchor_ideas = best_solution_anchor(left, right)
    relation_type, distance = suggested_type_and_distance(score, common_ideas, common_tags, common_profile)
    return {
        "from": left["id"],
        "to": right["id"],
        "score": round(score, 2),
        "suggested_type": relation_type,
        "suggested_distance": distance,
        "anchors": {
            "from_solution_id": from_solution,
            "to_solution_id": to_solution,
        },
        "anchor_standard_ideas": sorted(anchor_ideas),
        "reasons": reasons,
        "titles": {
            "from": left["title"],
            "to": right["title"],
        },
    }


def existing_pairs(relations):
    return {tuple(sorted((relation["from"], relation["to"]))) for relation in relations}


def suggest(problem_id=None, min_score=3.0, limit=30):
    problems = load_problems()
    relations = load_relations()
    existing = existing_pairs(relations)
    ids = sorted(problems)
    candidates = []
    for index, left_id in enumerate(ids):
        for right_id in ids[index + 1 :]:
            if problem_id and problem_id not in {left_id, right_id}:
                continue
            pair = tuple(sorted((left_id, right_id)))
            if pair in existing:
                continue
            left = problems[left_id]
            right = problems[right_id]
            score, reasons, common_ideas, common_tags, common_profile = score_pair(left, right)
            if score >= min_score:
                candidates.append(make_candidate(left, right, score, reasons, common_ideas, common_tags, common_profile))
    candidates.sort(key=lambda item: (-item["score"], item["from"], item["to"]))
    return candidates[:limit]


def print_text(candidates):
    for item in candidates:
        print(f"{item['score']:>5}  {item['from']}  <->  {item['to']}")
        print(f"       {item['titles']['from']}")
        print(f"       {item['titles']['to']}")
        print(f"       type={item['suggested_type']} distance={item['suggested_distance']}")
        print(f"       anchors={item['anchors']['from_solution_id']} / {item['anchors']['to_solution_id']}")
        print(f"       reasons: {'; '.join(item['reasons'])}")
        print()


def main():
    parser = argparse.ArgumentParser(description="Suggest candidate relation pairs from tags, ideas, profiles, and text.")
    parser.add_argument("--problem", help="Only show candidates touching this problem id")
    parser.add_argument("--min-score", type=float, default=3.0)
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    args = parser.parse_args()

    candidates = suggest(problem_id=args.problem, min_score=args.min_score, limit=args.limit)
    if args.json:
        print(json.dumps({"candidates": candidates}, ensure_ascii=False, indent=2))
    else:
        print_text(candidates)


if __name__ == "__main__":
    main()
