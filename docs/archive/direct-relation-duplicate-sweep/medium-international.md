# Direct relation duplicate sweep: medium international

Scope: `data/relations/relations.d/*`, direct `distance: 1` relations touching international-series cards:
IMO/Shortlist, APMO, EGMO, MEMO, RMM, Baltic Way, Balkan if present, Polish MO, CMO, BMO, INMO.

Relation types checked: `same_motif`, `prerequisite`, `solution_transfer`, `reformulation`, `specialization`; `paired_variant` and `false_friend` were only skimmed for suspicious near-duplicates.

Result summary: no strong hidden duplicate found. The best candidates below look like close lemma/motif transfers rather than identical tasks under different wording.

## Strong candidates

None found in this medium sweep.

## Medium candidates

### `baltic-way-1992-p14-mother-vertex-reachability` vs `utyum-2008_tur4_31_6_directed_cities`

- Relation: `prerequisite`, `distance: 1`, `rel-baltic-way-1992-utyum-2008-directed-reachability-median`.
- Why it looks close: both statements are about finite directed reachability with pairwise comparability: for any two vertices, one reaches the other. Baltic Way asks for a mother vertex; UTYUM asks, on `2m+1` vertices, for a vertex with at least `m` reachable out-neighbours and at least `m` reachable in-neighbours.
- Statement overlap: Baltic Way is essentially the core reachability lemma used inside UTYUM. The UTYUM graph-theory statement strictly adds the odd-order median/two-sided requirement.
- Solution overlap: UTYUM explicitly uses the same mother-vertex lemma, in dual form, on a subset of vertices; another solution route uses a reachability closure tournament/Hamiltonian path. Baltic Way is the standalone maximal-reachable-set proof.
- Duplicate verdict: not one task as written. This is a lemma-to-application relation, but it is the closest medium-risk item because one problem statement is a clean subclaim of the other's proof.
- High-agent check: confirm whether the database policy wants standalone olympiad lemmas that are also full problems to remain separate when another task is just the median strengthening.

### `cmo-2015-p3-grid-hamiltonian-turtle` vs `cmo-2026-p3-grid-hamiltonian-snail`

- Relation: `same_motif`, `distance: 1`, `rel-cmo-2015-p3-cmo-2026-p3-grid-hamiltonian-cycle`.
- Why it looks close: both are CMO grid problems whose solutions use Hamiltonian walks/cycles on square grids.
- Statement overlap: both use cell-grid adjacency and Hamiltonian traversal. CMO 2015 is a `(4n+2) x (4n+2)` Hamiltonian cycle problem asking for a forced maximum number of row/column entries. CMO 2026 is a `2n x 2n` minimax labelling game over a Hamiltonian path and a half-board set of monsters.
- Solution overlap: both use grid Hamiltonian-cycle constructions and averaging/pairing ideas. However, the CMO 2026 solution is primarily checkerboard lower bound plus opposite-direction cycle pairing; CMO 2015 is row/column entry counting plus sharp quadrant construction.
- Duplicate verdict: likely not duplicate. Same object family, different game/statistic and different extremal answer.
- High-agent check: verify that CMO 2026 did not reuse CMO 2015 as a hidden source with only a changed story; current card evidence suggests no.

## Weak candidates

### `cmo-2006-p4-cycle-triplets-tournament` vs `imo-2010-c5-bad-company-tournament`

- Relation: `same_motif`, `distance: 1`, `rel-cmo-2006-p4-imo-2010-c5-tournament-triples`.
- Why it looks close: both are tournament problems and both count cyclic triples/transitive triples using outdegrees.
- Statement overlap: CMO 2006 asks for the minimum and maximum possible number of cyclic triples in a tournament on `2n+1` teams. IMO 2010 C5 assumes no bad quadruple and proves a cubic degree-imbalance inequality.
- Solution overlap: both use identities involving sums of binomial coefficients in outdegrees. IMO 2010 also counts local winners/losers in triples and quadruples; CMO 2006 is a direct extremal count of 3-cycles.
- Duplicate verdict: not duplicate; shared tournament-counting toolkit only.
- High-agent check: no merge suggested; at most ensure relation remains `same_motif`, not `reformulation`.

### `cmo-1995-p3-polygon-quadrangulation-boomerangs` vs `putnam-2007-a6-admissible-triangulation-bound`

- Relation: `same_motif`, `distance: 1`, `rel-putnam-2007-cmo-1995-planar-decomposition-euler-count`.
- Why it looks close: both translate polygon decompositions into planar graphs and use Euler/face-degree counting.
- Statement overlap: CMO 1995 is about quadrangulations of a convex polygon and counts boomerang quadrilaterals. Putnam 2007 is about triangulations with all internal vertex degrees at least 6 and asks for a bound depending only on boundary size.
- Solution overlap: both use Euler formula and boundary/internal vertex accounting; the geometric constraints and final inequalities are different.
- Duplicate verdict: not duplicate; common planar-counting motif.
- High-agent check: none unless a future relation tries to mark this as `reformulation`.

### `utyum-2016_tur1_start2_1_octahedron_acquaintances` vs `imo-1995-nc5-greetings-regular-codegree-graph`

- Relation: `same_motif`, `distance: 1`, `rel-utyum-2016-octahedron-imo-1995-codegree`.
- Why it looks close: both use regular graphs with controlled common-neighbour counts.
- Statement overlap: UTYUM asks for the smallest graph where every vertex has degree 4 and every adjacent pair has exactly two common neighbours; answer is the 6-vertex octahedron graph. IMO Shortlist 1995 NC5 asks for `12k` people, degree `3k+6`, and the same number of common neighbours for every pair of vertices, then determines `12k`.
- Solution overlap: both look at degree/codegree rigidity, but UTYUM is a tiny construction-plus-exclusion problem; IMO is an arithmetic double-counting problem with constant codegree for all pairs.
- Duplicate verdict: not duplicate; the IMO condition is global and parametrized, while UTYUM only constrains adjacent pairs and minimizes order.
- High-agent check: verify whether this should perhaps be `same_motif` with lower confidence, not a duplicate candidate.

### `imo-2016-c8-domino-unique-tiling-cycles` vs `usamo-2009-p3-tasteful-domino-tiling-alternating-cycles`

- Relation: `same_motif`, `distance: 1`, `rel-imo-2016-c8-usamo-2009-domino-alternating-cycles`.
- Why it looks close: both compare domino tilings/perfect matchings using symmetric difference and alternating cycles.
- Statement overlap: IMO 2016 asks for the minimum number of marked cells on a `2n x 2n` board forcing a unique admissible domino tiling. USAMO 2009 asks existence and uniqueness of a locally constrained "tasteful" tiling for any tileable chessboard polygon.
- Solution overlap: alternating cycles are central to uniqueness in both; USAMO also uses induction/local forbidden `2 x 2` patterns, while IMO uses marked-cell constraints and a sharp `2n` construction/lower bound.
- Duplicate verdict: not duplicate; same uniqueness mechanism, different board class, constraints, and objective.
- High-agent check: no merge suggested; relation looks legitimate as motif/solution transfer.

### `putnam-2025-a4-cycle-commutation-graph-matrices` vs `cmo-1994-p3-voting-stabilizes-cycle`

- Relation: `reformulation`, `distance: 1`, `rel-putnam-2025-a4-cycle`.
- Why it looks suspicious: relation type says `reformulation`, but the two tasks are not reformulations of each other.
- Statement overlap: both mention a cycle graph. Putnam asks for the minimum matrix dimension realizing `C_2025` as a commutation graph. CMO 1994 asks for stabilization of a two-colour cellular automaton on `C_25`.
- Solution overlap: none meaningful beyond "cycle" as an ambient graph. Putnam uses rank-one projectors/vectors in `R^3`; CMO uses monotonic growth of adjacent equal-colour pairs on an odd cycle.
- Duplicate verdict: not duplicate; likely a relation-quality issue rather than a duplicate.
- High-agent check: consider downgrading/retyping this relation, possibly to weak `same_motif` or removing it from direct distance 1.

## Paired variants skim

No paired variant looked like an accidental hidden duplicate.

- `imo-1998-c6-k-le-4-rainbow-edges-impossible`, `imo-1998-c6-k5-rainbow-edges-construction`, `imo-1998-c6-k-ge-6-one-factorization`: split cases/parts of the same original IMO Shortlist problem, not duplicate cards with identical task statements.
- `imo-1996-c1-grid-knight-reachability-*`: variants are different parameter/case cards of the same reachability problem; keep as paired variants unless policy requires recombining split case cards.
- `imo-2024-c4-turbo-grid-monsters-two-attempts-lower-bound` vs `imo-2024-c4-turbo-grid-monsters-three-attempts-strategy`: paired lower/strategy variants, not duplicate.
- `egmo-2025-p5-rotating-arrows-odd-parity` vs `egmo-2025-p5-rotating-arrows-even-dynamic-cycle`: parity variants; not duplicate on this pass.

## Screened-out direct prerequisites

Most other distance-1 edges touching the scope are standard lemma-to-problem prerequisites, not duplicate candidates: `caro-wei-independent-set-bound -> imo-2012-c7`, `hall-marriage-theorem -> imo-2010-c2`, `menger-theorem -> imo-2021-c4`, `tree-equivalent-properties -> imo/memo/rmm tree tasks`, `handshaking-lemma -> cmo/egmo/imo tasks`, `eulerian-graph-criterion -> imo-2020/2023`, `ramsey/turan/mantel -> early IMO shortlist tasks`, and analogous grid/digraph extracted lemmas for APMO/BMO/CMO.
