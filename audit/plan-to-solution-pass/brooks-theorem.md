# Brooks theorem plan-to-solution pass

verdict: expanded_to_full_solution

changed files:
- data/problems/classical/brooks-theorem.yaml
- audit/plan-to-solution-pass/brooks-theorem.md

notes:
- Current YAML contained only a proof scheme and explicitly said the full proof needed case analysis.
- Replaced the sketch with a complete proof covering Delta <= 2, non-regular connected graphs, cut-vertex decomposition, and the 2-connected regular case via the standard Brooks lemma and greedy ordering.
- Set the solution status to ai_checked.
- Also fixed a malformed LaTeX escape in the graph-theory statement.

tests:
- python tools/validate.py: OK
- python tools/check_links.py: OK
