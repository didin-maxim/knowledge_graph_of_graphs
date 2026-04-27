# XHard: Kolmogorov 2024 T4 Independent Cutset

Date: 2026-04-27

Scope:

- `kolmogorov-2024-t4-independent-cutset-2n-4`
- `chen-yu-independent-cutset-kolmogorov-merged#sol-chen-yu-reference`

## Verdict

`deferred_needs_full_chen_yu_proof_or_checked_reconstruction`.

The Kolmogorov problem is not currently self-contained. It is exactly the Chen--Yu fragile-graph theorem: every connected graph on `n` vertices with at most `2n-4` edges has an independent vertex cutset. I did not find a complete local or openly portable proof of this theorem, and I did not invent the missing contraction induction.

## Sources Checked

- Local cards, source registry, relation files, generated viewer text, and prior audit reports.
- Official Kolmogorov Cup 2024 archive `https://turmath.ru/kolm/files/archive/kolm27.zip`. The extracted `Тур 4/tur4.zip/tur4.tex` confirms the exact statement and attribution `(G. Chen, X. Yu)` for the high league first-place fight, problem 3, but contains no solution.
- ScienceDirect article page `https://www.sciencedirect.com/science/article/pii/S0012365X01002266`, which confirms Chen--Yu, "A note on fragile graphs", Discrete Mathematics 249 (2002), 41--43, and the `2n-4` theorem statement.
- Le--Pfender, "Extremal Graphs Having No Stable Cutsets", and Chernyshev--Rauch--Rautenbach, "Forest Cuts in Sparse Graphs". These confirm the theorem, mention the stronger 2-connected version, and describe the proof as an induction with contractions, but do not reproduce the proof.

## Change Made

Updated `data/problems/classical/chen-yu-independent-cutset-kolmogorov-merged.yaml` so the solution explicitly says it is a theorem-dependent reduction, records the official-archive/source-search boundary, and keeps the repair deferred until the full Chen--Yu proof or a checked reconstruction is available.

I left the already-merged card structure intact: `data/problems/kolmogorov/kolmogorov-2024-t4-independent-cutset-2n-4.yaml` is deleted in the current worktree and replaced by the merged Chen--Yu/Kolmogorov helper card.

## Blocker

The missing piece is not the statement but the proof. The accessible sources do not provide the full Chen--Yu induction, and the later papers I could access rely on the theorem rather than giving a standalone proof of the `2n-4` bound.
