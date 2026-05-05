# High verification: classical theorem cards vs FYUM instances

Date: 2026-05-05

Scope: high-verification follow-up for three classical/FYUM candidates flagged in `medium-classical-overlap.md`.

Constraint followed: read-only over `data/`; this report only records the audit verdicts.

## Summary

| Pair | Verdict | same_problem / general theorem card? | numeric instance? | paired_variant? | false_friend? |
| --- | --- | --- | --- | --- | --- |
| `redei-odd-hamiltonian-paths-tournament` vs `fyum-2008-tur1a-p10` | Duplicate-level same statement | Yes: same theorem statement; classical card is the reusable theorem card | No | No | No |
| `cubic-graph-four-cycle-bound` vs `fyum-2013-tur2b-p7` | Theorem-instance overlap | Yes: classical card is a general extracted lemma | Yes: `n=300`, answer `450` | No | No |
| `greedy-strong-edge-coloring-bound` vs `fyum-2012-tur1a-p10` | Theorem-instance overlap | Yes: classical card is a general greedy bound | Yes: `Delta=11`, `2 Delta^2 - 2 Delta + 1 = 221` | No | No |

Overall recommendation: do not treat any of these as false friends. The first pair is duplicate-level same statement. The other two are deliberate theorem-card plus contest-instance pairs; keeping both cards is reasonable if the model distinguishes reusable theorem cards from source/numeric olympiad instances, but the relation type should be stronger than ordinary prerequisite where supported.

## `redei-odd-hamiltonian-paths-tournament` vs `fyum-2008-tur1a-p10`

Verdict: **same_problem / same_statement**, with the classical card acting as the canonical theorem card.

Classification answers:

- same_problem / general theorem card: **Yes**. Both cards ask/prove the same statement: in every finite tournament, the number of directed Hamiltonian paths is odd.
- numeric instance: **No**. There is no parameter specialization or contest-specific numeric value.
- paired_variant: **No**. This is not an A/B tour variant or reprint pair; it is a classical theorem card linked to an olympiad source card.
- false_friend: **No**. The overlap is exact at statement level, not just a shared parity or tournament motif.

Checked evidence:

- Classical card: `data/problems/classical/redei-odd-hamiltonian-paths-tournament.yaml`.
- FYUM card: `data/problems/fyum/fyum-2008-tur1a-p10.yaml`.
- Direct relation: `data/relations/relations.d/redei-odd-hamiltonian-paths-tournament.yaml`, id `rel-redei-odd-hamiltonian-paths-fyum-2008-tur1a-p10`, currently `same_motif`, confidence `0.99`.
- The relation text itself says the Redei theorem is exactly the classical statement required in FYUM 2008.
- Both solutions use parity invariance under reversing one tournament edge and reduction to a transitive tournament, although the classical card contains a more general/self-contained proof route.

Recommendation:

- Canonical mathematical identity should be the classical theorem card.
- Preserve `fyum-2008-tur1a-p10` only if contest-source cards are intentionally kept as source/instance records.
- If relation taxonomy supports it, replace `same_motif` with a duplicate-level relation such as `same_statement`, `contest_statement_of`, or `source_instance_of`. `same_motif` understates the overlap.

## `cubic-graph-four-cycle-bound` vs `fyum-2013-tur2b-p7`

Verdict: **numeric theorem instance**, not an accidental duplicate.

Classification answers:

- same_problem / general theorem card: **Yes, but not exact same problem wording**. The classical card is the general extracted lemma: a simple 3-regular graph on `n` vertices has at most `3n/2` cycles of length `4`, with sharpness from disjoint copies of `K_{3,3}` when applicable.
- numeric instance: **Yes**. The FYUM card fixes `n=300`; the general bound gives `3*300/2 = 450`, and the construction is `50` disjoint copies of `K_{3,3}`, each contributing `9` four-cycles.
- paired_variant: **No**. There is no second official variant of the same FYUM problem involved.
- false_friend: **No**. The classical lemma directly solves the FYUM problem after the substitution `n=300`.

Checked evidence:

- Classical card: `data/problems/classical/cubic-graph-four-cycle-bound.yaml`.
- FYUM card: `data/problems/fyum/fyum-2013-tur2b-p7.yaml`.
- Direct relation: `data/relations/relations.d/cubic-four-cycle-bound.yaml`, id `rel-cubic-four-cycle-bound-fyum-2013-tur2b-p7`, currently `prerequisite`, confidence `0.99`.
- The classical source role is `extracted_lemma` from `src-fyum-2013-tur2b-p7-official`.
- The FYUM solution performs the same double count: at most `6` four-cycles through each vertex, total `300*6/4 = 450`, with equality on `50` copies of `K_{3,3}`.

Recommendation:

- Keep both cards if the database wants both reusable theorem cards and contest numeric instances.
- Semantically better relation labels would be `numeric_instance_of`, `contest_instance_of`, `specialization`, or `extracted_theorem`; plain `prerequisite` is navigationally acceptable but too weak for duplicate control.
- Do not merge as a pure duplicate unless the project chooses to collapse theorem cards and all their numeric source instances.

## `greedy-strong-edge-coloring-bound` vs `fyum-2012-tur1a-p10`

Verdict: **numeric theorem instance**, not an accidental duplicate.

Classification answers:

- same_problem / general theorem card: **Yes, in theorem-instance form**. The classical card is the general greedy strong edge coloring bound for maximum degree at most `Delta`.
- numeric instance: **Yes**. The FYUM problem is exactly the `Delta=11` case: `2*11^2 - 2*11 + 1 = 242 - 22 + 1 = 221`.
- paired_variant: **No**. This is not a duplicate between two FYUM tour variants.
- false_friend: **No**. The local counting proof and the strong edge coloring condition match.

Checked evidence:

- Classical card: `data/problems/classical/greedy-strong-edge-coloring-bound.yaml`.
- FYUM card: `data/problems/fyum/fyum-2012-tur1a-p10.yaml`.
- Direct relation: `data/relations/relations.d/strong-edge-coloring-bound.yaml`, id `rel-greedy-strong-edge-coloring-bound-fyum-2012-tur1a-p10`, currently `prerequisite`, confidence `0.99`.
- The relation text explicitly says the greedy estimate proves FYUM 2012 after substituting `Delta=11`.
- The FYUM solution counts at most `20` adjacent edges plus at most `200` distance-two edges, hence at most `220` forbidden colors and one available color among `221`. This is the same count as the classical formula `2 Delta^2 - 2 Delta`.

Recommendation:

- Keep both cards if source-instance preservation matters.
- Prefer a relation such as `numeric_instance_of`, `contest_instance_of`, `specialization`, or `extracted_theorem` over ordinary `prerequisite`.
- Do not classify as `same_motif`: the connection is stronger than motif-level, but still parameter-specialized rather than an exact duplicate statement.

## Follow-up Notes

- These three candidates are safe to promote from medium overlap to high-confidence theorem-instance handling.
- No `data/` file was edited during this pass.
- If future schema work adds duplicate-control relation types, these are good seed examples: one exact same-statement theorem/source pair and two numeric instances of extracted general theorem cards.
