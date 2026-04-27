# Metadata Pass: Classical + USAMO

Date: 2026-04-26

Scope:
- `data/problems/classical/brooks-theorem.yaml`
- `data/problems/classical/menger-theorem.yaml`
- `data/problems/classical/ore-theorem.yaml`
- `data/problems/classical/turan-theorem.yaml`
- `data/problems/usamo/usamo-2008-p6-even-friends-two-rooms.yaml`
- `data/problems/usamo/usamo-2009-p3-tasteful-domino-tiling-alternating-cycles.yaml`
- `data/problems/usamo/usamo-2024-p3-balanced-regular-polygon-triangulation.yaml`
- `data/relations/relations.d/metadata-pass-classical-usamo-links.yaml`

## Metadata Updates

- Brooks: aligned the profile with greedy ordering, spanning-tree order, block decomposition, and local recoloring; added `central_method`, fuller solution `definition_ids`, checked idea/difficulty/editorial statuses, and a metadata note.
- Menger: aligned the profile with vertex splitting and max-flow/min-cut; added `simple_graph`/`directed_graph` definitions, `augmenting_path_method` as the nearest available standard idea, checked statuses, and promoted `central_method` to `ai_checked`.
- Ore: aligned the profile with maximal non-Hamiltonian completion, degree-sum closure, and longest-path closure; added `extremal_choice` to standard ideas, `central_method`, fuller definitions, and checked statuses.
- Turan: aligned the profile with Zykov symmetrization, balancing, complement reformulations, and part-size-square invariants; added `central_method`, fuller definitions, `symmetrization` tag, and checked statuses.
- USAMO 2008 P6: aligned the card around F2 affine solution spaces, parity constraints, and switching induction; replaced the weak top-level extremal tag with `graph_symmetry`, added a standard idea to the switching solution, and checked editorial status.
- USAMO 2009 P3: aligned around matching overlays, symmetric differences, alternating cycles, induction on area, and boundary obstruction; updated tags to `matching`, `planar_graphs`, `goal_characterization`, and marked the expanded solution pass public-ready.
- USAMO 2024 P3: aligned as graph-in-statement / outerplanar setup with algebraic central method; added roots-of-unity and cyclotomic-integrality profile fields, removed the weaker `extremal_choice` top-level tag, and marked the card checked while preserving the note that the decisive method is non-graph algebra.

## Relation Additions

Added only to `data/relations/relations.d/metadata-pass-classical-usamo-links.yaml`:

- `brooks-theorem` -> `color-reduction-by-odd-deletion-and-doubling`
- `menger-theorem` -> `usamo-2004-p4-black-path-grid-game`
- `ore-theorem` -> `dirac-theorem`
- `turan-theorem` -> `mantel-theorem`
- `handshaking-lemma` -> `usamo-2008-p6-even-friends-two-rooms`
- `egmo-2022-p5-domino-parity-bipartite-matching` -> `usamo-2009-p3-tasteful-domino-tiling-alternating-cycles`
- `euler-formula-planar` -> `usamo-2024-p3-balanced-regular-polygon-triangulation`

No existing relation shard was modified.

## Validation

- `python tools\validate.py`: baseline and post-metadata pass were OK; final rerun later failed on unrelated out-of-scope IMO files with unknown tags:
  `maximum_principle`, `grid_graphs`, `shortest_paths`, `menger_theorem`.
- `python tools\check_links.py`: OK
