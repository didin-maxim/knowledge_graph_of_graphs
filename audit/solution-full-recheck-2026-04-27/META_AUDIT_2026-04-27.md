# Meta Audit 2026-04-27

Scope: aggregate state after the multi-agent solution/status passes.

## Current Aggregate Counts

- Problems: 333.
- Problem `editorial.review_status`: `ai_checked` 62, `needs_human_review` 271.
- Problem `editorial.public_ready`: `true` 51, `false` 282.
- Problem `editorial.relations_status`: `deep_done` 318, `base_done` 7, `reviewed_no_links` 8.
- Solutions: 315 total entries across cards; status counts are `ai_checked` 297, `source_verified` 1, `needs_human_review` 15, `needs_review` 1, `ai_draft` 1.
- Solution distribution by card: 273 cards have 1 solution, 18 have 2, 2 have 3, and 40 have no solution entry.
- Statements: `ai_checked` 406, `needs_human_review` 97, `needs_review` 12.
- Ideas: `ai_checked` 233, `needs_human_review` 82, `ai_draft` 20, `source_verified` 3.
- Problem profiles: `ai_checked` 184, `needs_human_review` 149.
- Difficulty blocks: `ai_checked` 199, `needs_human_review` 130, `ai_draft` 4.
- Comments: 9 total, all `resolved`.
- Relations: 386 total; `ai_checked` 113, `needs_human_review` 267, `ai_draft` 6.

No card has `public_ready=true` together with an uncertain `editorial.review_status`.

## Remaining Hard Tails

Structural backlog:

- 40 cards currently have no `solutions[]`: 8 Kolmogorov cards (`kolmogorov-2009-*` and `kolmogorov-2014-*`) and 32 YUMT cards.
- 18 solution entries are not `ai_checked`; these are the most direct solution-status tail:
  - `fyum-2009-tur3a-p7#sol-official-archive` is `source_verified`.
  - `kolmogorov-2004-round3-higher-league-problem-10#sol-official-compressed` is `needs_review`.
  - `yumt-2015-grand-final-problem5#sol-archive-card` is `ai_draft`.
  - 15 others are `needs_human_review`, mostly compressed Kolmogorov/YUMT/UTYUM/IMO entries.

Full-recheck audit tail still worth preserving:

- `kolmogorov-2015-round-2-graph-coloring-problem#sol-official-compressed`
- `kolmogorov-2015-round-4-spies-and-opergroups-problem#sol-official-compressed`
- `kolmogorov-2021-round1-second-league-problem-8#sol-official-compressed`
- `kolmogorov-2004-round3-higher-league-problem-10#sol-official-compressed`
- `kolmogorov-2016-individual-olympiad-juniors-problem-7#sol-official-compressed`
- `fyum-2008-tur4a-p7#sol-official-archive`
- `fyum-2010-tur2a-p1#sol-official-archive`
- `utyum-2018_lichol_8_tree_cities#sol-official`
- `complete-graph-triangle-edge-weights-minimum-parametric#sol-parametric`

`usamo-2023-p3-domino-slides-special-square-digraph#sol-special-square-digraph` is no longer a current hard tail according to the problem card: it is now `ai_checked` and `editorial.public_ready=true`.

## Stale Or Contradictory Audit Notes

- `audit/solution-completeness-sample-2026-04-27/xhard-usamo-2023-p3.md` says `deferred_needs_textual_small-k_construction`.
- `audit/solution-completeness-sample-2026-04-27/FINAL_SOURCE_AND_IMAGE_PASS.md` says USAMO 2023 P3 is "still deferred" and is the remaining genuine blocker.
- `audit/solution-full-recheck-2026-04-27/bucket-5.md` still lists USAMO 2023 P3 as hard/deferred.
- Older fast/repair-pass notes also list USAMO 2023 P3 as source-insufficient. Those notes are historical, but should not be used as current state.

Current source of truth contradicting those notes:

- `data/problems/usamo/usamo-2023-p3-domino-slides-special-square-digraph.yaml` has `solutions[0].status = ai_checked`, `editorial.review_status = ai_checked`, `editorial.public_ready = true`, and an editorial note beginning `Resolved 2026-04-27`.

## Generated Artifacts

`build_index.py` and `build_viewer.py` were not run because they write outside this task's write scope (`index/generated.sqlite`, `viewer/index.html`, `docs/index.html`, and generated assets). Instead, freshness was checked without writing:

- In-memory `build_viewer.build_html(build_viewer.load_viewer_data())` does not match either `viewer/index.html` or `docs/index.html`.
- `docs/index.html` still contains the stale deferred USAMO 2023 P3 text, while the source card is resolved/public-ready.
- `index/generated.sqlite` has the right top-level counts (333 problems, 386 relations, 27 definitions, 15 standard ideas, 19 import batches), but 232 source YAML files are newer than the database mtime.

Conclusion: viewer/docs and sqlite index should be rebuilt after the write scope is widened or in the next normal refresh pass.

## Commands Run

```powershell
python tools\validate.py
python tools\check_links.py
python tools\audit_rules.py --max-items 50
```

Results:

- `validate.py`: passed on rerun: `OK: 333 problems, 386 relations, 9 comments, 353 sources, 27 definitions, 15 standard ideas, 19 import batches.`
- `check_links.py`: passed: `OK: 375 internal routes, 353 external source URLs syntactically valid.`
- `audit_rules.py`: passed: `Audit rules: 0 errors, 0 warnings.`

Note: an earlier `validate.py` run transiently reported `rel-kolm-2008-team-seniors-usamo-1976-rectangle` pointing at missing `sol-official-compressed`; current data now has that relation anchored to `sol-double-counting-expanded` and `sol-column-pair-double-counting`, and validation passes.
