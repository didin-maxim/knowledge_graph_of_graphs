# vosh-1991-zonal-one-way-streets-return

Deep pass date: 2026-05-05

## Source Check

Primary source: Kvant Digital, Агаханов Н. Х., Купцов Л. П., Резниченко С. В., "[XVII Всероссийская олимпиада школьников по математике]", Квант, 1991, N 10, pp. 57-58.

Checked URLs:

- https://www.kvant.digital/issues/1991/10/agahanov_kuptsov_reznichenko-xvii_vserossiyskaya_olimpiada_shkolnikov_po_matematike-7e28f95c/
- https://www.kvant.digital/data/kvant_1991_10/jpg/0057.jpg
- https://www.kvant.digital/data/kvant_1991_10/jpg/0058.jpg

The statement is on page image 57, in the 10th grade section, first day, problem 3, worth 10 points. The statement in the card matches the source text. Page 58 continues the problem list and names "Публикацию подготовили Н. Агаханов, Л. Купцов, С. Резниченко"; it does not identify an individual proposer for this problem.

## Published Solution Search

Searched exact and near-exact Russian phrases, including:

- "Город в форме многоугольника" "квартал" "одностороннее движение"
- "На каждой улице введено одностороннее движение" "можно приехать" "можно уехать"
- "в городе имеется квартал" "можно объехать" "улицам"
- "весь город можно объехать вдоль его границы" "квартал"

No official, forum, book, or other published solution was found in accessible web results. Kvant Digital provides article images/PDF only and no text solution layer for this article.

## Graph Formulation Audit

The previous graph formulation said that every vertex has positive internal indegree and internal outdegree. That is stronger than the original and not equivalent for boundary vertices: in the city statement, "на каждую площадь можно приехать" and "с каждой площади можно уехать" refer to all streets incident to the square, including boundary streets.

Updated formulation:

- finite connected plane directed graph embedded in a disk as a polygonal subdivision;
- the outer boundary is an oriented simple cycle;
- every vertex has positive total indegree and positive total outdegree;
- prove that a bounded face has directed boundary.

The polygonal-subdivision language is intentional: the AI proof uses that a nonempty component strictly inside a simple cycle cannot be attached to that cycle in only one vertex, otherwise some block boundary would repeat a vertex and would not be a polygon.

## Solution Classification

Classification set to:

```json
{
  "type": "ai_original",
  "label": "ИИ-решение с нуля"
}
```

Reason: no published solution was found, but a self-contained school-level proof was added. The proof chooses a directed cycle with minimal number of blocks inside. If it is not a block boundary, the graph remaining inside it has no directed cycle and no directed path between two distinct boundary vertices, otherwise a smaller directed cycle appears. A connected internal component is acyclic, so it has a source and a sink; internal sources/sinks contradict the original in/out conditions, hence a directed path must run between two distinct vertices of the chosen cycle, contradiction.

## Residual Risks

- The solution is AI-authored, not source-published.
- The topological step depends on interpreting "кварталы-многоугольники" as simple polygonal faces. This matches the wording but is still the most delicate part of the proof.
- The source confirms publication authors/preparers only; no individual proposer is known.
