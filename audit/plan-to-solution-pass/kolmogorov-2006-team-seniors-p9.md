# Kolmogorov 2006 Team Olympiad Seniors Problem 9

## Verdict

`expanded_to_full_solution`.

The compressed plan was sufficient to identify the object being counted: connected choices of `n` roads in the wheel graph with `n + 1` vertices are exactly spanning trees of the wheel. I replaced the compressed solution with a complete proof using Kirchhoff's matrix-tree theorem.

The expanded proof deletes the central vertex from the Laplacian, diagonalizes the resulting cycle matrix, and evaluates
`prod_{k=0}^{n-1}(3 - zeta^k - zeta^{-k})`
as `L_{2n} - 2 = F_{2n+1} + F_{2n-1} - 2`.

This is a safe reconstruction of the count, though not necessarily a verbatim expansion of the official elementary presentation via the auxiliary "fan" graph.

## Changed Files

- `data/problems/kolmogorov/kolmogorov-2006-team-olympiad-seniors-problem-9.yaml`
- `audit/plan-to-solution-pass/kolmogorov-2006-team-seniors-p9.md`

## Tests

- Passed: `python tools/validate.py`
- Passed: `python tools/check_links.py`
