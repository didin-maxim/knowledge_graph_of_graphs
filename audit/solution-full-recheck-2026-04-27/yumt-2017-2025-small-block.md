# YUMT 2017-2025 Small Block Recheck

Date: 2026-04-27.

Scope: `data/problems/yumt/yumt-2017-*.yaml`, `yumt-2018-*.yaml`, `yumt-2020-*.yaml`, `yumt-2021-*.yaml`, `yumt-2022-*.yaml`, `yumt-2023-*.yaml`, `yumt-2024-*.yaml`, `yumt-2025-*.yaml`.

## Repaired / Promoted

- `yumt-2020-start-round2-problem4`: repaired the proof. The previous Euler-cycle alternating-color argument silently assumed an even Euler-cycle length. Replaced it with the standard construction: add fake edges to make degrees even, take an Euler cycle, remove fake edges to obtain trails, then alternate colors on each trail. Promoted to `editorial.review_status=ai_checked`, `public_ready=true`.
- `yumt-2022-start-final-problem6`: local maximal-matching proof is self-contained; promoted to `editorial.review_status=ai_checked`, `public_ready=true`.
- `yumt-2023-granda-round2-problem9`: local Hall + Euler face-counting proof is self-contained; promoted to `editorial.review_status=ai_checked`, `public_ready=true`.
- `yumt-2025-unior-round1-problem1`: local low-degree induction proof is self-contained; promoted to `editorial.review_status=ai_checked`, `public_ready=true`.

## Mechanical Cleanup

The remaining exact placeholder solutions with text `Решение пока не найдено.` were changed from `solution.status=ai_checked` to `solution.status=needs_human_review`. They remain non-public and need real source material or a human-authored proof.

## Hard / Backlog

For each item below:

- reason: only an exact placeholder solution is present in the local YAML; no local proof text or source excerpt was available in the repository during this pass.
- needed: official YUMT solution, archived working card with proof, or an independently written and checked self-contained Russian solution.
- next_agent: do not promote to public-ready from the placeholder alone; replace the placeholder with a full proof, then rerun `validate.py`, `check_links.py`, and `audit_rules.py`.

Items:

- `yumt-2017-premier-round1-problem2`
- `yumt-2017-start-first-round1-problem3`
- `yumt-2017-start-high-round1-problem3`
- `yumt-2018-grand-final-problem1`
- `yumt-2018-grand-round1-problem3`
- `yumt-2020-100-v-shapes-disjoint`
- `yumt-2020-start-round1-problem4`
- `yumt-2021-grand-final-problem7`
- `yumt-2021-grand-round1-problem2`
- `yumt-2021-grand-round4-problem3`
- `yumt-2022-grand-final-problem1`
- `yumt-2023-granda-final-problem6`
- `yumt-2023-granda-round4-problem3`
- `yumt-2024-grand-final-problem9`
- `yumt-2024-grand-round3-problem8`
- `yumt-2024-start-final-problem7`
- `yumt-2024-unior-final-problem2`
- `yumt-2025-grand-final-problem3`
- `yumt-2025-grand-final-problem5`
- `yumt-2025-grand-round1-problem4`
- `yumt-2025-grand-round1-problem9`
- `yumt-2025-grand-round2-problem1`
- `yumt-2025-grand-round4-problem3`
- `yumt-2025-unior-round1-problem8`
- `yumt-2025-unior-round3-problem1`

## Validation

- `python tools\validate.py`: failed before completing on an out-of-scope JSON parse error in `data/problems/usamo/usamo-2023-p3-domino-slides-special-square-digraph.yaml` (`Invalid \escape`, line 117 column 3061). Per instruction, USAMO 2023 P3 was not touched.
- `python tools\check_links.py`: failed for the same out-of-scope JSON parse error before link checking could proceed.
- `python tools\audit_rules.py --max-items 10`: ran and reported 1 error, 251 warnings. The single error is the same out-of-scope USAMO 2023 P3 JSON parse error. Warnings include existing low-confidence relations, placeholder solutions, public-ready uncertainty, and solution red flags.
