# Cross-link pass: trees / Euler / handshaking / connectivity

Date: 2026-04-26

Scope: corrected graph-theory cards whose updated `tags`, `problem_profile`, `standard_idea_ids`, and `definition_ids` mention trees, forests, spanning trees, Eulerian walks, handshaking, connectedness, degree sums, or deletion preserving connectivity.

## Added shard

Created `data/relations/relations.d/metadata-pass-cross-links-tree-euler.yaml` with 8 new relations:

- `tree-equivalent-properties` -> `memo-2021-i2-bishop-circuit-forest`
- `tree-equivalent-properties` -> `rmm-2023-p6-colored-spanning-tree-suspicious-edges`
- `tree-equivalent-properties` -> `kolmogorov-2022-round2-high-colored-integers-infinite-tree`
- `eulerian-graph-criterion` -> `kolmogorov-2022-round4-high-airport-walk-parity`
- `eulerian-graph-criterion` -> `kolmogorov-2022-round4-second-third-even-degree-odd-walks`
- `handshaking-lemma` -> `egmo-2016-p3-blue-cells-bipartite-incidence`
- `handshaking-lemma` -> `bmo-2022-p4-frog-grid-boundary-graph`
- `handshaking-lemma` -> `imo-2010-c5-bad-company-tournament`

## Duplicate audit

All existing relation files were loaded through `tools/lib.py::load_relations`, including metadata-pass shards and `metadata-pass-cross-links-after-tags.yaml`.

Pairs intentionally skipped because an equivalent relation already exists:

- `tree-equivalent-properties` <-> `tc-2015-16-connectivity-query-lower-bound`
- `tree-equivalent-properties` <-> `tc-2018-19-simple-complex-state-game`
- `tree-equivalent-properties` <-> `tc-2023-24-coins-pairing-weighing-forest`
- `tree-equivalent-properties` <-> `imo-2004-c3-delete-edge-from-4cycle`
- `kolmogorov-2022-round4-high-airport-walk-parity` <-> `kolmogorov-2022-round4-second-third-even-degree-odd-walks`
- `handshaking-lemma` <-> `kolmogorov-2022-round4-high-airport-walk-parity`
- `handshaking-lemma` <-> `kolmogorov-2022-round4-second-third-even-degree-odd-walks`
- `egmo-2016-p3-blue-cells-bipartite-incidence` <-> `memo-2021-i2-bishop-circuit-forest`

## Notes

- No problem YAML files were edited.
- Direct prerequisite links were used only when the target solution visibly depends on the classical method; motif-level links were marked `needs_human_review` where the updated metadata supports navigation but the proof does not invoke the theorem directly.
