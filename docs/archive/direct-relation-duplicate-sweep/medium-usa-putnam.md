# Direct relation duplicate sweep: USA / Putnam / USAMO / USAJMO / USA TST

Scope D checked:

- archives in scope: `putnam`, `usamo`, `usajmo`, `usa-tst` cards indexed as source `usa`;
- plus direct relation neighbors of those cards;
- read-only for `data/`: no problem cards or relation files were edited.

Index snapshot used: `index/generated.sqlite`.

## Summary

- Scope problems: 35.
- Direct relation rows touching scope: 89.
- Direct-neighbor node set size: 96.
- Strong duplicate / reprint candidates found: 1 pair.
- Near misses worth keeping as relations, not duplicate merges: 3 pairs.

## Duplicate candidate

### `fyum-2009-tur1a-p7` <-> `usa-tst-2009-p6-tournament-gap-ordering`

Verdict: same problem, high confidence.

Files:

- `data/problems/fyum/fyum-2009-tur1a-p7.yaml`
- `data/problems/usa-tst/usa-tst-2009-p6-tournament-gap-ordering.yaml`

Current relation:

- `same_motif`, distance `1`, status `needs_human_review`.

Why this is duplicate-level:

- FYUM statement: a tournament on `n` vertices has no directed cycle of length `m+1`; prove an ordering such that for `i >= k+m-1`, the edge goes from vertex `i` to vertex `k`.
- USA TST statement: for any directed path `P_0 -> P_1 -> ... -> P_M` of `M` edges, `P_0` also beats `P_M`; prove an ordering such that for `a >= b+M-1`, player `a` beats player `b`.
- In a tournament, the USA TST path condition is equivalent to forbidding a directed cycle of length `M+1`: if the last vertex beats the first, the path closes to such a cycle; if the first beats the last, the condition holds for that path.
- Parameters and conclusion match after renaming `n/N` and `m/M`.

Suggested follow-up, not performed in this read-only sweep:

- Treat as a duplicate/reprint-level pair rather than merely `same_motif`.
- Decide which card should be canonical before changing relations or adding aliases.

## Near misses checked

### `usamo-2023-p3-domino-slides-special-square-digraph` <-> `usajmo-2023-p3-domino-slides-special-square-digraph`

Verdict: close official senior/junior variant, not same task.

Reason: same board model, same moves, same `k(C)` object, and same graph core. However USAMO asks for all possible values of `k(C)`, while USAJMO asks only for the maximum possible value. This is a genuine nested variant, but not the same requested result.

### `putnam-2025-a4-cycle-commutation-graph-matrices` <-> `cmo-1994-p3-voting-stabilizes-cycle`

Verdict: not duplicate.

Reason: the current `reformulation` relation is graph-language overlap around cycles, but the objects and goals differ completely: matrix commutation graph realization of `C_2025` versus stabilization of binary voting dynamics on a 25-cycle.

### `imc-2001-day2-p4-zero-principal-minors-acyclic-digraph` <-> `putnam-2021-b5-very-odd-matrices-dag`

Verdict: not duplicate.

Reason: both use the same minimal directed cycle / acyclic support graph mechanism for principal minors, but the hypotheses and conclusions differ: zero principal minors and nilpotence/permutation triangularization versus odd principal determinants and closure under powers.

## Other distance-1 relation pairs sampled

These remained motif-level after checking statements:

- `cmo-1995-p3-polygon-quadrangulation-boomerangs` <-> `putnam-2007-a6-admissible-triangulation-bound`: planar dissection counting, but quadrangulations/boomerangs versus admissible triangulations.
- `imo-2016-c8-domino-unique-tiling-cycles` <-> `usamo-2009-p3-tasteful-domino-tiling-alternating-cycles`: domino tiling uniqueness via alternating cycles, but different boards, constraints, and target statements.
- `putnam-1990-b4-cayley-euler-tour` <-> `putnam-2016-a5-cayley-digraph-short-words`: Cayley digraph language, but Euler tour existence versus short word representation.
- `usamo-2022-p1-amber-bronze-transversal` <-> `imo-2010-c2-flags-diagonal-matching`: bipartite matching/transversal mechanism, but different extremal problems.

## Notes

- There appears to be a duplicate relation row for `imc-2001-day2-p4-zero-principal-minors-acyclic-digraph` -> `putnam-2021-b5-very-odd-matrices-dag` with different statuses in the generated index. I did not inspect or edit relation source files because this sweep was limited to problem-duplicate identification and `data/` was read-only.
