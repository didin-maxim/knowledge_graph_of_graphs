# False friends second pass: CMO/BMO/INMO/Baltic Way/Balkan MO/Polish MO

Scope: candidates from `audit/false-friends-first-pass/national-archives-cmo-bmo-inmo-baltic-balkan-polish.md`.

Criterion used in this pass: keep only tasks that really contain two or more independent, self-contained formulations/variants. I did not count ordinary graph translations, hint reformulations, upper-bound plus construction structure, or internal proof cases as variants.

Summary: 41 candidates reviewed; 2 accepted, 39 rejected. The first pass was mostly a mechanical list of cards with graph/hint reformulations, so most entries below are intentionally rejected.

## Accepted

### cmo-2006-p4-cycle-triplets-tournament
- File: `data/problems/cmo/cmo-2006-p4-cycle-triplets-tournament.yaml`
- Classification: **false_friend**
- Relation type: `false_friend`
- Basis: The original statement asks for both the minimum and the maximum possible number of cyclic triples. These are self-contained extremal variants on the same object, but the solutions are not just mirror images: the minimum is the transitive tournament construction with value 0, while the maximum uses counting non-cyclic triples by outdegrees, convexity/Cauchy, and a regular cyclic tournament construction.

### baltic-way-1997-p19-edge-disjoint-hamiltonian-cycles
- File: `data/problems/baltic-way/baltic-way-1997-p19-edge-disjoint-hamiltonian-cycles.yaml`
- Classification: **pair_variant**
- Relation type: `pair_variant`
- Basis: The original statement explicitly has two independent parts: (a) the prime `n` formula and (b) the special case `n=9`. They share the same edge-counting upper bound and Hamiltonian-cycle packing language, but the constructions differ: modular step cycles for prime `n`, and an explicit four-cycle packing for `K_9`.

## Rejected

### cmo-1971-p10-one-way-phone-gossip
- File: `data/problems/cmo/cmo-1971-p10-one-way-phone-gossip.yaml`
- Classification: **reject**
- Basis: The graph and hint versions are equivalent reformulations of the same minimum-call problem. The gather-then-broadcast phases are parts of one proof/algorithm, not separate self-contained tasks.

### cmo-1973-p4-triangulated-nonagon-labelings
- File: `data/problems/cmo/cmo-1973-p4-triangulated-nonagon-labelings.yaml`
- Classification: **reject**
- Basis: The matching formulation and forced-neighbor hint are just the graph model and solution path for one counting problem.

### cmo-1976-p8-red-blue-k9-clique
- File: `data/problems/cmo/cmo-1976-p8-red-blue-k9-clique.yaml`
- Classification: **reject**
- Basis: The red-blue, blue-complement, and independent-set forms are equivalent statements of the same Ramsey bound `R(3,4) <= 9`; no independent variant is hidden.

### cmo-1977-p7-rectangular-city-self-avoiding-paths
- File: `data/problems/cmo/cmo-1977-p7-rectangular-city-self-avoiding-paths.yaml`
- Classification: **reject**
- Basis: The city wording and grid-graph wording are the same bound in different language.

### cmo-1979-p5-square-lattice-self-avoiding-walks
- File: `data/problems/cmo/cmo-1979-p5-square-lattice-self-avoiding-walks.yaml`
- Classification: **reject**
- Basis: The small exact values and the two inequalities are bundled computations/estimates for one function, not independent formulations. The hint is just the standard branching/lower-bound proof.

### cmo-1989-p4-ladders-ropes-monkeys
- File: `data/problems/cmo/cmo-1989-p4-ladders-ropes-monkeys.yaml`
- Classification: **reject**
- Basis: The graph/permutation view models the same ladder process; the level-by-level matching argument is one invariant proof.

### cmo-1991-p4-edge-difference-labeling-diagram
- File: `data/problems/cmo/cmo-1991-p4-edge-difference-labeling-diagram.yaml`
- Classification: **reject**
- Basis: The diagram and graph-labeling versions are the same impossibility question. Parity counting is an internal proof device.

### cmo-1994-p3-voting-stabilizes-cycle
- File: `data/problems/cmo/cmo-1994-p3-voting-stabilizes-cycle.yaml`
- Classification: **reject**
- Basis: Only one stabilization statement is present; the graph/cycle-language reformulation does not create a second task.

### cmo-1995-p3-polygon-quadrangulation-boomerangs
- File: `data/problems/cmo/cmo-1995-p3-polygon-quadrangulation-boomerangs.yaml`
- Classification: **reject**
- Basis: This is a single inequality for one geometric decomposition. The graph/planar-counting viewpoint is a proof model, not a variant.

### cmo-1996-p3-permutation-step-two-mod3
- File: `data/problems/cmo/cmo-1996-p3-permutation-step-two-mod3.yaml`
- Classification: **reject**
- Basis: One divisibility question for one recurrence/counting setup; the cases `a_2=2` and `a_2=3` are ordinary recurrence cases.

### cmo-2004-p2-rooks-same-colour
- File: `data/problems/cmo/cmo-2004-p2-rooks-same-colour.yaml`
- Classification: **reject**
- Basis: Counting black and white squares separately is the normal decomposition of one enumeration problem, not two independent formulations.

### cmo-2005-p1-triangular-grid-paths
- File: `data/problems/cmo/cmo-2005-p1-triangular-grid-paths.yaml`
- Classification: **reject**
- Basis: The graph/hint formulations express the same path-counting problem. The line-crossing argument is a proof strategy.

### cmo-2008-p5-self-avoiding-rook-walks
- File: `data/problems/cmo/cmo-2008-p5-self-avoiding-rook-walks.yaml`
- Classification: **reject**
- Basis: The supplied base values and the requested formula for `R(3,n)` are components of one recurrence problem.

### cmo-2010-p4-graph-neighborhood-toggle
- File: `data/problems/cmo/cmo-2010-p4-graph-neighborhood-toggle.yaml`
- Classification: **reject**
- Basis: This is one reachability/parity question. Linear-algebra or graph formulations are equivalent proof languages.

### cmo-2012-p4-synchronizing-grid-robots
- File: `data/problems/cmo/cmo-2012-p4-synchronizing-grid-robots.yaml`
- Classification: **reject**
- Basis: The two-robot merge claim is a lemma used to prove synchronization of all robots. It is not an independent self-contained variant of the original task.

### cmo-2015-p3-grid-hamiltonian-turtle
- File: `data/problems/cmo/cmo-2015-p3-grid-hamiltonian-turtle.yaml`
- Classification: **reject**
- Basis: One extremal guaranteed-entry question on a Hamiltonian grid cycle; graph reformulation and row/column counting are not separate tasks.

### cmo-2018-p3-divisor-prime-related-cycle
- File: `data/problems/cmo/cmo-2018-p3-divisor-prime-related-cycle.yaml`
- Classification: **reject**
- Basis: This is a single classification problem for `n`; divisor graph/cycle wording is only the natural model.

### cmo-2019-p5-odd-cycle-edge-game
- File: `data/problems/cmo/cmo-2019-p5-odd-cycle-edge-game.yaml`
- Classification: **reject**
- Basis: One impartial game classification is present. Strategy cases by parity/graph state are internal proof cases.

### cmo-2020-p5-friendship-induced-subgraphs
- File: `data/problems/cmo/cmo-2020-p5-friendship-induced-subgraphs.yaml`
- Classification: **reject**
- Basis: The construction and lower bound are the standard two halves of one extremal proof; they are not separate formulations.

### cmo-2022-p4-region-adjacency-coloring
- File: `data/problems/cmo/cmo-2022-p4-region-adjacency-coloring.yaml`
- Classification: **reject**
- Basis: Conditions (a) and (b) jointly define one coloring property. They are constraints, not separate tasks or variants.

### cmo-2023-p2-three-regular-bootstrap-friendship
- File: `data/problems/cmo/cmo-2023-p2-three-regular-bootstrap-friendship.yaml`
- Classification: **reject**
- Basis: One yes/no bootstrap-percolation question; graph formulation is equivalent.

### cmo-2023-p5-cut-bound-independent-set
- File: `data/problems/cmo/cmo-2023-p5-cut-bound-independent-set.yaml`
- Classification: **reject**
- Basis: The lower guarantee and sharpness example are ordinary halves of one exact-bound problem.

### cmo-2025-p1-voting-functional-graph
- File: `data/problems/cmo/cmo-2025-p1-voting-functional-graph.yaml`
- Classification: **reject**
- Basis: One convergence statement for one update process. Functional-graph language is a model, not a second formulation.

### cmo-2025-p5-ant-planar-graph
- File: `data/problems/cmo/cmo-2025-p5-ant-planar-graph.yaml`
- Classification: **reject**
- Basis: One contradiction/existence statement about repeated rectangle use; planar graph interpretation is proof infrastructure.

### cmo-2026-p3-grid-hamiltonian-snail
- File: `data/problems/cmo/cmo-2026-p3-grid-hamiltonian-snail.yaml`
- Classification: **reject**
- Basis: This is one minimax value problem. Monster placement and snail response are the two players' roles, not independent variants.

### bmo-2013-p4-weakly-friendly-cycles-three-rooms
- File: `data/problems/bmo/bmo-2013-p4-weakly-friendly-cycles-three-rooms.yaml`
- Classification: **reject**
- Basis: One coloring/partition theorem is present. The graph-theory restatement does not add a separate formulation.

### bmo-2016-p4-infinite-grid-diamond-coloring
- File: `data/problems/bmo/bmo-2016-p4-infinite-grid-diamond-coloring.yaml`
- Classification: **reject**
- Basis: The `1 x 1201` and `1201 x 1` rectangles are symmetric orientations of the same conclusion, not independent variants. The diamond tiling facts are lemmas inside one proof.

### bmo-2022-p4-frog-grid-boundary-graph
- File: `data/problems/bmo/bmo-2022-p4-frog-grid-boundary-graph.yaml`
- Classification: **reject**
- Basis: One guaranteed-covering number is requested. Component/boundary graph language is the solution model.

### bmo-2025-p4-flights-long-short-paths
- File: `data/problems/bmo/bmo-2025-p4-flights-long-short-paths.yaml`
- Classification: **reject**
- Basis: Although the answer classifies several graph families, the task asks for one set of possible values `F`. Checking families and proving the converse are normal parts of one classification proof.

### inmo-2021-p4-detective-cards-hamiltonian-path
- File: `data/problems/inmo/inmo-2021-p4-detective-cards-hamiltonian-path.yaml`
- Classification: **reject**
- Basis: The sufficiency and necessity of 50 questions are two directions of one threshold theorem, not separate problem variants.

### inmo-2023-p1-square-products-components
- File: `data/problems/inmo/inmo-2023-p1-square-products-components.yaml`
- Classification: **reject**
- Basis: The example in the statement illustrates the count; it is not a second task. The component/clique graph model proves the single requested independent-set conclusion.

### baltic-way-1992-p14-mother-vertex-reachability
- File: `data/problems/baltic-way/baltic-way-1992-p14-mother-vertex-reachability.yaml`
- Classification: **reject**
- Basis: One reachability theorem is present; directed-graph wording is equivalent to the city wording.

### baltic-way-1993-p12-three-transport-connected-unions
- File: `data/problems/baltic-way/baltic-way-1993-p12-three-transport-connected-unions.yaml`
- Classification: **reject**
- Basis: Lower bound and construction are the usual exact-minimum proof. The three transport pairs are symmetric constraints of one problem, not separate variants.

### baltic-way-1994-p19-directed-spy-cycles
- File: `data/problems/baltic-way/baltic-way-1994-p19-directed-spy-cycles.yaml`
- Classification: **reject**
- Basis: One implication from 10-subsets to 11-subsets is asked. Degree inequalities and cycle insertion are proof components.

### baltic-way-2020-p9-cool-graph-labeling
- File: `data/problems/baltic-way/baltic-way-2020-p9-cool-graph-labeling.yaml`
- Classification: **reject**
- Basis: One universal labeling-existence theorem; vertex and edge labels are parts of the same definition.

### baltic-way-2023-p6-colour-touch-graph
- File: `data/problems/baltic-way/baltic-way-2023-p6-colour-touch-graph.yaml`
- Classification: **reject**
- Basis: Special values for small `n` and the general formula are cases of one exact maximum problem, not independent formulations.

### baltic-way-2024-p6-tree-edge-slide-labyrinth
- File: `data/problems/baltic-way/baltic-way-2024-p6-tree-edge-slide-labyrinth.yaml`
- Classification: **reject**
- Basis: The graph-theory statement is the same tree-transformation problem in cleaned notation. Reversibility and reduction to a star are lemmas.

### polish-mo-2022-ii-p6-badminton-euler-cycles
- File: `data/problems/polish-mo/polish-mo-2022-ii-p6-badminton-euler-cycles.yaml`
- Classification: **reject**
- Basis: One cancellation theorem is present. The split into one-sided and tied two-match meetings is a proof decomposition.

### polish-mo-2022-iii-p3-robust-chord-graph-sparsification
- File: `data/problems/polish-mo/polish-mo-2022-iii-p3-robust-chord-graph-sparsification.yaml`
- Classification: **reject**
- Basis: The chord and graph formulations are equivalent. The 2022-layer forest claim and component lemma are useful proof lemmas but not independent self-contained variants needing a relation.
