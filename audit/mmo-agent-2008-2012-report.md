# MMO graph pass 2008-2012

Date: 2026-05-03

Scope:
- Manifest filter: only records with `family=mmo` from `audit/mmo-tc-clean-text-manifest.json`.
- Local archive: `audit/_mmo_tc_pdfs`, `audit/_mmo_tc_text_clean`.
- Write scope used: this report and new cards under `data/problems/mmo/`.
- Shared files intentionally not touched: `data/sources/sources.yaml`, `docs/index.html`, `viewer/index.html`, `index/generated.sqlite`, relations.

## Confirmed and added

### MMO 2008, 10 class, problem 4: athletes, arbiters, photos

- Card: `data/problems/mmo/mmo-2008-athletes-arbiters-photos.yaml`.
- Source URL: `http://olympiads.mccme.ru/mmo/2008/solutions.pdf`.
- Local PDF: `audit/_mmo_tc_pdfs/85624c5f252bd93c.pdf`.
- Local text: `audit/_mmo_tc_text_clean/85624c5f252bd93c.txt`.
- Author: Б. Р. Френкин.
- Statement: 20 athletes, 10 arbiters, every pair of athletes plays once, each game has one arbiter, both players are photographed with the arbiter; from the stack of all photos, not every person's role can be determined. Find how many such people there could be.
- Official solution: answer is two; it calls such people suspicious and compares how many people each one was photographed with. Arbiters are photographed only with athletes, at most 20 people; athletes with all 19 other athletes and at least one arbiter, at least 20 people. Ambiguous people have exactly 20 co-photo neighbours, forcing a unique pair of interchangeable roles.
- Why graph: not explicit in the statement, but the official solution is naturally and substantially a co-occurrence graph/degree argument on people as vertices and shared photos as adjacency, with multiplicity also used.
- graph_role: `implicit_model_in_solution`.
- Tags: `degree_counting`, `co_occurrence_graph`, `ambiguity`, `application`.
- Confidence/status: confirmed, `ai_checked`; `public_ready=false` until permanent source IDs are created.
- TC/base relation: no exact TC duplicate found in existing `data/problems/tournament-cities`; no relation file written.

### MMO 2010, 10 class, problem 6: unit-distance segments

- Card: `data/problems/mmo/mmo-2010-unit-distance-segments.yaml`.
- Source URL: `http://olympiads.mccme.ru/mmo/2010/solutions.pdf`.
- Local PDF: `audit/_mmo_tc_pdfs/41e3aa0f9672ede0.pdf`.
- Local text: `audit/_mmo_tc_text_clean/41e3aa0f9672ede0.txt`.
- Author: А. М. Райгородский.
- Statement: 4n points on the plane; all pairs at distance 1 cm are joined by segments; among any n+1 points two are joined. Prove at least 7n segments are drawn.
- Official solution: explicitly says "Рассмотрим граф" whose vertices are the marked points and edges are the drawn segments; uses maximal independent sets, edge counting, and the impossibility of realizing K4 by unit segments in the plane. The commentary identifies distance/unit-distance graphs.
- Why graph: graph is central in the official solution.
- graph_role: `official_solution_core`.
- Tags: `unit_distance_graph`, `independent_set`, `edge_counting`, `combinatorial_geometry`.
- Confidence/status: confirmed, `ai_checked`; `public_ready=false` until permanent source IDs are created.
- TC/base relation: no exact TC duplicate found in existing `data/problems/tournament-cities`.

### MMO 2011, 10 class, problem 6: firms and programmers

- Card: `data/problems/mmo/mmo-2011-firms-programmers-geniuses.yaml`.
- Source URL: `http://olympiads.mccme.ru/mmo/2011/74mmo.pdf`.
- Local PDF: `audit/_mmo_tc_pdfs/e2912b92a11e0f2c.pdf`.
- Local text: `audit/_mmo_tc_text_clean/e2912b92a11e0f2c.txt`.
- Author: А. В. Шаповалов.
- Statement: two firms alternately hire programmers; each firm's next hire must be acquainted with someone already hired by that firm; there are 4 geniuses. Can the acquaintance relation be arranged so the second firm can guarantee at least 3 geniuses?
- Official solution: constructs a graph with four geniuses `G0..G3`, four famous programmers `F0..F3`, and paths between each `Fi` and `Gj` of prescribed lengths. The second firm keeps three target geniuses closer to itself than to the first firm.
- Why graph: acquaintances are an explicit graph in the statement; solution uses paths and distances.
- graph_role: `explicit_statement_application`.
- Tags: `acquaintance_graph`, `positional_game`, `distance_strategy`, `paths`.
- Confidence/status: confirmed, `ai_checked`; `public_ready=false` until permanent source IDs are created.
- TC/base relation: close relative but not duplicate of `data/problems/tournament-cities/tc-2011-programmers-connected-hiring-game.yaml`. The existing TC card/report notes a different parameter version; do not merge automatically.

### MMO 2012, 10 class, problem 6: graph on 3-subsets

- Card: `data/problems/mmo/mmo-2012-three-subsets-coloring.yaml`.
- Main source URL: `http://olympiads.mccme.ru/mmo/2012/75mmo.pdf`.
- Main local PDF: `audit/_mmo_tc_pdfs/f8647446cd0b1f39.pdf`.
- Main local text: `audit/_mmo_tc_text_clean/f8647446cd0b1f39.txt`.
- Statement-only source URL: `http://olympiads.mccme.ru/mmo/2012/10.pdf`.
- Statement-only local PDF: `audit/_mmo_tc_pdfs/56e87746d294196f.pdf`.
- Statement-only local text: `audit/_mmo_tc_text_clean/56e87746d294196f.txt`.
- Author: А. М. Райгородский.
- Statement: graph vertices are all 3-element subsets of `{1,2,...,2k}`; edges join pairs intersecting in exactly one element; find the minimum number of colours for a proper vertex colouring.
- Official solution: answer `(2k-1)(2k-2)/6`. It introduces `G=(V,E)`, chromatic number, maximum independent set size, proves `alpha(G)<=n` for `n=2k`, and gives explicit colourings by induction and by binary-vector coding with sums mod 2.
- Why graph: graph is explicit in the statement and central throughout the official solution.
- graph_role: `explicit_graph_in_statement`.
- Tags: `chromatic_number`, `independent_set`, `set_system_graph`, `kneser_like_graph`.
- Confidence/status: confirmed, `ai_checked`; `public_ready=false` until permanent source IDs are created.
- TC/base relation: no exact TC duplicate found in existing `data/problems/tournament-cities`.

## Source IDs to create later

- `src-mmo-TODO-2008-solutions`: official solutions PDF `http://olympiads.mccme.ru/mmo/2008/solutions.pdf`, local `audit/_mmo_tc_pdfs/85624c5f252bd93c.pdf`.
- `src-mmo-TODO-2010-solutions`: official solutions PDF `http://olympiads.mccme.ru/mmo/2010/solutions.pdf`, local `audit/_mmo_tc_pdfs/41e3aa0f9672ede0.pdf`.
- `src-mmo-TODO-2011-74mmo`: official booklet `http://olympiads.mccme.ru/mmo/2011/74mmo.pdf`, local `audit/_mmo_tc_pdfs/e2912b92a11e0f2c.pdf`.
- `src-mmo-TODO-2012-75mmo`: official booklet `http://olympiads.mccme.ru/mmo/2012/75mmo.pdf`, local `audit/_mmo_tc_pdfs/f8647446cd0b1f39.pdf`.
- Optional supporting source for the 2012 statement-only PDF: `src-mmo-TODO-2012-10-class`, URL `http://olympiads.mccme.ru/mmo/2012/10.pdf`, local `audit/_mmo_tc_pdfs/56e87746d294196f.pdf`.

## Manual-check notes

- The cards intentionally use temporary `src-mmo-TODO-*` IDs because `data/sources/sources.yaml` is outside this agent's write scope.
- No relations were written. Suggested relation work later: connect MMO 2011 firms/programmers as a close variant/relative of the existing TC programmers card, but not as a duplicate.
- The 2008 card is included because the official solution's co-photo degree argument is graph-substantial; if the project requires only explicitly named graphs, mark it for manual review rather than deleting.
- Keyword false positives from function graphs and geometry segments were ignored unless a graph was explicit or official-solution-essential.
