# IMO / IMO Shortlist Import Plan

## Scope

Import only combinatorics problems from IMO and IMO Shortlist.
In shortlist PDFs, combinatorics problems are labelled `C1`, `C2`, ...

A problem belongs in this graph database only if:

- a graph, grid graph, matching, tree, path, cycle, colouring graph, or similar graph object appears in the statement; or
- a graph is central in at least one published solution.

Skip beautiful combinatorics problems when the graph connection is only cosmetic, optional, or appears only in a comment that is not part of the solution.

All statements, ideas, and solutions in problem cards are written in Russian.

## Per-Year Workflow

1. Locate official sources:
   - official IMO problem PDF for the contest problems;
   - official IMO Shortlist PDF with solutions.
2. Extract the shortlist combinatorics section into a lightweight local file.
3. For each `C*` problem, record:
   - statement summary;
   - solution count;
   - whether a graph appears in the statement;
   - whether a graph is central in a solution;
   - preliminary decision: `candidate`, `skipped`, `duplicate`, or `needs_review`.
4. Analyze only candidates deeply.
5. Add one problem card at a time.
6. For each card:
   - translate the statement into Russian;
   - add a graph-theory statement only if it is genuinely standalone and equivalent;
   - otherwise use `graph_in_solution` and explain the absence of a graph statement;
   - include all substantive published solutions, translated and compressed;
   - fill `problem_profile`, tags, ideas, solutions, difficulty, sources, and editorial fields.
7. Search duplicates and relatives:
   - `python tools/search.py query "<keywords>"`
   - `python tools/suggest_relations.py --problem <id>`
   - manually reject weak suggestions.
8. Add relations only with meaningful `forward_text`, `backward_text`, and valid anchors.
9. Update the import batch.
10. Run:
   - `python tools/validate.py`
   - `python tools/check_links.py`
   - `python tools/build_index.py`
   - `python tools/build_viewer.py`

## Context Discipline

Do not keep full PDF excerpts in active context after extraction.

After finishing a card, keep only:

- problem id;
- source ids;
- added files;
- relation ids;
- validation status;
- unresolved doubts.

Then compact before moving to the next problem or year.

