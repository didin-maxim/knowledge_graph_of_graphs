# Kolmogorov 2007 Team Seniors Problem 7

## Verdict

`ai_checked`. The compressed official solution was sufficient to reconstruct a complete proof. I expanded the graph-of-acquaintances argument by comparing two `m`-person groups that differ in one vertex; this proves every two vertices have the same adjacency pattern toward any third vertex, hence all pairs have the same status. Since the statement says there is at least one acquaintance pair, the graph is complete and the answer is `n(n-1)/2`.

## Changed Files

- `data/problems/kolmogorov/kolmogorov-2007-team-olympiad-seniors-problem-7.yaml`
- `audit/plan-to-solution-pass/kolmogorov-2007-team-seniors-p7.md`

## Tests

- passed: `python tools/validate.py`
- passed: `python tools/check_links.py`
- passed: target file parses as JSON via `ConvertFrom-Json`
- passed: `git diff --check` for the target files
