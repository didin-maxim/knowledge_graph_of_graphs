# Kolmogorov 2003 Team Seniors Problem 8

## Verdict

`ai_checked`. The locally available compressed official summary was sufficient to reconstruct a complete solution. The expanded proof uses the standard ear-building argument for a minimally strongly connected oriented graph and proves the bound `m <= 2n - 3`, matching the construction with `197` roads.

## Changed Files

- `data/problems/kolmogorov/kolmogorov-2003-team-olympiad-seniors-problem-8.yaml`
- `audit/plan-to-solution-pass/kolmogorov-2003-team-seniors-p8.md`

## Tests

- `python tools/validate.py` - failed before reaching this problem because `data/problems/usamo/usamo-2024-p3-balanced-regular-polygon-triangulation.yaml` has an unrelated pre-existing JSON escape error: `Invalid \escape: line 102 column 566`.
- `python tools/check_links.py` - failed for the same unrelated pre-existing JSON escape error in `data/problems/usamo/usamo-2024-p3-balanced-regular-polygon-triangulation.yaml`.
- Targeted parse check for `data/problems/kolmogorov/kolmogorov-2003-team-olympiad-seniors-problem-8.yaml` - passed.
