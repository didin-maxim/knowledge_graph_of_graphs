# Repair: Classical/Paper Cards

Date: 2026-04-27

Scope: `tree-equivalent-properties#sol-leaf-induction`, `chen-yu-fragile-graphs-theorem#sol-paper-theorem`, `benjamini-tzalik-shortest-paths-bound#sol-paper-bound`.

## Repaired

- `tree-equivalent-properties#sol-leaf-induction`: expanded to a full proof of all three equivalences: connected acyclic graph, connected graph with `n-1` edges, and unique simple path between every two vertices.
- `benjamini-tzalik-shortest-paths-bound#sol-paper-bound`: replaced the compressed note with a full Russian proof following the arXiv paper's entropy argument. The proof establishes the stronger bound
  `Delta * (floor(Delta/2) ceil(Delta/2))^((t-1)/2)` and derives `2(Delta/2)^t`; it also records the cycle-with-parallel-edges extremal example.

## Deferred

- `chen-yu-fragile-graphs-theorem#sol-paper-theorem`: deferred as `deferred_needs_source_or_reconstruction`. The available repository/source metadata confirms the theorem statement, but I did not have a full locally checkable proof of the Chen-Yu paper theorem. The solution text now explicitly says it is not a proof, and the solution remains `needs_human_review`.

## Validation

- `python tools/validate.py`
- `python tools/check_links.py`
