# Hard Repair: Chen--Yu Fragile Graph Dependency

Date: 2026-04-27

Scope:

- `chen-yu-fragile-graphs-theorem#sol-paper-theorem`
- `kolmogorov-2024-t4-independent-cutset-2n-4#sol-chen-yu`

## Source Search

Checked local cards, source registry, prior audit notes, generated viewer snapshots, and related relation files. The local repository did not contain a full proof of Guantao Chen and Xingxing Yu, "A note on fragile graphs", Discrete Mathematics 249 (2002), 41--43.

Checked public web sources:

- ScienceDirect article page: `https://www.sciencedirect.com/science/article/pii/S0012365X01002266`
- Le--Pfender, "Extremal Graphs Having No Stable Cutsets", Electronic Journal of Combinatorics 20(1) (2013), `https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i1p35/pdf/`
- Rauch--Rautenbach, "Revisiting Extremal Graphs Having No Stable Cutsets", Electronic Journal of Combinatorics 32(4) (2025), `https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i4p25/pdf/`
- Chernyshev--Rauch--Rautenbach, "Forest Cuts in Sparse Graphs", arXiv:2409.17724, `https://arxiv.org/abs/2409.17724`
- Cheng--Tang--Zhan, "Sparse graphs with an independent or foresty minimum vertex cut", Discrete Mathematics 349 (2026), `https://math.ecnu.edu.cn/~zhan/papers/Cheng_Tang_Zhan2026.pdf`

## Findings

The theorem statement is source-confirmed in multiple independent places: every graph of order \(n\) with fewer than \(2n-3\) edges, equivalently at most \(2n-4\) edges, has an independent/stable vertex cut.

Le--Pfender report that Chen--Yu proved a stronger 2-connected version: if \(G\) is 2-connected, has fewer than \(2n-3\) edges, and \(u\in V(G)\), then \(G\) has an independent cut avoiding \(u\). Chernyshev--Rauch--Rautenbach also identify this as Chen--Yu Theorem 1 and state that the proof is an elegant induction relying on contractions.

I did not find a complete openly portable proof text. Direct attempts to fetch ScienceDirect PDF endpoints for `S0012365X01002266` returned HTTP 403. The accessible secondary sources cite the result and sometimes the stronger theorem, but do not reproduce the proof. Because the missing part is the contraction induction and its case checks, I did not invent a self-contained Russian proof.

## Changes Made

- Kept `chen-yu-fragile-graphs-theorem#sol-paper-theorem` deferred, but made the deferred note more precise: it now records the `<2n-3` form, the stronger 2-connected version, and the known proof shape.
- Marked `kolmogorov-2024-t4-independent-cutset-2n-4#sol-chen-yu` as theorem-dependent and `needs_human_review`, with explicit dependency on the deferred Chen--Yu proof.
- Fixed a damaged phrase in the Kolmogorov graph relation text.

## Remaining Deferred

- `chen-yu-fragile-graphs-theorem#sol-paper-theorem`: needs the full Chen--Yu proof or a fully checked independent reconstruction of the induction with contractions.
- `kolmogorov-2024-t4-independent-cutset-2n-4#sol-chen-yu`: remains acceptable only as a citation-based theorem reduction until the Chen--Yu proof is imported or reconstructed.
