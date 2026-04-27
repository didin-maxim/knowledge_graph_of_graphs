# Matching/Tiling Cross-Link Pass

Date: 2026-04-26

Scope: synchronized cross-link pass over already corrected problem cards, restricted to motifs around matching, Hall, bipartite graph models, domino/tiling, alternating cycles, symmetric difference, and parity matching. Problem YAML files were not edited.

## Method

- Used the modified problem-card set from `git diff --name-only` as the corrected-card scope.
- Searched only metadata already updated in the previous passes: top-level `tags`, `problem_profile` fields, `central_method`, solution `standard_idea_ids`, and statement/solution `definition_ids`.
- Loaded all existing relations from `data/relations/relations.yaml` and every `data/relations/relations.d/*.yaml` file.
- Treated endpoint pairs as unordered duplicates, so a reverse-direction relation was also rejected.
- Added new links only to `data/relations/relations.d/metadata-pass-cross-links-matching-tiling.yaml`.

## Counts

- Corrected problem cards scanned: 129.
- Corrected cards matching the requested motifs: 29.
- Candidate endpoint pairs with shared requested motif metadata: 248.
- Rejected as existing endpoint duplicates: 16.
- New relations added: 8.

## Added Relations

- `rel-matching-tiling-konig-imo-2016-c8-alternating-cycles`: Kőnig alternating paths to IMO 2016 C8 domino alternating cycles.
- `rel-matching-tiling-rmm-2017-imo-2010-hall-incidence`: RMM 2017 and IMO 2010 C2 via Hall-certified bipartite incidence matchings.
- `rel-matching-tiling-kolm-2002-rmm-2017-hall-deficiency`: Kolmogorov 2002 and RMM 2017 via Hall-neighborhood/deficiency control.
- `rel-matching-tiling-usamo-2009-imo-2020-alternating-decomposition`: symmetric-difference tiling cycles to alternating coloring of Eulerian cycles.
- `rel-matching-tiling-kolm-2007-usamo-2009-cycle-decomposition`: grid tiling cycle decomposition to domino overlay cycles.
- `rel-matching-tiling-memo-2022-usamo-2009-domino-pairing`: domino pairing as board-cell parity bookkeeping.
- `rel-matching-tiling-memo-2021-rmm-2017-grid-incidence-bigraph`: grid objects encoded as bipartite incidence graphs.
- `rel-matching-tiling-hall-usamo-2009-perfect-matching`: Hall/perfect-matching language behind domino tilings, with USAMO 2009 using uniqueness by alternating cycles.

## Rejected Duplicates

- `egmo-2016-p3-blue-cells-bipartite-incidence` / `memo-2021-i2-bishop-circuit-forest`: existing `rel-egmo-2016-p3-memo-2021-i2-incidence-forest` in `data/relations/relations.d/official-archives-idea-links.yaml`.
- `egmo-2016-p3-blue-cells-bipartite-incidence` / `rmm-2017-p5-sieve-sticks-bipartite-matching`: existing `rel-rmm-2017-p5-egmo-2016-p3-grid-incidence` in `data/relations/relations.d/official-archives-idea-links.yaml`.
- `hall-marriage-theorem` / `imo-2010-c2-flags-diagonal-matching`: existing `rel-hall-imo-2010-c2` in `data/relations/relations.d/imo-shortlist-graph.yaml`.
- `hall-marriage-theorem` / `kolmogorov-2002-team-olympiad-seniors-problem-8`: existing `rel-kolm-2002-blocks-hall-lemma` in `data/relations/relations.d/kolmogorov-2026-import-links.yaml` and `rel-metadata-pass-hall-kolm-2002-blocks` in `data/relations/relations.d/metadata-pass-cross-links.yaml`.
- `hall-marriage-theorem` / `konig-vertex-cover-theorem`: existing `rel-hall-konig` in `data/relations/relations.yaml`.
- `hall-marriage-theorem` / `rmm-2012-p1-sociable-sets-bipartite-parity`: existing `rel-rmm-2012-p1-hall-cover-parity` in `data/relations/relations.d/official-archives-idea-links.yaml`.
- `hall-marriage-theorem` / `rmm-2017-p5-sieve-sticks-bipartite-matching`: existing `rel-hall-rmm-2017-p5-grid-matching` in `data/relations/relations.d/official-archives-idea-links.yaml`.
- `imo-2010-c2-flags-diagonal-matching` / `imo-2016-c8-domino-unique-tiling-cycles`: existing `rel-imo-2010-c2-imo-2016-c8-matching-alternation` in `data/relations/relations.d/imo-shortlist-2010-2024-idea-links.yaml`.
- `imo-2010-c2-flags-diagonal-matching` / `konig-vertex-cover-theorem`: existing `rel-after-tags-imo-2010-flags-konig-cover` in `data/relations/relations.d/metadata-pass-cross-links-after-tags.yaml`.
- `imo-2016-c8-domino-unique-tiling-cycles` / `imo-2020-c6-colored-coins-eulerian-multigraph`: existing `rel-imo-2016-c8-imo-2020-c6-alternating-cycles` in `data/relations/relations.d/imo-shortlist-2010-2024-idea-links.yaml`.
- `imo-2016-c8-domino-unique-tiling-cycles` / `usamo-2009-p3-tasteful-domino-tiling-alternating-cycles`: existing `rel-imo-2016-c8-usamo-2009-p3` in `data/relations/relations.yaml` and `rel-imo-2016-c8-usamo-2009-domino-alternating-cycles` in `data/relations/relations.d/solution-repair-imo-links.yaml`.
- `kolmogorov-2006-round-1-super-high-first-league-problem-1` / `mantel-theorem`: existing `rel-metadata-kolm-2006-triangle-free-mantel` in `data/relations/relations.d/metadata-pass-kolmogorov-early-links.yaml`.
- `kolmogorov-2006-round-2-first-junior-league-problem-8` / `kolmogorov-2006-round-2-super-league-problem-6`: existing `rel-kolm-2006-grid-tree-round2` in `data/relations/relations.d/kolmogorov-final-confirmed-links.yaml`.
- `kolmogorov-2008-individual-olympiad-juniors-problem-8` / `kolmogorov-2008-individual-olympiad-seniors-problem-5`: existing `rel-kolm-2008-bipartite-coloring-pair` in `data/relations/relations.d/kolmogorov-final-confirmed-links.yaml`.
- `kolmogorov-2008-round-4-first-league-and-higher-junior-problem-1` / `kolmogorov-2008-round-4-second-league-problem-7`: existing `rel-kolm-2008-tree-bipartition-round4` in `data/relations/relations.d/kolmogorov-final-confirmed-links.yaml`.
- `konig-vertex-cover-theorem` / `usamo-2009-p3-tasteful-domino-tiling-alternating-cycles`: existing `rel-after-tags-konig-usamo-2009-tiling` in `data/relations/relations.d/metadata-pass-cross-links-after-tags.yaml`.

## Notes

- Lower-confidence motif links are deliberately marked `needs_human_review`.
- No problem YAML was edited in this pass.
