# External source pass: USAMO 2021 P2

Problem file: `data/problems/usamo/usamo-2021-p2-planar-national-park-turning-walk.yaml`

Verdict: external source insufficient; no YAML construction repair made.

Checked sources:

- `src-usamo-2021-p2-aops-wiki`: accessible. The AoPS Wiki page contains the problem statement and diagram only; it does not include a solution or the pentagonal-prism walk.
- `src-usamo-2021-eric-shen-pdf`: accessible. The PDF contains the Problem 2 statement and the solution text says the answer is 3, gives only a terse upper-bound remark, and names "a pentagonal prism" as a construction. It does not spell out the starting edge, cyclic embedding choices, or the actual alternating left/right walk.

Reason: the backlog item asks for the missing explicit walk. The cited external source verifies that the intended extremal graph is the pentagonal prism, but it does not provide a full construction to transfer into the YAML without reconstruction. Per external-source-pass rules, I did not invent the missing walk.
