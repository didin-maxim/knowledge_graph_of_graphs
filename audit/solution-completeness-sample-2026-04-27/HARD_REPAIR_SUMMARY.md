# Hard Repair Pass Summary

Date: 2026-04-27

This pass used high-reasoning agents on the deferred non-placeholder solution defects. Placeholder no-solution entries were not edited.

## Repaired In This Pass

10 hard deferred items were repaired:

- `fyum-2009-tur3a-p7`
- `imo-1998-c6-complete-graph-rainbow-edges`
- `imo-2005-c8-noncrossing-diagonals-crossings`
- `usamo-2021-p2-planar-national-park-turning-walk`
- `yumt-2015-grand-round4-problem10`
- `utyum-2023_komol60_7_7_room_departures`
- `utyum-2025_komol64_8_7_tree_matchings_path`
- `tc-2001-02-rooks-odd-attacks`
- `tc-2013-14-vertex-transitive-not-transposition`
- `tc-2023-24-coins-pairing-weighing-forest`

Four additional helper/family cards were added during the repair work:

- `balanced-bipartite-edge-coloring-two-colors`
- `benjamini-tzalik-shortest-paths-kolmogorov-merged`
- `chen-yu-independent-cutset-kolmogorov-merged`
- `complete-graph-triangle-edge-weights-minimum-parametric`

They consolidate reusable theorem/family material that came up while making local repairs self-contained.

## Still Deferred

7 hard non-placeholder items remain deferred:

- `chen-yu-fragile-graphs-theorem#sol-paper-theorem`
- `kolmogorov-2024-t4-independent-cutset-2n-4#sol-chen-yu`
- `fyum-2013-tur2a-p1`
- `fyum-2011-finalb-p4`
- `fyum-2009-final-p2`
- `yumt-2015-grand-final-problem5#sol-external-mse-chromatic-partition`
- `usamo-2023-p3-domino-slides-special-square-digraph#sol-special-square-digraph`

## Why These Are Still Serious

- Chen-Yu / Kolmogorov 2024: the full proof of the fragile-graph theorem is not openly available in the checked sources; accessible papers cite or strengthen it but do not reproduce the induction proof.
- FYUM 2013 T2A P1: depends on a strong edge-coloring theorem for planar graphs of large girth.
- FYUM 2011 Final B P4: depends on a theorem about two-block oriented Hamiltonian paths in tournaments.
- FYUM 2009 Final P2: depends on the Burr-Erdos-Spencer Ramsey theorem `R(nK_3,nK_3)=5n`.
- YUMT 2015 Grand Final P5: needs a self-contained special case of the Stiebitz/Tihany-style chromatic partition theorem.
- USAMO 2023 P3: sources give key constructions by figures/local modifications; a complete text-only construction still needs careful transfer.

## Checks

```text
python tools/validate.py
OK: 332 problems, 379 relations, 9 comments, 350 sources, 27 definitions, 15 standard ideas, 19 import batches.

python tools/check_links.py
OK: 374 internal routes, 350 external source URLs syntactically valid.
```
