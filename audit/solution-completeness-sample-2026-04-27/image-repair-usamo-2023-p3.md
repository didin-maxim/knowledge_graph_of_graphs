# Image repair: USAMO 2023 P3 domino slides

Date: 2026-04-27

Scope:

- `data/problems/usamo/usamo-2023-p3-domino-slides-special-square-digraph.yaml`
- `tools/generate_example_images.py`
- `data/assets/examples/usamo-2023-p3/`
- `docs/assets/examples/usamo-2023-p3/`

## Verdict

`deferred`

I added local, checked diagrams, but did not promote the card to a complete solution. The diagrams now make the source construction reconstructible for the finite `n=7` picture family and make the general blue-snake cut unambiguous. They still do not supply a written proof of the red-domino retiling for every `n=2m+1` and every `1 <= k <= m^2`.

## Sources Used

- Evan Chen, `USAMO 2023 Solution Notes`, section 1.3. It gives the special-square digraph proof, the red snake for the large value, and nine `n=7` blue-snake pictures for `k=9,8,...,1`.
- Holden Mui, `Dominoes on a Grid` proposal. It describes the small-value construction as blue cells in a snake, with the snake path blocked by a red domino and an empty square, then the rest filled with red dominoes.
- AoPS Wiki, `2023 USAMO Problems/Problem 3`. Used for the statement.
- Draft `Report on the 52nd Annual USA Mathematical Olympiad`. It confirms the same graph proof, the red spanning snake, and the blue-snake/red-blocker construction.

## Added Schemes

- `n7-small-k-blue-snake.png`: nine complete `7 x 7` configurations, read left-to-right and top-to-bottom as `k=9,8,...,1`. This proves, by direct reconstruction from the image, all small values for `n=7`: every domino is drawn, the empty square is drawn, and the checked component size is the displayed `k`.
- `blue-snake-cut-schematic.png`: a general schematic for `n=2m+1`. It fixes the snake order on even-even cells and the cut after the `k`-th snake vertex. This proves that the intended blue digraph component has size `k` for every `1 <= k <= m^2`, provided the red cells can be tiled after the cut.
- `n7-red-spanning-snake.png`: a complete `7 x 7` configuration for the exceptional value `((7+1)/2)^2=16`. It illustrates the red spanning snake used by the sources for the general exceptional value `((n+1)/2)^2`.

## Verification

The image generator now verifies the generated USAMO diagrams before writing them:

- For `m=1..9`, every blue-snake construction with `1 <= k <= m^2` is completed by a matching on the remaining red/white cells and the empty component has size `k`.
- For `m=1..9`, the red-spanning construction is completed by a matching on the remaining blue/white cells and the empty component has size `(m+1)^2`.
- The rendered `n=7` panels are the exact checked configurations from that generator.

This is a useful sanity check, but it is not a mathematical proof for all `m`. The missing proof is still an explicit all-`m,k` red-domino retiling rule, or an all-`m,k` proof that the matching used by the generator always exists.

## Card Status

Still `needs_human_review`, `public_ready=false`.

The card now says exactly what each diagram proves and why the finite/configurational diagrams do not yet cover the full general case.

## Validation

- passed: `python tools/validate.py`
- passed: `python tools/check_links.py`
- passed: `git diff --check -- data/problems/usamo/usamo-2023-p3-domino-slides-special-square-digraph.yaml data/sources/sources.yaml tools/generate_example_images.py audit/solution-completeness-sample-2026-04-27/image-repair-usamo-2023-p3.md`
