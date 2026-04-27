# Kolmogorov 2012 Individual Seniors P6

Verdict: `deferred_needs_source_or_reconstruction`.

The current YAML contains only a compressed official summary. It gives the answer and the high-level graph model, but the proof-critical parts are underspecified: the diagonal-cut lower bound is summarized without the detailed count, and the construction that deletes exactly `4n - 4` directed edges/short paths is not described explicitly enough to verify the Eulerian/path argument.

Per the pass instructions, I did not reconstruct or invent the missing proof. The YAML now records the deferred verdict while keeping the solution status as `needs_human_review`, because `deferred_needs_source_or_reconstruction` is not an allowed taxonomy status.

Changed files:

- `data/problems/kolmogorov/kolmogorov-2012-individual-olympiad-seniors-problem-6.yaml`
- `audit/plan-to-solution-pass/kolmogorov-2012-individual-seniors-p6.md`

Tests:

- Passed: `python tools/validate.py`
- Passed: `python tools/check_links.py`
