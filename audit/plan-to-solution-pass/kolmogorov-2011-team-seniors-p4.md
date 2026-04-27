# Kolmogorov 2011 Team Seniors Problem 4

## Verdict

`ai_checked`. The compressed official solution was sufficient to reconstruct a complete proof. I expanded the color-graph argument: a longest trail in one color's diagonal graph must have endpoints at two odd cube-corner vertices; after deleting the trail, the other two odd cube corners remain connected in the unused graph, forcing at least `11` unused edges. Hence at most `6 * 11^2 - 11 = 715` cell centers can be visited, so `720` is impossible.

## Changed Files

- `data/problems/kolmogorov/kolmogorov-2011-team-olympiad-seniors-problem-4.yaml`
- `audit/plan-to-solution-pass/kolmogorov-2011-team-seniors-p4.md`

## Tests

- passed: `python tools/validate.py`
- passed: `python tools/check_links.py`
- passed: target file parses as JSON via `ConvertFrom-Json`
- passed: `git diff --check` for the target files
