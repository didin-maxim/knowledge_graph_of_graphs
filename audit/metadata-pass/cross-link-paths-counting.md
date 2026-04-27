# Metadata Pass Cross-Link: Paths and Counting

Date: 2026-04-26

Scope: synchronized cross-link pass after the metadata pass, focused on corrected cards with longest-path, Hamiltonian path/cycle, reachability/distance-layer, projection/solid-angle, injection, double-counting, and product/counting-inequality motifs.

## Added relation shard

Created only:

- `data/relations/relations.d/metadata-pass-cross-links-paths-counting.yaml`

No problem YAML files were edited.

## Duplicate audit

Before adding links, existing relation shards were scanned for exact and reverse pairs involving the proposed endpoints. One candidate was rejected as an existing exact duplicate:

- `handshaking-lemma` -> `memo-2025-t4-toll-complete-graph` already exists in `data/relations/relations.d/official-archives-idea-links.yaml`.

The final 10 relations in the new shard had no existing exact or reverse endpoint pair at creation time.

## Relations added

- `longest-path-endpoints-shortest-detour` -> `kolmogorov-2008-round-1-high-league-problem-1`
- `longest-path-endpoints-shortest-detour` -> `kolmogorov-2008-round-3-high-league-problem-1`
- `kolmogorov-2010-individual-olympiad-seniors-problem-4` -> `fyum-2011-finalb-p4`
- `kolmogorov-2010-individual-olympiad-seniors-problem-4` -> `imo-2023-c7-ferry-companies-hamiltonian-paths`
- `imo-1996-c1-grid-knight-reachability` -> `imo-2013-c6-flight-distance-layers`
- `imo-2005-c3-black-paths-injection` -> `imo-1996-c1-grid-knight-reachability`
- `kolmogorov-2008-individual-olympiad-seniors-problem-7` -> `euler-formula-planar`
- `usamo-1976-p1-monochromatic-rectangle-bipartite` -> `imo-1996-c2-grid-vertices-two-red`
- `mantel-theorem` -> `usa-tst-2013-dec-p1-language-club-rainbow-triangles`
- `usamo-1976-p1-monochromatic-rectangle-bipartite` -> `kolmogorov-2007-team-olympiad-seniors-problem-7`

## Metadata basis

The pass used post-metadata fields rather than problem text edits:

- `tags` and `problem_profile` for motif clustering.
- `properties.central_method` for checked method alignment.
- solution `standard_idea_ids` for longest-path, double-counting, extremal-choice, and induction anchors.
- statement/solution `definition_ids` for path, cycle, Hamiltonian path/cycle, planar graph, tournament, connected graph, degree, and complete graph anchors.

## Verification

```text
python tools/validate.py
OK: 328 problems, 384 relations, 9 comments, 349 sources, 27 definitions, 15 standard ideas, 19 import batches.

python tools/check_links.py
OK: 370 internal routes, 349 external source URLs syntactically valid.
```
