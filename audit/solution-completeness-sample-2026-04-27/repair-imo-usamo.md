# IMO/USAMO Sample Repair

Date: 2026-04-27

Scope: requested IMO/USAMO sampled serious problems only. Placeholder no-solution entries were not touched.

## Repaired

- `imo-2004-c3-delete-edge-from-4cycle#sol-reviewed-secondary`
  - Expanded the lower bound to the connected/non-bipartite invariant.
  - Added the explicit deletion order leaving exactly the `n` edges `V_1V_i` for `2 <= i <= n` and `V_2V_n`.
  - Source checked during this pass: StudyRes mirror of IMO Shortlist 2004 solution.

- `imo-1994-c6-infinite-grid-pairing-strategy#sol-reviewed-secondary`
  - Inserted the missing periodic `10 x 10` pairing table.
  - Added the response strategy and the reason every length-11 line hits a full pair.
  - Source checked during this pass: Kalva/John Scholes IMO Shortlist 1994 C6 solution.

- `usamo-2025-p3-gabriel-graph-road-network#sol-gabriel-planar-bound`
  - Replaced the incorrect finite planar average-degree sketch with the actual Alice strategy.
  - Added the choice of `S`, the Gabriel-graph equivalence, the squared-distance descent for connectedness, and the crossing contradiction for planarity.
  - Source checked during this pass: AoPS Wiki problem solution and Evan Chen USAMO 2025 notes.

## Deferred

- `imo-2005-c8-noncrossing-diagonals-crossings#sol-reviewed-web`
  - Deferred: the upper-bound summation and equality construction require a careful full transfer. I did not find and verify a compact complete construction quickly enough for a safe local rewrite.

- `imo-1998-c6-complete-graph-rainbow-edges#sol-reviewed-web`
  - Deferred: the `k=5` construction and the reductions for the other `k` values are still outline-level. A safe repair needs the full explicit coloring or a checked equivalent construction.

- `usamo-2021-p2-planar-national-park-turning-walk#sol-local-state-bound-and-prism`
  - Deferred: previous external-source pass found that the cited source gives only a terse upper bound and names the pentagonal prism without the explicit embedding/start/walk. I did not reconstruct it independently in this pass.

- `usamo-2023-p3-domino-slides-special-square-digraph#sol-special-square-digraph`
  - Deferred: the current solution itself says the constructive realization of all values is not self-contained. I left it as `needs_human_review` rather than inventing the missing construction.

## Validation

- `python tools/validate.py`
- `python tools/check_links.py`

