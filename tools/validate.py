import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

from lib import (
    ROOT,
    load_comments,
    load_definitions,
    load_import_batches,
    load_problems,
    load_relations,
    load_sources,
    load_standard_ideas,
    load_taxonomy,
)


def add_error(errors, path, message):
    errors.append(f"{path}: {message}")


def ids(items):
    return {item["id"] for item in items}


def statement_source_ids(statement):
    source_ids = []
    if statement.get("source_id"):
        source_ids.append(statement["source_id"])
    source_ids.extend(statement.get("source_ids", []))
    return source_ids


def validate_shared_statement_group(errors, path, section_name, statement):
    group = statement.get("shared_statement_group")
    if group is None:
        return
    prefix = f"{section_name} statement {statement.get('id')} shared_statement_group"
    if not isinstance(group, dict):
        add_error(errors, path, f"{prefix} must be an object")
        return
    for field in ["id", "case_id"]:
        if not isinstance(group.get(field), str) or not group.get(field).strip():
            add_error(errors, path, f"{prefix}.{field} must be a non-empty string")
    if "note" in group and not isinstance(group.get("note"), str):
        add_error(errors, path, f"{prefix}.note must be a string")


def has_encoding_damage(text):
    damaged_markers = ["???", "Рџ", "Рњ", "Рљ", "Р°", "СЃ", "С‚", "С‡"]
    return any(marker in text for marker in damaged_markers)


def graph_theory_statement_problems(text):
    lowered = re.sub(r"\s+", " ", text.lower()).strip()
    problems = []

    meta_markers = [
        "в официальном решении",
        "в одном из решений",
        "одно из решений",
        "построим граф",
        "построим двудольный граф",
        "строится",
        "представляется",
        "изучается через",
        "задача спрашивает",
        "модель присутствует",
    ]
    for marker in meta_markers:
        if marker in lowered:
            problems.append(f"meta or solution-language marker '{marker}'")

    summary_starts = [
        "это задача",
        "это игра",
        "это красно-синяя раскраска",
        "карточка фиксирует",
    ]
    for marker in summary_starts:
        if lowered.startswith(marker):
            problems.append(f"summary-like start '{marker}'")

    if "стремится" in lowered:
        problems.append("game goal is described as a role summary, not a rule")

    has_task_verb = any(
        marker in lowered
        for marker in [
            "докаж",
            "найд",
            "определ",
            "каково",
            "какие",
            "можно ли",
            "обязательно ли",
            "существует ли",
            "требуется",
        ]
    )
    has_setup = any(
        marker in lowered
        for marker in [
            "дан",
            "пусть",
            "рассмотрим",
            "на окружности",
            "изначально",
            "неизвестен",
            "разрешено",
        ]
    )
    if len(lowered) < 180 and "нужно" in lowered and not (has_setup and has_task_verb):
        problems.append("too compressed: uses 'нужно' without a full setup and task")

    return problems


def normalize_statement_text(text):
    text = text.lower()
    text = re.sub(r"\\\(|\\\)|\\\[|\\\]", " ", text)
    replacements = {
        "\\deg": "deg",
        "\\ge": ">=",
        "\\le": "<=",
        "|v(g)|": "n",
        "число вершин графа": "n",
        "гамильтонов цикл": "цикл проходящий через все вершины ровно один раз",
        "гамильтонова цикла": "цикл проходящий через все вершины ровно один раз",
        "то есть": " ",
        "иначе говоря": " ",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"[{}_,.;:()—–-]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def statement_similarity(left, right):
    left_norm = normalize_statement_text(left)
    right_norm = normalize_statement_text(right)
    sequence = SequenceMatcher(None, left_norm, right_norm).ratio()
    left_tokens = {token for token in left_norm.split() if len(token) > 1}
    right_tokens = {token for token in right_norm.split() if len(token) > 1}
    if not left_tokens or not right_tokens:
        return sequence
    containment = len(left_tokens & right_tokens) / min(len(left_tokens), len(right_tokens))
    return max(sequence, containment)


def main():
    errors = []
    problems = load_problems()
    relations = load_relations()
    sources = load_sources()
    definitions = load_definitions()
    standard_ideas = load_standard_ideas()
    comments = load_comments()
    import_batches = load_import_batches()
    statuses = set(load_taxonomy("statuses.yaml", "statuses"))
    relations_statuses = set(load_taxonomy("relations-statuses.yaml", "relations_statuses"))
    comment_kinds = set(load_taxonomy("comment-kinds.yaml", "comment_kinds"))
    comment_statuses = set(load_taxonomy("comment-statuses.yaml", "comment_statuses"))
    tags = set(load_taxonomy("tags.yaml", "tags"))
    relation_types = set(load_taxonomy("relation-types.yaml", "relation_types"))
    difficulty_levels = set(load_taxonomy("difficulty.yaml", "difficulty_levels"))
    properties = set(load_taxonomy("properties.yaml", "properties"))
    sourced_statement_records = []

    for problem_id, problem in problems.items():
        path = problem["_path"]
        for field in ["id", "title", "statements", "ideas", "solutions", "difficulty", "tags", "sources", "editorial"]:
            if field not in problem:
                add_error(errors, path, f"missing required field {field}")

        statements = problem.get("statements", {})
        if not statements.get("original"):
            add_error(errors, path, "missing original statement")
        editorial = problem.get("editorial", {})
        graph_theory_optional = (
            editorial.get("graph_theory_duplicate_removed")
            or (
                "graph_in_solution" in problem.get("kind", {}).get("secondary", [])
                and editorial.get("graph_theory_absent_reason")
            )
        )
        if not statements.get("graph_theory") and not graph_theory_optional:
            add_error(errors, path, "missing graph_theory statement, graph_theory_duplicate_removed flag, or graph_theory_absent_reason for graph_in_solution card")

        local_solution_ids = ids(problem.get("solutions", []))
        local_idea_ids = ids(problem.get("ideas", []))
        statement_items = []

        for tag in problem.get("tags", []):
            if tag not in tags:
                add_error(errors, path, f"unknown tag {tag}")

        for prop in problem.get("properties", {}):
            if prop not in properties:
                add_error(errors, path, f"unknown property {prop}")

        profile = problem.get("problem_profile")
        if profile is not None:
            if not isinstance(profile, dict):
                add_error(errors, path, "problem_profile must be an object")
            else:
                for key in [
                    "objects",
                    "methods",
                    "transformations",
                    "goal",
                    "auxiliary_graph_type",
                    "invariants",
                    "keywords",
                ]:
                    if key in profile and not isinstance(profile[key], list):
                        add_error(errors, path, f"problem_profile.{key} must be a list")
                status = profile.get("status")
                if status and status not in statuses:
                    add_error(errors, path, f"unknown problem_profile status {status}")

        difficulty = problem.get("difficulty", {})
        if difficulty.get("main") not in difficulty_levels:
            add_error(errors, path, f"unknown difficulty {difficulty.get('main')}")
        if difficulty.get("status") not in statuses:
            add_error(errors, path, f"unknown difficulty status {difficulty.get('status')}")

        for section_name in ["original", "graph_theory", "olympiad_reformulations"]:
            for statement in statements.get(section_name, []):
                statement_items.append((section_name, statement.get("id"), statement.get("text", "")))
                if not statement.get("text"):
                    add_error(errors, path, f"{section_name} statement {statement.get('id')} has empty text")
                elif has_encoding_damage(statement.get("text", "")):
                    add_error(errors, path, f"{section_name} statement {statement.get('id')} looks like damaged encoding")
                if section_name == "graph_theory":
                    for statement_problem in graph_theory_statement_problems(statement.get("text", "")):
                        add_error(
                            errors,
                            path,
                            f"graph_theory statement {statement.get('id')} is not self-contained: {statement_problem}",
                        )
                if statement.get("status") not in statuses:
                    add_error(errors, path, f"unknown statement status {statement.get('status')}")
                self_contained = statement.get("self_contained")
                if not isinstance(self_contained, dict):
                    add_error(errors, path, f"{section_name} statement {statement.get('id')} missing self_contained check")
                elif self_contained.get("status") not in statuses:
                    add_error(errors, path, f"unknown self_contained status {self_contained.get('status')}")
                elif self_contained.get("status") in {"needs_review", "needs_human_review", "disputed"} and not statement.get("review_notes"):
                    add_error(errors, path, f"{section_name} statement {statement.get('id')} needs review_notes for uncertain self_contained status")
                definition_ids = statement.get("definition_ids")
                if not isinstance(definition_ids, list):
                    add_error(errors, path, f"{section_name} statement {statement.get('id')} missing definition_ids list")
                else:
                    for definition_id in definition_ids:
                        if definition_id not in definitions:
                            add_error(errors, path, f"{section_name} statement {statement.get('id')} references unknown definition {definition_id}")
                source_ids = statement.get("source_ids")
                if source_ids is not None and not isinstance(source_ids, list):
                    add_error(errors, path, f"{section_name} statement {statement.get('id')} source_ids must be a list")
                validate_shared_statement_group(errors, path, section_name, statement)
                shared_group = statement.get("shared_statement_group") or {}
                for source_id in statement_source_ids(statement):
                    if source_id not in sources:
                        add_error(errors, path, f"unknown statement source {source_id}")
                    sourced_statement_records.append(
                        {
                            "problem_id": problem_id,
                            "path": path,
                            "section": section_name,
                            "statement_id": statement.get("id"),
                            "source_id": source_id,
                            "text": normalize_statement_text(statement.get("text", "")),
                            "shared_group_id": shared_group.get("id"),
                            "shared_case_id": shared_group.get("case_id"),
                        }
                    )

        for index, left in enumerate(statement_items):
            for right in statement_items[index + 1 :]:
                left_section, left_id, left_text = left
                right_section, right_id, right_text = right
                left_statement = next(item for item in statements[left_section] if item.get("id") == left_id)
                right_statement = next(item for item in statements[right_section] if item.get("id") == right_id)
                if right_id in left_statement.get("distinct_from", []) or left_id in right_statement.get("distinct_from", []):
                    continue
                if left_section == right_section == "olympiad_reformulations":
                    continue
                similarity = statement_similarity(left_text, right_text)
                if similarity >= 0.66:
                    add_error(
                        errors,
                        path,
                        f"duplicate-like statements {left_section}/{left_id} and {right_section}/{right_id} similarity={similarity:.2f}",
                    )

        for idea in problem.get("ideas", []):
            if idea.get("status") not in statuses:
                add_error(errors, path, f"unknown idea status {idea.get('status')}")
            for tag in idea.get("tags", []):
                if tag not in tags:
                    add_error(errors, path, f"unknown idea tag {tag}")

        for solution in problem.get("solutions", []):
            if solution.get("status") not in statuses:
                add_error(errors, path, f"unknown solution status {solution.get('status')}")
            for idea_id in solution.get("idea_ids", []):
                if idea_id not in local_idea_ids:
                    add_error(errors, path, f"solution references unknown idea {idea_id}")
            standard_idea_ids = solution.get("standard_idea_ids")
            if not isinstance(standard_idea_ids, list):
                add_error(errors, path, f"solution {solution.get('id')} missing standard_idea_ids list")
            else:
                for standard_idea_id in standard_idea_ids:
                    if standard_idea_id not in standard_ideas:
                        add_error(errors, path, f"solution {solution.get('id')} references unknown standard idea {standard_idea_id}")

        statement_ids = {
            statement_id
            for _section_name, statement_id, _text in statement_items
            if statement_id
        }
        for source in problem.get("sources", []):
            if source.get("source_id") not in sources:
                add_error(errors, path, f"unknown source {source.get('source_id')}")
            if source.get("status") not in statuses:
                add_error(errors, path, f"unknown source status {source.get('status')}")
            scoped_statement_ids = source.get("statement_ids")
            if scoped_statement_ids is not None:
                if not isinstance(scoped_statement_ids, list):
                    add_error(errors, path, f"source {source.get('source_id')} statement_ids must be a list")
                else:
                    for statement_id in scoped_statement_ids:
                        if statement_id not in statement_ids:
                            add_error(errors, path, f"source {source.get('source_id')} references unknown statement {statement_id}")

        review_status = problem.get("editorial", {}).get("review_status")
        if review_status not in statuses:
            add_error(errors, path, f"unknown review status {review_status}")
        relations_status = problem.get("editorial", {}).get("relations_status")
        if relations_status not in relations_statuses:
            add_error(errors, path, f"unknown relations status {relations_status}")

    records_by_statement_source = {}
    for record in sourced_statement_records:
        if not record["source_id"] or not record["text"]:
            continue
        key = (record["source_id"], record["text"])
        records_by_statement_source.setdefault(key, []).append(record)
    for (source_id, _text), records in records_by_statement_source.items():
        problem_ids = {record["problem_id"] for record in records}
        if len(problem_ids) <= 1:
            continue
        group_ids = {record.get("shared_group_id") for record in records if record.get("shared_group_id")}
        missing = [record for record in records if not record.get("shared_group_id") or not record.get("shared_case_id")]
        if missing or len(group_ids) != 1:
            locations = ", ".join(
                f"{record['problem_id']}#{record['statement_id']}"
                for record in records
            )
            add_error(
                errors,
                "data/problems",
                f"same statement text and source {source_id} appear in multiple cards without one shared_statement_group: {locations}",
            )
            continue
        case_to_problem = {}
        for record in records:
            case_id = record.get("shared_case_id")
            previous = case_to_problem.setdefault(case_id, record["problem_id"])
            if previous != record["problem_id"]:
                add_error(
                    errors,
                    "data/problems",
                    f"shared_statement_group {next(iter(group_ids))} reuses case_id {case_id} for both {previous} and {record['problem_id']}",
                )

    for source_id, source in sources.items():
        url = source.get("url", "")
        if not (url.startswith("https://") or url.startswith("http://")):
            add_error(errors, "data/sources/sources.yaml", f"{source_id}: source url must be browser-openable http(s) link")
        if source.get("status") not in statuses:
            add_error(errors, "data/sources/sources.yaml", f"{source_id}: unknown source status {source.get('status')}")
        if "browser_openable" not in source:
            add_error(errors, "data/sources/sources.yaml", f"{source_id}: missing browser_openable flag")

    for definition_id, definition in definitions.items():
        if not definition.get("title"):
            add_error(errors, "data/definitions/definitions.yaml", f"{definition_id}: missing title")
        if not definition.get("text"):
            add_error(errors, "data/definitions/definitions.yaml", f"{definition_id}: missing text")
        if not definition.get("examples"):
            add_error(errors, "data/definitions/definitions.yaml", f"{definition_id}: missing examples")
        if definition.get("status") not in statuses:
            add_error(errors, "data/definitions/definitions.yaml", f"{definition_id}: unknown status {definition.get('status')}")
        aliases = definition.get("aliases")
        if not isinstance(aliases, list) or not aliases:
            add_error(errors, "data/definitions/definitions.yaml", f"{definition_id}: missing aliases")

    for idea_id, idea in standard_ideas.items():
        if not idea.get("title"):
            add_error(errors, "data/standard_ideas/standard-ideas.yaml", f"{idea_id}: missing title")
        if not idea.get("text"):
            add_error(errors, "data/standard_ideas/standard-ideas.yaml", f"{idea_id}: missing text")
        if not idea.get("examples"):
            add_error(errors, "data/standard_ideas/standard-ideas.yaml", f"{idea_id}: missing examples")
        if idea.get("status") not in statuses:
            add_error(errors, "data/standard_ideas/standard-ideas.yaml", f"{idea_id}: unknown status {idea.get('status')}")
        aliases = idea.get("aliases")
        if not isinstance(aliases, list) or not aliases:
            add_error(errors, "data/standard_ideas/standard-ideas.yaml", f"{idea_id}: missing aliases")

    relation_ids = set()
    for relation in relations:
        rid = relation.get("id", "<missing>")
        if rid in relation_ids:
            add_error(errors, "data/relations/relations.yaml", f"duplicate relation id {rid}")
        relation_ids.add(rid)

        for endpoint in ["from", "to"]:
            if relation.get(endpoint) not in problems:
                add_error(errors, "data/relations/relations.yaml", f"{rid}: unknown {endpoint} problem {relation.get(endpoint)}")
        if relation.get("type") not in relation_types:
            add_error(errors, "data/relations/relations.yaml", f"{rid}: unknown relation type {relation.get('type')}")
        if relation.get("status") not in statuses:
            add_error(errors, "data/relations/relations.yaml", f"{rid}: unknown status {relation.get('status')}")
        if not relation.get("forward_text") or not relation.get("backward_text"):
            add_error(errors, "data/relations/relations.yaml", f"{rid}: relation must have forward_text and backward_text")
        distance = relation.get("distance")
        if not isinstance(distance, int) or not 1 <= distance <= 5:
            add_error(errors, "data/relations/relations.yaml", f"{rid}: distance must be integer from 1 to 5")

        anchors = relation.get("anchors", {})
        for side, problem_key in [("from_solution_id", "from"), ("to_solution_id", "to")]:
            solution_id = anchors.get(side)
            if solution_id and relation.get(problem_key) in problems:
                solution_ids = ids(problems[relation[problem_key]].get("solutions", []))
                if solution_id not in solution_ids:
                    add_error(errors, "data/relations/relations.yaml", f"{rid}: unknown {side} {solution_id}")

    import_statuses = {"candidate", "added", "skipped", "duplicate", "needs_review", "needs_human_review", "ai_checked"}
    import_batch_ids = set()
    for batch in import_batches:
        path = batch.get("_path", "data/import_batches")
        batch_id = batch.get("id", "<missing>")
        if batch_id in import_batch_ids:
            add_error(errors, path, f"duplicate import batch id {batch_id}")
        import_batch_ids.add(batch_id)
        for field in ["id", "title", "source_scope", "items", "status"]:
            if field not in batch:
                add_error(errors, path, f"missing required field {field}")
        if batch.get("status") not in statuses and batch.get("status") not in import_statuses:
            add_error(errors, path, f"unknown import batch status {batch.get('status')}")
        source_scope = batch.get("source_scope", {})
        if not isinstance(source_scope, dict):
            add_error(errors, path, "source_scope must be an object")
        else:
            for source_id in source_scope.get("source_ids", []):
                if source_id not in sources:
                    add_error(errors, path, f"source_scope references unknown source {source_id}")
        seen_item_ids = set()
        for item in batch.get("items", []):
            item_id = item.get("id", "<missing>")
            if item_id in seen_item_ids:
                add_error(errors, path, f"duplicate import item id {item_id}")
            seen_item_ids.add(item_id)
            status = item.get("status")
            if status not in import_statuses:
                add_error(errors, path, f"{item_id}: unknown import item status {status}")
            for source_id in item.get("source_ids", []):
                if source_id not in sources:
                    add_error(errors, path, f"{item_id}: references unknown source {source_id}")
            problem_id = item.get("problem_id")
            if status == "added" and problem_id not in problems:
                add_error(errors, path, f"{item_id}: added item references unknown problem_id {problem_id}")
            profile = item.get("problem_profile")
            if profile is not None and not isinstance(profile, dict):
                add_error(errors, path, f"{item_id}: problem_profile must be an object")

    for comment_id, comment in comments.items():
        path = comment.get("_path", "data/comments")
        for field in ["id", "target", "kind", "title", "text", "author", "created_at", "status"]:
            if field not in comment:
                add_error(errors, path, f"{comment_id}: missing required field {field}")
        if comment.get("kind") not in comment_kinds:
            add_error(errors, path, f"{comment_id}: unknown comment kind {comment.get('kind')}")
        if comment.get("status") not in comment_statuses:
            add_error(errors, path, f"{comment_id}: unknown comment status {comment.get('status')}")
        target = comment.get("target")
        if not isinstance(target, dict):
            add_error(errors, path, f"{comment_id}: target must be an object")
        else:
            target_type = target.get("type")
            if target_type not in {"problem", "architecture"}:
                add_error(errors, path, f"{comment_id}: unknown target type {target_type}")
            if target_type == "problem":
                problem_id = target.get("problem_id")
                if problem_id not in problems:
                    add_error(errors, path, f"{comment_id}: unknown target problem_id {problem_id}")
            if target_type == "architecture" and target.get("problem_id"):
                add_error(errors, path, f"{comment_id}: architecture comment must not contain problem_id")
        response = comment.get("response")
        if response is not None:
            if not isinstance(response, dict):
                add_error(errors, path, f"{comment_id}: response must be an object")
            else:
                response_status = response.get("status")
                if response_status and response_status not in comment_statuses:
                    add_error(errors, path, f"{comment_id}: unknown response status {response_status}")
        editorial = comment.get("editorial")
        if editorial is not None and not isinstance(editorial, dict):
            add_error(errors, path, f"{comment_id}: editorial must be an object")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"OK: {len(problems)} problems, {len(relations)} relations, {len(comments)} comments, "
        f"{len(sources)} sources, {len(definitions)} definitions, {len(standard_ideas)} standard ideas, "
        f"{len(import_batches)} import batches."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
