# False friends / paired variants first pass: USA + Putnam

Scope: only `data/problems/usamo`, `data/problems/usajmo`, `data/problems/usa-tst`, `data/problems/putnam`.

This is a broad, low-reasoning candidate filter. I included problems where the statement or solution visibly contains multiple parts, separate requirements, exact-bound proof plus construction, or a graph-theory reformulation that may deserve pair/false-friend review.

## Candidates

### usamo-1976-p1-monochromatic-rectangle-bipartite
- File: `data/problems/usamo/usamo-1976-p1-monochromatic-rectangle-bipartite.yaml`
- Seen variants/parts: explicit `a)` proves every `4x7` two-coloring has a monochromatic rectangle; explicit `b)` constructs a `4x6` coloring without one.
- Preliminary classification: `парный вариант`.

### usamo-1999-p1-checkers-board-graph-rank
- File: `data/problems/usamo/usamo-1999-p1-checkers-board-graph-rank.yaml`
- Seen variants/parts: statement has two separate assumptions `a)` domination of empty cells and `b)` connectedness of occupied cells. Solution also has two viewpoints: incremental "good cells" count and graph rank/circuit-rank count.
- Preliminary classification: `нужно проверить`.

### usamo-2009-p3-tasteful-domino-tiling-alternating-cycles
- File: `data/problems/usamo/usamo-2009-p3-tasteful-domino-tiling-alternating-cycles.yaml`
- Seen variants/parts: explicit `a)` existence of a tasteful domino tiling whenever a tiling exists; explicit `b)` uniqueness of such a tiling. These are different proof tasks.
- Preliminary classification: `ложный друг`.

### usamo-2022-p1-amber-bronze-transversal
- File: `data/problems/usamo/usamo-2022-p1-amber-bronze-transversal.yaml`
- Seen variants/parts: two color quotas and a mixed selection requirement: choose `a` amber and `b` bronze cells with no shared row/column. Could split into two-color matching/transversal constraints rather than a single monotone matching problem.
- Preliminary classification: `нужно проверить`.

### usamo-2022-p6-mathbook-two-common-friends-closure
- File: `data/problems/usamo/usamo-2022-p6-mathbook-two-common-friends-closure.yaml`
- Seen variants/parts: exact minimum problem. Solution visibly separates construction/example for `ceil(3n/2)-2` edges and lower bound/proof of necessity; graph formulation also gives two equivalent operations, "two common neighbors" and completing a `C_4` to `K_4`.
- Preliminary classification: `парный вариант`.

### usamo-2024-p3-balanced-regular-polygon-triangulation
- File: `data/problems/usamo/usamo-2024-p3-balanced-regular-polygon-triangulation.yaml`
- Seen variants/parts: classification/existence problem "for which `n`" with solution split into necessary condition and construction via fan triangulation when `m` is a proper divisor of `n`.
- Preliminary classification: `парный вариант`.

### usamo-2025-p3-gabriel-graph-road-network
- File: `data/problems/usamo/usamo-2025-p3-gabriel-graph-road-network.yaml`
- Seen variants/parts: Alice must force two independent-looking network properties for every Bob placement: finite-chain connectivity between any two cities and no crossings of road interiors. Solution identifies Gabriel graph, then needs both planarity and connectivity under distance assumptions.
- Preliminary classification: `нужно проверить`.

### usajmo-2023-p3-domino-slides-special-square-digraph
- File: `data/problems/usajmo/usajmo-2023-p3-domino-slides-special-square-digraph.yaml`
- Seen variants/parts: asks maximum possible `k(C)`; solution uses special-square digraph/component structure and then optimizes. Related USAMO version asks all possible values, so this may be a paired variant against the broader formulation.
- Preliminary classification: `парный вариант`.

### usamo-2023-p3-domino-slides-special-square-digraph
- File: `data/problems/usamo/usamo-2023-p3-domino-slides-special-square-digraph.yaml`
- Seen variants/parts: asks all possible values of `k(C)`, not just the maximum. Solution goes through invariant/special-square digraph and then classification of achievable component sizes. Paired with the USAJMO maximum-only version.
- Preliminary classification: `парный вариант`.

### usa-tst-2005-p1-set-system-incidence-graph
- File: `data/problems/usa-tst/usa-tst-2005-p1-set-system-incidence-graph.yaml`
- Seen variants/parts: set-system statement has two structural constraints, pairwise intersections at most one and each ground element in exactly two sets. Graph reformulation collapses these into existence of a simple `m`-regular graph on `2n` vertices; likely a formulation-pair candidate.
- Preliminary classification: `нужно проверить`.

### putnam-1990-b4-cayley-euler-tour
- File: `data/problems/putnam/putnam-1990-b4-cayley-euler-tour.yaml`
- Seen variants/parts: statement says "prove or disprove"; graph formulation asks for a closed directed walk in a Cayley digraph with every vertex appearing exactly twice. Potential false-friend risk if treated as a plain Hamilton/Euler-style existence problem.
- Preliminary classification: `нужно проверить`.

### putnam-1996-a3-course-hypergraph
- File: `data/problems/putnam/putnam-1996-a3-course-hypergraph.yaml`
- Seen variants/parts: statement explicitly asks whether a Ramsey-type alternative is forced, "prove or give a counterexample"; the desired configuration itself has two alternatives: 5 students all taking both courses or 5 students taking neither course.
- Preliminary classification: `ложный друг`.

### putnam-1996-a4-oriented-triples-order
- File: `data/problems/putnam/putnam-1996-a4-oriented-triples-order.yaml`
- Seen variants/parts: statement has three numbered axioms for the ternary relation. Solution includes a key insertion lemma/claim about a unique interval for inserting a new element.
- Preliminary classification: `нужно проверить`.

### putnam-2002-b2-polyhedron-face-game-four-edge-face
- File: `data/problems/putnam/putnam-2002-b2-polyhedron-face-game-four-edge-face.yaml`
- Seen variants/parts: game-strategy proof appears to first prove a structural lemma about a face with at least four sides, then use it for first-player strategy. Candidate for "independent lemma in solution" rather than statement split.
- Preliminary classification: `нужно проверить`.

### putnam-2004-a5-random-checkerboard-components
- File: `data/problems/putnam/putnam-2004-a5-random-checkerboard-components.yaml`
- Seen variants/parts: solution separates random graph translation, deletion of one edge per monochromatic `2x2` block without changing components, and expectation estimate. The `2x2` block lemma may be an independent graph formulation.
- Preliminary classification: `нужно проверить`.

### putnam-2005-a2-rook-tours-grid-hamiltonian-paths
- File: `data/problems/putnam/putnam-2005-a2-rook-tours-grid-hamiltonian-paths.yaml`
- Seen variants/parts: counting problem with special case `n=1`, then a structural decomposition lemma into switching-column blocks before enumeration. Possible pair between grid-walk statement and Hamiltonian-path graph formulation.
- Preliminary classification: `нужно проверить`.

### putnam-2007-a6-admissible-triangulation-bound
- File: `data/problems/putnam/putnam-2007-a6-admissible-triangulation-bound.yaml`
- Seen variants/parts: asks existence of a bound `M_n`; solution proves a boundary-degree estimate, then derives global boundedness. This is an estimate-plus-structural-lemma candidate.
- Preliminary classification: `нужно проверить`.

### putnam-2012-b3-round-robin-winners-hall
- File: `data/problems/putnam/putnam-2012-b3-round-robin-winners-hall.yaml`
- Seen variants/parts: selection problem over days/teams; solution first proves a Hall-type winner-count estimate for arbitrary sets of days, then constructs matching. Graph formulation turns it into choosing one oriented edge from each perfect matching with distinct initial vertices.
- Preliminary classification: `нужно проверить`.

### putnam-2013-b5-functions-iterate-into-roots
- File: `data/problems/putnam/putnam-2013-b5-functions-iterate-into-roots.yaml`
- Seen variants/parts: original functional-iteration statement and graph-theory formulation are marked distinct; solution splits values on root set `R` from a rooted-forest count outside `R`.
- Preliminary classification: `парный вариант`.

### putnam-2016-a5-cayley-digraph-short-words
- File: `data/problems/putnam/putnam-2016-a5-cayley-digraph-short-words.yaml`
- Seen variants/parts: original word form has alternating `g`/`h` exponents in `{−1,1}`; graph formulation uses Cayley digraph generators `{gh, gh^{-1}, g^{-1}h, g^{-1}h^{-1}}` and a short directed route. This is a nontrivial formulation-pair candidate.
- Preliminary classification: `парный вариант`.

### putnam-2017-a6-icosahedron-edge-colorings
- File: `data/problems/putnam/putnam-2017-a6-icosahedron-edge-colorings.yaml`
- Seen variants/parts: face condition is "two edges one color and the third another", equivalently neither all equal nor all different. Solution uses a finite-field reformulation and a surjectivity/counting split.
- Preliminary classification: `нужно проверить`.

### putnam-2021-b5-very-odd-matrices-dag
- File: `data/problems/putnam/putnam-2021-b5-very-odd-matrices-dag.yaml`
- Seen variants/parts: matrix statement and graph-theory statement differ substantially: odd principal minors become an acyclic digraph condition, then powers preserve triangular-unipotent form. Candidate for graph-formulation pair.
- Preliminary classification: `парный вариант`.

### putnam-2025-a3-ternary-string-game-perfect-matching
- File: `data/problems/putnam/putnam-2025-a3-ternary-string-game-perfect-matching.yaml`
- Seen variants/parts: statement asks winner for every `n>=1`; solution uses graph-game formulation plus perfect matching on all nonzero strings. Potential split between game statement and matching strategy lemma.
- Preliminary classification: `нужно проверить`.

### putnam-2025-a4-cycle-commutation-graph-matrices
- File: `data/problems/putnam/putnam-2025-a4-cycle-commutation-graph-matrices.yaml`
- Seen variants/parts: exact minimum `k`; solution must show construction for `k<=3` and impossibility for smaller `k`. Statement also has an iff commutation condition: commute for adjacent cycle indices and do not commute otherwise.
- Preliminary classification: `парный вариант`.

## Borderline non-inclusions from first pass

- `usamo-1976`, `usamo-2009`, and the `2023` domino-slide pair are the clearest explicit paired variants.
- Many remaining files have both `original` and `graph_theory` statements in the data model. I did not list every such file automatically; I listed the ones where the reformulation looked like it might change the working problem or expose an independent lemma.
- Files that looked mostly like single-target translations after this pass: `usamo-2004-p4`, `usamo-2008-p3`, `usamo-2008-p6`, `usamo-2021-p2`, `putnam-1988-a4`, `putnam-1994-a3`, `putnam-2013-a1`, `putnam-2014-b3`.
