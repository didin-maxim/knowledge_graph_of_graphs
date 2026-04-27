# Sampled Completeness Backlog

Date: 2026-04-27

This file preserves the current sampled audit state before repair agents start editing. Placeholder entries whose only content is `Решение пока не найдено` are intentionally excluded from the repair queue for now; they represent cards without solutions and should not be treated in this pass.

## Agent Sample Sizes

- bucket 0: 21 inspected out of 63.
- bucket 1: 24 inspected out of 60.
- bucket 2: 38 inspected out of 65.
- bucket 3: 30 inspected out of 49.
- bucket 4: 21 inspected out of 49.
- bucket 5: 39 inspected out of 64.

Total inspected: 173 solution entries.

## Repair Queue: Serious Non-Placeholder Problems

These are sampled solutions that appear to contain a real but incomplete/broken solution text.

- `tree-equivalent-properties#sol-leaf-induction` — missing the unique-simple-path equivalence.
- `imo-2004-c3-delete-edge-from-4cycle#sol-reviewed-secondary` — key odd-cycle and induction steps are sketchy.
- `yumt-2015-grand-final-problem5#sol-external-mse-chromatic-partition` — close external problem, not a transferred solution.
- `tc-2013-14-vertex-transitive-not-transposition#sol-counterexample-from-source` — verification depends on source figure.
- `fyum-2013-tur2a-p1#sol-official-archive` — relies on an external theorem without proof.
- `egmo-2025-p5-rotating-arrows-dynamic-cycle#sol-official-compressed` — damaged encoding.
- `fyum-2009-tur3a-p7#sol-official-archive` — relies on Bondy-Simonovits without proof.
- `fyum-2011-finalb-p4#sol-official-archive` — relies on an external theorem about two-block Hamiltonian paths.
- `fyum-2010-tur3a-p7#sol-official-archive` — key edge count in two-colored forests is missing.
- `utyum-2012_komol39_8_binary_tree_ordering#sol-official` — counterexample impossibility is not proved.
- `utyum-2025_komol64_8_7_tree_matchings_path#sol-official` — induction/equality estimates are only summarized.
- `usamo-2025-p3-gabriel-graph-road-network#sol-gabriel-planar-bound` — finite reduction and choice of `S` are missing.
- `chen-yu-fragile-graphs-theorem#sol-paper-theorem` — paper theorem cited, not proved.
- `fyum-2010-tur1a-p8#sol-official-archive` — general `k` step is only asserted.
- `tc-2001-02-rooks-odd-attacks#sol-construct-63` — construction on 63 rooks is external.
- `yumt-2015-grand-round4-problem10#sol-archive-card` — external general theorem not transferred.
- `tc-2023-24-coins-pairing-weighing-forest#sol-forest-accounting` — weighing algorithm is not described.
- `kolmogorov-2008-team-olympiad-seniors-problem-7#sol-official-compressed` — key monochromatic-triangle-to-4-cycle/counting step is missing or suspicious.
- `egmo-2016-p3-blue-cells-bipartite-incidence#sol-official-compressed` — damaged encoding.
- `kolmogorov-2024-t4-independent-cutset-2n-4#sol-chen-yu` — Chen-Yu theorem cited, not proved.
- `imo-2005-c8-noncrossing-diagonals-crossings#sol-reviewed-web` — upper bound and extremal construction are outline-level.
- `imo-1998-c6-complete-graph-rainbow-edges#sol-reviewed-web` — construction for `k=5` and case reductions are missing.
- `fyum-2009-final-p2#sol-official-archive` — external Burr-Erdos-Spencer theorem/construction not transferred.
- `benjamini-tzalik-shortest-paths-bound#sol-paper-bound` — article result compressed too far; layered inequality/construction missing.
- `imo-1994-c6-infinite-grid-pairing-strategy#sol-reviewed-secondary` — depends on a missing periodic pairing/table.
- `kolmogorov-2004-round3-higher-league-problem-10#sol-official-compressed` — summary says details are investigated but does not give contradiction.
- `utyum-2023_komol60_7_7_room_departures#sol-official` — lower bound present, construction for 51 people missing.
- `utyum-2025_komol65_7_6_airlines_degree_sum#sol-official` — constructions for admissible values are named but not described.
- `usamo-2021-p2-planar-national-park-turning-walk#sol-local-state-bound-and-prism` — schematic upper bound and external construction.
- `usamo-2023-p3-domino-slides-special-square-digraph#sol-special-square-digraph` — explicitly says construction is not self-contained.
- `utyum-2019_komol_7_airline_costs#sol-official` — cases and estimates are summarized without details.
- `apmo-2010-p3-common-acquaintance-extremal#sol-official-compressed` — damaged encoding.
- `bmo-2022-p4-frog-grid-boundary-graph#sol-official-compressed` — damaged encoding.

## Borderline Queue

These should not block the easy repair pass unless an agent finds an obvious low-risk fix.

- `fyum-2008-tur2a-p5#sol-official-archive`
- `vosh-2000-01-final-universal-acquaintance#sol-complement-domination`
- `fyum-2010-tur1b-p8#sol-official-archive`
- `imo-1964-p4-three-topic-ramsey#sol-graph-review`
- `five-color-theorem#sol-kempe-sketch`
- `kolmogorov-2008-round-2-first-league-and-higher-junior-problem-1#sol-official-compressed`
- `kolmogorov-2022-round2-juniors-hamiltonian-path-parity#sol-official-restored`
- `kolmogorov-2022-round4-high-airport-walk-parity#sol-official-restored`
- `fyum-2009-tur1a-p7#sol-official-archive`
- `kolmogorov-2006-round-2-first-junior-league-problem-8#sol-official-compressed`
- `usamo-2008-p6-even-friends-two-rooms#sol-good-configurations-as-group`
- `fyum-2008-tur1a-p10#sol-official-archive`
- `tc-2018-19-simple-complex-state-game#sol-tree-cycle`
- `yumt-2015-grand-round3-problem9#sol-archive-card`
- `kolmogorov-2004-round1-higher-league-problem-3#sol-official-compressed`
- `usamo-2024-p3-balanced-regular-polygon-triangulation#sol-fan-and-integrality`
- `kolmogorov-2006-round-3-super-league-problem-3#sol-official-compressed`
- `utyum-1993_ii_7kl_1#sol-official`
- `fyum-2008-tur4a-p7#sol-official-archive`
- `fyum-2009-tur4a-p2#sol-official-archive`
- `utyum-2023_komol61_8_5_yozhgorod_registry#sol-official`
- `fyum-2009-tur2a-p4#sol-official-archive`
- `fyum-2010-tur2a-p1#sol-official-archive`
- `usamo-2004-p4-black-path-grid-game#sol-bob-useless-squares`

## Severity Estimate

Ignoring placeholder no-solution entries, the sampled audit still found many real defects. The most severe classes are:

- damaged encoding: solution unusable;
- external dependency not transferred: the card cannot be checked locally;
- outline-level proof: decisive construction/counting/contradiction absent.

The holes are serious enough that the database should not be considered solution-complete yet. After excluding placeholders, a working estimate is that roughly 12-20% of all solution entries still have serious non-placeholder defects, with another 7-10% borderline.
