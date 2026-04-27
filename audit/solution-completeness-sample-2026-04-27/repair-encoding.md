# Repair encoding pass, 2026-04-27

Scope: only the four requested problem files with damaged `solutions[0].text`.

## Repaired

| Problem file | Action | Notes |
| --- | --- | --- |
| `data/problems/apmo/apmo-2010-p3-common-acquaintance-extremal.yaml` | Replaced literal `????` solution text | Reconstructed the complete Russian proof from the preserved formulas and local problem/idea metadata: star construction and component-count upper bound. |
| `data/problems/bmo/bmo-2022-p4-frog-grid-boundary-graph.yaml` | Replaced literal `????` solution text | Reconstructed the complete Russian proof from the preserved formulas and local problem/idea metadata: boundary graph, component bound, and odd-grid construction. |
| `data/problems/egmo/egmo-2016-p3-blue-cells-bipartite-incidence.yaml` | Replaced literal `????` solution text | Reconstructed the complete Russian proof from the preserved formulas and local problem/idea metadata: row-column incidence graph, component lower bound, and block construction. |
| `data/problems/egmo/egmo-2025-p5-rotating-arrows-dynamic-cycle.yaml` | Replaced literal `????` solution text | Reconstructed the complete Russian proof from the preserved formulas and local problem/idea metadata: parity obstruction, Hamiltonian-cycle construction, and modulo-4 uniqueness bound. |

## Deferred

None.

## Verification

- `python tools/validate.py` - OK: 328 problems, 379 relations, 9 comments, 349 sources, 27 definitions, 15 standard ideas, 19 import batches.
- `python tools/check_links.py` - OK: 370 internal routes, 349 external source URLs syntactically valid.
