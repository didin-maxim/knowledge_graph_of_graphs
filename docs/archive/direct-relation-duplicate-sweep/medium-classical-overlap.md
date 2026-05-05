# Direct relation duplicate sweep: medium classical overlap

Date: 2026-05-05

Scope E: direct relations where one endpoint is a `data/problems/classical/*` lemma/theorem/problem-family style card and the other endpoint is an olympiad card. `data/definitions/definitions.yaml` was also checked; no direct relation endpoints point to definition ids, so the definition-like part of this pass is represented by classical lemma/tool cards rather than actual definition records.

Method: parsed all problem cards and relation files read-only. Found 584 problem cards, 68 classical cards, 692 relation entries, and 278 direct classical-vs-olympiad relation entries. This report records the medium-priority overlaps where the classical card is close enough to the olympiad card that the relation may want a stronger model than ordinary prerequisite, plus explicit false positives where the current prerequisite interpretation should stay.

## Likely same-statement / theorem-card overlaps

These are not necessarily bad data: in most cases the classical card is the cleaner reusable theorem/lemma form and the olympiad card is a source instance. The issue is that a plain `prerequisite` / `same_motif` relation can hide the fact that the olympiad card is substantially the same mathematical statement.

### `bounded-forward-rays-balanced-sums` vs `imo-2015-c5-sequence-rays`

- Relation: `rel-bounded-forward-rays-balanced-sums-imo-2015-c5`, type `prerequisite`, distance `1`, in `data/relations/relations.d/bounded-forward-rays-balanced-sums.yaml`.
- Classical card: `data/problems/classical/bounded-forward-rays-balanced-sums.yaml`.
- Olympiad card: `data/problems/imo/imo-2015-c5-sequence-rays.yaml`.
- Assessment: high-confidence overlap. The classical statement is the parameterized version with arbitrary `L`; the IMO card's `graph_theory` statement is essentially the same theorem, and the original IMO instance is `L=2015`.
- Recommendation: keep one canonical theorem/lemma card and make the IMO card an instance/source formulation, or mark the relation as same-statement / extracted-theorem rather than ordinary prerequisite. If the data model does not support that relation type, add a note/shared statement group when editing later.

### `third-fourth-distance-layer-bound` vs `imo-2013-c6-flight-distance-layers`

- Relation: `rel-third-fourth-distance-layer-bound-imo-2013-c6`, type `prerequisite`, distance `1`, in `data/relations/relations.d/third-fourth-distance-layer-bound.yaml`.
- Classical card: `data/problems/classical/third-fourth-distance-layer-bound.yaml`.
- Olympiad card: `data/problems/imo/imo-2013-c6-flight-distance-layers.yaml`.
- Assessment: high-confidence overlap. The classical lemma is exactly the parameterized graph-theory form already present in the IMO card; the olympiad instance uses `M=100` and bound `2550`.
- Recommendation: theorem-card canonicalization is preferable to treating this as merely a prerequisite. The olympiad card can remain as the contest-language instance if source provenance matters.

### `redei-odd-hamiltonian-paths-tournament` vs `fyum-2008-tur1a-p10`

- Relation: `rel-redei-odd-hamiltonian-paths-fyum-2008-tur1a-p10`, type `same_motif`, distance `1`, in `data/relations/relations.d/redei-odd-hamiltonian-paths-tournament.yaml`.
- Classical card: `data/problems/classical/redei-odd-hamiltonian-paths-tournament.yaml`.
- Olympiad card: `data/problems/fyum/fyum-2008-tur1a-p10.yaml`.
- Assessment: high-confidence duplicate/same-statement. The FYUM statement is "prove that every tournament has an odd number of Hamiltonian paths", which is the classical theorem statement.
- Recommendation: merge into a single theorem card with FYUM as an olympiad source/instance, or explicitly mark the FYUM card as a contest instance of the theorem. `same_motif` understates the overlap.

### `cubic-graph-four-cycle-bound` vs `fyum-2013-tur2b-p7`

- Relation: `rel-cubic-four-cycle-bound-fyum-2013-tur2b-p7`, type `prerequisite`, distance `1`, in `data/relations/relations.d/cubic-four-cycle-bound.yaml`.
- Classical card: `data/problems/classical/cubic-graph-four-cycle-bound.yaml`.
- Olympiad card: `data/problems/fyum/fyum-2013-tur2b-p7.yaml`.
- Assessment: strong theorem-instance overlap. The FYUM problem asks for the maximum number of 4-cycles in a 3-regular graph on 300 vertices; the classical card is the general `3n/2` bound, extracted from that source.
- Recommendation: make the classical card the canonical theorem/lemma and treat FYUM as a numeric instance. Current prerequisite is serviceable but semantically weaker than extracted theorem / specialization.

### `greedy-strong-edge-coloring-bound` vs `fyum-2012-tur1a-p10`

- Relation: `rel-greedy-strong-edge-coloring-bound-fyum-2012-tur1a-p10`, type `prerequisite`, distance `1`, in `data/relations/relations.d/greedy-strong-edge-coloring-bound.yaml`.
- Classical card: `data/problems/classical/greedy-strong-edge-coloring-bound.yaml`.
- Olympiad card: `data/problems/fyum/fyum-2012-tur1a-p10.yaml`.
- Assessment: strong theorem-instance overlap. The FYUM problem is the `Delta=11` case of the classical greedy bound `2 Delta^2 - 2 Delta + 1 = 221`.
- Recommendation: keep as canonical theorem card plus contest instance, or use a specialization/extracted-theorem relation instead of prerequisite.

## Borderline overlaps: extracted lemma, not full duplicate

These are close because the classical card was extracted from an olympiad solution, but the olympiad problem still has additional modeling, construction, or final steps. I would not merge these outright without a stronger same-statement relation type.

### `grid-boundary-components-coloring-lemma` vs `bmo-2022-p4-frog-grid-boundary-graph`

- Relation: `rel-grid-boundary-components-bmo-2022-p4`, type `prerequisite`, distance `1`, in `data/relations/relations.d/grid-boundary-components-coloring-lemma.yaml`.
- Assessment: the lemma gives the core upper-bound mechanism for the BMO grid/frog problem, but the olympiad card asks for the guaranteed minimum/maximum and still includes the board interpretation and extremal coloring side.
- Recommendation: keep separate. If relation taxonomy grows, `extracted_solution_tool` would be more precise than prerequisite.

### `color-reduction-by-odd-deletion-and-doubling` vs `imo-2013-c3-imons-graph-coloring`

- Relations: `rel-color-reduction-imons` in `data/relations/relations.yaml` and `rel-color-reduction-imo-2013-c3` in `data/relations/relations.d/extracted-graph-lemmas.yaml`; both are `prerequisite`, distance `1`.
- Assessment: the classical card is the main color-reduction step; iterating it solves the IMO problem. It is not exactly the same statement as the full imons problem, but there is also a duplicate relation entry for the same ordered pair.
- Recommendation: do not merge the cards as duplicates. Later data cleanup should deduplicate the two relation entries or intentionally keep one canonical relation with richer text.

### `balanced-bipartite-edge-coloring-two-colors` vs `fyum-2010-tur1a-p8`

- Relation: `rel-fyum-2010-tur1a-p8-tur1b-p8-balanced-edge-coloring`, type `specialization`, distance `1`, in `data/relations/relations.d/fyum-links.yaml`.
- Assessment: related but not a duplicate. The classical card is a two-color/problem-family version; FYUM asks for balanced `k`-coloring. The current relation direction as specialization is more accurate than prerequisite.
- Recommendation: keep separate unless a broader `balanced-bipartite-edge-coloring-k-colors` theorem card is introduced.

### `functional-digraph-pointer-jumping-round-halving` vs `cmo-2025-p1-voting-functional-graph`

- Relation: `rel-cmo-2025-p1-functional-halving-lemma`, type `prerequisite`, distance `1`, in `data/relations/relations.d/cmo-2025-p1-voting-functional-graph.yaml`.
- Assessment: extracted lemma is central but not the full contest problem: CMO starts from the voting cycle and needs iteration to unanimity.
- Recommendation: keep as prerequisite/extracted tool, not duplicate.

## False positives: prerequisite should stay

These were visually/lexically close direct relations but the classical card is a real prerequisite or reusable tool, not the same task.

- `caro-wei-independent-set-bound` -> `imo-2012-c7-equal-sum-chords-independent-set`: Caro-Wei is only the independent-set estimate after building the chord intersection graph.
- `complete-graph-minus-n-minus-2-edges-hamiltonian-path` -> `inmo-2021-p4-detective-cards-hamiltonian-path`: the lemma supports the lower-bound strategy; the game/adversary statement is additional.
- `line-arrangement-side-count-levels` -> `cmo-2022-p4-region-adjacency-coloring`: side-count levels are a coloring invariant/tool, not the full 2-by-3 coloring characterization.
- `quadrangulation-euler-face-count` -> `cmo-1995-p3-polygon-quadrangulation-boomerangs`: Euler face count is one counting step; the boomerang/reflex-vertex argument is separate.
- `gabriel-graph-connected-separated-points` -> `usamo-2025-p3-gabriel-graph-road-network`: connectivity of the Gabriel graph is one of the selected graph properties after Alice's construction; the original problem includes the choice of `P,Q,S` and planarity.
- `gabriel-graph-straight-line-planar` -> `usamo-2025-p3-gabriel-graph-road-network`: same reason; planarity is a prerequisite property, not the whole road-network problem.
- `ferry-network-repartition-lemma` -> `imo-2016-c6-ferry-graph-dynamics`: the lemma preserves a complete bipartite cut structure during the process; the IMO problem needs the global cut-closing hypothesis and terminal universal vertex.
- `tree-vs-independent-set-ramsey-bound` -> `fyum-2008-tur3a-p2`: the Ramsey tree/independent-set lemma supplies the existence of the target tree in a dense graph; the numbered-parent construction is the application.
- `tree-equivalent-properties` relations to olympiad tree problems: usually genuine prerequisites about leaves/unique paths/connected acyclic structure, not duplicate statements.
- `handshaking-lemma`, `euler-formula-planar`, `planar-edge-bound`, `hall-marriage-theorem`, and `konig-vertex-cover-theorem` relations to olympiad cards: broad classical tools; leave as prerequisites unless a specific card repeats the theorem statement verbatim.

## Follow-up candidates

- Add or use a relation type such as `same_statement`, `contest_instance`, or `extracted_theorem` for theorem-instance pairs. Several current `prerequisite` edges are semantically correct for navigation but too weak for duplicate control.
- Consider canonicalizing the strongest same-statement pairs first: `bounded-forward-rays-balanced-sums`, `third-fourth-distance-layer-bound`, `redei-odd-hamiltonian-paths-tournament`, `cubic-graph-four-cycle-bound`, and `greedy-strong-edge-coloring-bound`.
- Clean up the duplicate ordered relation pair `color-reduction-by-odd-deletion-and-doubling` -> `imo-2013-c3-imons-graph-coloring` when write access to data is in scope.
