# Card Merge Workflow

This note records the database convention for merging several near-duplicate
problem cards into one card with multiple statement versions.

## Statement-Level Sources

Use `source_ids` on a statement when several sources support that exact
formulation, or when the card has a parameterized main formulation but contest
sources support only fixed-parameter versions.

Legacy `source_id` remains supported.

```json
{
  "id": "stmt-contest-n2000",
  "title": "Contest version, n = 2000",
  "text": "...",
  "source_ids": ["src-example-official"],
  "status": "ai_checked",
  "self_contained": {"status": "ai_checked"},
  "definition_ids": ["complete_graph"]
}
```

## Scoped Bibliography Entries

Use `statement_ids` in the problem-level `sources` list when a source applies
only to specific statements rather than to the whole merged problem.

```json
{
  "source_id": "src-example-official",
  "role": "problem_and_solutions_official",
  "status": "source_verified",
  "statement_ids": ["stmt-contest-n2000"]
}
```

## Main Formulation

For a merged family, the main formulation may live in `graph_theory`, including
a parameterized version such as `K_n`. The original contest statements can stay
in `original` as source-scoped fixed cases.

If the same text is intentionally present in several statement groups, add
`distinct_from` between the statement IDs so duplicate detection knows the
duplication is editorially deliberate.

## Shared Source Statements Across Cards

Sometimes one published problem statement naturally splits into two independent
cards: for example, two numbered subparts, or two fundamentally different cases
with different solutions. In that situation the two cards may intentionally use
the same statement text and the same source.

Mark every copied statement with the same `shared_statement_group.id` and a
different `case_id`.

```json
{
  "id": "stmt-original",
  "title": "Original statement",
  "text": "...",
  "source_ids": ["src-example-official"],
  "shared_statement_group": {
    "id": "src-example-problem-7-two-cases",
    "case_id": "case-a",
    "note": "This card treats the first genuinely different case."
  },
  "status": "ai_checked",
  "self_contained": {"status": "ai_checked"},
  "definition_ids": ["graph"]
}
```

The validator treats an exact same statement+source pair across different
problem cards as an error unless the statements share one group id and use
distinct case ids.
