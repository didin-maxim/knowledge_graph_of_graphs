# High Recheck: USAMO 2022 P6

Date: 2026-04-27

Entry: `usamo-2022-p6-mathbook-two-common-friends-closure#sol-c4-closure-extremal`

## Source Check

- Primary usable solution source found: Evan Chen, `USAMO 2022 Solution Notes`, section 2.3, Problem 6, <https://web.evanchen.cc/exams/USAMO-2022-notes.pdf>.
- AoPS Wiki page found and retained as statement archive: <https://artofproblemsolving.com/wiki/index.php?title=2022_USAMO_Problems%2FProblem_6>.
- I did not locate a public official MAA solution PDF for this exact USAMO problem in the pass; the available MAA search hits were unrelated AMC material.

## Repair

Status: repaired.

Changes made:

- Expanded the construction for even and odd `n`, including the explicit completion after the shared-edge `C_4` blocks.
- Replaced the summarized lower bound with a self-contained Russian transfer of Chen's closure/minimal-saturated proof:
  - label each current edge by a clique containing it;
  - merge the 2-4 clique labels on a `C_4` whose side labels are not all equal;
  - justify that the batched additions are legal;
  - prove that stopping with all `C_4` side labels equal means no further friendship can be added;
  - prove by induction that every current clique `K` satisfies `theta(K) >= 3|K|/2-2`;
  - conclude the integer lower bound `ceil(3n/2)-2`.
- Added an access note to `src-usamo-2022-evan-chen-notes` documenting the transfer.

## Result

The solution is now self-contained enough for the full recheck bucket. For `n=2022`, the answer is `3031`.
