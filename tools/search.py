import argparse
import sys
from collections import deque

from lib import (
    extract_problem_year,
    has_real_solution,
    infer_source_key,
    infer_source_label,
    load_sources,
    load_problems,
    load_relations,
    problem_author_names,
    problem_source_labels,
    problem_text,
    problem_source_values,
    relation_neighbors,
)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def query_matches(text, words):
    return all(word in text for word in words)


def cmd_query(args):
    problems = load_problems()
    sources = load_sources()
    words = [word.lower() for word in args.text.split()]
    matches = []
    for problem in problems.values():
        if args.source:
            source_query = args.source.lower()
            source_values = problem_source_values(problem)
            if not any(source_query == value or source_query in value for value in source_values):
                continue
        if args.year and extract_problem_year(problem) != str(args.year):
            continue
        if args.solution == "with" and not has_real_solution(problem):
            continue
        if args.solution == "without" and has_real_solution(problem):
            continue
        text = problem_text(problem)
        if not query_matches(text, words):
            continue
        score = sum(text.count(word) for word in words)
        if score:
            matches.append((score, problem))
    for score, problem in sorted(matches, key=lambda item: (-item[0], item[1]["id"]))[: args.limit]:
        print(f"{problem['id']}: {problem['title']} ({score})")
        authors = ", ".join(problem_author_names(problem)) or "?"
        source_labels = "; ".join(problem_source_labels(problem, sources)) or infer_source_label(problem)
        print(f"  authors: {authors}")
        print(f"  sources: {source_labels}")
        print(f"  {problem['_path']}")


def cmd_problem(args):
    problems = load_problems()
    sources = load_sources()
    problem = problems[args.id]
    print(f"{problem['id']}: {problem['title']}")
    print(f"file: {problem['_path']}")
    print(f"authors: {', '.join(problem_author_names(problem)) or '?'}")
    print(f"sources: {'; '.join(problem_source_labels(problem, sources)) or infer_source_label(problem)}")
    print()
    for statement in problem["statements"].get("graph_theory", []):
        print("Графовая формулировка:")
        print(statement["text"])
    print()
    print("Идеи:")
    for idea in problem.get("ideas", []):
        print(f"- {idea['id']}: {idea['title']} [{idea['status']}]")
        print(f"  {idea['text']}")
    print()
    print("Решения:")
    for solution in problem.get("solutions", []):
        print(f"- {solution['id']}: {solution['title']} [{solution['status']}]")


def cmd_neighbors(args):
    problems = load_problems()
    relations = load_relations()
    seen = {args.id}
    queue = deque([(args.id, 0)])
    while queue:
        current, depth = queue.popleft()
        if depth == args.depth:
            continue
        for neighbor_id, relation, direction in relation_neighbors(current, relations):
            arrow = "->" if direction == "forward" else "<-"
            text = relation["forward_text"] if direction == "forward" else relation["backward_text"]
            indent = "  " * depth
            print(f"{indent}{current} {arrow} {neighbor_id} [{relation['type']}, d={relation['distance']}, {relation['status']}]")
            print(f"{indent}  {text}")
            if neighbor_id not in seen:
                seen.add(neighbor_id)
                queue.append((neighbor_id, depth + 1))


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(required=True)

    q = sub.add_parser("query")
    q.add_argument("text")
    q.add_argument("--limit", type=int, default=20)
    q.add_argument("--source")
    q.add_argument("--year", type=int)
    q.add_argument("--solution", choices=["all", "with", "without"], default="all")
    q.set_defaults(func=cmd_query)

    p = sub.add_parser("problem")
    p.add_argument("id")
    p.set_defaults(func=cmd_problem)

    n = sub.add_parser("neighbors")
    n.add_argument("id")
    n.add_argument("--depth", type=int, default=1)
    n.set_defaults(func=cmd_neighbors)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
