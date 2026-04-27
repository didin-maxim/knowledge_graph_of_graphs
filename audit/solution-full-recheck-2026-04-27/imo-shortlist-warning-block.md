# IMO Shortlist Warning Block

Date: 2026-04-27.

Scope: allowed IMO files for years 1994, 1996, 1999, 2010, 2012, 2013, 2014, 2016, 2019, 2020, 2021, 2023.

## Downgraded

These cards had `editorial.public_ready=true` while a local non-author field still had `status=needs_human_review`. I did not promote or rewrite from memory/source; I made the publication flag honest by setting `editorial.review_status=needs_human_review` and `editorial.public_ready=false`.

- `imo-1994-c2-city-ages-harmonic-graph`
- `imo-1996-c1-grid-knight-reachability-divisible-2-or-3`
- `imo-1996-c1-grid-knight-reachability-r73-path`
- `imo-1996-c1-grid-knight-reachability-r97-impossible`
- `imo-1996-c2-grid-vertices-two-red`
- `imo-2010-c5-bad-company-tournament`
- `imo-2012-c7-equal-sum-chords-independent-set`
- `imo-2013-c3-imons-graph-coloring`
- `imo-2013-c6-flight-distance-layers`
- `imo-2014-c9-snail-circles-tree`
- `imo-2016-c6-ferry-graph-dynamics`
- `imo-2019-c4-labyrinth-region-graph`
- `imo-2021-c4-anisotropy-menger`
- `imo-2023-c7-ferry-companies-hamiltonian-paths`

## Already Non-Public

These warning hits were already non-public and were left unchanged in this pass:

- `imo-1994-c6-infinite-grid-pairing-strategy`
- `imo-2019-c3-coin-process-digraph`
- `imo-2020-c4-fibonacci-difference-forest`
- `imo-2020-c6-colored-coins-eulerian-multigraph`
- `imo-2023-c4-strip-pieces-eulerian-graph`

## Hard / Backlog

For the downgraded and already non-public items above, the next pass needs either the official shortlist source text, an archived working proof, or a newly written self-contained proof before restoring `public_ready=true`. In particular, do not treat `sol-official-compressed` as sufficient evidence by itself: keep the card non-public if any statement, graph reformulation, difficulty, or solution-local status remains `needs_human_review`.

Compressed-id cards with no local non-author `needs_human_review` were not downgraded mechanically in this pass; their text may still deserve a later source comparison, but this block only resolved the explicit public-ready/local-review conflict.
