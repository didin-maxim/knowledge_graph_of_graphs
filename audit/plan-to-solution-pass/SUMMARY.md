# Plan-to-solution pass summary

Date: 2026-04-26

Scope: backlog entries where a solution plan/sketch existed and could potentially be expanded into a complete solution.

## Totals

| outcome | count |
|---|---:|
| expanded to full solution | 27 |
| already full, no problem YAML change | 10 |
| clarified partial/metadata only | 1 |
| deferred as insufficient plan | 8 |
| total reports | 46 |

## Expanded to Full Solution

- `imo-1994-c2-city-ages-harmonic-graph.yaml`
- `imo-1996-c1-grid-knight-reachability.yaml`
- `imo-1996-c2-grid-vertices-two-red.yaml`
- `imo-2005-c2-dynastic-vertices-forest.yaml`
- `imo-2013-c3-imons-graph-coloring.yaml`
- `brooks-theorem.yaml`
- `menger-theorem.yaml`
- `ore-theorem.yaml`
- `turan-theorem.yaml`
- `usamo-2009-p3-tasteful-domino-tiling-alternating-cycles.yaml`
- `usamo-2024-p3-balanced-regular-polygon-triangulation.yaml`
- `kolmogorov-2003-team-olympiad-seniors-problem-8.yaml`
- `kolmogorov-2004-round1-higher-league-problem-3.yaml`
- `kolmogorov-2006-round-1-super-high-first-league-problem-1.yaml`
- `kolmogorov-2006-round-4-super-league-problem-5.yaml`
- `kolmogorov-2006-team-olympiad-seniors-problem-9.yaml`
- `kolmogorov-2007-round-2-first-league-problem-8.yaml`
- `kolmogorov-2007-team-olympiad-seniors-problem-7.yaml`
- `kolmogorov-2008-round-1-high-league-problem-1.yaml`
- `kolmogorov-2008-round-2-high-league-problem-1.yaml`
- `kolmogorov-2008-round-3-high-league-problem-1.yaml`
- `kolmogorov-2010-individual-olympiad-juniors-problem-5.yaml`
- `kolmogorov-2011-individual-olympiad-seniors-problem-7.yaml`
- `kolmogorov-2011-team-olympiad-juniors-problem-6.yaml`
- `kolmogorov-2011-team-olympiad-seniors-problem-4.yaml`
- `kolmogorov-2013-individual-olympiad-seniors-problem-5.yaml`
- `kolmogorov-2013-team-olympiad-seniors-problem-8.yaml`

## Already Full

- `imo-2004-c8-triangles-tetrahedra-graph.yaml`
- `imo-2010-c2-flags-diagonal-matching.yaml`
- `imo-2010-c5-bad-company-tournament.yaml`
- `imo-2012-c7-equal-sum-chords-independent-set.yaml`
- `imo-2014-c9-snail-circles-tree.yaml`
- `imo-2016-c6-ferry-graph-dynamics.yaml`
- `imo-2016-c8-domino-unique-tiling-cycles.yaml`
- `imo-2019-c4-labyrinth-region-graph.yaml`
- `imo-2021-c4-anisotropy-menger.yaml`
- `imo-2023-c7-ferry-companies-hamiltonian-paths.yaml`

## Clarified Partial

- `usamo-2008-p6-even-friends-two-rooms.yaml`: the existence-only solution entry was kept as a partial alternative and clearly marked `needs_human_review`; other full count solutions remain available in the same card.

## Deferred

- `kolmogorov-2002-team-olympiad-seniors-problem-8.yaml`
- `kolmogorov-2004-round2-higher-league-problem-9.yaml`
- `kolmogorov-2004-round3-higher-league-problem-10.yaml`
- `kolmogorov-2006-round-2-super-league-problem-6.yaml`
- `kolmogorov-2006-round-3-super-league-problem-3.yaml`
- `kolmogorov-2008-individual-olympiad-seniors-problem-7.yaml`
- `kolmogorov-2010-individual-olympiad-seniors-problem-4.yaml`
- `kolmogorov-2012-individual-olympiad-seniors-problem-6.yaml`

## Verification

```text
python tools/validate.py
OK: 328 problems, 296 relations, 9 comments, 349 sources, 27 definitions, 15 standard ideas, 19 import batches.

python tools/check_links.py
OK: 370 internal routes, 349 external source URLs syntactically valid.
```
