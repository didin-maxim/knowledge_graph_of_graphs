# Hard IMO/USAMO Repair

Date: 2026-04-27

Scope: only the four requested hard deferred entries. Placeholder entries with `Решение пока не найдено` were not touched.

## Repaired

- `imo-1998-c6-complete-graph-rainbow-edges#sol-reviewed-web`
  - Corrected the answer for the generalized local statement: possible values are exactly `5,6,7,8,9,10`, not all values except `4`.
  - Added impossibility for `k=1,2,3`, the full Kalva/Scholes `k=4` contradiction, the explicit five-color construction, and the 1-factorization construction for `k=6..9`.
  - Source checked: Kalva/John Scholes IMO Shortlist 1998 C6 solution.

- `imo-2005-c8-noncrossing-diagonals-crossings#sol-reviewed-web`
  - Expanded the upper bound into the paired-ear summation.
  - Added the explicit extremal construction with vertices `A_1,...,A_n`, `l=floor(n/2)+1`, and the crossing count attaining `ceil(3(n-3)^2/4)`.
  - Source checked: IMO Compendium excerpt at imomath.

- `usamo-2021-p2-planar-national-park-turning-walk#sol-local-state-bound-and-prism`
  - Replaced the terse local-state sketch with the directed-turn argument from Evan Chen notes.
  - Added a fully explicit pentagonal-prism walk witnessing three entries into one vertex.
  - Sources checked: Evan Chen USAMO 2021 notes and Eric Shen USAMO 2021 PDF.

## Deferred

- `usamo-2023-p3-domino-slides-special-square-digraph#sol-special-square-digraph`
  - Left deferred. Evan Chen notes and Holden Mui's proposal verify the graph model, the tree component, and the answer set, but the construction of every small value `1..((n-1)/2)^2` is presented through snake diagrams/local perturbation pictures rather than a complete textual algorithm.
  - Needed to finish safely: an official/proposer text spelling out the general construction for each small `k`, or a separately verified formalization of the picture sequence into an explicit domino-placement algorithm.

## Validation

- `python tools/validate.py` — OK: 328 problems, 379 relations, 9 comments, 350 sources, 27 definitions, 15 standard ideas, 19 import batches.
- `python tools/check_links.py` — OK: 370 internal routes, 350 external source URLs syntactically valid.
