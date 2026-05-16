import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
YEAR_RE = re.compile(r"(19|20)\d{2}")
ID_YEAR_RE = re.compile(r"^(?P<prefix>[a-z0-9-]+)-(?P<year>(19|20)\d{2})(?:-|$)")
MISSING_SOLUTION_RE = re.compile(r"^\s*решение пока не найдено[.!]?\s*$", re.IGNORECASE)
NON_TRANSFERRED_NOTE_RE = re.compile(r"близк\w*\s+решени\w*", re.IGNORECASE)

SOURCE_ALIASES = {
    "yumt": ["yumt", "юмт"],
    "fyum": ["fyum", "фюм"],
    "imo": ["imo"],
    "apmo": ["apmo"],
    "bmo": ["bmo"],
    "egmo": ["egmo"],
    "usamo": ["usamo"],
    "rmm": ["rmm"],
}
EXTERNAL_PROBLEM_REF_PATTERNS = [
    re.compile(r"\bmemo[-_\s]+(?P<year>20\d{2})[-_\s]+(?P<section>[it])[-_\s]*(?P<number>\d+)\b", re.IGNORECASE),
    re.compile(r"\bmemo[-_\s]*(?P<year>20\d{2})[-_\s]*(?P<section>[it])(?P<number>\d+)\b", re.IGNORECASE),
]


def load_json_yaml(path):
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        try:
            location = path.relative_to(ROOT)
        except ValueError:
            location = path
        raise ValueError(f"{location}: UTF-8 BOM is not allowed")
    return json.loads(raw.decode("utf-8"))


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


def author_name(author):
    if isinstance(author, dict):
        return str(author.get("name", ""))
    return str(author)


def problem_author_names(problem, include_unknown=True):
    names = []
    for author in problem.get("authors", []):
        name = author_name(author).strip()
        if not name:
            continue
        if not include_unknown and name.lower() in {"?", "unknown"}:
            continue
        names.append(name)
    return names


def iter_problem_source_ids(problem):
    seen = set()
    for source in problem.get("sources", []):
        source_id = source.get("source_id")
        if source_id and source_id not in seen:
            seen.add(source_id)
            yield source_id
    for statements in problem.get("statements", {}).values():
        for statement in statements:
            source_ids = []
            if statement.get("source_id"):
                source_ids.append(statement["source_id"])
            source_ids.extend(statement.get("source_ids", []))
            for source_id in source_ids:
                if source_id and source_id not in seen:
                    seen.add(source_id)
                    yield source_id


def problem_source_labels(problem, sources=None):
    if sources is None:
        sources = load_sources()
    labels = []
    for source_id in iter_problem_source_ids(problem):
        source = sources.get(source_id)
        labels.append(source.get("title", source_id) if source else source_id)
    return labels


def problem_source_search_values(problem, sources=None):
    if sources is None:
        sources = load_sources()
    values = {infer_source_key(problem), infer_source_label(problem)}
    for source_id in iter_problem_source_ids(problem):
        values.add(source_id)
        source = sources.get(source_id)
        if source:
            values.add(source.get("title", ""))
            values.add(source.get("url", ""))
            values.add(source.get("type", ""))
    return {str(value).lower() for value in values if value}


def problem_text(problem):
    source_labels = problem_source_labels(problem)
    fields = [
        problem.get("id", ""),
        problem.get("title", ""),
        " ".join(problem_author_names(problem)),
        infer_source_key(problem),
        infer_source_label(problem),
        " ".join(source_labels),
        " ".join(problem_search_tokens(problem)),
        " ".join(external_problem_refs(problem)),
        collect_text(problem.get("statements", {})),
        collect_text(problem.get("ideas", [])),
        collect_text(problem.get("solutions", [])),
        " ".join(problem.get("tags", [])),
    ]
    return "\n".join(fields).lower()


def extract_problem_year(problem):
    match = ID_YEAR_RE.match(problem.get("id", ""))
    if match:
        return match.group("year")
    match = YEAR_RE.search(problem.get("id", "")) or YEAR_RE.search(problem.get("title", ""))
    return match.group(0) if match else ""


def infer_source_key(problem):
    problem_id = problem.get("id", "")
    match = ID_YEAR_RE.match(problem_id)
    if match:
        return match.group("prefix").split("-")[0]

    title = problem.get("title", "")
    for chunk in [part.strip() for part in title.split(",")]:
        year_match = YEAR_RE.search(chunk)
        if year_match:
            label = chunk[: year_match.start()].strip(" -")
            if label:
                token = re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")
                if token:
                    return token
    return "misc"


def infer_source_label(problem):
    title = problem.get("title", "")
    for chunk in [part.strip() for part in title.split(",")]:
        year_match = YEAR_RE.search(chunk)
        if year_match:
            label = chunk[: year_match.start()].strip(" -")
            if label:
                return label
    source_key = infer_source_key(problem)
    return source_key.upper() if source_key != "misc" else "Прочее"


def has_real_solution(problem):
    for solution in problem.get("solutions", []):
        text = (solution.get("text") or "").strip()
        title = (solution.get("title") or "").strip()
        if solution.get("status") == "needs_human_review":
            continue
        if not text or MISSING_SOLUTION_RE.match(text):
            continue
        if NON_TRANSFERRED_NOTE_RE.search(title):
            continue
        return True
    return False


def problem_search_tokens(problem):
    tokens = set()
    year = extract_problem_year(problem)
    source_key = infer_source_key(problem)
    source_label = infer_source_label(problem)
    compact_key = re.sub(r"[^a-z0-9а-яё]+", "", source_key.lower())
    compact_label = re.sub(r"[^a-z0-9а-яё]+", "", source_label.lower())
    if source_key:
        tokens.add(source_key.lower())
    if source_label:
        tokens.add(source_label.lower())
    if compact_key:
        tokens.add(compact_key)
        for alias in SOURCE_ALIASES.get(compact_key, []):
            tokens.add(alias)
            if year:
                tokens.add(f"{alias}{year}")
    if compact_label:
        tokens.add(compact_label)
    if year:
        tokens.add(year)
        if compact_key:
            tokens.add(f"{compact_key}{year}")
        if compact_label:
            tokens.add(f"{compact_label}{year}")
    for name in problem_author_names(problem, include_unknown=False):
        tokens.add(name.lower())
        compact_author = re.sub(r"[^a-z0-9Р°-СЏС‘]+", "", name.lower())
        if compact_author:
            tokens.add(compact_author)
    tokens.update(problem_source_search_values(problem))
    tokens.add("with_solution" if has_real_solution(problem) else "without_solution")
    tokens.update(external_problem_refs(problem))
    return sorted(token for token in tokens if token)


def normalize_external_problem_ref(value):
    text = str(value).lower().replace("_", "-")
    for pattern in EXTERNAL_PROBLEM_REF_PATTERNS:
        match = pattern.search(text)
        if match:
            section = match.group("section").lower()
            return f"memo-{match.group('year')}-{section}{int(match.group('number'))}"
    return ""


def external_problem_refs(problem):
    refs = set()
    fields = [
        problem.get("id", ""),
        problem.get("title", ""),
        collect_text(problem.get("problem_profile", {})),
        collect_text(problem.get("statements", {})),
        collect_text(problem.get("ideas", [])),
        collect_text(problem.get("solutions", [])),
        collect_text(problem.get("sources", [])),
        collect_text(problem.get("editorial", {})),
    ]
    for field in fields:
        text = str(field).lower().replace("_", "-")
        for pattern in EXTERNAL_PROBLEM_REF_PATTERNS:
            for match in pattern.finditer(text):
                section = match.group("section").lower()
                refs.add(f"memo-{match.group('year')}-{section}{int(match.group('number'))}")
    return sorted(refs)


def problem_source_values(problem):
    return problem_source_search_values(problem)


def relation_neighbors(problem_id, relations):
    for relation in relations:
        if relation["from"] == problem_id:
            yield relation["to"], relation, "forward"
        elif relation["to"] == problem_id:
            yield relation["from"], relation, "backward"
