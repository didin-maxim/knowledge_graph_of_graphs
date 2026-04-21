import argparse

from lib import load_comments, load_problems


def main():
    parser = argparse.ArgumentParser(description="List comments from data/comments")
    parser.add_argument("--problem", help="Filter by problem id")
    parser.add_argument("--architecture", action="store_true", help="Show only architecture comments")
    parser.add_argument("--status", help="Filter by comment status")
    args = parser.parse_args()

    comments = load_comments()
    problems = load_problems()
    items = sorted(
        comments.values(),
        key=lambda item: (str(item.get("created_at", "")), item["id"]),
        reverse=True,
    )

    filtered = []
    for item in items:
        target = item.get("target", {})
        if args.problem and target.get("problem_id") != args.problem:
            continue
        if args.architecture and target.get("type") != "architecture":
            continue
        if args.status and item.get("status") != args.status:
            continue
        filtered.append(item)

    if not filtered:
        print("No comments found.")
        return 0

    for item in filtered:
        target = item.get("target", {})
        if target.get("type") == "problem":
            target_label = f"{target.get('problem_id')} :: {problems.get(target.get('problem_id'), {}).get('title', '')}"
        else:
            target_label = "architecture"
        print(f"{item['id']} [{item.get('status', '')}]")
        print(f"  kind:   {item.get('kind', '')}")
        print(f"  target: {target_label}")
        print(f"  author: {item.get('author', '')}")
        print(f"  title:  {item.get('title', '')}")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
