# Hard Repair: YUMT/UTYUM Deferred

Date: 2026-04-27

Scope:

- `yumt-2015-grand-final-problem5#sol-external-mse-chromatic-partition`
- `yumt-2015-grand-round4-problem10`
- `utyum-2025_komol64_8_7_tree_matchings_path`
- `utyum-2023_komol60_7_7_room_departures`

## Repaired

- `yumt-2015-grand-round4-problem10#sol-archive-card`: expanded to a self-contained proof that `D = 5n`. The lower bound counts edges in monochromatic components of a complete 5-partite graph; the sharpness construction uses the finite field `Z_5`.
- `utyum-2023_komol60_7_7_room_departures#sol-official`: expanded the lower bound and added the explicit official construction on people numbered `1..99`, where person `k <= 48` knows exactly people `2k+1..99`.
- `utyum-2025_komol64_8_7_tree_matchings_path#sol-official`: expanded the official induction proving that a tree on `2n` vertices has at most `C(n+1,2)` matchings of size `n-1`, with equality for `n >= 3` only for the path; applying `n = 40` gives `820`.

## Deferred

- `yumt-2015-grand-final-problem5#sol-external-mse-chromatic-partition`: deferred as `needs_human_review`. The simple external MSE color-class argument only separates an independent color class; it does not supply the required second part with chromatic number at least 2. The needed result is a special case of the Stiebitz/Tihany chromatic partition theorem, and I did not reconstruct a compact self-contained proof for the `K_5`-free case in this pass.

## Sources Checked

- Math StackExchange, monochromatic paths in complete multipartite graphs: `src-mse-yumt-2015-grand-r4-p10`.
- UTYUM 2023 official archive `ural60.zip`, file `komol 60 7sol.pdf`.
- UTYUM 2025 official archive `ural64.zip`, file `komol_8_ural_64_sol.pdf`.

## Validation

- `python tools/validate.py`
- `python tools/check_links.py`
