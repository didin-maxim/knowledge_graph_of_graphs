# Kolmogorov 2004 Round 3 Higher League Problem 10

## Verdict

`deferred_needs_source_or_reconstruction`.

The current YAML contains only a compressed official summary. It identifies the contradiction setup and the choice of a maximal strongly connected component `K` of `G-a`, but it does not state the key restrictions on arcs between `K` and the rest of the graph, nor the detailed contradiction with the condition that each vertex has at least two outgoing edges.

Per the pass instructions, I did not reconstruct or invent the missing proof. The YAML now records the deferred verdict while keeping the solution status as `needs_human_review`, because `deferred_needs_source_or_reconstruction` is a repair marker rather than the normal solution status.

## Changed Files

- `data/problems/kolmogorov/kolmogorov-2004-round3-higher-league-problem-10.yaml`
- `audit/plan-to-solution-pass/kolmogorov-2004-round3-higher-p10.md`

## Tests

- Failed: `python tools/validate.py`
  - Blocked by unrelated relation errors in `data/relations/relations.yaml`: `rel-kolm-2003-2004-critical-strong-digraphs` and `rel-kolm-2003-connectivity-imo-2013-c6` reference unknown `from_solution_id sol-official-compressed`.
- Passed: `python tools/check_links.py`
- Passed: targeted parse check for `data/problems/kolmogorov/kolmogorov-2004-round3-higher-league-problem-10.yaml`
- Passed: `git diff --check` for the target problem file and this audit report
