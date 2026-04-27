# Bucket 4 Full Solution Recheck

Date: 2026-04-27

Scope: all current solution entries with `sha1(problem_id#solution_id) % 6 == 4`.

## Counts

- total: 48
- placeholders: 5
- checked_non_placeholder: 43
- repaired_easy: 2
- hard_cases: 3
- borderline: 4

Note: the earlier sample summary mentioned 49 entries in bucket 4. Recomputing against the current working tree gives 48 entries; the corpus has changed since that sample.

## Placeholder Entries

These are no-solution entries under the current rule and were counted only.

- `kolmogorov-2014-round4-diameter-cycle-length#sol-import-note`
- `yumt-2011-grand-round1-problem9#sol-archive-card`
- `yumt-2011-premier-round4-problem1#sol-archive-card`
- `yumt-2018-grand-round1-problem3#sol-archive-card`
- `yumt-2021-grand-final-problem7#sol-archive-card`

## Easy Repair

- `utyum-1993_ii_7kl_1#sol-official` — replaced the terse cycle-decomposition note with a self-contained permutation proof: the instruction is `p^2(i)=i+1`; for 7 agents a square root of the 7-cycle exists, while a square cannot be a single 8-cycle.
- `yumt-2013-start-round1-problem3#sol-archive-card` — solution was OK; while validating this bucket, also fixed the associated graph statement's broken `definition_id: graph` to `simple_graph` and restored the small LaTeX range `\(3,5,7,\ldots,49\)`.

## Hard Cases

- `imo-2005-c8-noncrossing-diagonals-crossings#sol-reviewed-web` — still not safely self-contained. The upper-bound pairing step and the extremal construction are stated too tersely for a first-principles check. Needs a careful transfer from IMO Compendium / official shortlist solution, including the exact ear-pair summation and construction count.
- `usamo-2022-p6-mathbook-two-common-friends-closure#sol-c4-closure-extremal` — lower bound is explicitly attributed to Evan Chen notes and summarized as "minimal graph analysis"; construction completion is also described as "quickly" becoming complete. Needs the full closure proof / minimal-saturated graph argument from a source.
- `yumt-2014-start-round4-problem2#sol-archive-card` — upper bound is mostly self-contained, but the lower-bound arrangement of 14 queens is only referenced as the official "propeller" construction. Needs the actual board placement/order or the official diagram.

## Borderline

- `kolmogorov-2002-team-olympiad-seniors-problem-8#sol-official-compressed` — retained as a short companion summary; the same card has `sol-official-full`, which is self-contained. If every `solutions[]` item must stand alone, convert this summary to a note or inline the full proof.
- `kolmogorov-2004-round3-higher-league-problem-10#sol-official-compressed` — same pattern: compressed summary is not standalone, but `sol-official-expanded` in the same card is self-contained.
- `rmm-2016-p6-ab-tree-termination-semiinvariant#sol-official-compressed` — likely correct, but the key potential-change identity is left as "direct calculation". Needs one local paragraph expanding which coefficients change.
- `utyum-1995_mb2_8_secret_object#sol-official` — construction is plausible, but the "49.5 turns" description is too informal for strict self-contained status. Needs a clearer invariant/state sequence for the moving illuminated pair.

## Checked OK

- `egmo-2022-p5-domino-parity-bipartite-matching#sol-official-compressed`
- `euler-formula-planar#sol-reduce-to-tree`
- `fyum-2008-tur2b-p5#sol-official-archive`
- `fyum-2009-final-p2#sol-official-archive` — previously hard; now checked as repaired, with the needed diagonal Ramsey theorem transferred into the card.
- `fyum-2010-tur3b-p3#sol-official-archive`
- `fyum-2013-tur2b-p7#sol-official-archive`
- `hall-marriage-theorem#sol-tight-set-splitting`
- `imo-1985-sl5-lattice-perfect-code#sol-graph-review`
- `imo-1989-sl14-seven-points-triangle-cover#sol-graph-review`
- `imo-1998-c6-k5-rainbow-edges-construction#sol-k5-explicit-construction`
- `kolmogorov-2002-individual-olympiad-8-9-output-problem-5#sol-official-compressed`
- `kolmogorov-2002-team-olympiad-seniors-problem-8#sol-official-full`
- `kolmogorov-2004-round3-higher-league-problem-10#sol-official-expanded`
- `kolmogorov-2005-team-olympiad-seniors-problem-9#sol-official-compressed`
- `kolmogorov-2006-round-3-super-league-problem-3#sol-official-compressed` — previous borderline; checked after expansion and now self-contained enough.
- `kolmogorov-2008-individual-olympiad-seniors-problem-5#sol-official-compressed`
- `kolmogorov-2018-team-olympiad-juniors-problem-6#sol-official-compressed`
- `kolmogorov-2021-individual-olympiad-seniors-problem-1#sol-official-compressed`
- `kolmogorov-2021-round1-second-league-problem-10#sol-official-compressed`
- `kolmogorov-2021-t1-critical-strong-orientation#sol-robbins-critical`
- `rmm-2013-p2-tester-pair-endomorphism-digraph#sol-official-compressed`
- `tc-1994-95-common-grandfather-intersecting-edges#sol-three-grandfathers`
- `tc-2015-16-connectivity-query-lower-bound#sol-adversary-cycle-bridge`
- `tc-2017-18-polyhedron-three-colors-parity#sol-handshaking`
- `tc-2020-21-gnomes-two-cycles-odd-n#sol-odd-bridge-strategy`
- `tc-2022-23-blue-red-cells-connectivity#sol-bound-boundary`
- `tournament-hamiltonian-path#sol-max-forward-edges`
- `usa-tst-2005-p1-set-system-incidence-graph#sol-regular-graph-bound`
- `usamo-1999-p1-checkers-board-graph-rank#sol-john-scholes-connected-induction`
- `usamo-2008-p3-diamond-lattice-path-partition#sol-red-black-imbalance`
- `usamo-2008-p6-even-friends-two-rooms#sol-existence-by-switching-odd-vertex` — previous borderline; checked after deep repair and now self-contained.
- `utyum-2024_komol63_67_capital_flights_bipartite#sol-official`
- `yumt-2013-start-round1-problem3#sol-archive-card`
- `yumt-2019-start-first-round4-problem1#sol-archive-card`
- `yumt-2022-start-final-problem6#sol-maximal-matching-independent-set`
- `yumt-2023-granda-round2-problem9#sol-hall-euler-face-counting`
