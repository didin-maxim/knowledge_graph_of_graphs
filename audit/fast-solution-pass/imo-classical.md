# Fast solution completeness pass: IMO + classical

| path | problem_id | solution_id/status | label | one-line reason |
|---|---|---|---|---|
| data/problems/imo/imo-1994-c2-city-ages-harmonic-graph.yaml | imo-1994-c2-city-ages-harmonic-graph | sol-secondary-sketch/ai_checked | incomplete_solution | solution is explicitly a compressed secondary sketch; maximum-principle propagation is terse |
| data/problems/imo/imo-1996-c1-grid-knight-reachability.yaml | imo-1996-c1-grid-knight-reachability | sol-secondary-sketch/ai_checked | incomplete_solution | compressed sketch for several r-cases; construction/invariant details look abbreviated |
| data/problems/imo/imo-1996-c2-grid-vertices-two-red.yaml | imo-1996-c2-grid-vertices-two-red | sol-secondary-sketch/ai_checked | incomplete_solution | compressed counting argument; row-transition cases are only sketched |
| data/problems/imo/imo-2004-c8-triangles-tetrahedra-graph.yaml | imo-2004-c8-triangles-tetrahedra-graph | sol-secondary-sketch/ai_checked | incomplete_solution | id says sketch and the neighborhood-counting proof is highly compressed |
| data/problems/imo/imo-2005-c2-dynastic-vertices-forest.yaml | imo-2005-c2-dynastic-vertices-forest | sol-secondary-sketch/ai_checked | incomplete_solution | minimal-dynastic-vertex charging argument says deletion/induction is equivalent but omits details |
| data/problems/imo/imo-2010-c2-flags-diagonal-matching.yaml | imo-2010-c2-flags-diagonal-matching | sol-official-compressed/ai_checked | incomplete_solution | explicitly compressed official solution; Hall setup likely needs expansion |
| data/problems/imo/imo-2010-c5-bad-company-tournament.yaml | imo-2010-c5-bad-company-tournament | sol-official-compressed/ai_checked | incomplete_solution | explicitly compressed official solution for tournament argument |
| data/problems/imo/imo-2012-c7-equal-sum-chords-independent-set.yaml | imo-2012-c7-equal-sum-chords-independent-set | sol-official-compressed/ai_checked | incomplete_solution | explicitly compressed official solution; independent-set construction likely underexplained |
| data/problems/imo/imo-2013-c3-imons-graph-coloring.yaml | imo-2013-c3-imons-graph-coloring | sol-official-compressed/ai_checked | suspicious_too_short | official-compressed solution is short for a C3 coloring problem |
| data/problems/imo/imo-2013-c6-flight-distance-layers.yaml | imo-2013-c6-flight-distance-layers | sol-official-compressed/needs_human_review | incomplete_solution | text says official solution shows key distinctness/alternatives but does not prove them |
| data/problems/imo/imo-2014-c9-snail-circles-tree.yaml | imo-2014-c9-snail-circles-tree | sol-official-compressed/ai_checked | incomplete_solution | explicitly compressed official tree/odd-region proof; complex enough to warrant expansion |
| data/problems/imo/imo-2015-c5-sequence-rays.yaml | imo-2015-c5-sequence-rays | sol-official-compressed/ai_checked | incomplete_solution | solution id still marks official-compressed despite more developed text |
| data/problems/imo/imo-2016-c6-ferry-graph-dynamics.yaml | imo-2016-c6-ferry-graph-dynamics | sol-official-compressed/ai_checked | incomplete_solution | solution id marks official-compressed; bipartite-network proof likely condensed |
| data/problems/imo/imo-2016-c8-domino-unique-tiling-cycles.yaml | imo-2016-c8-domino-unique-tiling-cycles | sol-official-compressed/ai_checked | incomplete_solution | explicitly compressed official diagonal-cycle proof |
| data/problems/imo/imo-2019-c3-coin-process-digraph.yaml | imo-2019-c3-coin-process-digraph | sol-official-compressed/ai_checked | suspicious_too_short | short official-compressed recurrence/graph construction; one connecting step is terse |
| data/problems/imo/imo-2019-c4-labyrinth-region-graph.yaml | imo-2019-c4-labyrinth-region-graph | sol-official-compressed/ai_checked | incomplete_solution | explicitly compressed official region-graph proof |
| data/problems/imo/imo-2020-c4-fibonacci-difference-forest.yaml | imo-2020-c4-fibonacci-difference-forest | sol-official-compressed/ai_checked | suspicious_too_short | short compressed proof; forest upper/lower bound details are dense |
| data/problems/imo/imo-2020-c6-colored-coins-eulerian-multigraph.yaml | imo-2020-c6-colored-coins-eulerian-multigraph | sol-official-compressed/ai_checked | suspicious_too_short | very short compressed Eulerian-multigraph argument |
| data/problems/imo/imo-2021-c4-anisotropy-menger.yaml | imo-2021-c4-anisotropy-menger | sol-official-compressed/ai_checked | incomplete_solution | explicitly compressed official solution invoking Menger-style machinery |
| data/problems/imo/imo-2023-c4-strip-pieces-eulerian-graph.yaml | imo-2023-c4-strip-pieces-eulerian-graph | sol-official-compressed/ai_checked | suspicious_too_short | compressed Eulerian-graph lower bound, likely needs more detail |
| data/problems/imo/imo-2023-c7-ferry-companies-hamiltonian-paths.yaml | imo-2023-c7-ferry-companies-hamiltonian-paths | sol-official-compressed/ai_checked | incomplete_solution | explicitly compressed official Hamiltonian-paths proof; long but marked compressed |
| data/problems/classical/brooks-theorem.yaml | brooks-theorem | sol-sketch/needs_review | incomplete_solution | opens by saying full proof requires case analysis; only a proof scheme is present |
| data/problems/classical/chen-yu-fragile-graphs-theorem.yaml | chen-yu-fragile-graphs-theorem | sol-paper-theorem/ai_checked | source_insufficient | solution only records what the paper proves, not an internal proof |
| data/problems/classical/dirac-theorem.yaml | dirac-theorem | sol-longest-path/ai_draft | suspicious_too_short | short ai_draft proof with standard position-intersection step compressed |
| data/problems/classical/five-color-theorem.yaml | five-color-theorem | sol-kempe-sketch/ai_draft | incomplete_solution | Kempe-chain proof is explicitly sketch-like and omits planar separation details |
| data/problems/classical/hall-marriage-theorem.yaml | hall-marriage-theorem | sol-induction/ai_draft | suspicious_too_short | short ai_draft induction; deletion case and residual Hall check are terse |
| data/problems/classical/konig-vertex-cover-theorem.yaml | konig-vertex-cover-theorem | sol-alternating/ai_draft | suspicious_too_short | short ai_draft proof; alternating reachability coverage argument is compressed |
| data/problems/classical/mantel-theorem.yaml | mantel-theorem | sol-degree-sum/ai_draft | suspicious_too_short | very short ai_draft proof; likely okay but too terse for full solution |
| data/problems/classical/menger-theorem.yaml | menger-theorem | sol-flow-sketch/ai_draft | incomplete_solution | flow reduction sketch omits vertex-splitting and min-cut/path decomposition details |
| data/problems/classical/ore-theorem.yaml | ore-theorem | sol-closure-sketch/ai_draft | incomplete_solution | closure proof says standard position argument closes the path without details |
| data/problems/classical/turan-theorem.yaml | turan-theorem | sol-symmetrization/ai_draft | suspicious_too_short | ai_draft symmetrization proof is compressed for a classical theorem |

## Counts

- incomplete_solution: 20
- missing_solution: 0
- suspicious_too_short: 10
- source_insufficient: 1
- likely_ok: 0

## Scale estimate

Quick pass over 68 YAML files found 31 suspicious solution entries. No missing solutions and no explicit source_insufficient statuses surfaced in this zone; the main issue is compressed/sketch-style proofs, especially IMO combinatorics entries and classical theorem cards.
