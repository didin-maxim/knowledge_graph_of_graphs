# High verification: `fyum-2009-tur1a-p7` <-> `usa-tst-2009-p6-tournament-gap-ordering`

## Verdict

This is duplicate-level: the two cards are the same mathematical problem in equivalent formulations.

More precise classification: **equivalent reformulation of the same tournament theorem/problem**, not an exact text reprint. I would merge them, but replace the current direct relation with `reformulation`, not `reprint`, unless a later source audit proves that one contest statement was copied verbatim from the other.

Confidence: high.

## Cards Checked

- `data/problems/fyum/fyum-2009-tur1a-p7.yaml`
- `data/problems/usa-tst/usa-tst-2009-p6-tournament-gap-ordering.yaml`
- Direct relation: `data/relations/relations.d/fyum-idea-links.yaml`, id `rel-fyum-2009-tur1a-p7-usa-tst-2009-gap-ordering`
- Medium report: `docs/archive/direct-relation-duplicate-sweep/medium-usa-putnam.md`

## Source Check

Local source ids checked:

- `src-fyum-2009-tur1a-p7-official`: `https://www.guas.info/competit/fest/fest20/tur1a.tex`, marked official/source_verified in `data/sources/sources.yaml`.
- `src-usa-tst-2009-aops-community`: `https://artofproblemsolving.com/downloads/printable_post_collections/4639`, marked secondary/source_verified.
- USA TST supporting solution sources: `src-mse-tournament-scc-ordering-lavrov`, `src-mse-strong-tournament-cycles-bof`.

Internet check:

- The AoPS printable archive for USA TST 2009 opens and lists Problem 6, proposer Gabriel Carroll. It states the path condition on `M+1` distinct players and the conclusion that players can be numbered so that whenever `a >= b + M - 1`, player `a` beat player `b`: https://artofproblemsolving.com/downloads/printable_post_collections/4639
- The current `guas.info` FYUM URL from the source record returned a 404/hosting placeholder during live check, so I did not treat live access to that URL as confirmation. However, the local card already records it as `source_verified`, and an external Moscow olympiad training PDF reproduces the same FYUM-style graph statement with the no-`m+1`-cycle hypothesis: https://math.mosolymp.ru/upload/files/2023/other/1568/9/9-1/Or_grafyi2_9-1.pdf

## Mathematical Equivalence

FYUM statement, normalized:

- Let `n > m > 1`.
- In a complete oriented graph/tournament on `n` vertices, there is no directed cycle on `m+1` vertices.
- Prove that the vertices can be numbered `1,...,n` so that for all `i,k` with `i >= k + m - 1`, the edge is directed from vertex `i` to vertex `k`.

USA TST statement, normalized:

- Let `N > M > 1`.
- In a round-robin tournament, for every sequence of `M+1` distinct players `P_0,...,P_M` with `P_{i-1}` beating `P_i`, player `P_0` also beat `P_M`.
- Prove that players can be numbered `1,...,N` so that whenever `a >= b + M - 1`, player `a` beat player `b`.

The hypotheses are equivalent in a tournament after `n=N`, `m=M`:

- If there is no directed cycle of length `M+1`, then any directed path `P_0 -> P_1 -> ... -> P_M` on distinct vertices cannot have the closing edge `P_M -> P_0`; since this is a tournament, the only remaining edge direction is `P_0 -> P_M`, which is exactly the USA TST condition.
- Conversely, if the USA TST path condition holds, a directed cycle `x_0 -> x_1 -> ... -> x_M -> x_0` would contradict it: applying the condition to the path `x_0 -> ... -> x_M` forces `x_0 -> x_M`, while the cycle gives `x_M -> x_0`.

The conclusions are identical after renaming variables and interpreting "beat" as the directed edge orientation.

## Merge Recommendation

Canonical card id: `usa-tst-2009-p6-tournament-gap-ordering`.

Reason: this card currently has stronger metadata and structure: verified proposer `Gabriel Carroll`, richer graph-theory statement, ideas, multiple solutions, and supporting solution sources. The FYUM card should not be discarded as evidence; its official/archive source and compact no-cycle formulation should be preserved on the canonical card.

Statements to preserve/merge:

- Keep the USA TST chess-tournament statement as the main original contest statement.
- Keep the existing USA graph-theory statement, but consider tightening it to explicitly say it is equivalent to forbidding directed cycles of length `M+1`.
- Add the FYUM statement as an alternate original/source statement or olympiad reformulation, because it states the equivalent no-cycle hypothesis directly.

Sources to preserve/merge:

- Keep `src-usa-tst-2009-aops-community` on the canonical card as the USA TST archive source.
- Add `src-fyum-2009-tur1a-p7-official` to the canonical card as an additional contest/archive source, with a note that the live URL returned 404 on this audit and may require archive recovery.
- Keep the two MSE solution/reference sources already attached to the USA TST card.

Solutions to preserve/merge:

- Keep `sol-components-hamiltonian-cycle` as the main complete solution.
- Keep `sol-mse-tournament-components` as the published/community alternative solution.
- Merge or attach FYUM `sol-official-archive` as an official/archive-derived short solution if source provenance is important; otherwise mark it as a short duplicate of the SCC/Hamiltonian-cycle solution and avoid presenting it as a separate mathematical method.

Relation change:

- Replace current `same_motif`, distance `1`, relation `rel-fyum-2009-tur1a-p7-usa-tst-2009-gap-ordering` with `reformulation`.
- Suggested distance: `0` if relation distance is used to mark duplicate-level identity; otherwise keep `1` but make type/status/confidence carry the duplicate-level meaning.
- Suggested confidence: `0.97` or higher.
- Do not use `reprint` unless a primary-source/provenance audit confirms literal copying or exact contest reprint direction.

## Risks / Follow-up

- The FYUM source URL in `data/sources/sources.yaml` did not open live during this audit. Because the source is already marked `source_verified`, this is probably link rot, but a future merge should either locate an archived copy or update the source access note.
- Some external PDF extraction/OCR renders the FYUM boundary condition inconsistently (`>` vs `>=`). The local card and USA TST source use the boundary `>=`; this boundary is mathematically important, so the original FYUM TeX/PDF should be checked before editing the statement text.
- The two contest provenances should remain visible after merge. Merging into the USA TST card should not erase the FYUM official/archive occurrence.
- The FYUM card text is mojibake in terminal output, so any future merge edit should use a UTF-8-safe editor/tooling path and avoid accidental re-encoding.
- Existing dirty/untracked split-process changes are present in the worktree. This audit did not edit `data/` or relation files; only this report was added.
