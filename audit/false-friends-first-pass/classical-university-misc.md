# False friends first pass: classical + university/misc

Scope checked: `data/problems/classical`, `data/problems/sums`, `data/problems/imc`, `data/problems/miklos-schweitzer`, `data/problems/mmo`, `data/problems/simon-marais`, `data/problems/vjimc`.

This is a broad low-reasoning filter for future relation type "ложный друг" and refinement "парный вариант". Classifications below are preliminary.

## Classical

| problem id | file | пункты / варианты | preliminary |
|---|---|---|---|
| `balanced-bipartite-edge-coloring-two-colors` | `data/problems/classical/balanced-bipartite-edge-coloring-two-colors.yaml` | Несколько исходных/graph_theory формулировок про разложение/раскраску ребер двудольного графа в два цвета; выглядят как близкие версии одной леммы. | нужно проверить |
| `benjamini-tzalik-shortest-paths-kolmogorov-merged` | `data/problems/classical/benjamini-tzalik-shortest-paths-kolmogorov-merged.yaml` | Две исходные формулировки в одной карточке; возможно объединены разные варианты задачи Колмогорова о кратчайших путях. | нужно проверить |
| `bounded-forward-rays-balanced-sums` | `data/problems/classical/bounded-forward-rays-balanced-sums.yaml` | Несколько формулировок: исходная, graph_theory и olympiad_reformulation; потенциально разные модели одной идеи. | нужно проверить |
| `c4-free-kovari-sos-turan-bound` | `data/problems/classical/c4-free-kovari-sos-turan-bound.yaml` | Оригинальная теорема и олимпиадная переформулировка; выглядит как пара близких экстремальных утверждений. | парный вариант |
| `cayley-prufer-labeled-trees` | `data/problems/classical/cayley-prufer-labeled-trees.yaml` | Формула Кэли и олимпиадная/кодовая формулировка через Прюфера; похожие, но доказательные акценты могут отличаться. | парный вариант |
| `chen-yu-independent-cutset-kolmogorov-merged` | `data/problems/classical/chen-yu-independent-cutset-kolmogorov-merged.yaml` | Две исходные формулировки в одной merged-карточке; возможно самостоятельные близкие утверждения. | нужно проверить |
| `color-reduction-by-odd-deletion-and-doubling` | `data/problems/classical/color-reduction-by-odd-deletion-and-doubling.yaml` | В условии явно две разрешенные операции: удалить вершину нечетной степени; заменить граф двумя копиями и добавить соответствующие ребра. | нужно проверить |
| `degeneracy-greedy-coloring` | `data/problems/classical/degeneracy-greedy-coloring.yaml` | Классическая формулировка и олимпиадная переформулировка про жадную раскраску/вырожденность. | парный вариант |
| `erdos-gallai-path-edge-bound` | `data/problems/classical/erdos-gallai-path-edge-bound.yaml` | Оригинальная теорема и олимпиадная формулировка про число ребер без длинного пути. | парный вариант |
| `euler-trail-extension-center-forest` | `data/problems/classical/euler-trail-extension-center-forest.yaml` | В условии есть эквивалентность: продолжимость любого пути из `c` до эйлерова цикла iff `G-c` лес; эквивалентно, каждый цикл содержит `c`; плюс олимпиадная версия. | ложный друг |
| `eulerian-graph-criterion` | `data/problems/classical/eulerian-graph-criterion.yaml` | Три формулировки критерия эйлеровости/обхода всех ребер; близкие, но могут требовать разных деталей связности и четности. | парный вариант |
| `five-color-theorem` | `data/problems/classical/five-color-theorem.yaml` | Теорема о пяти красках и олимпиадная переформулировка для планарных карт/графов. | парный вариант |
| `flashlight-batteries-tournament-cities-2015` | `data/problems/classical/flashlight-batteries-tournament-cities-2015.yaml` | Явные два варианта с батарейками: `2n+1` батареек, хороших на одну больше; `2n` батареек, хороших и плохих поровну. Также две graph_theory формулировки. | ложный друг |
| `gallai-hasse-roy-vitaver-theorem` | `data/problems/classical/gallai-hasse-roy-vitaver-theorem.yaml` | Внутри утверждения две стороны равенства: в любой ориентации есть длинный ориентированный путь; существует ориентация с верхней границей на длину пути. | ложный друг |
| `hall-marriage-theorem` | `data/problems/classical/hall-marriage-theorem.yaml` | Несколько эквивалентных формулировок: набор множеств/SDR, двудольный граф, юноши-девушки, списки девушек. | парный вариант |
| `havel-hakimi-graphical-degree-sequence` | `data/problems/classical/havel-hakimi-graphical-degree-sequence.yaml` | Критерий Хавела-Хакими и олимпиадная переформулировка; похожие, но возможны разные алгоритмические/индукционные акценты. | парный вариант |
| `konig-line-coloring-bipartite` | `data/problems/classical/konig-line-coloring-bipartite.yaml` | Теорема о реберной раскраске двудольного графа и олимпиадная формулировка. | парный вариант |
| `line-arrangement-side-count-levels` | `data/problems/classical/line-arrangement-side-count-levels.yaml` | Явные пункты: (1) соседние области имеют значения `k`, отличающиеся на 1; (2) для каждого `k=0..n` существует область с таким значением. | ложный друг |
| `minimal-half-subset-exchange-lemma` | `data/problems/classical/minimal-half-subset-exchange-lemma.yaml` | Основное неравенство для обмена `r in S`, `b notin S`; затем "в частности" две близкие версии: без ребра/с ребром `br`. | нужно проверить |
| `no-two-color-cycle-edge-bound` | `data/problems/classical/no-two-color-cycle-edge-bound.yaml` | Две самостоятельные ступени: каждый двухцветный индуцированный подграф `G_ij` лес; затем суммарная оценка на число ребер. | парный вариант |
| `planar-edge-bound` | `data/problems/classical/planar-edge-bound.yaml` | Две почти одинаковые формулировки оценки `e <= 3n-6` / `e(G) <= 3v(G)-6`. | парный вариант |
| `ramsey-r33` | `data/problems/classical/ramsey-r33.yaml` | Несколько эквивалентных формулировок Ramsey `R(3,3)=6`: раскраска ребер, граф/дополнение, люди. | парный вариант |
| `ramsey-r34` | `data/problems/classical/ramsey-r34.yaml` | Несколько формулировок `R(3,4)=9`; также включает положительное утверждение для `K_9` и отрицательное для `K_8`. | ложный друг |
| `ramsey-r35` | `data/problems/classical/ramsey-r35.yaml` | Несколько формулировок `R(3,5)=14`; включает положительное утверждение для `K_14` и контрпример/отрицание для `K_13`. | ложный друг |
| `ramsey-r44` | `data/problems/classical/ramsey-r44.yaml` | Несколько формулировок `R(4,4)=18`; вероятно положительная и нижняя оценка/контрпример. | ложный друг |
| `tree-equivalent-properties` | `data/problems/classical/tree-equivalent-properties.yaml` | Набор эквивалентных свойств дерева: связность+ацикличность; связность+`n-1` ребро; единственный простой путь между любыми двумя вершинами. | ложный друг |
| `turan-theorem` | `data/problems/classical/turan-theorem.yaml` | Теорема Турана и несколько олимпиадных переформулировок, включая комплементарную задачу с запретом антиклики. | ложный друг |

## SUMS

| problem id | file | пункты / варианты | preliminary |
|---|---|---|---|
| `sums-2011-p8-periodic-hexagon-tessellation-even-vertices` | `data/problems/sums/sums-2011-p8-periodic-hexagon-tessellation-even-vertices.yaml` | Оригинальная геометрическая формулировка и graph_theory-перевод про периодическую тесселяцию/граф. | нужно проверить |
| `sums-2012-p7-tree-connected-subsets-extrema` | `data/problems/sums/sums-2012-p7-tree-connected-subsets-extrema.yaml` | Требуется найти минимум и максимум числа связных непустых подмножеств вершин дерева. | ложный друг |

## IMC

| problem id | file | пункты / варианты | preliminary |
|---|---|---|---|
| `imc-1997-day1-p6-intersecting-families-finite-transversal` | `data/problems/imc/imc-1997-day1-p6-intersecting-families-finite-transversal.yaml` | Явные пункты: (a) существование конечного `Y` для попарно пересекающегося семейства; (b) тот же вопрос при равномерности семейств. | ложный друг |
| `imc-2001-day2-p4-zero-principal-minors-acyclic-digraph` | `data/problems/imc/imc-2001-day2-p4-zero-principal-minors-acyclic-digraph.yaml` | Два вывода из условия о нулевых главных минорах: доказать `A^n=0`; найти перестановку, делающую матрицу верхнетреугольной с нулевой диагональю. | ложный друг |
| `imc-2003-day2-p4-steiner-triples-elementary-abelian-2-group` | `data/problems/imc/imc-2003-day2-p4-steiner-triples-elementary-abelian-2-group.yaml` | Два условия на систему троек: каждая пара лежит ровно в одной тройке; дополнительное замыкание для третьих вершин. | нужно проверить |
| `imc-2006-day2-p1-polygon-triangulation-parity` | `data/problems/imc/imc-2006-day2-p1-polygon-triangulation-parity.yaml` | Явные пункты: (a) случай `3 | n`, все вершины нечетной инцидентности; (b) случай `3 ∤ n`, ровно две вершины четной инцидентности. | ложный друг |
| `imc-2011-day2-p2-tripartite-married-triples` | `data/problems/imc/imc-2011-day2-p2-tripartite-married-triples.yaml` | Явные пункты: (a) при четном `n`, `k=n/2` может не быть ни одной тройки; (b) при `k >= 3n/4` всегда есть совершенное покрытие треугольниками. | ложный друг |
| `imc-2024-day2-p9-young-tableaux-friend-graph` | `data/problems/imc/imc-2024-day2-p9-young-tableaux-friend-graph.yaml` | Определение nice-матрицы содержит четыре условия (i)-(iv); решение/переформулировка через граф таблиц Юнга и вершины нечетной степени. | нужно проверить |

## Miklos-Schweitzer

| problem id | file | пункты / варианты | preliminary |
|---|---|---|---|
| `miklos-schweitzer-1959-p10-even-circuit-edge-bound` | `data/problems/miklos-schweitzer/miklos-schweitzer-1959-p10-even-circuit-edge-bound.yaml` | Условие/решение выглядит как оценка для графов без четных циклов плюс graph_theory-переформулировка; в кандидат попало из-за явно разных случаев/вариантов в тексте. | нужно проверить |
| `miklos-schweitzer-2009-p2-smooth-difference-graphs` | `data/problems/miklos-schweitzer/miklos-schweitzer-2009-p2-smooth-difference-graphs.yaml` | Явные подпункты: для каждого `m` реализовать (i) полный граф; (ii) связный граф со степенями не больше 2 в графе разностей. | ложный друг |
| `miklos-schweitzer-2012-p10-knot-black-graph-spanning-trees` | `data/problems/miklos-schweitzer/miklos-schweitzer-2012-p10-knot-black-graph-spanning-trees.yaml` | Явные пункты: (a) классификация узлов с диаграммой, где черный граф имеет не более 3 остовных деревьев; (b) нечетность числа остовных деревьев для любого узла/диаграммы. | ложный друг |
| `miklos-schweitzer-2024-p1-bipartite-perfect-matching-edge-weights` | `data/problems/miklos-schweitzer/miklos-schweitzer-2024-p1-bipartite-perfect-matching-edge-weights.yaml` | Два требования к одной инъективной весовой функции: минимальные ребра у вершин доли `S` образуют совершенное паросочетание; максимальные ребра у вершин доли `T` тоже образуют совершенное паросочетание. | ложный друг |

## MMO

| problem id | file | пункты / варианты | preliminary |
|---|---|---|---|
| `mmo-2018-acquaintance-seating-clique-chromatic` | `data/problems/mmo/mmo-2018-acquaintance-seating-clique-chromatic.yaml` | Оригинальная олимпиадная формулировка про рассадку и graph_theory-формулировка через раскраску графа без монохроматического максимального клика. | парный вариант |

## Simon Marais

| problem id | file | пункты / варианты | preliminary |
|---|---|---|---|
| `simon-marais-2020-b4-rainbow-distance-clique-polygon` | `data/problems/simon-marais/simon-marais-2020-b4-rainbow-distance-clique-polygon.yaml` | Явные пункты: (a) доказать натянутость при простом `n-1`; (b) определить все натянутые `n`. | ложный друг |
| `simon-marais-2025-b1-beaut-functions-gcd-graph` | `data/problems/simon-marais/simon-marais-2025-b1-beaut-functions-gcd-graph.yaml` | Исходная задача про beaut-функции для всех `m` и graph_theory-формулировка как списочная раскраска графа по `gcd`; похоже на парную модель, но может скрывать разные идеи. | нужно проверить |

## VJIMC

| problem id | file | пункты / варианты | preliminary |
|---|---|---|---|
| `vjimc-2009-cat1-p3-partial-hypergraph-bicoloring` | `data/problems/vjimc/vjimc-2009-cat1-p3-partial-hypergraph-bicoloring.yaml` | Условие требует раскраску с несколькими самостоятельными требованиями: элемент не раскрашен/красный/синий; хотя бы один раскрашен; каждое `A_i` либо полностью не раскрашено, либо содержит оба цвета. | нужно проверить |
| `vjimc-2009-cat2-p4-transversal-hypergraph-polynomial-bound` | `data/problems/vjimc/vjimc-2009-cat2-p4-transversal-hypergraph-polynomial-bound.yaml` | В тексте есть несколько вариантов/случаев для гиперграфовой оценки; нужен ручной просмотр, попало как широкий кандидат. | нужно проверить |
| `vjimc-2017-cat1-p3-polyhedron-edge-products` | `data/problems/vjimc/vjimc-2017-cat1-p3-polyhedron-edge-products.yaml` | В условии/решении есть несколько самостоятельных условий на произведения/метки ребер многогранника; потенциально разные проверки. | нужно проверить |
| `vjimc-2022-cat1-p4-stone-game-state-graph` | `data/problems/vjimc/vjimc-2022-cat1-p4-stone-game-state-graph.yaml` | Игра с двумя типами хода: удалить три камня одного цвета; заменить два камня разных цветов двумя камнями третьего цвета. Возможны разные инварианты для ходов. | нужно проверить |

