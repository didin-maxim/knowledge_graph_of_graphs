import argparse
from collections import deque

from lib import load_problems, load_relations, problem_text, relation_neighbors


def cmd_query(args):
    problems = load_problems()
    words = [word.lower() for word in args.text.split()]
    matches = []
    for problem in problems.values():
        text = problem_text(problem)
        score = sum(text.count(word) for word in words)
        if score:
            matches.append((score, problem))
    for score, problem in sorted(matches, key=lambda item: (-item[0], item[1]["id"]))[: args.limit]:
        print(f"{problem['id']}: {problem['title']} ({score})")
        print(f"  {problem['_path']}")


def cmd_problem(args):
    problems = load_problems()
    problem = problems[args.id]
    print(f"{problem['id']}: {problem['title']}")
    print(f"file: {problem['_path']}")
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

