# XHard Per-Task Repair Summary

Date: 2026-04-27

This pass launched one maximum-reasoning agent per remaining hard deferred task. Some earlier cards had already been merged into helper/family cards; the agents followed the mathematical dependency rather than only the old filename.

## Closed

Two previously deferred tasks were fully repaired:

- `fyum-2013-tur2a-p1`: transferred a full Russian proof of the needed special case from the NTU/DMGT strong edge-coloring source.
- `fyum-2009-final-p2`: transferred the needed diagonal proof of `r(qK_3)=5q` from Burr--Erdos--Spencer, rather than leaving the Ramsey theorem as a black box.

## Still Deferred

Five hard blockers remain:

- `chen-yu-independent-cutset-kolmogorov-merged` / Chen--Yu fragile graph theorem:
  full proof remains unavailable in checked open sources; secondary papers cite or strengthen it but do not reproduce the contraction induction.
- Kolmogorov 2024 independent cutset:
  still depends on the same Chen--Yu proof; official KOLM archive has statement/attribution but no solution.
- `fyum-2011-finalb-p4`:
  needs a self-contained proof of the two-block Alspach--Rosenfeld/Straight tournament path theorem, or a compact special-case proof.
- `yumt-2015-grand-final-problem5`:
  needs a self-contained proof of the relevant Stiebitz/Tihany double-critical 5-chromatic theorem or a separate proved theorem card.
- `usamo-2023-p3-domino-slides-special-square-digraph`:
  upper bound and answer are sourced, but the construction still needs a text-only coordinate transfer from figure-based local retile patterns.

## Current Checks

```text
python tools/validate.py
OK: 324 problems, 375 relations, 9 comments, 352 sources, 27 definitions, 15 standard ideas, 19 import batches.

python tools/check_links.py
OK: 366 internal routes, 352 external source URLs syntactically valid.
```

Current solution counts:

```text
solutions 347
placeholders_no_solution 44
non_placeholder_solutions 303
damaged_encoding 0
```
