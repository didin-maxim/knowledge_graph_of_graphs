# vosh-1992-zonal-airlines-route-transfer deep audit

Date: 2026-05-05

## Verdict

Classification: `official_complete_or_near_complete`.

The problem has an official/house published solution in the `Kvant` Zadachnik archive: problem `M1367`, `Kvant` 1993, № 9/10, page 31. The solution is complete for the olympiad statement and uses only the elementary two-color alternating-chain exchange.

## Sources Checked

- Primary olympiad statement: `Kvant` 1992, № 10, page image 61, section "XVIII Всероссийская олимпиада по математике"; this is 9th grade, day 2, problem 8, worth 11 points. URL: https://www.kvant.digital/data/kvant_1992_10/jpg/0061.jpg
- `Kvant` 1992 issue metadata and contents: the article is listed as "Яковлев Г. Н. и др. [XVIII Всероссийская олимпиада по математике]" starting on page 60. URL: https://www.kvant.digital/issues/1992/10/
- `Kvant` Zadachnik 1992 № 10 states that problems `M1366`-`M1370` were proposed at the 1992 Vserossiyskaya Olympiad; `M1367` is this airline problem. URL: https://www.kvant.digital/issues/1992/10/zadachnik_kvanta-ddbb1db9/
- Published solution: `Kvant` 1993, № 9/10, page image 31, solution to `M1367`, signed `Б. Кукушкин`. URL: https://www.kvant.digital/data/kvant_1993_9-10/jpg/0031.jpg
- `Kvant` 1993 Zadachnik metadata lists "Решения задач М1366-М1380; Ф1378-Ф1387" on pages 30-47, 50-51. URL: https://www.kvant.digital/issues/1993/9-10/zadachnik_kvanta-43da9194/

## Authorship

The olympiad publication is credited in `Kvant` as "Яковлев Г. Н. и др."; no individual problem proposer is singled out in the checked source. The `M1367` solution page is signed `Б. Кукушкин`, so the card notes him as the author of the published solution, not as the problem author.

## Graph Formulation

The earlier card profile over-read "между городами существует авиационное сообщение" as a connectivity condition. The statement never asks to preserve reachability or connectedness; it asks only to redistribute ownership of existing flights while keeping the local law. The correct graph model is:

Given a loopless multigraph with a proper edge-coloring in `2k+1` colors, where color `i` has exactly `i` edges, recolor the same edge set properly so every color has exactly `k+1` edges.

Parallel edges are allowed in the model because the statement does not forbid two different companies from serving the same pair of cities. Loops are excluded because every flight connects two cities.

## Solution Audit

The published solution chooses an overfull airline `A` and an underfull airline `B`, looks at the two-color subgraph, and uses the fact that every vertex has degree at most 2 in that subgraph. Its components are alternating cycles and chains. Cycles have equal counts of `A` and `B`; since `A` has more edges overall, some chain has one more `A`-edge than `B`-edge. Swapping colors on that chain preserves the law and moves one flight from `A` to `B`. Repetition terminates at the equal distribution.

This is a full proof. It can be described as an edge-coloring Kempe-chain or alternating-path balancing argument. No external theorem such as equitable edge-coloring is needed.

## Internet / Relation Sweep

Searches for exact phrases from the statement and for `М1367` found the `Kvant` Zadachnik entry and its published solution. I did not find a stronger independent online solution archive for this exact problem in the checked results.

Related motifs inside the repository are Kempe-chain recoloring and alternating paths. I did not add a relation file in this pass because the closest internal entries are broader motifs rather than a tight reprint/generalization of this exact airline edge-recoloring problem.

## Risks

- The global source registry was not edited because the allowed file scope excluded `data/sources/sources.yaml`; therefore the 1993 solution source is documented here and in the solution `source_note`, but not as a registered `source_id`.
- The statement/source attribution remains at publication level (`Яковлев Г. Н. и др.`), not individual problem author level.
