# Full solution recheck, bucket 3

Date: 2026-04-27

Bucket rule: `sha1(problem_id#solution_id) % 6 == 3`.

## Counts

- total: 49
- placeholders: 4
- checked_non_placeholder: 45
- repaired_easy: 4
- hard_cases: 7
- borderline: 5

Placeholder entries counted as no-solution and left unchanged:

- `yumt-2012-start-round2-problem5#sol-archive-card`
- `yumt-2014-start-final-problem1#sol-archive-card`
- `yumt-2016-team-olympiad-9-11-problem8#sol-archive-card`
- `yumt-2025-grand-round4-problem3#sol-archive-card`

## Easy repairs made

- `dirac-theorem#sol-longest-path`: expanded the longest-path proof, including the index intersection, connectedness from minimum degree, and the final extension contradiction.
- `hall-marriage-theorem#sol-induction`: expanded the induction proof, including preservation of Hall's condition after deleting `x,y` and the tight-set decomposition case.
- `tree-equivalent-properties#sol-minimal-connected-subgraph`: expanded to prove all implications among the three stated tree characterizations.
- `kolmogorov-2007-round-3-high-and-first-league-problem-3#sol-official-compressed`: fixed the summation sentence; each edge is counted once among the induced two-class subgraphs, not three times.

## Hard list

- `menger-theorem#sol-flow-sketch`: the reduction is mathematically standard, but the proof depends on max-flow min-cut and integral flow decomposition without proving them. Needed: either an in-card proof of the finite integral max-flow min-cut theorem or a local theorem card/source explicitly allowed as dependency.
- `fyum-2008-tur1a-p10#sol-official-archive`: the parity lemma for reversing one edge of a tournament is only stated. Needed: official proof from `src-fyum-2008-tur1a-p10-official` or a complete induction/proof of Redei's odd-Hamilton-path theorem.
- `kolmogorov-2008-team-olympiad-seniors-problem-7#sol-official-compressed`: still schematic; it says a monochromatic triangle yields the required configuration and that a count of monochromatic 2-walks gives a monochromatic 4-cycle, but neither step is supplied. Needed: official source `work/kolm/text/2008/komol12.txt`, page 1, or a full Ramsey/counting proof.
- `kolmogorov-2016-team-olympiad-juniors-problem-6#sol-official-compressed`: the upper bound relies on an asserted 12-coloring of the distance graph, and the lower bound compresses the pigeonhole step too far. Needed: explicit 12-coloring and the matching lower-bound lemma for the relevant power of the 2017-cycle.
- `usa-tst-2009-p6-tournament-gap-ordering#sol-mse-tournament-components`: the solution is a summary of two external tournament lemmas from MSE. Needed: full proofs of strong-component ordering and the theorem that every strongly connected tournament on `s` vertices has directed cycles of all lengths `3..s`, or a transferred official/secondary solution.
- `usamo-2024-p3-balanced-regular-polygon-triangulation#sol-fan-and-integrality`: the construction is clear, but the necessity uses algebraic-integer/cyclotomic facts and a coordinate argument not proved in the card. Needed: Evan Chen note/official solution transfer or a self-contained cyclotomic integrality lemma.
- `yumt-2015-grand-round3-problem9#sol-archive-card`: depends on the Bondy-Chvatal closure theorem without proof. Needed: proof of the closure theorem in the card, a local theorem card dependency, or a complete transfer from Baltic Way 2014 problem 10.

## Borderline

- `fyum-2008-tur4b-p10#sol-official-archive`: likely correct, but the final degree-sum contradiction is compressed to one sentence; expand the algebra in a later polish pass.
- `imo-1991-sl9-min-degree-for-k6#sol-graph-review`: uses Turan/symmetrization. This is acceptable if standard theorem dependencies are allowed, but not fully local as written.
- `imo-1995-nc5-greetings-regular-codegree-graph#sol-reviewed-secondary`: proof is essentially complete, but the divisibility step `12k-1 | 525` and filtering to `35` should be expanded for self-contained arithmetic.
- `kolmogorov-2021-team-olympiad-seniors-problem-5#sol-official-compressed`: both the colored-sequence injection and the contraction/deletion induction have the right shape, but reconstruction details are still terse.
- `tc-2023-24-coins-pairing-weighing-forest#sol-forest-accounting`: substantially repaired and plausibly self-contained, but the rare final ambiguity cases in the algorithm are dense enough to merit a human read.

## Clear OK after this pass

This includes already repaired entries that were rechecked in bucket 3.

- `apmo-2010-p3-common-acquaintance-extremal#sol-official-compressed`
- `balanced-bipartite-edge-coloring-two-colors#sol-balanced-edge-coloring`
- `dirac-theorem#sol-longest-path`
- `hall-marriage-theorem#sol-induction`
- `ore-theorem#sol-closure-sketch`
- `tree-equivalent-properties#sol-minimal-connected-subgraph`
- `egmo-2016-p3-blue-cells-bipartite-incidence#sol-official-compressed`
- `egmo-2025-p5-rotating-arrows-odd-parity#sol-parity-bound`
- `fyum-2009-tur4b-p2#sol-official-archive`
- `fyum-2010-tur1a-p8#sol-official-archive`
- `imo-1996-c1-grid-knight-reachability-divisible-2-or-3#sol-modular-obstruction`
- `imo-1999-c5-grid-total-domination#sol-reviewed-web`
- `imo-2004-c8-triangles-tetrahedra-graph#sol-secondary-sketch`
- `kolmogorov-2004-round1-higher-league-problem-3#sol-official-compressed`
- `kolmogorov-2004-team-olympiad-seniors-problem-9#sol-official-compressed`
- `kolmogorov-2005-team-olympiad-juniors-problem-8#sol-official-compressed`
- `kolmogorov-2007-round-2-first-league-problem-8#sol-official-compressed`
- `kolmogorov-2007-round-3-high-and-first-league-problem-3#sol-official-compressed`
- `kolmogorov-2007-team-olympiad-seniors-problem-7#sol-official-compressed`
- `kolmogorov-2008-round-1-high-league-problem-1#sol-official-compressed`
- `kolmogorov-2008-round-4-second-league-problem-7#sol-official-compressed`
- `kolmogorov-2017-individual-olympiad-seniors-problem-7#sol-official-compressed`
- `kolmogorov-2017-team-olympiad-juniors-problem-6#sol-official-compressed`
- `kolmogorov-2022-round2-second-third-red-blue-k10-triangles#sol-official-restored`
- `memo-2025-t4-toll-complete-graph#sol-official-compressed`
- `tc-1980-distinct-rows-delete-column#sol-essential-column-forest`
- `tc-2001-02-rooks-odd-attacks#sol-construct-63`
- `yumt-2013-start-round4-problem8#sol-archive-card`
- `yumt-2014-junior-round1-problem1#sol-archive-card`
- `yumt-2015-grand-round4-problem10#sol-archive-card`
- `utyum-1993_ii_8kl_5#sol-official`
- `utyum-1996_tur3_10_central_cities#sol-official`
- `utyum-2007_lichol30_4_rectangle_coloring#sol-official`

Notes:

- `apmo-2010-p3-common-acquaintance-extremal`, `egmo-2016-p3-blue-cells-bipartite-incidence`, `fyum-2010-tur1a-p8`, `tc-2001-02-rooks-odd-attacks`, `tc-2023-24-coins-pairing-weighing-forest`, `yumt-2015-grand-round4-problem10`, and `kolmogorov-2004-round1-higher-league-problem-3` were among previously repaired or expanded entries and were included in this recheck.
- Placeholder entries were not edited.

## Validation

- `python tools/validate.py` - OK: 333 problems, 386 relations, 9 comments, 353 sources, 27 definitions, 15 standard ideas, 19 import batches.
- `python tools/check_links.py` - OK: 375 internal routes, 353 external source URLs syntactically valid.
