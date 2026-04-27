# Kolmogorov 2011 Team Juniors Problem 6

## Verdict

`ai_checked`. The compressed plan was sufficient to reconstruct a full solution.

The expanded solution makes explicit the auxiliary graph of same-color cell diagonals, proves the upper bound by deleting the trail and using the four odd cube vertices, and gives a matching construction by deleting a length-`15` diagonal path on one face so that the remaining graph is connected with exactly two odd vertices.

## Changed Files

- `data/problems/kolmogorov/kolmogorov-2011-team-olympiad-juniors-problem-6.yaml`
- `audit/plan-to-solution-pass/kolmogorov-2011-team-juniors-p6.md`

## Tests

- Passed: `python tools/validate.py`
- Passed: `python tools/check_links.py`
