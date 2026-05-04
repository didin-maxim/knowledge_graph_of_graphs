# MMO 2019-2025 graph scan

Scope: only local manifest records with `family=mmo` from `audit/_mmo_tc_*`. I did not edit shared files (`data/sources/sources.yaml`, generated indexes, docs/viewer, relations) and only created confirmed cards under `data/problems/mmo/`.

## Sources checked

- Manifest: `audit/mmo-tc-clean-text-manifest.json`.
- Local OCR/text: `audit/_mmo_tc_text_clean/*.txt`.
- Local PDFs: `audit/_mmo_tc_pdfs/*.pdf`.
- Years covered: `2019-20`, `2020-21`, `2021-22`, `2022-23`, `2023-24`, `2024-25`.
- Duplicate check: existing `data/problems/tournament-cities/*.yaml` and existing non-MMO graph cards. I did not modify TC files; several are untracked/dirty from other agents.

## Confirmed and added

### `mmo-2020-one-way-roads-acyclic-tournament`

- MMO: 2020/21, final, 8 class, problem 6.
- Statement source URL in manifest: `https://mos.olimpiada.ru/upload/files/Archive_tasks_2013-.../2020-21/math/tasks-math-8-final-20-21.pdf`.
- Solution source URL in manifest: `https://mos.olimpiada.ru/upload/files/Archive_tasks_2013-.../2020-21/math/ans-math-8-final-20-21.pdf`.
- Local text/PDF: `audit/_mmo_tc_text_clean/420811488dc5ec96.txt`, `audit/_mmo_tc_text_clean/bb781a139b3d1454.txt`; PDFs `audit/_mmo_tc_pdfs/420811488dc5ec96.pdf`, `audit/_mmo_tc_pdfs/bb781a139b3d1454.pdf`.
- Author: А. Заславский in official solution text.
- Why graph: every pair of 32 cities has one directed road; this is exactly a tournament. The goal is to reverse edges until no directed return is possible, i.e. an acyclic tournament.
- `graph_role`: graph in statement, central model.
- Tags: `tournament`, `directed_graph`, `edge_reversal`, `induction`.
- Confidence/status: high / `ai_checked`, still `needs_human_review` because source IDs are TODO.
- Relations: no direct TC duplicate found. Related only by theme to tournament/orientation tasks.

### `mmo-2023-hypergraph-club-acquaintance-graph`

- MMO: 2023/24, final, 10 class, problem 3.
- Statement source URL in manifest: `https://mos.olimpiada.ru/upload/files/Archive_tasks_2013-.../2023-24/math/tasks-math-10-final-23-24.pdf`.
- Solution source URL in manifest: `https://mos.olimpiada.ru/upload/files/Archive_tasks_2013-.../2023-24/math/sol-math-10-final-23-24.pdf`.
- Local text/PDF: `audit/_mmo_tc_text_clean/9c3c3a2e4b9dbcbb.txt`, `audit/_mmo_tc_text_clean/6c132d88b67c590f.txt`; PDFs `audit/_mmo_tc_pdfs/9c3c3a2e4b9dbcbb.pdf`, `audit/_mmo_tc_pdfs/6c132d88b67c590f.pdf`.
- Author: not visible in extracted local text.
- Why graph: the statement explicitly names hypergraphs; meetings are hyperedges and the acquaintance relation is the 2-section/intersection graph.
- `graph_role`: graph/hypergraph in statement, central model.
- Tags: `hypergraph`, `intersection_graph`, `acquaintance_graph`, `degree`, `construction`.
- Confidence/status: high / `ai_checked`, still `needs_human_review` because source IDs are TODO.
- Relations: no direct TC duplicate found; related to social/acquaintance graph problems in base.

### `mmo-2024-symposium-acquaintance-lies`

- MMO: 2024/25, final, 11 class, day 1, problem 1. Same model also appears in 8 class, problem 2, with 12 participants.
- Statement source URL in manifest: `https://mos.olimpiada.ru/upload/files/Archive_tasks_2013-.../2024-25/math/tasks-math-11-tur1-final-24-25.pdf`.
- Solution source URL in manifest: `https://mos.olimpiada.ru/upload/files/Archive_tasks_2013-.../2024-25/math/sol-math-11-tur1-final-24-25.pdf`.
- Local text/PDF: `audit/_mmo_tc_text_clean/d099d3fb24076b29.txt`, `audit/_mmo_tc_text_clean/d738368d897f6572.txt`; PDFs `audit/_mmo_tc_pdfs/d099d3fb24076b29.pdf`, `audit/_mmo_tc_pdfs/d738368d897f6572.pdf`.
- Author: М. Евдокимов in official solution text.
- Why graph: participants are vertices and acquaintance is a simple graph; liars answer on nonedges, truth-tellers on edges, so the complement graph is essential.
- `graph_role`: graph in statement, central counting model.
- Tags: `acquaintance_graph`, `complement_graph`, `double_counting`, `extremal_construction`.
- Confidence/status: high / `ai_checked`, still `needs_human_review` because source IDs are TODO.
- Relations: no direct TC duplicate found; related to acquaintance graph cards such as USAMO 2022 P6 only thematically.

## Confirmed but not added as cards in this pass

- MMO 2023/24, 11 class day 2, official solution uses an auxiliary bipartite graph for cell groups and Euler cycles. Local files: `audit/_mmo_tc_text_clean/6eff16152ea5991f.txt`, `audit/_mmo_tc_text_clean/e814ed18bb3a9877.txt`. I left this for manual carding because the statement extraction is noisy and the graph is only in one official solution route.
- MMO 2024/25, 8 class problem 4 and 9 class problem 2: infinite placement of knights so each knight attacks exactly 5 or 6 others. This is naturally an induced subgraph of the knight graph, but the local official text I checked does not make the graph formulation as cleanly as the three added cards. Candidate status: manual review.
- MMO 2021/22, 8 class problem 6: rook path through every cell of an `n x n` board, minimizing maximum difference between labels of adjacent cells. Author Б. Френкин. Local files: `audit/_mmo_tc_text_clean/0d21db8eee0f9f5a.txt`, `audit/_mmo_tc_text_clean/f75fb4618efc2dba.txt`. This is close to Hamiltonian paths in the grid graph, but the official solution is mostly board/path-ordering and it may overlap conceptually with TC grid/Hamiltonian material. Candidate status: do not add without human duplicate review.

## Rejected or de-prioritized candidates

- Graphs of functions in 2019/20, 2021/22, 2023/24 and 2024/25 were rejected as `график функции`, not graph theory.
- Football/handball tournaments in 2019/20 and 2023/24 were rejected for now: they are round-robin score-counting problems, but I did not find an essential graph-theoretic role in the local official solutions.
- Polyhedron vertex/edge counting in 2021/22 was rejected as geometry/polyhedra, not graph theory for this database pass.
- 2024/25 color/cell tasks: one 9-class problem about black/white cells with exactly two same-color side-neighbors is graph-adjacent via grid adjacency, but the condition is local coloring rather than a confirmed official graph solution. Candidate status: manual review.
- 2022/23 final tasks showed only weak hits (`graph` as function graph or incidental vertex/edge language) except ordinary geometry/polyhedron wording; no confident MMO graph card added.

## Source IDs to add later

- `src-mmo-TODO-2020-21-tasks-8-final`: official MMO 2020/21 final 8 class tasks PDF.
- `src-mmo-TODO-2020-21-ans-8-final`: official MMO 2020/21 final 8 class solutions PDF.
- `src-mmo-TODO-2023-24-tasks-10-final`: official MMO 2023/24 final 10 class tasks PDF.
- `src-mmo-TODO-2023-24-sol-10-final`: official MMO 2023/24 final 10 class solutions PDF.
- `src-mmo-TODO-2024-25-tasks-11-tur1-final`: official MMO 2024/25 final 11 class day 1 tasks PDF.
- `src-mmo-TODO-2024-25-sol-11-tur1-final`: official MMO 2024/25 final 11 class day 1 solutions PDF.

## Notes for the main agent

- The archive stores source URLs with `Archive_tasks_2013-...` truncation in the local manifests and HTML, so source creation should verify the exact public URL before replacing TODO IDs.
- Existing dirty/untracked TC files were present before this pass; I used them only for duplicate/context checks and did not edit them.
- Created cards deliberately keep `relations_status: not_started`; relation wiring should be handled by the main/base agent after source IDs are finalized.
