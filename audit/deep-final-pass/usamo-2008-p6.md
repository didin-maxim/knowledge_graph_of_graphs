# usamo-2008-p6-even-friends-two-rooms

verdict: promoted_to_full_count_solution

changed files:
- data/problems/usamo/usamo-2008-p6-even-friends-two-rooms.yaml
- audit/deep-final-pass/usamo-2008-p6.md

notes:
- The former `sol-existence-by-switching-odd-vertex` was not left as a partial: the odd-degree delete-and-switch step actually gives a bijection between good partitions of the switched smaller graph and good partitions of the original graph.
- The extension is unique because `deg(v)` is odd, so exactly one of the two rooms contains an even number of neighbors of `v`.
- After exhausting odd-degree vertices, the remaining Eulerian graph has a clean count base case: valid sides are exactly the subsets whose cut has even local degree at every vertex, and these subsets are closed under symmetric difference. Hence they form an `F_2`-vector space and are counted by a power of two.
- This avoids meaningless duplication of the existing matrix/group solutions: the count is obtained by the switching recursion plus a small Eulerian base argument, not by restating the full affine-system proof.

tests:
- failed: `python tools/validate.py` due unrelated pre-existing errors in `data/problems/kolmogorov/kolmogorov-2008-individual-olympiad-seniors-problem-7.yaml` (`polyhedra`, `solid_angles`, `projection` are unknown tags). No validation error was reported for the target USAMO file.
- passed: `python tools/check_links.py`
