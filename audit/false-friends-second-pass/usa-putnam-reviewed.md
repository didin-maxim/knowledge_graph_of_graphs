# False friends / paired variants second pass: USA + Putnam

Source: `audit/false-friends-first-pass/usa-putnam.md`.

Criterion for this pass: accept only when the candidate really contains two or more independent self-contained formulations/variants, or a substantial self-contained lemma that should be split out. Plain "upper/lower bound plus construction", routine proof subcases, and direct graph translations are rejected.

## Reviewed candidates

### usamo-1976-p1-monochromatic-rectangle-bipartite
- File: `data/problems/usamo/usamo-1976-p1-monochromatic-rectangle-bipartite.yaml`
- Verdict: accepted.
- Classification: `pair_variant`.
- Reason: the statement has two explicit self-contained tasks: force a monochromatic rectangle on `4x7`, and construct a `4x6` coloring avoiding one. They share the same threshold idea but are independently askable.
- Proposed relation type: `pair_variant/sharpness_pair`.

### usamo-1999-p1-checkers-board-graph-rank
- File: `data/problems/usamo/usamo-1999-p1-checkers-board-graph-rank.yaml`
- Verdict: rejected.
- Classification: `reject`.
- Reason: the two assumptions are simultaneous hypotheses of one domination/connectivity problem, not separate variants. The circuit-rank argument is an alternative solution strengthening, not a hidden second formulation.

### usamo-2009-p3-tasteful-domino-tiling-alternating-cycles
- File: `data/problems/usamo/usamo-2009-p3-tasteful-domino-tiling-alternating-cycles.yaml`
- Verdict: accepted.
- Classification: `false_friend`.
- Reason: parts (a) and (b) look like a natural existence-and-uniqueness pair, but the solution mechanisms are substantially different: induction/forced corner construction for existence, and symmetric-difference alternating cycles plus boundary obstruction for uniqueness.
- Proposed relation type: `false_friend/existence_vs_uniqueness`.

### usamo-2022-p1-amber-bronze-transversal
- File: `data/problems/usamo/usamo-2022-p1-amber-bronze-transversal.yaml`
- Verdict: rejected.
- Classification: `reject`.
- Reason: the amber and bronze quotas are coupled in one mixed matching/transversal assertion. There are not two standalone tasks; separating colors would lose the real content.

### usamo-2022-p6-mathbook-two-common-friends-closure
- File: `data/problems/usamo/usamo-2022-p6-mathbook-two-common-friends-closure.yaml`
- Verdict: rejected.
- Classification: `reject`.
- Reason: this is a standard exact minimum problem. Construction and lower bound are ordinary halves of one extremal answer; the `C_4` to `K_4` language is an equivalent description of the same closure rule.

### usamo-2024-p3-balanced-regular-polygon-triangulation
- File: `data/problems/usamo/usamo-2024-p3-balanced-regular-polygon-triangulation.yaml`
- Verdict: rejected.
- Classification: `reject`.
- Reason: necessity and construction are the usual two directions of one classification theorem. No independent variant survives the stricter criterion.

### usamo-2025-p3-gabriel-graph-road-network
- File: `data/problems/usamo/usamo-2025-p3-gabriel-graph-road-network.yaml`
- Verdict: accepted.
- Classification: `lemma_split`.
- Reason: after choosing `P,Q,S`, the solution reduces to two standard self-contained Gabriel-graph facts: planarity/noncrossing and connectivity under the distance condition. These should be lemma dependencies rather than relations between problem variants.
- Proposed relation type: `lemma_split/gabriel_planarity_connectivity`.

### usajmo-2023-p3-domino-slides-special-square-digraph
- File: `data/problems/usajmo/usajmo-2023-p3-domino-slides-special-square-digraph.yaml`
- Verdict: accepted.
- Classification: `pair_variant`.
- Reason: this is a genuine lighter variant of the USAMO 2023 P3 problem: same state graph and special-square machinery, but asks only for the maximum possible `k(C)`.
- Proposed relation type: `pair_variant/same_core_weaker_goal`, paired with `usamo-2023-p3-domino-slides-special-square-digraph`.

### usamo-2023-p3-domino-slides-special-square-digraph
- File: `data/problems/usamo/usamo-2023-p3-domino-slides-special-square-digraph.yaml`
- Verdict: accepted.
- Classification: `pair_variant`.
- Reason: this is the stronger companion to the USAJMO version: it asks for all possible values of `k(C)`, not only the maximum. The core invariant is shared, but the achievement/classification layer is additional.
- Proposed relation type: `pair_variant/same_core_stronger_goal`, paired with `usajmo-2023-p3-domino-slides-special-square-digraph`.

### usa-tst-2005-p1-set-system-incidence-graph
- File: `data/problems/usa-tst/usa-tst-2005-p1-set-system-incidence-graph.yaml`
- Verdict: rejected.
- Classification: `reject`.
- Reason: the set-system and simple regular graph statements are essentially an exact incidence translation. Useful as a formulation in the card, but not a false-friend or paired-variant relation.

### putnam-1990-b4-cayley-euler-tour
- File: `data/problems/putnam/putnam-1990-b4-cayley-euler-tour.yaml`
- Verdict: rejected.
- Classification: `reject`.
- Reason: "prove or disprove" is just the Putnam prompt format here; the solution proves the statement via an Euler tour in the Cayley digraph. No separate variant is hidden.

### putnam-1996-a3-course-hypergraph
- File: `data/problems/putnam/putnam-1996-a3-course-hypergraph.yaml`
- Verdict: rejected.
- Classification: `reject`.
- Reason: the two alternatives in the desired Ramsey-type conclusion are one combined target, and the actual answer is a single counterexample. Not two independent formulations.

### putnam-1996-a4-oriented-triples-order
- File: `data/problems/putnam/putnam-1996-a4-oriented-triples-order.yaml`
- Verdict: accepted.
- Classification: `lemma_split`.
- Reason: the induction uses a substantial insertion lemma: after deleting one element, the four-point rule determines a unique interval for reinsertion. That lemma is self-contained and more useful as a dependency than as a variant relation.
- Proposed relation type: `lemma_split/unique_insertion_interval`.

### putnam-2002-b2-polyhedron-face-game-four-edge-face
- File: `data/problems/putnam/putnam-2002-b2-polyhedron-face-game-four-edge-face.yaml`
- Verdict: accepted.
- Classification: `lemma_split`.
- Reason: the game strategy depends on a separate structural lemma for cubic polyhedra with at least five faces: existence of a sufficiently large face/fork. This is independently formulable and should not be encoded as a relation between game variants.
- Proposed relation type: `lemma_split/large_face_in_cubic_polyhedron`.

### putnam-2004-a5-random-checkerboard-components
- File: `data/problems/putnam/putnam-2004-a5-random-checkerboard-components.yaml`
- Verdict: rejected.
- Classification: `reject`.
- Reason: the random graph translation and the `2x2` deletion observation are proof infrastructure for one expectation estimate. The local observation is too small/routine for a standalone relation.

### putnam-2005-a2-rook-tours-grid-hamiltonian-paths
- File: `data/problems/putnam/putnam-2005-a2-rook-tours-grid-hamiltonian-paths.yaml`
- Verdict: rejected.
- Classification: `reject`.
- Reason: the rook-tour and Hamiltonian-path statements are the same problem in graph language. The decomposition into switching-column blocks is part of the enumeration proof.

### putnam-2007-a6-admissible-triangulation-bound
- File: `data/problems/putnam/putnam-2007-a6-admissible-triangulation-bound.yaml`
- Verdict: accepted.
- Classification: `lemma_split`.
- Reason: the proof has reusable graph lemmas about boundary-degree/removable boundary chains in disk triangulations with interior degree at least 6. These are better split as lemmas than treated as variants of the Putnam problem.
- Proposed relation type: `lemma_split/boundary_degree_triangulation`.

### putnam-2012-b3-round-robin-winners-hall
- File: `data/problems/putnam/putnam-2012-b3-round-robin-winners-hall.yaml`
- Verdict: accepted.
- Classification: `lemma_split`.
- Reason: the key Hall verification is a self-contained winner-count lemma for arbitrary sets of days. The tournament statement and matching formulation are one problem, but that lemma deserves separate dependency treatment.
- Proposed relation type: `lemma_split/hall_winner_count`.

### putnam-2013-b5-functions-iterate-into-roots
- File: `data/problems/putnam/putnam-2013-b5-functions-iterate-into-roots.yaml`
- Verdict: rejected.
- Classification: `reject`.
- Reason: the functional digraph form is a direct translation of function iteration into rooted components. It changes language but not the task into an independent variant.

### putnam-2016-a5-cayley-digraph-short-words
- File: `data/problems/putnam/putnam-2016-a5-cayley-digraph-short-words.yaml`
- Verdict: accepted.
- Classification: `pair_variant`.
- Reason: the word statement and the Cayley-digraph route statement are both self-contained and the block-generators `{gh, gh^{-1}, g^{-1}h, g^{-1}h^{-1}}` are a nontrivial repackaging of the alternating word condition. The ideas are close, but the working formulation is genuinely different.
- Proposed relation type: `pair_variant/nontrivial_graph_reformulation`.

### putnam-2017-a6-icosahedron-edge-colorings
- File: `data/problems/putnam/putnam-2017-a6-icosahedron-edge-colorings.yaml`
- Verdict: rejected.
- Classification: `reject`.
- Reason: the finite-field encoding and surjectivity/counting steps are one solution strategy for one counting problem. The face condition has equivalent phrasings, but no independent variant.

### putnam-2021-b5-very-odd-matrices-dag
- File: `data/problems/putnam/putnam-2021-b5-very-odd-matrices-dag.yaml`
- Verdict: accepted.
- Classification: `pair_variant`.
- Reason: the matrix problem and the mod-2 DAG/triangular-unipotent formulation are both self-contained, and the graph version exposes the central mechanism rather than merely renaming objects.
- Proposed relation type: `pair_variant/structural_graph_reformulation`.

### putnam-2025-a3-ternary-string-game-perfect-matching
- File: `data/problems/putnam/putnam-2025-a3-ternary-string-game-perfect-matching.yaml`
- Verdict: accepted.
- Classification: `lemma_split`.
- Reason: the winning strategy reduces to a standalone perfect-matching lemma on all nonzero ternary strings. The game and graph-game statements are equivalent; the matching lemma is the piece worth splitting out.
- Proposed relation type: `lemma_split/nonzero_ternary_string_matching`.

### putnam-2025-a4-cycle-commutation-graph-matrices
- File: `data/problems/putnam/putnam-2025-a4-cycle-commutation-graph-matrices.yaml`
- Verdict: rejected.
- Classification: `reject`.
- Reason: construction in dimension 3 and impossibility in dimension 2 are ordinary halves of one exact-minimum problem. The adjacency/nonadjacency commutation condition is a single target graph, not separate variants.

## Summary

- Accepted as `pair_variant`: `usamo-1976-p1`, `usajmo-2023-p3`, `usamo-2023-p3`, `putnam-2016-a5`, `putnam-2021-b5`.
- Accepted as `false_friend`: `usamo-2009-p3`.
- Accepted as `lemma_split`: `usamo-2025-p3`, `putnam-1996-a4`, `putnam-2002-b2`, `putnam-2007-a6`, `putnam-2012-b3`, `putnam-2025-a3`.
- Rejected: `usamo-1999-p1`, `usamo-2022-p1`, `usamo-2022-p6`, `usamo-2024-p3`, `usa-tst-2005-p1`, `putnam-1990-b4`, `putnam-1996-a3`, `putnam-2004-a5`, `putnam-2005-a2`, `putnam-2013-b5`, `putnam-2017-a6`, `putnam-2025-a4`.
