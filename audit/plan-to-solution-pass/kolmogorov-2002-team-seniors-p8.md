# Kolmogorov 2002 Team Seniors P8

Verdict: `deferred_needs_source_or_reconstruction`.

The current YAML contains only a compressed official summary. It names the two main lemmas, but does not give enough detail to safely expand the solution: Lemma 2 leaves the parameter `k` and the induced-subgraph reduction underspecified, and the Hall/minimal-counterexample proof of Lemma 1 is only referenced.

Per the pass instructions, I did not reconstruct or invent the missing proof. The YAML now records the deferred verdict while keeping the solution status as `needs_human_review`, because `deferred_needs_source_or_reconstruction` is not an allowed taxonomy status.

Changed files:

- `data/problems/kolmogorov/kolmogorov-2002-team-olympiad-seniors-problem-8.yaml`
- `audit/plan-to-solution-pass/kolmogorov-2002-team-seniors-p8.md`

Tests:

- Passed: `python tools/validate.py`
- Passed: `python tools/check_links.py`
