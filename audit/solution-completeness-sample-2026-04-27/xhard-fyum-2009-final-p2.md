# XHard FYUM 2009 Final P2

Verdict: `repaired_full_solution`.

## Scope

- Card: `data/problems/fyum/fyum-2009-final-p2.yaml`
- Task: replace/defer the theorem-level upper bound for the answer `n=500`.
- Placeholder tasks were not edited.

## Source Check

- Primary theorem source found and checked: S. A. Burr, P. Erdos, J. H. Spencer, "Ramsey Theorems for Multiple Copies of Graphs", Transactions of the AMS 209 (1975), PDF: `https://www.renyi.hu/~p_erdos/1975-35.pdf`.
- The article states in the abstract that `r(mK3,nK3)=3m+2n` for `m>=n`, `m>=2`.
- The proof of Theorem 2 gives the diagonal case `r(qK3)=5q`, with the bowtie induction; Theorem 7 records the off-diagonal formula. For this FYUM task only the diagonal `q=100` case is needed.

## Repair

- Replaced the one-line import of Burr--Erdos--Spencer in the solution with a self-contained Russian proof of the needed upper bound:
  - proves `R(3,3)=6`;
  - proves the base case `r(2K3)=10` by the two-vertex-deletion property and maximal red clique argument;
  - proves the induction step by producing a red-blue bowtie from disjoint red/blue triangles and deleting its five vertices;
  - applies the result at `q=100`.
- Kept the already written lower-bound construction on `499` vertices, since it is exactly the BES extremal coloring and directly rules out 100 disjoint odd cycles in either color.
- Marked the card `review_status: ai_checked` and `public_ready: true`.

## Blockers

None. The former deferred dependency is removed for this card: the upper bound is now written in-card rather than imported as a black-box theorem.

## Validation

- `python tools\validate.py`: OK, 324 problems, 375 relations, 9 comments, 352 sources, 27 definitions, 15 standard ideas, 19 import batches.
- `python tools\check_links.py`: OK, 366 internal routes, 352 external source URLs syntactically valid.
