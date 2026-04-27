# Repair Local Misc

Date: 2026-04-27

Scope: sampled serious UTYUM/YUMT/TC problems. Placeholder no-solution cards were not touched.

## Repaired

- `utyum-2012_komol39_8_binary_tree_ordering`: replaced the summary with a self-contained counterexample using the full binary tree of depth 18 and a width bound for the ordering.
- `utyum-2025_komol65_7_6_airlines_degree_sum`: added a full solution via an auxiliary graph, classification of possible edge-degree sums, and constructions for all admissible `k`.
- `utyum-2019_komol_7_airline_costs`: added a full solution by counting cheap and expensive edges in triangles.

## Deferred

- `yumt-2015-grand-final-problem5#sol-external-mse-chromatic-partition`: deferred; the current text depends on a broader theorem about partitions by chromatic number, and a self-contained transfer was not ready in this pass.
- `yumt-2015-grand-round4-problem10`: deferred; the card cites an external theorem about monochromatic components in complete multipartite graphs.
- `utyum-2025_komol64_8_7_tree_matchings_path`: deferred; a full proof needs a careful extremal count of near-perfect matchings in trees.
- `utyum-2023_komol60_7_7_room_departures`: deferred; the lower bound is present, but the construction with 51 remaining people is missing.
- `tc-2013-14-vertex-transitive-not-transposition`: deferred; the counterexample depends on a source figure.
- `tc-2001-02-rooks-odd-attacks`: deferred; the upper bound is easy, but the 63-rook construction requires an explicit arrangement or figure.
- `tc-2023-24-coins-pairing-weighing-forest`: deferred; a full weighing algorithm is missing.
