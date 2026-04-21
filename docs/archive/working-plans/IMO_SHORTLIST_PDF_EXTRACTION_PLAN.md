# IMO Shortlist PDF Extraction Plan

## Why Extract First

It is more memory-efficient to extract all combinatorics problems from a shortlist PDF into a small structured file before doing mathematical analysis.

The full PDF contains algebra, geometry, number theory, figures, repeated headers, and long solutions. Keeping it in context wastes space. A compact extraction lets the import pass work from short records instead of PDF pages.

## Recommended Intermediate Format

Use one JSON-compatible file per year, for example:

`data/import_batches/extracted/imo-2024-combinatorics-extract.json`

Suggested shape:

```json
{
  "year": 2024,
  "source_ids": ["src-imo-2024-shortlist"],
  "problems": [
    {
      "shortlist_id": "C8",
      "contest_id": null,
      "country": "Peru",
      "statement_ru_draft": "...",
      "statement_en_summary": "...",
      "answer_summary": "...",
      "solution_summaries": [
        {
          "label": "Solution 1",
          "graph_role": "central",
          "ru_summary": "..."
        }
      ],
      "graph_signal": {
        "in_statement": false,
        "in_solution": true,
        "objects": ["tree", "grid_board", "l_tromino"],
        "methods": ["tree_cycle_contradiction", "induction"]
      },
      "decision": "candidate",
      "decision_reason": "..."
    }
  ]
}
```

## Extraction Pass

For each `C*` problem, extract only:

- exact shortlist id;
- whether it appeared on the actual IMO paper;
- source country;
- concise Russian draft of the statement;
- answer, if present;
- list of published solutions;
- graph role: `none`, `weak`, `statement`, `central_solution`;
- graph objects and methods;
- skip/add decision with reason.

Do not extract full solution prose unless the problem is already a strong candidate.

## Analysis Pass

Analyze only records with:

- `graph_role = "statement"`; or
- `graph_role = "central_solution"`.

For each candidate, then reopen only the relevant PDF pages/lines if needed to check exact solution details.

## Memory Rule

The active context should contain at most:

- the extraction record for the current problem;
- 3-5 likely related local database cards;
- selected relation suggestions;
- current validation errors, if any.

Everything else should live in files, not in chat context.

