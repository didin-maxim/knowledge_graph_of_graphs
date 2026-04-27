# Kolmogorov 2008 Individual Olympiad Seniors Problem 7

## Verdict

`deferred_needs_source_or_reconstruction`.

The current YAML contains a compressed official-style projection argument. I did not expand it into a full solution because the argument depends on the unsupported claim that, after a generic projection, the outer boundary of the projection passes through every vertex of the polyhedron.

More seriously, the apparent statement asks for a Hamiltonian cycle in the graph of every convex polyhedron whose faces are triangles. That is not a valid general theorem: non-Hamiltonian maximal planar/polyhedral triangulations are known, for example the Goldner-Harary graph/polyhedron. This suggests that either the imported statement/summary is missing a condition, the source was misread, or the problem needs a corrected reconstruction from the official archive.

## Changed Files

- `data/problems/kolmogorov/kolmogorov-2008-individual-olympiad-seniors-problem-7.yaml`
- `audit/plan-to-solution-pass/kolmogorov-2008-individual-seniors-p7.md`

## Notes

- Left `sol-official-compressed` as `needs_human_review`.
- Added `repair_status: deferred_needs_source_or_reconstruction`.
- Added a review note explaining why a full solution should not be fabricated from the compressed plan.

## Tests

- Passed: `python tools/validate.py`
- Passed: `python tools/check_links.py`
