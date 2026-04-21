import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def load_json_yaml(path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def problem_paths():
    return sorted((DATA / "problems").rglob("*.yaml"))


def load_problems():
    problems = {}
    for path in problem_paths():
        item = load_json_yaml(path)
        item["_path"] = str(path.relative_to(ROOT))
        if item["id"] in problems:
            raise ValueError(f"Duplicate problem id: {item['id']}")
        problems[item["id"]] = item
    return problems


def load_sources():
    path = DATA / "sources" / "sources.yaml"
    return {source["id"]: source for source in load_json_yaml(path)["sources"]}


def load_definitions():
    path = DATA / "definitions" / "definitions.yaml"
    return {item["id"]: item for item in load_json_yaml(path)["definitions"]}


def load_standard_ideas():
    path = DATA / "standard_ideas" / "standard-ideas.yaml"
    return {item["id"]: item for item in load_json_yaml(path)["standard_ideas"]}


def comment_paths():
    path = DATA / "comments"
    if not path.exists():
        return []
    return sorted(
        item for item in path.rglob("*.yaml")
        if not item.name.startswith("comment-template-")
    )


def load_comments():
    comments = {}
    for path in comment_paths():
        item = load_json_yaml(path)
        item["_path"] = str(path.relative_to(ROOT))
        if item["id"] in comments:
            raise ValueError(f"Duplicate comment id: {item['id']}")
        comments[item["id"]] = item
    return comments


def load_taxonomy(name, key):
    path = DATA / "taxonomy" / name
    return load_json_yaml(path)[key]


def relation_paths():
    paths = [DATA / "relations" / "relations.yaml"]
    split_dir = DATA / "relations" / "relations.d"
    if split_dir.exists():
        paths.extend(sorted(split_dir.glob("*.yaml")))
    return [path for path in paths if path.exists()]


def load_relations():
    relations = []
    seen = set()
    for path in relation_paths():
        payload = load_json_yaml(path)
        for relation in payload.get("relations", []):
            relation["_path"] = str(path.relative_to(ROOT))
            if relation["id"] in seen:
                raise ValueError(f"Duplicate relation id: {relation['id']}")
            seen.add(relation["id"])
            relations.append(relation)
    return relations


def import_batch_paths():
    path = DATA / "import_batches"
    if not path.exists():
        return []
    return sorted(path.glob("*.yaml"))


def load_import_batches():
    batches = []
    for path in import_batch_paths():
        batch = load_json_yaml(path)
        batch["_path"] = str(path.relative_to(ROOT))
        batches.append(batch)
    return batches


def load_legacy_relations():
    path = DATA / "relations" / "relations.yaml"
    return load_json_yaml(path)["relations"]


def collect_text(value):
    parts = []
    if isinstance(value, dict):
        for item in value.values():
            parts.append(collect_text(item))
    elif isinstance(value, list):
        for item in value:
            parts.append(collect_text(item))
    elif isinstance(value, str):
        parts.append(value)
    return "\n".join(part for part in parts if part)


def problem_text(problem):
    fields = [
        problem.get("id", ""),
        problem.get("title", ""),
        collect_text(problem.get("statements", {})),
        collect_text(problem.get("ideas", [])),
        collect_text(problem.get("solutions", [])),
        " ".join(problem.get("tags", [])),
    ]
    return "\n".join(fields).lower()


def relation_neighbors(problem_id, relations):
    for relation in relations:
        if relation["from"] == problem_id:
            yield relation["to"], relation, "forward"
        elif relation["to"] == problem_id:
            yield relation["from"], relation, "backward"
