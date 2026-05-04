# MMO vs Tournament of Cities local archive overlap

Date: 2026-05-03

Scope:
- Local archive manifest: `audit/mmo-tc-clean-text-manifest.json`
- Local keyword scan: `audit/mmo-tc-keyword-scan.json`
- Existing database cards under `data/problems`
- Existing Tournament of Cities cards under `data/problems/tournament-cities`

## Source inventory

- `mmo`: 171 cleaned PDF/text records.
- `tc`: 127 cleaned PDF/text records from `turgor.ru`.
- `tc-page`: 8 cleaned PDF/text records from modern `tasks.olimpiada.ru` Tournament of Cities pages.

The local `_mmo_tc_*` archive is a mixed corpus. It should be filtered by the manifest field `family`; otherwise Moscow Mathematical Olympiad and Tournament of Cities materials are easy to mix.

## What is already in the database

There is no separate MMO/Moscow Mathematical Olympiad problem folder in `data/problems`, and `data/sources/sources.yaml` currently has no `src-mmo-*` / `mos.olimpiada.ru` / `mccme.ru/mmo` source entries.

Automated near-match comparison of MMO graph-keyword chunks against existing database problem cards found no reliable exact database duplicate.

Closest graph-relevant relative:
- MMO 2011/74th MMO, problem about two firms hiring programmers and geniuses.
- TC 2010/11 card already in database: `tc-2011-programmers-connected-hiring-game`.
- Difference: the MMO statement has 4 geniuses and a different target, while the TC archive version has 11 geniuses and different parameters. Treat as a close relative, not the same card.

## MMO/TC overlaps found in the local text archive

The automated text comparison found 13 near matches between MMO chunks and TC chunks. Most are exact reused problems in the local archive but are not graph cards in the current database.

Notable overlaps:
- MMO 2018/19 9th grade problem on colored chords of a regular 100-gon matches TC 2018/19 spring hard 8-9 solutions.
- MMO 2013/14 9th grade square tablecloth problem matches TC 35 spring hard archive.
- MMO 2013 problem on 1000 alternating colored numbers on a circle matches TC 34 spring hard archive.
- MMO 2018/19 10th grade “worms” from monotone lattice paths matches TC 2018/19 spring hard 10-11 solutions.
- MMO 2018/19 8th grade `n x n` table with consecutive numbers in side-neighbor cells matches TC 2018/19 spring hard 8-9 solutions.
- MMO 2013/14 grasshoppers on 10 marked circle points matches TC 35 spring hard archive.
- MMO 2021/22 spaceship in a half-space matches TC 2021/22 spring hard 10-11 archive.
- MMO 2012 pear pairing problem matches TC 33 spring hard archive.
- MMO 2021/22 rook Hamiltonian walk on an `n x n` board matches TC 2021/22 spring hard 10-11 archive.
- MMO 2011 firms hiring programmers is a close relative of TC 32 spring hard, but not identical.

## MMO graph candidates not matched to reviewed TC cards

These are the main MMO-only graph candidates surfaced by the current scan. They are not yet database cards and need the normal inclusion pass before adding.

- MMO 2012 / 75th MMO: explicit graph on 3-element subsets of `{1, ..., 2k}`, edges between triples intersecting in exactly one element; asks for chromatic number. Source text: `audit/_mmo_tc_text_clean/f8647446cd0b1f39.txt`.
- MMO 2015/16 solutions: linguists/languages reformulated as a subgraph of a Kneser graph; official commentary explicitly uses Kneser graph, independence number, and edge lower bound. Source text: `audit/_mmo_tc_text_clean/8c75a829a791e463.txt`.
- MMO 2010 solutions: point/segment extremal problem; official solution builds a graph whose vertices are marked points and whose edges are drawn segments, then uses independent sets and degree/counting. Source text: `audit/_mmo_tc_text_clean/41e3aa0f9672ede0.txt`.
- MMO 2008 solutions: tournament with 20 athletes and 10 arbiters, photos after each game; likely graph/design interpretation in solution, needs manual extraction. Source text: `audit/_mmo_tc_text_clean/85624c5f252bd93c.txt`.
- MMO 2017/18 9th grade solutions: seating/auditorium acquaintance problem; commentary mentions clique chromatic number of a graph. Source text: `audit/_mmo_tc_text_clean/6fb40982bcbcc4fb.txt`.
- MMO 2020/21 8th grade solutions: state with 32 cities and one-way roads between each pair; explicit tournament/directed complete graph. Source text: `audit/_mmo_tc_text_clean/bb781a139b3d1454.txt`.
- MMO 2023/24 10th grade: hypergraph club / meetings / acquaintance graph problem; explicit hypergraph framing and acquaintance graph relation. Source texts: `audit/_mmo_tc_text_clean/9c3c3a2e4b9dbcbb.txt`, `audit/_mmo_tc_text_clean/6c132d88b67c590f.txt`.

## Manual-check notes

- The keyword scan has many false positives from analytic "graph of a function", "графства", and non-graph uses of "вершина".
- For MMO, source URLs in the manifest are sometimes shortened with `Archive_tasks_2013-...`; use the manifest record and local PDF filename as the stable local source until full source IDs are created.
- Before adding MMO cards, create a separate MMO source namespace and tournament folder, rather than folding them into Tournament of Cities.
