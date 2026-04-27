# Kolmogorov 2006 Round 4 Super League Problem 5

## Verdict

`expanded_to_full_solution`.

The compressed plan was sufficient to reconstruct the full argument. I expanded the dual-tree solution: a triangulation of an `n`-gon gives a subcubic tree on `N = n - 2` vertices, and the side-length type of a triangle is determined by the three component sizes after deleting the corresponding tree vertex.

The upper bound separates leaves, degree-2 vertices, and degree-3 vertices. If the tree has `t` degree-3 vertices, then it has `N - 2t - 2` degree-2 vertices; all leaves contribute one type, degree-2 vertices contribute at most `floor((N - 1) / 2)` types, and degree-3 vertices contribute at most `t` types. Maximizing

`1 + t + min(N - 2t - 2, floor((N - 1) / 2))`

gives `floor((3N - 1) / 4) = floor((3n - 7) / 4)`.

For sharpness, the YAML now includes the explicit caterpillar-tree construction: take a path on `N - t` vertices and attach one leaf to each of `x_2, ..., x_{t+1}`, where `t` is an integer attaining the above maximum. The component-size triples give exactly the required number of distinct triangle types, and every subcubic tree is realized by a triangulation of a convex polygon.

## Changed Files

- `data/problems/kolmogorov/kolmogorov-2006-round-4-super-league-problem-5.yaml`
- `audit/plan-to-solution-pass/kolmogorov-2006-round4-super-p5.md`

## Tests

- Passed: `python tools/validate.py`
- Passed: `python tools/check_links.py`
- Passed: targeted JSON parse for `data/problems/kolmogorov/kolmogorov-2006-round-4-super-league-problem-5.yaml`
- Passed: `git diff --check` for the target problem file and this audit report
