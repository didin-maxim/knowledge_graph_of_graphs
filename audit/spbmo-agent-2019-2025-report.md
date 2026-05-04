# СПбМО 2019-2025: graph scan

Scope: modern archive of Санкт-Петербургская олимпиада школьников / СПбМО, with focus on 2019-2025. I used official `olimpiada.ru/activity/246/tasks` pages for 2019-2021/22 RSR PDFs with solutions, and official PDMI pages `https://www.pdmi.ras.ru/~olymp/{year}/problems.html` for 2019-2025 city statement PDFs. I did not edit shared source registries, relations, docs/viewer, or generated files.

## Sources Checked

- `olimpiada.ru/activity/246/tasks`, classes 6-11, years 2019, 2020, 2021; PDFs from `rsr-olymp.ru/upload/files/tasks/246/...`.
- PDMI official archive pages `https://www.pdmi.ras.ru/~olymp/2019/problems.html` through `https://www.pdmi.ras.ru/~olymp/2025/problems.html`.
- PDMI statement PDFs checked for each year: `distYY.pdf`, `c_68_YY.pdf`, `c_911_YY.pdf`.
- Temporary local extraction outside repo: `%TEMP%/spbmo_scan_2019_2025/`; manifest: `%TEMP%/spbmo_scan_2019_2025/manifest_hits.json`.
- Duplicate check: exact phrase search across `data/problems` for candidate-specific strings (`каракатиц`, `5000 точек`, `Пафнутий`, `Эльдорадо`, `10000 маленьких`, etc.). No direct duplicates found.

## Confirmed and Added

### `spbmo-2020-karakatitsa-edge-weights`

- СПбМО / Санкт-Петербургская олимпиада школьников: 2019/20, заключительный этап, 9 класс, задача 7.
- Statement source: `https://rsr-olymp.ru/upload/files/tasks/246/2019/14211324-tasks-math-9-tur2_stage-19-20.pdf`.
- Official solution source: `https://rsr-olymp.ru/upload/files/tasks/246/2019/14211324-sol-math-9-tur2_stage-19-20.pdf`.
- Author: not found in checked RSR/PDF text.
- why_graph: graph is explicit in the statement: 400 vertices, edge weights, edge-neighborhood "каракатица".
- graph_role: `explicit_graph_in_statement_and_official_solution_core`.
- Tags: `graph_weights`, `matching`, `double_counting`, `extremal_graph_theory`.
- Confidence/status: high for graph relevance and source; card left `needs_human_review` because source IDs are TODO and proof is compact.
- Possible relations: maximum matching lemma, weighted graph/double-counting cards.

### `spbmo-2021-coordinate-points-two-colored-2factor`

- СПбМО / Санкт-Петербургская олимпиада школьников: 2020/21, заключительный этап, 7 класс, задача 5.
- Problem+official solution source: `https://rsr-olymp.ru/upload/files/tasks/246/2020/18474156-taskssol-math-7-final-20-21.pdf`.
- Author: not found in checked RSR/PDF text.
- why_graph: official solution explicitly constructs a graph `G` on the 5000 points; red edges pair consecutive points by x-order and blue edges pair consecutive points by y-order. Each vertex has one red and one blue edge, so the graph is a union of even cycles and is bipartite.
- graph_role: `official_solution_core`.
- Tags: `auxiliary_graph`, `bipartite_graph`, `cycle_decomposition`, `coloring`.
- Confidence/status: high for official graph role; card left `needs_human_review`.
- Possible relations: balanced bipartite coloring / even-cycle bipartition cards.

### `spbmo-2022-big-small-cities-spanning-forest-leaves`

- СПбМО / Санкт-Петербургская олимпиада школьников: 2021/22, заключительный этап, 8 класс, задача 5.
- Statement source: `https://rsr-olymp.ru/upload/files/tasks/246/2021/246-tasks-math-8-final-21-22.pdf`.
- Official solution source: `https://rsr-olymp.ru/upload/files/tasks/246/2021/246-sol-math-8-final-21-22.pdf`.
- Author: not found in checked RSR/PDF text.
- why_graph: statement is a connected road graph; official solution chooses a spanning forest rooted at 500 large cities and counts leaves after reconnecting the forest.
- graph_role: `explicit_statement_application_and_official_solution_core`.
- Tags: `connected_graph`, `spanning_tree`, `spanning_forest`, `leaves`.
- Confidence/status: high for graph relevance and source; card left `needs_human_review`.
- Possible relations: spanning-tree leaf-counting problems.

### `spbmo-2022-eldorado-friendship-tree-potential`

- СПбМО / Санкт-Петербургская олимпиада школьников: 2021/22, заключительный этап, 10 класс, задача 7.
- Problem+official solution source: `https://rsr-olymp.ru/upload/files/tasks/246/2021/246-sol-math-10-final-21-22.pdf`.
- Author: not found in checked RSR/PDF text.
- why_graph: the club-growth rule creates a tree; official solution explicitly says "Переведем задачу на язык графов" and works on a rooted tree with edge differences.
- graph_role: `official_solution_core`.
- Tags: `trees`, `rooted_tree`, `potential_function`, `induction`, `path_bound`.
- Confidence/status: high for official graph role; card left `needs_human_review`.
- Possible relations: rooted-tree potential/path-sum cards.

## Confirmed Condition-Only / No Official Solution Found in This Pass

- PDMI 2019, city round, 6-8 classes, problem 6: company with no "общительные" and no "стеснительные" people; natural graph/complement graph extremal problem. Source: `https://www.pdmi.ras.ru/~olymp/2019/problems/c_68_19.pdf`. No official solution found in online PDMI/RSR pass for this exact PDMI city statement.
- PDMI 2019, city round, 9-11 classes, problem 2: connected metro graph on 2019 stations, cover stations by at most k simple paths/lines. Source: `https://www.pdmi.ras.ru/~olymp/2019/problems/c_911_19.pdf`. No official solution found.
- PDMI 2019, city round, 9-11 classes, problem 6: 100-regular road graphs and 2-switches (`AB,CD -> BC,AD`). Source: `https://www.pdmi.ras.ru/~olymp/2019/problems/c_911_19.pdf`. No official solution found.
- PDMI 2023, city round, 9-11 classes, problem on graph `G`, disjoint sets `X,Y`, and components of `G-X`, `G-Y`, `G-(X union Y)`. Source: `https://www.pdmi.ras.ru/~olymp/2023/problems/c_911_23.pdf`. No official solution found.
- PDMI 2024, city round, 9-11 classes, problem on decomposing all tunnels of any connected metro graph into simple non-cyclic lines so that no route needs more than 100 transfers; asks largest `N`. Source: `https://www.pdmi.ras.ru/~olymp/2024/problems/c_911_24.pdf`. No official solution found.
- PDMI 2024, city round, 6-8 classes, problem on an "атомизированный город" with acquaintance pairs and at most 998 acquaintance pairs among any 1000 residents. Source: `https://www.pdmi.ras.ru/~olymp/2024/problems/c_68_24.pdf`. No official solution found.

## Rejected / De-Prioritized Hits

- "График функции" hits in district PDFs were rejected as function graphs, not graph theory.
- Ordinary geometry "вершины" and "стороны/соседи" hits were rejected.
- Tournament/round-robin wording without a graph-theoretic official solution was not carded.
- Grid, rook, and local-neighbor board problems were kept out unless an official graph solution was explicit.
- 2019/20 class 11 oligarch road/corporation problem has a graph-like road network and official solution, but I left it for manual review because it is closer to hypergraph/design counting and the graph role is less clean than the added cards.

## Source IDs To Add Later

- `src-spbmo-TODO-2019-20-final-9-tasks`: RSR official SPbMO 2019/20 final, 9 class tasks PDF.
- `src-spbmo-TODO-2019-20-final-9-sol`: RSR official SPbMO 2019/20 final, 9 class solutions PDF.
- `src-spbmo-TODO-2020-21-final-7-taskssol`: RSR official SPbMO 2020/21 final, 7 class tasks+solutions PDF.
- `src-spbmo-TODO-2021-22-final-8-tasks`: RSR official SPbMO 2021/22 final, 8 class tasks PDF.
- `src-spbmo-TODO-2021-22-final-8-sol`: RSR official SPbMO 2021/22 final, 8 class solutions PDF.
- `src-spbmo-TODO-2021-22-final-10-sol`: RSR official SPbMO 2021/22 final, 10 class tasks+solutions PDF.
- Optional condition-only sources if carded later: `src-spbmo-TODO-pdmi-2019-c68`, `src-spbmo-TODO-pdmi-2019-c911`, `src-spbmo-TODO-pdmi-2023-c911`, `src-spbmo-TODO-pdmi-2024-c68`, `src-spbmo-TODO-pdmi-2024-c911`.

## Summary

- Years in work: 2019, 2020, 2021, 2022, 2023, 2024, 2025 archive pages/PDFs; official RSR solution PDFs available and used for 2019/20, 2020/21, 2021/22.
- Found by sources: 56 keyword-hit PDFs out of 64 scanned; after false-positive filtering, 10 graph-relevant candidates.
- Confirmed with official solution and added: 4 cards.
- Condition-only candidates without official solution found: 6.
- Requires manual check: PDMI condition-only candidates; 2019/20 class 11 oligarch road/corporation problem; final source registry creation for all TODO source IDs.
- Files created: `data/problems/spbmo/spbmo-2020-karakatitsa-edge-weights.yaml`, `data/problems/spbmo/spbmo-2021-coordinate-points-two-colored-2factor.yaml`, `data/problems/spbmo/spbmo-2022-big-small-cities-spanning-forest-leaves.yaml`, `data/problems/spbmo/spbmo-2022-eldorado-friendship-tree-potential.yaml`, `audit/spbmo-agent-2019-2025-report.md`.
