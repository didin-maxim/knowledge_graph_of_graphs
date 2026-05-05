# False friends second pass: Russian VOSH/SPbMO/School239/TC

Scope: candidates from `audit/false-friends-first-pass/russian-vosh-spb-school239-tc.md`.

Rule used in this pass: accept only genuinely independent self-contained variants or paired formulations. A normal `original`/`graph_theory` reformulation, a routine estimate+construction, or subcases inside one proof is rejected.

## Accepted

### all-union-1986-final-9-tree-distances-one-to-nchoose2

- Classification: `false_friend`
- Relation type to propose: `false_friend`
- Basis: the statement explicitly asks two independent cases, `n=6` and `n=1986`. The `n=6` part is a constructive weighted-tree example; the `n=1986` part is an impossibility/parity obstruction. They look like parameter variants of the same question, but the mathematical tasks and solution modes are genuinely different.

### spbmo-2010-9-p5-k2010-cycle-game and spbmo-2010-11-p3-k2009-long-cycle-game

- Classification: `pair_variant`
- Relation type to propose: `pair_variant`
- Basis: these are separate self-contained maker-breaker cycle-game problems on complete graphs. The ideas are related: reserve/threat edges beat the ten blocked edges. The target cycle lengths and numerical buffers differ enough that neither is just a subcase of the other.

### tc-2018-19-simple-state-tree-game and tc-2018-19-complex-state-cycle-game

- Classification: `false_friend`
- Relation type to propose: `false_friend`
- Basis: the pair was split from one compound source and consists of two self-contained variants of the same orientation game. The tree/simple case gives Petya a non-losing strategy by an orientation invariant; the cyclic/complex case gives Vasya a finite winning strategy by induction/cycle deletion. The formulations are deliberately parallel but the winning side and proof mechanism change.

### tc-2020-21-gnomes-two-cycles-even-n and tc-2020-21-gnomes-two-cycles-odd-n

- Classification: `false_friend`
- Relation type to propose: `false_friend`
- Basis: the even and odd cases are independent parity variants of the same two-cycles/Hamiltonian-cycle game. For even `n` the evil wizard has a coloring obstruction; for odd `n` the good wizard has a constructive bridge strategy. Same shell, opposite outcome and different key argument.

## Non-taxonomy Finding

### spbmo-2024-9-11-metric-path-with-shortcuts and spbmo-2024-9-11-metro-lines-transfer-bound

- Classification for this audit: `reject`
- Suggested separate relation, if duplicate cleanup is allowed later: `duplicate` or `same_problem`
- Basis: these two cards contain the same official statement and graph formulation. This is not a pair-variant/false-friend situation; it is a merge/deduplication issue outside the requested taxonomy.

## Rejected

### vosh-1991-zonal-one-way-streets-return

- Classification: `reject`
- Basis: one problem plus an equivalent graph formulation. The lettered `a), b), c)` items are conditions of one theorem, not independent variants.

### vosh-1992-zonal-air-travel-one-city-redundant

- Classification: `reject`
- Basis: one reachability/cut problem; `original` and `graph_theory` are the same formulation in different language.

### vosh-1992-zonal-airlines-route-transfer

- Classification: `reject`
- Basis: the apparent “or/either” is part of the recoloring/exchange condition; no independent self-contained variants.

### vosh-2000-01-final-tree-leaves-bridge-proof

- Classification: `reject`
- Basis: city and tree versions are equivalent; the proof is a single pairing/max-distance argument.

### vosh-2000-01-final-universal-acquaintance

- Classification: `reject`
- Basis: two solutions are complementary viewpoints for one claim, not separate problem variants.

### vosh-2005-06-final-dominoes-three-color-neighbors

- Classification: `reject`
- Basis: one coloring problem; alternatives are local proof cases inside the same construction.

### vosh-2008-regional-bureaucrats-common-neighborhood

- Classification: `reject`
- Basis: one double-counting statement; no separate formulations beyond graph translation.

### vosh-2010-11-final-nonbreakable-company

- Classification: `reject`
- Basis: one partition/non-bipartite graph claim; subcases belong to the same minimal odd-cycle proof.

### vosh-2010-11-regional-warehouses-cement-routing

- Classification: `reject`
- Basis: one connected-graph transport/routing problem; induction cases are not variants.

### vosh-2013-14-regional-even-rows-columns

- Classification: `reject`
- Basis: `graph_hint_reformulations` is a complement-graph hint for the same task, not an independent formulation.

### vosh-2014-15-regional-grid-rainbow-rectangle

- Classification: `reject`
- Basis: exact-bound problem with proof and construction; this is ordinary estimate+example structure.

### vosh-2017-18-regional-friendship-triangle-factor

- Classification: `reject`
- Basis: exact minimum edge count with construction plus induction; no hidden self-contained variants.

### vosh-2018-19-final-shirt-recoloring

- Classification: `reject`
- Basis: one recoloring theorem; multiple solution viewpoints are not separate tasks.

### vosh-2022-23-final-optimal-road-networks

- Classification: `reject`
- Basis: one theorem about nested optimal rooted forests; `k=1..N` is a parameter range inside one proof, not separate variants.

### vosh-2022-23-regional-connected-country-cut

- Classification: `reject`
- Basis: one connected-country cut theorem; induction subcases are not standalone formulations.

### vosh-2025-26-final-regions-friendship-coloring

- Classification: `reject`
- Basis: same statement in olympiad and graph language. The `11.3 (9.4)` label is grade/number metadata, not two variants.

### vosh-2025-26-regional-common-neighborhood-red-pairs

- Classification: `reject`
- Basis: one exact-bound neighborhood problem; no independent variants.

### vosh-2025-26-regional-degree-difference-friendship

- Classification: `reject`
- Basis: one extremal degree-layer problem; construction and upper bound are standard halves of one solution.

### all-union-1981-final-9-football-independent-triple

- Classification: `reject`
- Basis: football and graph statements are equivalent; one counting proof.

### all-union-1985-final-9-complete-graph-edge-coloring

- Classification: `reject`
- Basis: one geometric edge-coloring exact-value problem; lower and upper bounds are not variants.

### all-union-1987-final-9-tournament-score-squares

- Classification: `reject`
- Basis: one tournament identity; no independent statement split.

### spbmo-1992-11-p55-two-connected-halves

- Classification: `reject`
- Basis: one 2-connected graph partition theorem; original and graph versions are equivalent.

### spbmo-1993-7-p12-unsociable-eccentrics

- Classification: `reject`
- Basis: one social-graph counting problem; no standalone alternatives.

### spbmo-1996-11-p63-metro-distant-stations

- Classification: `reject`
- Basis: one exact maximum problem; upper bound and construction are ordinary solution halves.

### spbmo-1996-9-p46-strongly-connected-tournament-orientations

- Classification: `reject`
- Basis: one probability/counting statement about tournament orientations.

### spbmo-1997-10-p34-million-common-acquaintance-dominating-set

- Classification: `reject`
- Basis: one dominating-set existence problem; degree split is a proof device.

### spbmo-1997-11-p54-triangular-polyhedron-degrees

- Classification: `reject`
- Basis: one Euler/counting polyhedron claim; no independent variants.

### spbmo-1997-11-p63-red-blue-complete-graph-two-edge-count

- Classification: `reject`
- Basis: graph and complement formulations are equivalent tools for one equality.

### spbmo-1997-7-p13-left-right-city-walk

- Classification: `reject`
- Basis: one planar turning-walk statement; “variant/version” was only a reformulation note.

### spbmo-1997-9-p27-common-acquaintance-dominating-set

- Classification: `reject`
- Basis: one smaller-parameter version of a dominating-set problem; this card itself has no hidden split.

### spbmo-2003-11-qual-p6-kernel-graph-shortened

- Classification: `reject`
- Basis: one graph-shortening/spanning-subgraph problem; the graph wording is not a second variant.

### spbmo-2003-9-qual-p5-edge-colored-graph-vertex-coloring

- Classification: `reject`
- Basis: one edge-colored graph coloring theorem.

### spbmo-2009-11-6-monochromatic-long-cycle

- Classification: `reject`
- Basis: one Ramsey-style long-cycle statement; proof cases are internal.

### spbmo-2010-10-p4-cubic-edge-company-game

- Classification: `reject`
- Basis: one edge-coloring game on a cubic graph; no paired self-contained variant in the card.

### spbmo-2011-9-10-p4-triangle-in-every-2000-set-k4

- Classification: `reject`
- Basis: one extremal graph claim; no split into independent variants.

### spbmo-2012-11-p7-bipartite-acyclic-orientations-mod3

- Classification: `reject`
- Basis: one modular/orientation problem; “or” cases are proof alternatives.

### spbmo-2012-7-p4-forty-regular-acquaintance-four-people

- Classification: `reject`
- Basis: one regular-social-graph existence claim.

### spbmo-2012-8-p7-forty-regular-acquaintance-22-cycle

- Classification: `reject`
- Basis: one regular-social-graph cycle claim.

### spbmo-2013-10-11-girls-boys-friendship-cover

- Classification: `reject`
- Basis: the “either older or taller” alternatives define allowed neighborhoods in one bipartite threshold model; they are not two tasks.

### spbmo-2013-8-p5-capital-directed-disjoint-paths

- Classification: `reject`
- Basis: one rooted-digraph closeness theorem; graph version is equivalent to the city wording.

### spbmo-2014-10-p7-digraph-no-odd-cycles-dominating-independent

- Classification: `reject`
- Basis: one directed-graph theorem; cases are structural proof components.

### spbmo-2014-11-2-maximal-matchings-delete-graph

- Classification: `reject`
- Basis: one matching/deletion problem; no independent formulations.

### spbmo-2015-11-6-regular-graph-10-stars

- Classification: `reject`
- Basis: one regular-graph decomposition/counting problem.

### spbmo-2017-10-p7-remove-directed-cycle-keep-strong

- Classification: `reject`
- Basis: one strongly-connected digraph cycle-removal theorem.

### spbmo-2017-11-p6-chordal-clique-euler-characteristic

- Classification: `reject`
- Basis: one chordal/clique-count identity; proof lemmas are not separate problem statements.

### spbmo-2018-10-p1-complete-graph-road-destruction-path

- Classification: `reject`
- Basis: one game/path claim; no hidden variants.

### spbmo-2018-7-p7-bus-graph-no-odd-cycle-paths

- Classification: `reject`
- Basis: one bipartite/no-odd-cycle path problem.

### spbmo-2018-8-p7-k4-edge-spanning-tree-few-degree2

- Classification: `reject`
- Basis: one spanning-tree existence theorem; construction/proof cases are internal.

### spbmo-2019-6-8-p6-company-no-sociable-shy

- Classification: `reject`
- Basis: one social-graph problem; “sociable/shy” are complementary definitions in one statement.

### spbmo-2019-9-11-p2-metro-cover-by-simple-paths

- Classification: `reject`
- Basis: one path-cover problem; no independent statement split.

### spbmo-2019-9-11-p6-regular-graph-2-switches

- Classification: `reject`
- Basis: one regular-graph switch problem; cases are proof mechanics.

### spbmo-2020-karakatitsa-edge-weights

- Classification: `reject`
- Basis: one weighted-edge inequality; matching argument is a proof lemma, not a second formulation.

### spbmo-2021-coordinate-points-two-colored-2factor

- Classification: `reject`
- Basis: one yes/no existence problem; the answer is settled by one construction/argument, not separate variants.

### spbmo-2022-big-small-cities-spanning-forest-leaves

- Classification: `reject`
- Basis: one spanning-forest/leaves problem; “big/small” are roles inside one theorem.

### spbmo-2022-eldorado-friendship-tree-potential

- Classification: `reject`
- Basis: one tree-potential inequality; club wording and tree wording are equivalent.

### spbmo-2023-9-11-components-after-deleting-x-y

- Classification: `reject`
- Basis: one exact component-count problem; no standalone variants.

### spbmo-2024-6-8-atomized-city-acquaintance-pairs

- Classification: `reject`
- Basis: one extremal edge-count problem; construction and bound are ordinary halves.

### spbmo-2024-9-11-metric-path-with-shortcuts

- Classification: `reject`
- Basis: same statement as the metro-lines card; duplicate issue, not a false-friend/pair-variant relation.

### spbmo-2024-9-11-metro-lines-transfer-bound

- Classification: `reject`
- Basis: same statement as the metric-path card; duplicate issue, not a false-friend/pair-variant relation.

### school239-2021-10-11-p8-friendship-parity-postcards

- Classification: `reject`
- Basis: one parity-counting problem; multiple algebraic/graph models support one statement.

### school239-2021-8-9-p3-nonbipartite-min-degree-odd-cycle

- Classification: `reject`
- Basis: one best-bound problem; upper bound and construction are standard exact-answer structure.

### school239-2024-10-11-p8-empty-disk-perfect-matching

- Classification: `reject`
- Basis: one geometric perfect-matching existence theorem.

### school239-2024-8-9-p2-noncrossing-segments-perfect-matching

- Classification: `reject`
- Basis: one yes/no geometric matching problem; counterexample is the answer, not a second variant.

### tc-1980-distinct-rows-delete-column

- Classification: `reject`
- Basis: one table problem with a graph used only in the solution.

### tc-1994-95-common-grandfather-intersecting-edges

- Classification: `reject`
- Basis: original and graph statements are equivalent; the two listed solutions are alternative proofs of one claim.

### tc-2001-02-rooks-odd-attacks

- Classification: `reject`
- Basis: one exact maximum sequence problem; construction and impossibility are ordinary exact-answer halves.

### tc-2009-10-acquaintances-even-cycle

- Classification: `reject`
- Basis: one even-cycle existence problem.

### tc-2010-11-odd-main-roads

- Classification: `reject`
- Basis: one odd-degree spanning-subgraph existence claim.

### tc-2011-ants-two-hamiltonian-cycles-grid

- Classification: `reject`
- Basis: one minimum common-edge problem; graph version and construction are not separate variants.

### tc-2011-programmers-connected-hiring-game

- Classification: `reject`
- Basis: one connected-hiring game; “variant/version” came from source/provenance notes, not from two formulations.

### tc-2012-polyhedron-three-equal-edges

- Classification: `reject`
- Basis: one polyhedron edge-length problem.

### tc-2013-14-vertex-transitive-not-transposition

- Classification: `reject`
- Basis: one yes/no automorphism counterexample problem.

### tc-2015-16-connectivity-query-lower-bound

- Classification: `reject`
- Basis: one query lower-bound problem; adversary cases are proof structure.

### tc-2016-tennis-masters-juniors-regular-bipartite

- Classification: `reject`
- Basis: one regular-bipartite matching/game problem.

### tc-2017-18-polyhedron-three-colors-parity

- Classification: `reject`
- Basis: one parity theorem; the two solutions are alternate proofs, not variants.

### tc-2017-pingpong-same-pairs-tournament-graph

- Classification: `reject`
- Basis: one maximum-`n` graph-of-games problem.

### tc-2018-19-complex-state-cycle-game

- Classification: accepted above as cross-card `false_friend`; not rejected.
- Basis: paired with `tc-2018-19-simple-state-tree-game`.

### tc-2018-19-simple-state-tree-game

- Classification: accepted above as cross-card `false_friend`; not rejected.
- Basis: paired with `tc-2018-19-complex-state-cycle-game`.

### tc-2018-cards-4x4-neighbor-numbers-graph

- Classification: `reject`
- Basis: one reconstruction problem; graph is a solution model only.

### tc-2020-21-gnomes-two-cycles-even-n

- Classification: accepted above as cross-card `false_friend`; not rejected.
- Basis: paired with the odd-`n` card.

### tc-2020-21-gnomes-two-cycles-odd-n

- Classification: accepted above as cross-card `false_friend`; not rejected.
- Basis: paired with the even-`n` card.

### tc-2022-23-blue-red-cells-connectivity

- Classification: `reject`
- Basis: one grid-connectivity counting problem.

### tc-2022-bug-one-way-doors-bridgeless-grid

- Classification: `reject`
- Basis: one reachability theorem in a bridgeless grid graph.

### tc-2022-crossword-word-cell-bipartite-graph

- Classification: `reject`
- Basis: one crossword incidence-counting problem; graph appears only as a model in solution.

### tc-2023-24-coins-pairing-weighing-forest

- Classification: `reject`
- Basis: one weighing algorithm; graph/forest is bookkeeping inside the proof, not a graph formulation of a second task.

### tc-2024-connected-paper-pieces-chessboard-coloring

- Classification: `reject`
- Basis: one connected-pieces coloring problem; alternatives are proof cases, not standalone variants.

