# Active Plan: Extract IMO / IMO Shortlist Combinatorics

## Goal

Build a lightweight, readable catalogue of all available IMO and IMO Shortlist combinatorics problems, then identify which of them belong in this graph-problem database.

The database should receive only problems where:

- a graph or graph-like object appears in the statement; or
- at least one published solution uses graphs essentially.

Beautiful combinatorics problems with weak or cosmetic graph connections should be recorded as skipped, not added to the graph database.

## Source Scope

Use official IMO sources first:

- official IMO problem PDFs from `https://www.imo-official.org/problems.aspx`;
- official IMO Shortlist PDFs linked from the same page, usually named like `problems/IMO2024SL.pdf`.

Do not assume the year range manually. In the new chat, discover available years dynamically from the official IMO problems page and collect all years with available official problem PDFs and/or shortlist PDFs.

If an official shortlist PDF is unavailable for a year, record that year as unavailable rather than filling from unofficial sources.

## Main Output

Create a lightweight extraction dataset before adding any new problem cards.

Preferred output directory:

`data/import_batches/extracted/`

Preferred file naming:

- `imo-YYYY-combinatorics-extract.json`
- optionally, one aggregate index: `imo-combinatorics-extract-index.json`

The extracted files should be JSON-compatible and easy to review.

## Per-Year Extraction Format

Each year file should contain records like:

```json
{
  "year": 2024,
  "source_ids": ["src-imo-2024-problems-eng", "src-imo-2024-shortlist"],
  "availability": {
    "official_problem_pdf": true,
    "official_shortlist_pdf": true
  },
  "problems": [
    {
      "id": "imo-2024-sl-c8",
      "shortlist_id": "C8",
      "contest_problem": null,
      "country": "Peru",
      "statement_ru": "...",
      "source": {
        "source_id": "src-imo-2024-shortlist",
        "pdf_url": "https://www.imo-official.org/problems/IMO2024SL.pdf",
        "page_hint": "Shortlisted problems, Combinatorics C8"
      },
      "solutions": [
        {
          "label": "Solution 1",
          "ru_summary": "...",
          "graph_role": "central_solution",
          "graph_objects": ["tree", "grid_board"],
          "graph_methods": ["cycle_contradiction", "halving"]
        }
      ],
      "graph_signal": {
        "in_statement": false,
        "in_solution": true,
        "strength": "central",
        "reason": "The official solution builds a tree from colouring operations."
      },
      "decision": "candidate",
      "decision_reason": "Graph is essential in the official solution."
    }
  ]
}
```

## Decision Labels

Use these labels consistently:

- `candidate`: should be considered for a database card.
- `added`: already added to the database.
- `skipped`: not graph-related enough.
- `duplicate`: already represented by an existing database card.
- `needs_review`: graph role or source status is unclear.

## Graph Role Labels

Use these labels for `graph_role`:

- `none`: no meaningful graph content.
- `weak`: optional or cosmetic graph interpretation only.
- `statement`: graph appears naturally in the problem statement.
- `central_solution`: a published solution essentially uses a graph.

Only `statement` and `central_solution` should normally become database cards.

## Workflow For New Chat

1. Read:
   - `docs/IMO_SHORTLIST_IMPORT_PLAN.md`
   - `docs/IMO_SHORTLIST_PDF_EXTRACTION_PLAN.md`
   - this file.
2. Discover official IMO PDF and shortlist availability from `imo-official.org`.
3. Create or update source entries in `data/sources/sources.yaml` only when a year is actually processed.
4. For each available year:
   - download or read the official problem PDF and shortlist PDF;
   - extract only combinatorics problems, especially shortlist `C*` problems;
   - translate each statement into Russian in concise but complete form;
   - summarize each published solution enough to identify methods and graph usage;
   - write the extraction file for that year.
5. Do not add database problem cards during the extraction pass unless explicitly asked.
6. After extraction, review all `candidate` records year by year.
7. Add database cards one at a time, with full relation search and validation after each card or small batch.

## Existing 2024 Status

The 2024 pass has already been added to the database.

Added:

- `imo-2024-c8-board-coloring-tree`
- `imo-2024-c3-knights-chord-uncrossing`
- `imo-2024-c4-turbo-grid-monsters`

Skipped in 2024:

- C1
- C2
- C5
- C6
- C7

Related files:

- `data/import_batches/imo-2024-combinatorics.yaml`
- `data/relations/relations.d/imo-2024.yaml`

When building the aggregate extraction catalogue, include 2024 by reading these existing database/import-batch files rather than redoing the full analysis unless verification is requested.

## Memory Discipline

Never keep full PDF text in active context.

For each year, keep only:

- source URLs and local filenames;
- extracted `C*` records;
- candidate list;
- current validation errors.

Once a year file is written, drop the PDF excerpts from context and continue from the extracted JSON.

For relation analysis, load only:

- the current candidate record;
- 3-5 likely related database cards;
- output of `tools/suggest_relations.py --problem <id>`.

## Validation Commands

When database cards are eventually added, run:

```powershell
python tools/validate.py
python tools/check_links.py
python tools/build_index.py
python tools/build_viewer.py
```

For extraction-only files, validate by loading the JSON with Python before relying on it.

