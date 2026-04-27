# Kolmogorov 2004 Round 3 Higher League Problem 10

## Verdict

`repaired_from_official_archive_with_expansion`.

The official 2004 Kolmogorov Cup archive listed in `data/sources/sources.yaml` was downloaded outside the repository from:

- `https://turmath.ru/kolm/files/archive/kolm8.zip`

The needed statement and solution are in `tur3.doc`, Round 3, Higher League, Problem 10. The official proof is short but contains the key maximal strongly connected component argument that was missing in the prior pass. I expanded the compressed step by contracting the maximal component `K` and using a directed cycle through the contracted vertex and `a`.

## Reconstruction

The complete proof now appears as `sol-official-expanded`.

The key missing lemma is:

If `K` is a largest strongly connected component among all one-vertex deletions, then after contracting `K` to `k`, any directed cycle through `k` and `a` must contain every vertex outside `K`; otherwise deleting an omitted vertex would leave a strongly connected component containing `K` and `a`, larger than `K`.

Once all outside vertices lie on this cycle, take the first two outside vertices `c,d` after `K`. The second outgoing edge from `c` cannot also go to `d`; it either enters `K` or jumps to a later outside vertex on the cycle. In both cases, after deleting `d`, the graph has a strongly connected component containing `K` and `c`, again contradicting maximality.

## Changed Files

- `data/problems/kolmogorov/kolmogorov-2004-round3-higher-league-problem-10.yaml`
- `audit/deep-final-pass/kolmogorov-2004-round3-higher-p10.md`

## Status Updates

- Statement status set to `source_verified`.
- Idea status set to `ai_checked`.
- Added `sol-official-expanded` with status `ai_checked`.
- Marked the old compressed solution as `superseded_by_expanded_official_solution`.
- Editorial review status set to `ai_checked`, while `public_ready` remains `false` because the author is still unknown and the broader card metadata was not part of this repair.

## Validation

- Passed: `python tools/validate.py`
- Passed: `python tools/check_links.py`
- Passed: `git diff --check -- data/problems/kolmogorov/kolmogorov-2004-round3-higher-league-problem-10.yaml audit/deep-final-pass/kolmogorov-2004-round3-higher-p10.md`
