# Repair Pass Summary

Date: 2026-04-27

This repair pass followed the sampled completeness audit. It intentionally did not touch placeholder no-solution entries (`Решение пока не найдено`).

## Fixed

17 sampled non-placeholder serious defects were fixed:

- 4 damaged-encoding solutions restored.
- 2 classical/paper cards repaired with complete proofs.
- 3 IMO/USAMO cards repaired.
- 3 FYUM cards repaired.
- 2 Kolmogorov cards repaired.
- 3 UTYUM/local cards repaired.

The damaged-encoding count is now zero.

## Deferred

17 sampled non-placeholder serious defects were deferred because they require substantial external theorem transfer, a missing figure/construction, or a long independent reconstruction:

- `chen-yu-fragile-graphs-theorem#sol-paper-theorem`
- `kolmogorov-2024-t4-independent-cutset-2n-4`
- `imo-2005-c8-noncrossing-diagonals-crossings#sol-reviewed-web`
- `imo-1998-c6-complete-graph-rainbow-edges#sol-reviewed-web`
- `usamo-2021-p2-planar-national-park-turning-walk#sol-local-state-bound-and-prism`
- `usamo-2023-p3-domino-slides-special-square-digraph#sol-special-square-digraph`
- `fyum-2013-tur2a-p1`
- `fyum-2009-tur3a-p7`
- `fyum-2011-finalb-p4`
- `fyum-2009-final-p2`
- `yumt-2015-grand-final-problem5#sol-external-mse-chromatic-partition`
- `yumt-2015-grand-round4-problem10`
- `utyum-2025_komol64_8_7_tree_matchings_path`
- `utyum-2023_komol60_7_7_room_departures`
- `tc-2013-14-vertex-transitive-not-transposition`
- `tc-2001-02-rooks-odd-attacks`
- `tc-2023-24-coins-pairing-weighing-forest`

## Severity

The remaining deferred holes are serious. They are not cosmetic metadata issues; most are cases where the current solution is not locally checkable because it cites a large external theorem, omits an explicit construction, or depends on a missing figure/table/algorithm.

After this easy repair pass, the obvious encoding failures are gone, but the database still has a meaningful hard backlog. Ignoring placeholder no-solution cards, a reasonable remaining estimate is about 7-12% serious non-placeholder solution defects, plus about 7-10% borderline cases.

## Verification

```text
python tools/validate.py
OK: 328 problems, 379 relations, 9 comments, 349 sources, 27 definitions, 15 standard ideas, 19 import batches.

python tools/check_links.py
OK: 370 internal routes, 349 external source URLs syntactically valid.
```
