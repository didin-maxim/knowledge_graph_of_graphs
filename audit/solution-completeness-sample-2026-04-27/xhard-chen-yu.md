# XHard: Chen--Yu Fragile Graphs Theorem

Date: 2026-04-27

Scope:

- `chen-yu-independent-cutset-kolmogorov-merged#sol-chen-yu-reference`
- removed/superseded local cards:
  - `chen-yu-fragile-graphs-theorem`
  - `kolmogorov-2024-t4-independent-cutset-2n-4`

## Verdict

`deferred_needs_original_proof_or_checked_reconstruction`

The exact Kolmogorov task is source-confirmed as the Chen--Yu theorem: every connected graph of order `n` and size at most `2n-4` is fragile, i.e. has an independent vertex cut. I did not close the card as a self-contained solution, because I did not find a full portable proof of the Chen--Yu induction and did not reconstruct all contraction-lifting cases to a standard that is safe for the database.

## Sources Checked

- Local merged card and deleted pre-merge cards via `git show`.
- Local prior audit: `audit/external-source-pass/chen-yu-fragile-graphs-theorem.md`.
- ScienceDirect metadata for Guantao Chen and Xingxing Yu, "A note on fragile graphs", Discrete Mathematics 249 (2002), 41--43, DOI `10.1016/S0012-365X(01)00226-6`: confirms the statement and sharpness, but the full proof/PDF was not accessible from this environment.
- Le--Pfender, "Extremal Graphs Having No Stable Cutsets", EJC 20(1) (2013), #P35: confirms Chen--Yu Theorem 1 and the stronger 2-connected Theorem 2.
- Chernyshev--Rauch--Rautenbach, "Forest Cuts in Sparse Graphs", arXiv:2409.17724 / Discrete Mathematics 348 (2025): states the same stronger Chen--Yu Theorem 1 and says the proof is an inductive contraction argument.
- Cheng--Tang--Zhan, "Sparse graphs with an independent or foresty minimum vertex cut", Discrete Mathematics 349 (2026), 114658: independently confirms the connected fragile theorem and the sharp `2n-4` threshold.
- Rauch--Rautenbach, "Revisiting Extremal Graphs Having No Stable Cutsets", EJC 32(4) (2025), #P4.25: confirms the theorem and the Le--Pfender extremal context, but does not reproduce the Chen--Yu proof.

## What Is Confirmed

The theorem statement is reliable:

- A connected graph is fragile if it contains an independent vertex cut.
- Chen--Yu proved that every connected graph with `n` vertices and at most `2n-4` edges is fragile.
- Le--Pfender record the stronger version: if `G` is 2-connected, `|E(G)| <= 2|V(G)| - 4`, and `x` is any vertex, then there is a stable/independent cutset not containing `x`.
- The connected theorem follows immediately from that stronger version: if the graph has a cut vertex, a singleton cut works; otherwise the graph is 2-connected.

## Missing Proof

The unavailable proof is not the final reduction from Kolmogorov to Chen--Yu; that reduction is immediate. The missing proof is the internal Chen--Yu induction:

- choosing a low-degree vertex from `|E(G)| <= 2|V(G)| - 4`;
- contracting or suppressing local configurations while preserving the sparse bound;
- applying the stronger theorem to the smaller graph with a forbidden marked vertex;
- lifting an independent cutset through the contraction back to the original graph in all cases.

I checked several plausible reconstructions. The degree-2 contraction lift can be made to work, but the degree-3 and marked-vertex cases require case distinctions that are exactly the missing Chen--Yu argument. I did not promote a partial reconstruction to a solution.

## Changes Made

- Updated `data/problems/classical/chen-yu-independent-cutset-kolmogorov-merged.yaml` so the solution is explicitly `Deferred`, theorem-dependent, and names the missing contraction-induction proof.
- Added `repair_status: deferred_missing_chen_yu_contraction_induction` and a `review_notes` field to the solution.
- Added this xhard audit report.

## Tests

- passed: `python tools/validate.py`
- passed: `python tools/check_links.py`
- passed: `git diff --check -- data/problems/classical/chen-yu-independent-cutset-kolmogorov-merged.yaml audit/solution-completeness-sample-2026-04-27/xhard-chen-yu.md`

## Remaining Blockers

- Need the full Chen--Yu paper text/PDF, or a separately checked reconstruction of the 2-connected marked-vertex induction.
- Until then, the Kolmogorov reduction remains citation-based and should stay `needs_human_review`.
