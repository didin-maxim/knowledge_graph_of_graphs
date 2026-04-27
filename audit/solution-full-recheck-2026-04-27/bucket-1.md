# Solution Full Recheck 2026-04-27: Bucket 1

Bucket rule: `sha1(problem_id#solution_id) % 6 == 1`.

## Counts

- total: 57
- placeholders: 6
- checked_non_placeholder: 51
- repaired_easy: 7
- hard_cases: 8
- borderline: 5

## Repairs Made

- `imo-1964-p4-three-topic-ramsey#sol-graph-review`: expanded the use of `R(3,3)=6` into a local one-paragraph proof for two-coloured `K_6`.
- `imo-1992-p3-nine-points-partial-ramsey#sol-aops-six-vertex-ramsey`: expanded the final `R(3,3)=6` step locally.
- `kolmogorov-2008-round-2-first-league-and-higher-junior-problem-1#sol-official-compressed`: replaced the incorrect explanation of the factor `2` with the block/boundary-edge argument from the detailed wheel solution.
- `kolmogorov-2022-round2-juniors-hamiltonian-path-parity#sol-official-restored`: removed a stray closing brace from restored TeX text.
- `kolmogorov-2022-round4-high-airport-walk-parity#sol-official-restored`: removed rubric artefacts and the stray closing brace from restored TeX text.
- `kolmogorov-2022-round4-high-maximum-length-tree-diameter-circles#sol-official-restored`: removed rubric artefacts and the stray closing brace from restored TeX text.
- `usamo-1976-p1-monochromatic-rectangle-bipartite#sol-column-pair-double-counting`: replaced the reference to a "standard" `4x6` colouring with an explicit column construction using the six 2-subsets of four rows.

## Placeholders Counted Only

These are exact `Решение пока не найдено` entries and were not edited.

- `kolmogorov-2009-round2-high-local-vertex-cover-coloring#sol-import-note`
- `kolmogorov-2009-round3-high-edge-label-three-edge-path#sol-import-note`
- `kolmogorov-2014-round1-complete-graph-orientation-game#sol-import-note`
- `yumt-2021-grand-round4-problem3#sol-archive-card`
- `yumt-2024-grand-final-problem9#sol-archive-card`
- `yumt-2025-grand-final-problem5#sol-archive-card`

## Hard List

- `imo-1991-p4-connected-graph-gcd-edge-labels#sol-aops-maximal-path-labeling`: not self-contained. The path-processing algorithm is only sketched; it does not rigorously prove that every vertex of degree at least 2 receives two consecutive incident labels. Needs the official IMO 1991 P4 proof or a fully specified path-removal/labeling invariant.
- `imo-2024-c8-board-coloring-tree#sol-directed-tromino-tree`: not self-contained as a standalone solution. The "no parallel arrows / no zigzag" claims and the grouping into `2x2` blocks are asserted without enough local proof. Needs the official shortlist solution or a diagram-backed proof of the directed tromino tree reduction.
- `kolmogorov-2008-round-2-high-league-problem-1#sol-official-compressed`: does not answer the exact extremal question. It gives merge-sort sufficiency and an information lower bound, i.e. the right order, but not an exact worst-case number if the problem asks "сколько вопросов достаточно" as an olympiad answer. Needs the official solution/answer or a clear statement that asymptotic sufficiency is all that is claimed.
- `tc-1994-95-common-grandfather-intersecting-edges#sol-star-or-triangle`: depends on modelling each child as an edge between exactly two grandfathers, while the stored statement only says every two children have a common grandfather. Needs the original wording/source confirming the two-grandfather model, or a proof that a pairwise-intersecting two-choice reduction can be made.
- `usamo-2004-p4-black-path-grid-game#sol-bob-shifted-row-pairing`: not self-contained. The Bob strategy for rows `3,4,5,6` is compressed to "answers inside the same block", and the shifted-row maximum invariant is not written as an actual legal response strategy with rational numbers. Needs the full AoPS/official strategy, preferably with the separator invariant.
- `usamo-2008-p3-diamond-lattice-path-partition#sol-complement-trim-induction`: outline only. It says to delete the outer shell and "a small number of edges" to get a smaller path-cover counterexample, but the edge counts and trimming rules are missing. Needs the full AoPS proof or replacement by a complete invariant proof.
- `utyum-2018_lichol_6_strategic_cities#sol-official`: not self-contained. The upper bound cites "the same local procedure as in the villages/cities problem" without giving the removal lemma or induction. Needs the official solution or a local proof of the `2n/3` dominating-set bound for trees.
- `yumt-2015-grand-final-problem5#sol-external-mse-chromatic-partition`: depends on the Stiebitz double-critical theorem by reference to another card. The reduction is clear, but this solution entry is not standalone unless theorem-card references are accepted as self-contained. Needs either an inline theorem statement/proof or explicit policy that local theorem cards may be prerequisites.

## Borderline

- `five-color-theorem#sol-kempe-sketch`: passable for a theorem card, but the Kempe-chain noncrossing obstruction is compressed to one sentence.
- `fyum-2013-tur1a-p4#sol-official-archive`: long and coherent, but the maximal-period argument is dense; future polish should spell out why the period bound gives enough outside vertices in every case.
- `imo-2024-c8-board-coloring-tree#sol-x-graph-halving`: likely correct and more complete than the directed-tromino version, but the "empty block gives a closed cycle of neighbouring crosses" step would benefit from a small figure or more formal planar argument.
- `kolmogorov-2018-team-olympiad-seniors-problem-5#sol-official-compressed`: likely correct, but the inequalities in the four-part split and the extremal example are quite compressed; keep for future source comparison.
- `utyum-2025_komol65_8_6_oriented_graph_bound#sol-official`: likely the intended induction, but the claims `|A|>k-1`, "`A` satisfies the analogous condition", and the final size algebra are only sketched.

## Checked As Self-Contained

- `flashlight-batteries-tournament-cities-2015#sol-pile-construction`
- `mantel-theorem#sol-degree-sum`
- `tournament-hamiltonian-path#sol-insertion`
- `fyum-2008-tur3a-p2#sol-official-archive`
- `fyum-2009-tur3b-p7#sol-official-archive`
- `fyum-2011-tur1a-p5#sol-official-archive`
- `fyum-2012-tur1a-p10#sol-greedy-distance-two-bound`
- `fyum-2013-tur2a-p1#sol-official-archive`
- `imo-1964-p4-three-topic-ramsey#sol-graph-review`
- `imo-1992-p3-nine-points-partial-ramsey#sol-aops-six-vertex-ramsey`
- `imo-1996-c1-grid-knight-reachability-r97-impossible#sol-band-parity-obstruction`
- `imo-2005-c2-dynastic-vertices-forest#sol-secondary-sketch`
- `imo-2015-c5-sequence-rays#sol-official-compressed`
- `imo-2019-c4-labyrinth-region-graph#sol-official-compressed`
- `kolmogorov-2003-team-olympiad-seniors-problem-8#sol-official-expanded`
- `kolmogorov-2008-round-2-first-junior-league-problem-1#sol-official-compressed`
- `kolmogorov-2008-round-2-first-league-and-higher-junior-problem-1#sol-official-compressed`
- `kolmogorov-2015-individual-olympiad-juniors-problem-7#sol-official-compressed`
- `kolmogorov-2015-round-3-missionaries-and-cannibals-problem#sol-official-compressed`
- `kolmogorov-2021-t2-circulant-rainbow-reachability#sol-mod-20-coloring`
- `kolmogorov-2022-round2-juniors-hamiltonian-path-parity#sol-official-restored`
- `kolmogorov-2022-round4-high-airport-walk-parity#sol-official-restored`
- `kolmogorov-2022-round4-high-maximum-length-tree-diameter-circles#sol-official-restored`
- `memo-2025-i2-ruby-rooks-two-step-reachability#sol-official-compressed`
- `rmm-2012-p1-sociable-sets-bipartite-parity#sol-official-compressed`
- `tc-2013-14-vertex-transitive-not-transposition#sol-counterexample-from-source`
- `usa-tst-2009-p6-tournament-gap-ordering#sol-components-hamiltonian-cycle`
- `usamo-1976-p1-monochromatic-rectangle-bipartite#sol-column-pair-double-counting`
- `usamo-1999-p1-checkers-board-graph-rank#sol-good-squares-in-connected-order`
- `usamo-1999-p1-checkers-board-graph-rank#sol-circuit-rank-bound`
- `utyum-2006_ural27_8_acquaintance_pairs#sol-official`
- `utyum-2008_tur4_31_6_directed_cities#sol-official`
- `utyum-2010_tur4_36_4_islands_bridges#sol-official`
- `utyum-2023_komol60_6_7_company_departures#sol-official`
- `utyum-2023_komol61_6_2_common_acquaintances#sol-official`
- `utyum-2025_komol64_7_5_important_cities_tree#sol-official`
- `vosh-2025-26-final-regions-friendship-coloring#sol-official-compressed`
- `yumt-2025-unior-round1-problem1#sol-archive-card`

## Validation

- `python tools\validate.py`: OK (`333 problems, 386 relations, 9 comments, 353 sources, 27 definitions, 15 standard ideas, 19 import batches`)
- `python tools\check_links.py`: OK (`375 internal routes, 353 external source URLs syntactically valid`)
