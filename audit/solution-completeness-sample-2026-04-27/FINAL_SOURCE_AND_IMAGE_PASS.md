# Final Source And Image Pass

Date: 2026-04-27

## Closed From Primary Sources

- Chen--Yu / Kolmogorov independent cutset:
  - Source: local original PDF `C:\Users\Admin\Downloads\fragile_graphs.pdf`.
  - Result: merged theorem/Kolmogorov card now has a self-contained Russian proof and is `ai_checked`.

- YUMT 2015 Grand Final Problem 5:
  - Source: Stiebitz PDF, `https://kostochk.web.illinois.edu/math583/stiebitz.pdf`.
  - Result: added local theorem-card `stiebitz-double-critical-k5` and solved YUMT via prerequisite relation.

- FYUM 2011 Final B P4:
  - Result: solved locally for the exact `200`-vertex `100/99` two-block case, avoiding a black-box theorem dependency.

## Visual Rule Added

The repository rules now say that when a proof is naturally visual, the visual object should be part of the solution rather than being replaced by an unreadable coordinate surrogate. The image/table/schematic must be local and checked: the solution must explain what the visual encodes, which cases it covers, and why the proof step follows from it.

Updated files:

- `CONTRIBUTING.md`
- `docs/IMPORT_WORKFLOW.md`

## USAMO 2023 P3

Status: still deferred, but improved.

Added checked image assets:

- `data/assets/examples/usamo-2023-p3/n7-small-k-blue-snake.png`
- `data/assets/examples/usamo-2023-p3/blue-snake-cut-schematic.png`
- `data/assets/examples/usamo-2023-p3/n7-red-spanning-snake.png`

Mirrors:

- `docs/assets/examples/usamo-2023-p3/`
- `viewer/assets/examples/usamo-2023-p3/`

The images now recover the `n=7`, `k=9..1` constructions and the general blue-snake cut idea. The card remains deferred because the sources still do not provide a verified general proof that the remaining red dominoes can always be retiled for every `m,k`. The next step is to prove the visual retile rule, probably as a blue Hamilton snake plus an alternating-path retile lemma.

## Remaining Genuine Blocker

- `usamo-2023-p3-domino-slides-special-square-digraph`: needs the general visual construction proof, not just examples and diagrams.

## Checks

```text
python tools/validate.py
OK: 333 problems, 386 relations, 9 comments, 353 sources, 27 definitions, 15 standard ideas, 19 import batches.

python tools/check_links.py
OK: 375 internal routes, 353 external source URLs syntactically valid.
```
