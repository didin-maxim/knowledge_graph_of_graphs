# Metadata pass: IMO

Date: 2026-04-26

Scope: IMO cards repaired in `audit/plan-to-solution-pass` and `audit/external-source-pass`, plus already-full IMO cards whose solution metadata still used old `compressed`/`sketch` wording.

## Updated problem cards

- `data/problems/imo/imo-1994-c2-city-ages-harmonic-graph.yaml`: raised metadata statuses to `ai_checked`, clarified full solution title, and recorded review note.
- `data/problems/imo/imo-1996-c1-grid-knight-reachability.yaml`: added `component_analysis` to the profile, refined standard ideas for the two solutions, raised review statuses, and recorded review note.
- `data/problems/imo/imo-1996-c2-grid-vertices-two-red.yaml`: added `cycle` definition anchor, raised statuses, and recorded review note.
- `data/problems/imo/imo-2005-c2-dynastic-vertices-forest.yaml`: added `tree` definition anchor, raised statuses, and recorded review note.
- `data/problems/imo/imo-2013-c3-imons-graph-coloring.yaml`: refined object/profile metadata to `simple_graph`, added induction tag, replaced the old compressed solution title, raised statuses, and recorded review note.
- `data/problems/imo/imo-2013-c6-flight-distance-layers.yaml`: raised profile status after external-source repair and appended metadata note to the restored-source note.

## Already-full IMO cards cleaned

- `data/problems/imo/imo-2004-c8-triangles-tetrahedra-graph.yaml`: marked profile/public readiness as checked and clarified that the sketch id is retained only for relation stability.
- `data/problems/imo/imo-2010-c2-flags-diagonal-matching.yaml`: added standard idea anchor and metadata note while preserving `sol-official-compressed`.
- `data/problems/imo/imo-2010-c5-bad-company-tournament.yaml`: raised profile/ideas/central/editorial statuses, updated solution title, and added metadata note.
- `data/problems/imo/imo-2012-c7-equal-sum-chords-independent-set.yaml`: raised statuses, added `extremal_choice`, updated solution title, and added metadata note.
- `data/problems/imo/imo-2014-c9-snail-circles-tree.yaml`: raised profile/ideas/central/editorial statuses and added metadata note.
- `data/problems/imo/imo-2016-c6-ferry-graph-dynamics.yaml`: raised profile/editorial readiness and added metadata note.
- `data/problems/imo/imo-2016-c8-domino-unique-tiling-cycles.yaml`: raised editorial readiness and added metadata note.
- `data/problems/imo/imo-2019-c4-labyrinth-region-graph.yaml`: raised statuses, updated solution title, added `connected_graph`/`planar_graph` definition anchors, and added metadata note.
- `data/problems/imo/imo-2021-c4-anisotropy-menger.yaml`: raised statuses, added `double_counting` standard idea, updated solution title, and added metadata note.
- `data/problems/imo/imo-2023-c7-ferry-companies-hamiltonian-paths.yaml`: raised statuses, updated solution title, and added metadata note.

## Relations

Added `data/relations/relations.d/metadata-pass-imo-links.yaml` with seven non-duplicate relation records:

- `imo-1985-sl5-lattice-perfect-code` -> `imo-1996-c1-grid-knight-reachability`
- `utyum-2007_lichol30_4_rectangle_coloring` -> `imo-1996-c2-grid-vertices-two-red`
- `utyum-2012_komol39_8_binary_tree_ordering` -> `imo-2005-c2-dynastic-vertices-forest`
- `five-color-theorem` -> `imo-2013-c3-imons-graph-coloring`
- `benjamini-tzalik-shortest-paths-bound` -> `imo-2013-c6-flight-distance-layers`
- `usamo-2008-p3-diamond-lattice-path-partition` -> `imo-2016-c8-domino-unique-tiling-cycles`
- `kolmogorov-2022-round2-juniors-hamiltonian-path-parity` -> `imo-2023-c7-ferry-companies-hamiltonian-paths`

No existing relation files were edited.

## Verification

```text
python tools/validate.py
OK: 328 problems, 336 relations, 9 comments, 349 sources, 27 definitions, 15 standard ideas, 19 import batches.

python tools/check_links.py
OK: 370 internal routes, 349 external source URLs syntactically valid.
```
