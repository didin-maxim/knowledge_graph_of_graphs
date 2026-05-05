# vosh-1992-zonal-air-travel-one-city-redundant deep audit

Date: 2026-05-05

## Verdict

Classification: `unofficial_published`.

The primary `Kvant` source gives the statement and article authors, but I did not find an official olympiad solution. A complete short published solution exists in N. V. Gorbachev's 2004 collection, problem `6.15 (ВО 92)`, so the card should not be `no_solution_hard`.

## Sources Checked

- Primary statement: `Kvant` 1992, № 10, page image 61, section "XVIII Всероссийская олимпиада по математике"; this is 11th grade, first day, problem 3, worth 8 points. URL: https://www.kvant.digital/data/kvant_1992_10/jpg/0061.jpg
- `Kvant` issue/article metadata: the article is listed as "Яковлев Г. Н. и др. [XVIII Всероссийская олимпиада по математике]", pages 60-62, with authors Г. Н. Яковлев, А. Б. Куперман, Л. Г. Ковалёва, О. Р. Зурабов, П. И. Городецкий, М. В. Кабанова, Г. А. Аматуни. URL: https://www.kvant.digital/issues/1992/10/yakovlev-xviii_vserossiyskaya_olimpiada_po_matematike-b6a0a3e4/
- Issue landing page for `Kvant` 1992 № 10. URL: https://www.kvant.digital/issues/1992/10/
- VMO/MCCME prize page: records the historical status of the 1992 Vserossiyskaya Olympiad as the then-penultimate stage before the Interrepublican Olympiad. URL: https://olympiads.mccme.ru/vmo/prisery.htm
- Published solution: Н. В. Горбачёв, "Сборник олимпиадных задач по математике", 2004, OCR access copy; problem `6.15 (ВО 92)` and its solution. URL: https://djvu.online/file/5Gmg79HRXJzLC
- Exact-phrase internet searches for the statement also found a MalMehmat problem-list mirror, but not a stronger official source or independent solution archive.

## Authorship

The checked `Kvant` metadata gives publication authors, not an individual proposer for this problem. The card therefore records the full article-author list with a note that the proposer was not found, rather than inferring authorship from the publication.

## Statement Check

The scanned statement says: "В стране несколько городов. Между некоторыми из них в одном направлении летают самолеты." The card was corrected to include "между некоторыми из них"; without this phrase the statement could be misread as a complete tournament, which would make the premise incompatible with the standard tournament mother-vertex lemma.

The rest of the statement matches the card: there is a city from which not every city can be visited by successive flights, and one must prove that a nonempty part can separate so that no separated city is reachable from any remaining city.

## Graph Formulation

The correct graph formulation is:

In a finite directed graph there is a vertex from which not all vertices are reachable. Prove that there is a nonempty proper set \(S\subset V\) with no edge from \(V\setminus S\) into \(S\).

This is equivalent to the original statement if cities are vertices and one-way flights are directed edges. Choosing \(S\) as the set of vertices unreachable from the specified vertex makes \(S\) nonempty and proper. If an edge entered \(S\) from outside, its tail would be reachable from the chosen vertex and then its head would be reachable too, contradiction. A multi-step route from the complement into \(S\) is also impossible, because its first entering edge would already contradict the no-incoming-edge property.

## Solution Audit

Gorbachev's published solution uses exactly the unreachable-city set. The local solution is a self-contained adaptation and spells out the final "no route, not just no direct flight" step, which is implicit but elementary.

No heavy theorem is needed. This is a one-lemma reachability argument suitable for school olympiad level.

## Relations

Added a relation to `baltic-way-1992-p14-mother-vertex-reachability`. The link is not a reprint: Baltic Way assumes pairwise reachability comparability and proves a mother vertex exists. The present VOSH card isolates the complementary cut lemma; it can be used as an alternative proof tool for Baltic Way, but the statements are not identical.

## Risks

- No official solution source was found; classification is `unofficial_published`, not official.
- The Gorbachev source is not registered in `data/sources/sources.yaml` because this pass stayed within the requested one-card/deep-note/relation-file scope.
- `public_ready` remains `false` because the solution source is documented in the audit note and `source_note`, not as a registered source id.
