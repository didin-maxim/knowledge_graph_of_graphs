# High verification: CMO grid and Putnam cycle candidates

Scope: two international direct-relation candidates promoted from
`docs/archive/direct-relation-duplicate-sweep/medium-international.md`.

Constraint followed: `data/` was read only; no `data/` edits were made.

## Verdict summary

| Pair | Current direct relation | Classification | Action |
| --- | --- | --- | --- |
| `cmo-2015-p3-grid-hamiltonian-turtle` vs `cmo-2026-p3-grid-hamiltonian-snail` | `same_motif`, distance 1 | weak motif / relation cleanup | Keep separate; relation is legitimate but should not be treated as duplicate-risk. |
| `putnam-2025-a4-cycle-commutation-graph-matrices` vs `cmo-1994-p3-voting-stabilizes-cycle` | `reformulation`, distance 1 | false_friend | Not a reformulation; retype/remove as relation-quality cleanup. |

## 1. CMO 2015 P3 grid turtle vs CMO 2026 P3 grid snail

Classification: weak motif / relation cleanup.

Not `same_problem/generalize`: neither statement contains the other, and the
answers are for different extremal quantities. CMO 2015 asks for the largest
forced `k` such that some row or column is entered at least `k` times during a
Hamiltonian cycle on a `(4n+2) x (4n+2)` cell grid; the card solution gives
answer `2n+2`. CMO 2026 asks for the minimax value of a labelling game on a
`2n x 2n` grid, where `2n^2` monster cells are chosen first and Turbo then
chooses a Hamiltonian path; the card solution gives answer `4n^4`.

Not `paired_variant`: the two cards are not split cases of one source problem
and do not share a common parameterized statement. The shared object is a square
grid Hamiltonian traversal, not a common theorem with two complementary cases.

Not `false_friend`: there is real solution-level contact. The direct relation
`rel-cmo-2015-p3-cmo-2026-p3-grid-hamiltonian-cycle` accurately says both
solutions use Hamiltonian traversals/cycles on square cell grids. The 2026 upper
bound explicitly uses a Hamiltonian cycle and compares the two opposite
directions around it; the 2015 solution uses a Hamiltonian cycle and
row/column-entry averaging plus a sharp quadrant construction.

Why only weak motif / cleanup: the relation is currently high-confidence
`same_motif` at distance 1, but as a duplicate-sweep candidate it should be
de-emphasized. The decisive statistics are unrelated:

- CMO 2015: row/column entry counts `r_i, c_j`, total move count `m^2`, average
  `m/2 = 2n+1`, non-equality forcing `2n+2`, and a four-quadrant Hamiltonian
  cycle construction.
- CMO 2026: a half-board marked set, checkerboard lower bound, and reverse
  traversal averaging along a Hamiltonian cycle to cap the minimax score at
  `4n^4`.

Recommendation: keep both cards separate. If relation cleanup is desired, keep
`same_motif` but treat it as a low duplicate-risk motif edge; no merge,
generalization, or paired-variant handling is indicated.

## 2. Putnam 2025 A4 cycle commutation graph matrices vs CMO 1994 P3 voting stabilizes cycle

Classification: false_friend.

Not `same_problem/generalize`: the statements are about fundamentally different
objects and goals. Putnam 2025 A4 asks for the minimum matrix dimension `k` so
that real matrices `A_1,...,A_2025` commute exactly for equal or adjacent
indices modulo a cycle; the card solution gives `k=3`. CMO 1994 P3 asks for
eventual stabilization of a synchronous two-answer voting process on 25 people
around a table, equivalently a two-color cellular dynamic on `C_25`.

Not `paired_variant`: the tasks are not source siblings, not complementary
cases, and not two variants of one cycle theorem.

False-friend reason: the common word/object "cycle" is doing almost all the
work. In Putnam, `C_2025` is the target commutation graph to realize by
matrices; the proof uses rank-one projectors in `R^3`, vectors
`v_i=(1,i,i^2)^T`, cross products `w_i=v_{i-1} x v_{i+1}`, and a `2 x 2`
centralizer obstruction. In CMO 1994, `C_25` is the physical/local-neighbor
support for a deterministic coloring process; the proof uses monotone growth of
the set of vertices having a same-color neighbor and the impossibility of a
perfect alternating coloring on an odd cycle.

Relation-quality issue: the current direct relation
`rel-putnam-2025-a4-cycle` is typed as `reformulation`, distance 1, with text
only explaining that Putnam realizes a prescribed cycle as a commutation graph.
That does not describe the CMO target at all and is not bidirectionally
meaningful as a reformulation.

Recommendation: remove this direct edge or replace it with a very weak
`same_motif`/`false_friend` cleanup edge, depending on taxonomy policy. It
should not remain `reformulation` and should not contribute to duplicate or
near-duplicate discovery.
