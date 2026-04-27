# PDF Repair: Chen--Yu Fragile Graphs

Date: 2026-04-27

Scope:

- `chen-yu-independent-cutset-kolmogorov-merged#sol-chen-yu-reference`
- local source: `C:\Users\Admin\Downloads\fragile_graphs.pdf`

## Result

Closed as `ai_checked`.

The local PDF is Guantao Chen and Xingxing Yu, "A note on fragile graphs", Discrete Mathematics 249 (2002), 41--43. It contains the full short proof needed by the merged Chen--Yu/Kolmogorov card:

- Theorem 1: for every 2-connected graph `G` on `n` vertices with `e(G) <= 2n-4`, and every vertex `x`, there is an independent cut not containing `x`.
- Corollary 2: every connected graph on `n` vertices with `e(G) <= 2n-4` contains an independent cut.

## Proof Transferred

The card now contains a self-contained Russian proof, not just a citation. The transferred proof includes:

- induction bases `n=3` and `n=4`;
- the case where the marked vertex `x` is in no triangle, using `N(x)` as an independent cut;
- contraction of an edge `xy` in a triangle `xyz`, with the edge count drop `e(H) <= e(G)-2`;
- lifting an independent cut from the contracted graph `H` back to `G`;
- the non-2-connected contracted case, where `x*` is the only possible cut vertex of `H`;
- the decomposition over the cut pair `{x,y}` into two induced 2-connected subgraphs `G1` and `G2`;
- the counting contradiction
  `e(G) = e(G1)+e(G2)-1 >= (2|V(G1)|-3)+(2|V(G2)|-3)-1 = 2n-3`.

I added the standard local verification that the induced side subgraphs over a cut pair `{x,y}` are 2-connected, because the original paper states this step tersely.

## Kolmogorov Reduction

The Kolmogorov statement is exactly the connected Chen--Yu corollary: a connected graph with at most `2n-4` edges has an independent vertex set whose deletion disconnects the graph. No additional transformation is needed, so the reduction is now closed with the theorem-card.

## Files Updated

- `data/problems/classical/chen-yu-independent-cutset-kolmogorov-merged.yaml`
- `data/sources/sources.yaml`
- `audit/solution-completeness-sample-2026-04-27/pdf-repair-chen-yu.md`

## Verification

Attempted:

- `python tools/validate.py` -- blocked before validation by unrelated JSON syntax error in `data/problems/memo/memo-2025-t4-toll-complete-graph.yaml`, line 67: invalid `\g` escape inside a LaTeX fragment.
- `python tools/check_links.py` -- blocked by the same parse error during `load_problems()`.

Local parse check for the edited Chen--Yu card succeeds.
