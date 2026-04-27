# XHard: USAMO 2023 P3 Domino Slides

Date: 2026-04-27

Scope:

- `data/problems/usamo/usamo-2023-p3-domino-slides-special-square-digraph.yaml`
- solution id `sol-special-square-digraph`

## Verdict

`deferred_needs_textual_small-k_construction`

I did not promote the card to a complete Russian solution. The graph proof and the answer set are source-confirmed, but the construction for every small value still depends on diagrams and local perturbations that are not yet encoded as a checked coordinate algorithm.

## Sources Checked

- Evan Chen, `USAMO 2023 Solution Notes`, section 1.3, updated 2026-03-13: https://web.evanchen.cc/exams/USAMO-2023-notes.pdf
- Holden Mui, `Dominoes on a Grid` proposal: https://www.mit.edu/~hsmui/files/proposals/2023usamo3.pdf
- AoPS Wiki, `2023 USAMO Problems/Problem 3`: https://artofproblemsolving.com/wiki/index.php/2023_USAMO_Problems/Problem_3
- Draft `Report on the 52nd Annual USA Mathematical Olympiad`: https://campus.lakeforest.edu/trevino/USAMO2023.pdf

## What Is Confirmed

The answer is

`\{1,2,\ldots,((n-1)/2)^2\}\cup\{((n+1)/2)^2\}`.

The upper-bound proof is portable:

- The empty cell remains in the same coordinate-parity class after every slide.
- For that special class, draw a directed edge from each covered special square to the special square pointed to by its domino, when the target exists.
- Every cycle in the underlying graph encloses an odd number of cells, hence must enclose the empty square.
- Therefore the component `T` containing the empty square is a tree.
- In `T`, all arrows point to the empty square, and moving dominoes just changes the sink of this tree, so `k(C)=|V(T)|`.
- If the red odd-odd class gives more than `((n-1)/2)^2`, the component must contain a boundary red square after sliding; then no red vertex can be trapped in a separate cycle, so all `((n+1)/2)^2` red vertices are in the component.

## Construction Gap

All sources use the same construction idea for the values `1..((n-1)/2)^2`: put the even-even blue cells in a snake, cut the snake after the desired number of vertices, block the next snake edge using a red domino and an empty square, then fill the rest with red dominoes.

What is still missing for a self-contained database solution:

- A coordinate order for the blue snake on the `m x m` grid of even-even cells, where `n=2m+1`.
- For each `k`, exact coordinates of the empty blue cell, the `k-1` blue dominoes pointing through the reachable component, the first outside blue domino, the endpoint blue domino that points outside the board, and the red blocker on the cut edge.
- A coordinate rule for all remaining red dominoes after the blocker moves.
- Or, equivalently, a proved alternating-path retile algorithm: start from the full blue-snake tiling, replace the far endpoint white square by the freed cut-edge white square, and toggle red dominoes along an explicitly described alternating path. I found this as a plausible formalization, but did not prove the required path/retiling rule for all `m,k`, so I did not promote it.

The exact diagrams/modifications to transfer are:

- Evan Chen notes, page with the nine `n=7` pictures for `k=9,8,...,1`.
- Evan Chen notes, previous page: the full red-snake picture for `k=((n+1)/2)^2`.
- Holden Mui proposal / USAMO draft figures: the `n=7`, `k=5` blocked-blue-snake construction, plus the textual sentence "blocking the snake's path with a red domino and an empty square".

## Changes Made

- Updated `sol-special-square-digraph` to keep `Deferred`, but with a sharper blocker statement naming the exact missing coordinate data.
- Updated the editorial note to record the additional sources and the specific missing construction pieces.
- Added this audit report.

## Validation

- passed: `python tools/validate.py`
- passed: `python tools/check_links.py`
- passed: `git diff --check -- data/problems/usamo/usamo-2023-p3-domino-slides-special-square-digraph.yaml audit/solution-completeness-sample-2026-04-27/xhard-usamo-2023-p3.md`

## Remaining Blockers

- Need a checked textual construction for all small values, not just the answer and upper bound.
- The most promising route is to formalize the picture sequence as a blue Hamilton snake plus an explicit red-domino alternating-path retile rule.
