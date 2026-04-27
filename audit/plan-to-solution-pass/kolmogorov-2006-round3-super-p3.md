# Kolmogorov 2006 Round 3 Super League Problem 3

## Verdict

`deferred_needs_source_or_reconstruction`.

The current YAML contains only a compressed official summary. It identifies the contradiction setup, the use of induced subgraphs on two colors, Kempe-style recoloring by connected components, and a final degree/counting contradiction, but it does not state the key structural lemma or the actual count that forces the contradiction.

Per the pass instructions, I did not reconstruct or invent the missing proof. The YAML now records the deferred verdict while keeping the solution status as `needs_human_review`, because `deferred_needs_source_or_reconstruction` is a repair marker rather than the normal solution status.

## Changed Files

- `data/problems/kolmogorov/kolmogorov-2006-round-3-super-league-problem-3.yaml`
- `audit/plan-to-solution-pass/kolmogorov-2006-round3-super-p3.md`

## Tests

- Failed: `python tools/validate.py`
  - Blocked by unrelated relation errors in `data/relations/relations.yaml`: `rel-kolm-2005-junior-senior-spanning-tree-parity` references unknown `from_solution_id sol-official-expanded`; `rel-kolm-2003-2004-critical-strong-digraphs` references unknown `from_solution_id sol-official-compressed`; `rel-kolm-2008-wheel-first-second-league` references unknown `from_solution_id sol-official-expanded`; `rel-kolm-2003-connectivity-imo-2013-c6` references unknown `from_solution_id sol-official-compressed`.
- Passed: `python tools/check_links.py`
- Passed: targeted parse check for `data/problems/kolmogorov/kolmogorov-2006-round-3-super-league-problem-3.yaml`
- Passed: `git diff --check` for the target problem file and this audit report
