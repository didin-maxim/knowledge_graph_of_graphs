# Cross-Link Pass After Tags

Date: 2026-04-26

Scope: post-metadata cross-link synchronization after the final card metadata update. Problem YAML files were not edited.

## Method

- Loaded the 129 modified problem cards reported by `git diff --name-only`.
- Extracted only metadata fields that were part of the final tagging pass: top-level `tags`, `problem_profile.objects`, `problem_profile.methods`, `problem_profile.transformations`, `problem_profile.goal`, `problem_profile.auxiliary_graph_type`, `problem_profile.invariants`, `problem_profile.keywords`, `problem_profile.central_method`, `properties.central_method.value`, solution `standard_idea_ids`, solution `definition_ids`, statement `definition_ids`, and local idea `tags`.
- Built thematic buckets requested in the task: Hall/matching, tree/eulerian/handshaking, Zykov/Brooks/recoloring, longest path/Hamiltonian, grid/tiling/alternating cycles, solid angle/projection, counting/injection, and strong connectivity.
- Loaded all existing relation endpoints from `data/relations/relations.yaml` and every file in `data/relations/relations.d`, including all `metadata-pass-*.yaml`, then treated an unordered endpoint pair as a duplicate.
- Ranked remaining pairs by shared metadata fields and theme-token overlap, then manually inspected the strongest and targeted candidates before adding only non-duplicate links.

## Counts

- Modified problem cards scanned: 129.
- Total modified-card pairs scanned: 8,256.
- Pairs matching at least one requested theme bucket: 3,277.
- Thematic pairs rejected as existing endpoint duplicates: 71.
- Non-duplicate thematic candidates ranked for review: 3,206.
- New relations added: 12.

## Added Relations

- `rel-after-tags-imo-2010-flags-konig-cover`: Kőnig alternating-path theorem to IMO 2010 C2 diagonal matching.
- `rel-after-tags-konig-usamo-2009-tiling`: Kőnig alternating paths to USAMO 2009 domino alternating cycles.
- `rel-after-tags-kolm-2011-2012-eulerian-construction`: KOLM 2011 team seniors to KOLM 2012 snowplow Eulerian construction.
- `rel-after-tags-imo-2020-2023-eulerian-parity`: IMO 2020 C6 to IMO 2023 C4 by Eulerian parity/degree modeling.
- `rel-after-tags-kolm-2010-2011-hamiltonian-cycles`: KOLM 2010 juniors to KOLM 2011 seniors by Hamiltonian-cycle extension/obstruction.
- `rel-after-tags-ore-kolm-2022-hamiltonian-parity`: Ore theorem to KOLM 2022 Hamiltonian-path parity as a nearby Hamiltonian forcing motif.
- `rel-after-tags-kolm-2007-2008-local-recoloring`: KOLM 2007 to KOLM 2008 local recoloring plus double counting.
- `rel-after-tags-kolm-2008-recoloring-counting-pair`: KOLM 2008 first-junior to second-league near-pair by identical recoloring/counting metadata.
- `rel-after-tags-turan-kolm-2022-complement-extremal`: Turan/Zykov symmetrization to KOLM 2022 complement extremal edge-counting.
- `rel-after-tags-kolm-2008-solid-angle-imo-2004-tetrahedra`: KOLM 2008 solid-angle/projection card to IMO 2004 tetrahedra incidence counting.
- `rel-after-tags-imo-2005-injection-imo-2013-layers`: IMO 2005 injection to IMO 2013 distance-layer counting.
- `rel-after-tags-menger-imo-2021-kolm-2004-strong-digraph`: IMO 2021 Menger/tournament cuts to KOLM 2004 strong digraph connectivity.

## Duplicate Rejections

Representative duplicate endpoint pairs found and not re-added:

- `hall-marriage-theorem` / `kolmogorov-2002-team-olympiad-seniors-problem-8` already in `metadata-pass-cross-links.yaml`.
- `brooks-theorem` / `kolmogorov-2006-round-3-super-league-problem-3` already in `metadata-pass-cross-links.yaml`.
- `tournament-hamiltonian-path` / `kolmogorov-2010-individual-olympiad-seniors-problem-4` already in `metadata-pass-cross-links.yaml`.
- `turan-theorem` / `mantel-theorem` already in `metadata-pass-classical-usamo-links.yaml`.
- `brooks-theorem` / `imo-2013-c3-imons-graph-coloring` already in an existing relation file.
- `brooks-theorem` / `vosh-2025-26-final-regions-friendship-coloring` already in an existing relation file.
- `kolmogorov-2003-team-olympiad-seniors-problem-8` / `kolmogorov-2004-round3-higher-league-problem-10` already in `base-done-second-pass.yaml`.

## Notes

- Several lower-confidence but useful thematic links were marked `needs_human_review` rather than `ai_checked`, especially where the metadata overlap is conceptual rather than a direct proof transfer.
- No problem YAML files were changed in this pass.
