import json
import sys
from pathlib import Path
from urllib.parse import urlparse

from lib import ROOT, load_definitions, load_problems, load_sources, load_standard_ideas


def main():
    errors = []
    problems = load_problems()
    definitions = load_definitions()
    standard_ideas = load_standard_ideas()
    sources = load_sources()

    valid_routes = set(problems)
    valid_routes.update(f"def-{item}" for item in definitions)
    valid_routes.update(f"stdidea-{item}" for item in standard_ideas)

    for problem_id, problem in problems.items():
        for section, statements in problem.get("statements", {}).items():
            for statement in statements:
                for definition_id in statement.get("definition_ids", []):
                    if f"def-{definition_id}" not in valid_routes:
                        errors.append(f"{problem_id}: broken definition route {definition_id}")
                statement_source_ids = []
                if statement.get("source_id"):
                    statement_source_ids.append(statement["source_id"])
                statement_source_ids.extend(statement.get("source_ids", []))
                for source_id in statement_source_ids:
                    if source_id not in sources:
                        errors.append(f"{problem_id}: broken statement source {source_id}")
        for solution in problem.get("solutions", []):
            for idea_id in solution.get("standard_idea_ids", []):
                if f"stdidea-{idea_id}" not in valid_routes:
                    errors.append(f"{problem_id}: broken standard idea route {idea_id}")

    for source_id, source in sources.items():
        url = source.get("url", "")
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            errors.append(f"{source_id}: malformed source url {url}")

    if errors:
        print("Link check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"OK: {len(valid_routes)} internal routes, "
        f"{len(sources)} external source URLs syntactically valid."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
