# Kolmogorov 2004 Round 2 Higher League Problem 9

## Verdict

`deferred_needs_source_or_reconstruction`.

The current YAML contains only a compressed official summary. It gives the high-level contradiction strategy: if every sufficiently long arithmetic progression contains an edge, then repeated densification should force a complete bipartite subgraph `K_{k,k}`, contradicting the absence of 4-cycles. However, the summary omits the actual counting and iteration estimates that make this implication rigorous.

I checked the obvious direct counting route for 5-term progressions, but it is not strong enough by itself: the crude upper bound on the number of 5-progressions containing a fixed edge leaves a numerical gap against the standard `C_4`-free edge bound. Therefore a complete solution would require the official source/OCR or a fresh reconstruction of the missing densification argument.

## Changed Files

- `data/problems/kolmogorov/kolmogorov-2004-round2-higher-league-problem-9.yaml`
- `audit/plan-to-solution-pass/kolmogorov-2004-round2-higher-p9.md`

## Tests

- Failed: `python tools/validate.py` stopped on unrelated pre-existing relation errors in `data/relations/relations.yaml`: `rel-kolm-2003-2004-critical-strong-digraphs` and `rel-kolm-2003-connectivity-imo-2013-c6` both reference unknown `from_solution_id sol-official-compressed`.
- Passed: `python tools/check_links.py`
- Passed: targeted JSON parse for `data/problems/kolmogorov/kolmogorov-2004-round2-higher-league-problem-9.yaml`
