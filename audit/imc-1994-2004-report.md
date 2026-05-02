# IMC 1994-2004: графовые задачи

Дата аудита: 2026-05-02.

## Созданные карточки

- `data/problems/imc/imc-1997-day1-p6-intersecting-families-finite-transversal.yaml`
  - `source_id`: `src-imc-1997-day1-p6-official`
  - официальный URL: https://www.homepages.ucl.ac.uk/~ucahjej/imc/imc1997/prob_sol1.pdf
  - модель: попарно пересекающееся семейство как конечный гиперграф; в равномерном случае доказывается конечный носитель всех попарных пересечений.

- `data/problems/imc/imc-1999-day1-p5-marked-grid-cycle.yaml`
  - `source_id`: `src-imc-1999-day1-p5-official`
  - официальный URL: https://www.homepages.ucl.ac.uk/~ucahjej/imc/imc1999/prob_sol1.pdf
  - модель: двудольный граф строк и столбцов; отмеченные клетки - ребра; цикл дает требуемую чередующуюся последовательность точек.

- `data/problems/imc/imc-2001-day2-p4-zero-principal-minors-acyclic-digraph.yaml`
  - `source_id`: `src-imc-2001-day2-p4-official`
  - официальный URL: https://www.homepages.ucl.ac.uk/~ucahjej/imc/imc2001/prob_sol2.pdf
  - модель: ориентированный граф ненулевых элементов матрицы; нулевые главные миноры исключают ориентированные циклы; топологический порядок дает строго верхнетреугольный вид.

- `data/problems/imc/imc-2002-day2-p2-students-problems-dominating-pair.yaml`
  - `source_id`: `src-imc-2002-day2-p2-official`
  - официальный URL: https://www.homepages.ucl.ac.uk/~ucahjej/imc/imc2002/prob_sol2.pdf
  - модель: двудольный граф студентов и задач; требуется пара вершин-студентов, покрывающая все вершины-задачи.

- `data/problems/imc/imc-2003-day2-p4-steiner-triples-elementary-abelian-2-group.yaml`
  - `source_id`: `src-imc-2003-day2-p4-official`
  - официальный URL: https://www.ucl.ac.uk/~ucahjej/imc/imc2003/day2_solutions.pdf
  - модель: 3-однородный гиперграф/система троек Штейнера с правилом замыкания; решение алгебраизует тройки в элементарную абелеву 2-группу.

## Исключенные пограничные задачи

- IMC 2001 Day 1 P1, официальный URL: https://www.homepages.ucl.ac.uk/~ucahjej/imc/imc2001/prob_sol1.pdf. Не добавлена: выбор одной клетки в каждой строке и каждом столбце можно назвать совершенным паросочетанием в `K_{n,n}`, но сумма сразу вычисляется из перестановки, и графовая модель не несет решения.

- IMC 2004 Day 1 P4, официальный URL: https://www.homepages.ucl.ac.uk/~ucahjej/imc/imc2004/day1_solutions.pdf. Не добавлена: можно формально рассматривать гиперграф подмножеств точек, лежащих на одной сфере, но официальное решение является геометрическим подсчетом по сферам через функцию окраски; графовая оболочка выглядит искусственной.

## Идеи для родственных связей

- `imc-1999-day1-p5-marked-grid-cycle` связать с карточками про двудольные модели решеток и циклы: например `bmo-2022-p4-frog-grid-boundary-graph`, `usamo-1999-p1-checkers-board-graph-rank`, а также с классическими карточками про оценку ребер в лесу.

- `imc-2001-day2-p4-zero-principal-minors-acyclic-digraph` связать с задачами про ориентированные ациклические графы, топологический порядок и нильпотентность по носителю матрицы; потенциально близко к `classical/digraph-outdegree-greedy-coloring-bound.yaml` только по ориентированному графовому языку.

- `imc-2002-day2-p2-students-problems-dominating-pair` связать с задачами на двудольную инцидентность, покрытие соседств и подсчет плохих пар; возможна слабая связь с `usa-tst-2005-p1-set-system-incidence-graph.yaml`.

- `imc-2003-day2-p4-steiner-triples-elementary-abelian-2-group` связать с будущими карточками про системы троек Штейнера, булевы группы и XOR-конструкции; в текущей базе прямой связи может не быть, поэтому лучше пометить как отдельный кластер гиперграфов/дизайнов.

- `imc-1997-day1-p6-intersecting-families-finite-transversal` связать с задачами про гиперграфы, трансверсали и пересекающиеся семейства; если появятся карточки Эрдеша-Ко-Радо или конечных hitting set-лемм, связь будет естественной.
