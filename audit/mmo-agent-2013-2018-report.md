# MMO graph audit, 2013-2018

Date: 2026-05-03

Scope and constraints:
- Repository: `C:\Users\Admin\Documents\Codex\2026-04-20-c-users-admin-documents-codex-2026`.
- Read corpus: `audit/_mmo_tc_*`, filtered to manifest records with `family=mmo`.
- Years covered: MMO seasons `2013-14`, `2014-15`, `2015-16`, `2016-17`, `2017-18`, `2018-19`, plus the local 2013 MMO booklet record.
- Write scope used: this report and new YAML files under `data/problems/mmo/`.
- Not touched: `data/sources/sources.yaml`, `docs/index.html`, `viewer/index.html`, `index/generated.sqlite`, relations.

## Confirmed and added

### `mmo-2016-linguists-kneser-edge-bound`

- Status: confirmed; YAML created at `data/problems/mmo/mmo-2016-linguists-kneser-edge-bound.yaml`.
- Source URL: `https://mos.olimpiada.ru/upload/files/Archive_tasks_2013-.../2015-16/math/ans-math-8-11-final-15-6.pdf`.
- Local source: `audit/_mmo_tc_text_clean/8c75a829a791e463.txt`; PDF `audit/_mmo_tc_pdfs/8c75a829a791e463.pdf`.
- Original placement: LXXIX MMO, 2015/16 final booklet, grade 9 problem 6.
- Author: A. M. Raigorodskii, printed in the booklet.
- Statement summary: in a country with `n` languages, `m` people know distinct triples of languages; the largest mutually communicating set has size `k`, with `11n <= k <= m/2`; prove at least `mn` pairs cannot communicate without an intermediary.
- Official solution summary: choose a largest mutually communicating set `B`; every outside person has a disjoint-language witness in `B`; at most `9n` people in `B` can communicate with that outside person, giving `(m-k)(k-9n) >= mn` non-communicating pairs.
- Why graph: the official commentary explicitly reformulates the problem as a subgraph of the Kneser graph with `r=3`; people are vertices, disjoint language triples are edges, and the maximum mutually communicating set is an independent set.
- `graph_role`: official solution reformulation.
- Tags: `kneser_graph`, `independent_set`, `edge_counting`, `graph_in_solution`.
- Duplicate check: no exact match found in existing `data/problems`; no TC duplicate found in `data/problems/tournament-cities`.
- Confidence: high; status in YAML is `needs_human_review` only because source ids are temporary.

### `mmo-2018-acquaintance-seating-clique-chromatic`

- Status: confirmed; YAML created at `data/problems/mmo/mmo-2018-acquaintance-seating-clique-chromatic.yaml`.
- Problem source URL: `https://mos.olimpiada.ru/upload/files/Archive_tasks_2013-.../2017-18/math/tasks-math-9-final-17-8.pdf`.
- Problem local source: `audit/_mmo_tc_text_clean/89e4f339ef8abcc1.txt`; PDF `audit/_mmo_tc_pdfs/89e4f339ef8abcc1.pdf`.
- Solution source URL: `https://mos.olimpiada.ru/upload/files/Archive_tasks_2013-.../2017-18/math/ans-math-9-final-17-8.pdf`.
- Solution local source: `audit/_mmo_tc_text_clean/6fb40982bcbcc4fb.txt`; PDF `audit/_mmo_tc_pdfs/6fb40982bcbcc4fb.pdf`.
- Original placement: LXXXI MMO, 2017/18 final, grade 9 problem 6.
- Author: not found in the local task/solution text.
- Statement summary: 2018 participants, some acquainted; a set of pairwise acquainted participants is a "circle" if every outside participant is not acquainted with at least one member of it; seat everyone in 90 rooms so that no room contains all members of a circle.
- Official solution summary: prove by induction that at most `k^2` participants can be seated in `2k` rooms; for `k=45`, use either a vertex of degree at least `2k-2` and induction on the remaining participants, or greedy coloring when maximum degree is below `2k-2`.
- Why graph: the official commentary explicitly says the problem is about clique chromatic number; participants are vertices, acquaintances are edges, and circles are maximal cliques.
- `graph_role`: official solution commentary and model.
- Tags: `clique_coloring`, `acquaintance_graph`, `induction`, `greedy_coloring`.
- Duplicate check: no exact match found in existing `data/problems`; no TC duplicate found in `data/problems/tournament-cities`.
- Confidence: high; status in YAML is `needs_human_review` only because source ids are temporary and author is not identified.

## Confirmed but not added because already in TC/base

### MMO 2013/14, kingdom roads / vertex-transitive not transposition

- MMO source URL: `https://mos.olimpiada.ru/upload/files/Archive_tasks_2013-.../2013-14/mmo/tasks-math-11-final-13-4.pdf`; local text `audit/_mmo_tc_text_clean/14d313d48f138074.txt`.
- MMO booklet/source with solution: `http://olympiads.mccme.ru/mmo/2014/77mmo.pdf`; local text `audit/_mmo_tc_text_clean/29537a4c3c3d1b0b.txt`.
- Statement summary: some pairs of cities are joined by railway; every ordered pair of cities can be renamed so the first receives the second's name without changing the king's road list; ask whether every pair can be swapped by such a renaming.
- Why graph: explicit finite graph of cities and railways; the graph-theory formulation is vertex-transitivity versus the existence of automorphisms swapping arbitrary pairs.
- Official solution: gives a counterexample from the graph/skeleton of a truncated tetrahedron and proves a particular pair cannot be swapped.
- Duplicate: already present as `data/problems/tournament-cities/tc-2013-14-vertex-transitive-not-transposition.yaml`.
- Action: not added as an MMO YAML to avoid duplicate problem cards. Suggested future relation, if relation editing is allowed: add MMO source/variant to the existing TC card or link as same/duplicate source occurrence.

## Reviewed candidates not added

- MMO 2015/16 remote grade 11, party with 65 people: explicit acquaintance graph in the statement, but I only found the task text (`audit/_mmo_tc_text_clean/a8f23c0892de03b3.txt`) and not a usable official solution in the paired answer record (`audit/_mmo_tc_text_clean/ea4f58505f205536.txt`). Needs manual source verification before adding.
- MMO 2016/17 grade 10/11, Chicago gangs: graph-like conflict/independent-set formulation in the statement (`audit/_mmo_tc_text_clean/965124a875eeaf44.txt`, duplicated in `6b4626a16b736700.txt`), but I did not find the official solution in the local answer text. Needs manual check.
- MMO 2014/15 grade 10, football rounds: can be interpreted as matchings/edge-coloring in a complete graph, but the statement does not explicitly require graph theory and I did not find an official graph solution in the local text. Not added.
- MMO 2018/19 grade 9, colored chords of regular 100-gon: TC overlap report marks it as a TC repeat; statement is geometric/algebraic, not a graph card under the current inclusion rule. Not added.
- MMO 2018/19 grade 8, `n x n` table with consecutive numbers in side-neighbor cells: TC repeat; grid adjacency is incidental to a table construction/parity problem and an existing TC graph card is only for a different 4x4 neighbor-number problem. Not added.
- MMO 2018/19 grade 10/11, worms from monotone lattice paths: TC repeat; tiling/enumeration problem, not a graph problem under the current rule. Not added.
- MMO 2013/14 grade 9, square tablecloth: TC repeat; geometry, not graph. Not added.
- MMO 2013/14 grade 9, grasshoppers on marked circle points: TC repeat; movement on a circle, not graph. Not added.
- MMO 2013 booklet, alternating colored numbers on a circle: TC repeat; cyclic sequence problem, not graph. Not added.
- MMO 2013 booklet, rectangular islands divided into "graphstva": false positive from the Russian word for counties/regions; not graph theory. Not added.
- Geometry hits involving `graph of a function`, polyhedron vertices/edges, and circle/neighbor wording were treated as false positives unless the official solution used graph theory essentially.

## Source IDs to add later

- `src-mmo-TODO-2016-final-8-11`: LXXIX MMO 2015/16 final solutions booklet, `ans-math-8-11-final-15-6.pdf`, local PDF `audit/_mmo_tc_pdfs/8c75a829a791e463.pdf`.
- `src-mmo-TODO-2018-grade9-final`: LXXXI MMO 2017/18 grade 9 final tasks, `tasks-math-9-final-17-8.pdf`, local PDF `audit/_mmo_tc_pdfs/89e4f339ef8abcc1.pdf`.
- `src-mmo-TODO-2018-grade9-final-solutions`: LXXXI MMO 2017/18 grade 9 final solutions, `ans-math-9-final-17-8.pdf`, local PDF `audit/_mmo_tc_pdfs/6fb40982bcbcc4fb.pdf`.

## Summary

- Years/sources reviewed: MMO manifest records for 2013-2018 in `audit/mmo-tc-clean-text-manifest.json`, with task and solution texts from `audit/_mmo_tc_text_clean`.
- Main confirmed new cards: 2.
- Confirmed duplicate already in TC/base: 1.
- Manual-check candidates left: 3.
- TC/repeat or non-graph false positives explicitly marked above: tablecloth, circle numbers, worms, `n x n` table, grasshoppers, colored chords, graphstva, graph-of-function/polyhedron wording.
