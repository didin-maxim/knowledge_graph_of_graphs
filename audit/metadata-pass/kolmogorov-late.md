# Kolmogorov Late Metadata Pass

Date: 2026-04-26
Scope: repaired Kolmogorov graph cards from 2008-2013 listed in the task.

## Updated problem metadata

Aligned the following fields across the 12 target cards:

- titles
- tags
- problem_profile.objects/methods/keywords/status
- properties.central_method
- solution standard_idea_ids and definition_ids
- statement definition_ids and self_contained/status fields
- solution status, repair_status, review_notes
- editorial review_status/public_ready/relations_status notes

Target cards:

- kolmogorov-2008-individual-olympiad-seniors-problem-7
- kolmogorov-2008-round-1-high-league-problem-1
- kolmogorov-2008-round-2-high-league-problem-1
- kolmogorov-2008-round-3-high-league-problem-1
- kolmogorov-2010-individual-olympiad-juniors-problem-5
- kolmogorov-2010-individual-olympiad-seniors-problem-4
- kolmogorov-2011-individual-olympiad-seniors-problem-7
- kolmogorov-2011-team-olympiad-juniors-problem-6
- kolmogorov-2011-team-olympiad-seniors-problem-4
- kolmogorov-2012-individual-olympiad-seniors-problem-6
- kolmogorov-2013-individual-olympiad-seniors-problem-5
- kolmogorov-2013-team-olympiad-seniors-problem-8

## Relations

Created only the requested dedicated shard:

- data/relations/relations.d/metadata-pass-kolmogorov-late-links.yaml

Added 11 relation records linking the repaired cards to nearby Kolmogorov/classical/olympiad graph cards. Existing relation shards were not edited.

Main link themes:

- solid-angle/polyhedron repair to planar counting
- longest-path and degree arguments to Ore/Dirac style cards
- tournament/comparison metadata to tournament counting
- tree/cube Hamiltonicity to tree prerequisites
- parity/Euler-trail team problems to the Eulerian criterion
- tree/coloring and chromatic-number tasks to five-color/Brooks style neighbors

## Validation

- python tools/check_links.py: OK
- python tools/validate.py: final full-repo run failed on unrelated IMO tag errors outside this pass:
  - data/problems/imo/imo-1994-c2-city-ages-harmonic-graph.yaml: unknown tag maximum_principle
  - data/problems/imo/imo-1996-c1-grid-knight-reachability.yaml: unknown tag grid_graphs
  - data/problems/imo/imo-1996-c2-grid-vertices-two-red.yaml: unknown tag grid_graphs
  - data/problems/imo/imo-2013-c6-flight-distance-layers.yaml: unknown tag shortest_paths
  - data/problems/imo/imo-2021-c4-anisotropy-menger.yaml: unknown tag menger_theorem

No validation errors were reported for the Kolmogorov target files or for data/relations/relations.d/metadata-pass-kolmogorov-late-links.yaml. A target metadata reference self-check for tags, definition_ids, and standard_idea_ids also passed.
