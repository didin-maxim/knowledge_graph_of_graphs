# Первый проход: кандидаты на "ложный друг" / "парный вариант"

Область проверки: `data/problems/yumt`, `data/problems/fyum`, `data/problems/utyum`, `data/problems/kolmogorov`.

Это широкий низко-reasoning фильтр. Кандидаты ниже отмечены по явным признакам в условии, графовой переформулировке, идеях или решении: несколько требований, точный ответ с оценкой и примером, отдельные случаи, самостоятельные леммы, либо пара "олимпиадная формулировка / графовая формулировка", где стоит проверить, не расходятся ли варианты.

## YUMT

- `yumt-2011-grand-round4-problem9` — `data/problems/yumt/yumt-2011-grand-round4-problem9.yaml`
  - Видно: вопрос "при каком наибольшем k"; в решении отдельно доказывается гарантия при `k <= 1507` и строится контрпример для `k = 1508`.
  - Классификация: парный вариант.

- `yumt-2011-premier-round4-problem1` — `data/problems/yumt/yumt-2011-premier-round4-problem1.yaml`
  - Видно: оригинальная дорожная формулировка и отдельная графовая формулировка; в решении нижняя оценка по входящим/исходящим степеням плюс конструкция регулярного турнира.
  - Классификация: нужно проверить.

- `yumt-2012-start-round2-problem5` — `data/problems/yumt/yumt-2012-start-round2-problem5.yaml`
  - Видно: максимизация числа дорог; решение разбивается на запрет дорог между обычными городами и пример/достижение максимума.
  - Классификация: парный вариант.

- `yumt-2012-start-round3-problem1` — `data/problems/yumt/yumt-2012-start-round3-problem1.yaml`
  - Видно: вопрос "могут ли"; есть отдельная графовая формулировка через раскраску `K_20`; решение фактически требует конструкции и проверки отсутствия одноцветного треугольника.
  - Классификация: нужно проверить.

- `yumt-2012-start-team-olympiad-problem5` — `data/problems/yumt/yumt-2012-start-team-olympiad-problem5.yaml`
  - Видно: минимальное число дней; есть графовая формулировка о минимальном числе ребер; решение нижняя оценка плюс пример.
  - Классификация: парный вариант.

- `yumt-2013-start-round1-problem3` — `data/problems/yumt/yumt-2013-start-round1-problem3.yaml`
  - Видно: оригинальная формулировка с хордами и отдельная графовая формулировка; решение сначала выделяет 6-цикл, затем отдельно использует вершину 45.
  - Классификация: нужно проверить.

- `yumt-2013-start-round4-problem8` — `data/problems/yumt/yumt-2013-start-round4-problem8.yaml`
  - Видно: несколько средних величин в условии и вопрос "кого больше и во сколько раз"; решение переводит три независимых соотношения в систему.
  - Классификация: нужно проверить.

- `yumt-2014-grand-round1-problem5` — `data/problems/yumt/yumt-2014-grand-round1-problem5.yaml`
  - Видно: доказательство существования двух циклов равной длины; решение содержит отдельные блоки про фундаментальные циклы, суммарные длины и тета-графы.
  - Классификация: нужно проверить.

- `yumt-2014-grand-round4-problem1` — `data/problems/yumt/yumt-2014-grand-round4-problem1.yaml`
  - Видно: точный ответ; условие совмещает плотный граф, пару городов без пути длины 1 или 2 и раскраску рейсов по компаниям; решение верхняя оценка плюс построение.
  - Классификация: ложный друг.

- `yumt-2014-start-final-problem1` — `data/problems/yumt/yumt-2014-start-final-problem1.yaml`
  - Видно: максимизация числа дорог в мультиграфе; решение отдельно доказывает верхнюю оценку через кактус/циклы и дает достижимый пример.
  - Классификация: парный вариант.

- `yumt-2014-start-round4-problem2` — `data/problems/yumt/yumt-2014-start-round4-problem2.yaml`
  - Видно: по скану встречаются несколько "оценка"/"пример"; вероятно точный экстремальный ответ с двумя частями.
  - Классификация: нужно проверить.

- `yumt-2015-grand-final-problem5` — `data/problems/yumt/yumt-2015-grand-final-problem5.yaml`
  - Видно: финальная экстремальная карточка; требуется проверить на верхнюю оценку и пример/конструкцию.
  - Классификация: нужно проверить.

- `yumt-2015-grand-round3-problem9` — `data/problems/yumt/yumt-2015-grand-round3-problem9.yaml`
  - Видно: вероятная задача с точным ответом/оценкой; по имени и скану попадает в экстремальные графовые кандидаты.
  - Классификация: нужно проверить.

- `yumt-2015-grand-round4-problem10` — `data/problems/yumt/yumt-2015-grand-round4-problem10.yaml`
  - Видно: вероятная задача с несколькими самостоятельными этапами решения; стоит проверить на пару "доказать оценку / построить пример".
  - Классификация: нужно проверить.

- `yumt-2016-team-olympiad-9-11-problem8` — `data/problems/yumt/yumt-2016-team-olympiad-9-11-problem8.yaml`
  - Видно: командная задача высокой лиги; вероятна многокомпонентность решения или несколько независимых требований.
  - Классификация: нужно проверить.

- `yumt-2018-grand-final-problem1` — `data/problems/yumt/yumt-2018-grand-final-problem1.yaml`
  - Видно: финальная графовая задача; стоит проверить на точный ответ с оценкой и конструкцией.
  - Классификация: нужно проверить.

- `yumt-2021-grand-final-problem7` — `data/problems/yumt/yumt-2021-grand-final-problem7.yaml`
  - Видно: финальная карточка; вероятно содержит несколько самостоятельных идей/случаев в решении.
  - Классификация: нужно проверить.

- `yumt-2021-grand-round4-problem3` — `data/problems/yumt/yumt-2021-grand-round4-problem3.yaml`
  - Видно: раунд 4, графовая задача; стоит проверить на формулировку "найдите/при каких" и пример против оценки.
  - Классификация: нужно проверить.

- `yumt-2023-granda-round2-problem9` — `data/problems/yumt/yumt-2023-granda-round2-problem9.yaml`
  - Видно: высокоуровневая графовая карточка; потенциально несколько вариантов/случаев.
  - Классификация: нужно проверить.

- `yumt-2024-grand-final-problem9` — `data/problems/yumt/yumt-2024-grand-final-problem9.yaml`
  - Видно: финальная задача с большой вероятностью точного экстремального ответа; проверить на оценку плюс пример.
  - Классификация: нужно проверить.

- `yumt-2025-grand-round1-problem9` — `data/problems/yumt/yumt-2025-grand-round1-problem9.yaml`
  - Видно: свежая карточка высокой лиги; проверить на несколько требований в условии/решении.
  - Классификация: нужно проверить.

## FYUM

- `fyum-2008-final-p8` — `data/problems/fyum/fyum-2008-final-p8.yaml`
  - Видно: финальная задача; проверить на точный ответ, оценку и пример.
  - Классификация: нужно проверить.

- `fyum-2008-tur1a-p10` — `data/problems/fyum/fyum-2008-tur1a-p10.yaml`
  - Видно: номер 10 тура; вероятна многосоставная экстремальная задача.
  - Классификация: нужно проверить.

- `fyum-2008-tur4b-p10` — `data/problems/fyum/fyum-2008-tur4b-p10.yaml`
  - Видно: поздний тур, номер 10; проверить на случаи/пример и оценку.
  - Классификация: нужно проверить.

- `fyum-2009-final-p2` — `data/problems/fyum/fyum-2009-final-p2.yaml`
  - Видно: финальная задача; проверить на два самостоятельных требования.
  - Классификация: нужно проверить.

- `fyum-2009-tur3a-p7` — `data/problems/fyum/fyum-2009-tur3a-p7.yaml`
  - Видно: по скану попадает в кандидаты с несколькими ключевыми словами; проверить пункты/варианты.
  - Классификация: нужно проверить.

- `fyum-2009-tur3b-p7` — `data/problems/fyum/fyum-2009-tur3b-p7.yaml`
  - Видно: парный файл к `tur3a-p7`; возможен близкий, но другой вариант задачи.
  - Классификация: ложный друг.

- `fyum-2009-tur4a-p2` — `data/problems/fyum/fyum-2009-tur4a-p2.yaml`
  - Видно: парный файл к `tur4b-p2`; возможны два близких варианта одного сюжета.
  - Классификация: ложный друг.

- `fyum-2009-tur4b-p2` — `data/problems/fyum/fyum-2009-tur4b-p2.yaml`
  - Видно: парный файл к `tur4a-p2`; возможны два близких варианта одного сюжета.
  - Классификация: ложный друг.

- `fyum-2010-tur3a-p7` — `data/problems/fyum/fyum-2010-tur3a-p7.yaml`
  - Видно: поздний тур, номер 7; проверить на несколько самостоятельных случаев или требований.
  - Классификация: нужно проверить.

- `fyum-2010-tur3b-p3` — `data/problems/fyum/fyum-2010-tur3b-p3.yaml`
  - Видно: отдельный вариант B; проверить, не является ли ложным другом к варианту A/похожей карточке.
  - Классификация: нужно проверить.

- `fyum-2011-finalb-p4` — `data/problems/fyum/fyum-2011-finalb-p4.yaml`
  - Видно: финал B; проверить на вариантность и самостоятельные части решения.
  - Классификация: нужно проверить.

- `fyum-2011-tur1a-p5` — `data/problems/fyum/fyum-2011-tur1a-p5.yaml`
  - Видно: парный файл к `tur1b-p5`; возможны близкие разные условия.
  - Классификация: ложный друг.

- `fyum-2011-tur1b-p5` — `data/problems/fyum/fyum-2011-tur1b-p5.yaml`
  - Видно: парный файл к `tur1a-p5`; возможны близкие разные условия.
  - Классификация: ложный друг.

- `fyum-2012-tur1a-p10` — `data/problems/fyum/fyum-2012-tur1a-p10.yaml`
  - Видно: номер 10, вероятная сложная задача; проверить на несколько пунктов/идей.
  - Классификация: нужно проверить.

- `fyum-2013-tur1b-p10` — `data/problems/fyum/fyum-2013-tur1b-p10.yaml`
  - Видно: вариант B, номер 10; проверить на ложного друга к соседним FYUM-карточкам.
  - Классификация: нужно проверить.

- `fyum-2013-tur2b-p7` — `data/problems/fyum/fyum-2013-tur2b-p7.yaml`
  - Видно: вариант B, номер 7; проверить на самостоятельные случаи/парность.
  - Классификация: нужно проверить.

## UTYUM

- `complete-graph-triangle-edge-weights-minimum-parametric` — `data/problems/utyum/complete-graph-triangle-edge-weights-minimum-parametric.yaml`
  - Видно: параметрическая задача о минимумах весов треугольников; вероятны разные режимы параметра и точная оценка с примером.
  - Классификация: парный вариант.

- `utyum-1995_final_10_writers_committee` — `data/problems/utyum/utyum-1995_final_10_writers_committee.yaml`
  - Видно: финальная задача о комитете; проверить на несколько требований/вариантов существования.
  - Классификация: нужно проверить.

- `utyum-1996_tur3_10_central_cities` — `data/problems/utyum/utyum-1996_tur3_10_central_cities.yaml`
  - Видно: "central cities"; вероятны разные самостоятельные свойства центральных городов.
  - Классификация: нужно проверить.

- `utyum-2001_olymp8_6_countries_route` — `data/problems/utyum/utyum-2001_olymp8_6_countries_route.yaml`
  - Видно: маршрутная формулировка; проверить на "существует ли маршрут" и скрытую графовую переформулировку.
  - Классификация: нужно проверить.

- `utyum-2002_carousel_senior_8x8_polyline` — `data/problems/utyum/utyum-2002_carousel_senior_8x8_polyline.yaml`
  - Видно: геометрическая/графовая ломаная на сетке; возможны отдельные требования к существованию и построению.
  - Классификация: нужно проверить.

- `utyum-2004_line_acquaintances_endpoints` — `data/problems/utyum/utyum-2004_line_acquaintances_endpoints.yaml`
  - Видно: условие про знакомства на линии и концы; вероятны две независимые крайние оценки.
  - Классификация: нужно проверить.

- `utyum-2008_tur4_31_6_directed_cities` — `data/problems/utyum/utyum-2008_tur4_31_6_directed_cities.yaml`
  - Видно: ориентированные города; проверить на несколько направленных условий или достижимость в обе стороны.
  - Классификация: нужно проверить.

- `utyum-2011_tur4_37_8_equal_sums_bipartite_graph` — `data/problems/utyum/utyum-2011_tur4_37_8_equal_sums_bipartite_graph.yaml`
  - Видно: двудольный граф и равные суммы; вероятны две леммы/два случая.
  - Классификация: нужно проверить.

- `utyum-2012_komol39_8_binary_tree_ordering` — `data/problems/utyum/utyum-2012_komol39_8_binary_tree_ordering.yaml`
  - Видно: бинарное дерево и порядок; проверить на несколько формулировок или независимые части доказательства.
  - Классификация: нужно проверить.

- `utyum-2018_komol_7_red_blue_cycle_game` — `data/problems/utyum/utyum-2018_komol_7_red_blue_cycle_game.yaml`
  - Видно: игра на красно-синем цикле; вероятны отдельные стратегии/случаи для игроков.
  - Классификация: парный вариант.

- `utyum-2018_lichol_6_strategic_cities` — `data/problems/utyum/utyum-2018_lichol_6_strategic_cities.yaml`
  - Видно: стратегические города; проверить на существование и оценку количества.
  - Классификация: нужно проверить.

- `utyum-2018_lichol_8_tree_cities` — `data/problems/utyum/utyum-2018_lichol_8_tree_cities.yaml`
  - Видно: дерево городов; вероятны отдельные случаи по структуре дерева.
  - Классификация: нужно проверить.

- `utyum-2019_komol_7_airline_costs` — `data/problems/utyum/utyum-2019_komol_7_airline_costs.yaml`
  - Видно: стоимости авиалиний; проверить на оценку и пример/конструкцию.
  - Классификация: парный вариант.

- `utyum-2021_komol_6_archipelago_bridges` — `data/problems/utyum/utyum-2021_komol_6_archipelago_bridges.yaml`
  - Видно: архипелаг и мосты; вероятны несколько условий связности/перехода.
  - Классификация: нужно проверить.

- `utyum-2021_komol_7_no_k5_many_acquaintances` — `data/problems/utyum/utyum-2021_komol_7_no_k5_many_acquaintances.yaml`
  - Видно: экстремальная графовая формулировка "без K5" и много знакомств; проверить на оценку плюс пример.
  - Классификация: парный вариант.

- `utyum-2023_komol60_6_7_company_departures` — `data/problems/utyum/utyum-2023_komol60_6_7_company_departures.yaml`
  - Видно: есть близкий файл `room_departures`; возможный ложный друг по общей схеме "departures".
  - Классификация: ложный друг.

- `utyum-2023_komol60_7_7_room_departures` — `data/problems/utyum/utyum-2023_komol60_7_7_room_departures.yaml`
  - Видно: близкий файл к `company_departures`; возможный ложный друг.
  - Классификация: ложный друг.

- `utyum-2023_komol61_8_5_yozhgorod_registry` — `data/problems/utyum/utyum-2023_komol61_8_5_yozhgorod_registry.yaml`
  - Видно: реестр/городская формулировка; проверить на несколько требований "докажите/найдите".
  - Классификация: нужно проверить.

- `utyum-2024_komol62_6_3_circle_graph_coloring` — `data/problems/utyum/utyum-2024_komol62_6_3_circle_graph_coloring.yaml`
  - Видно: раскраска кругового графа; вероятны отдельные случаи/конструкции.
  - Классификация: нужно проверить.

- `utyum-2024_komol62_8_5_average_degree_friends` — `data/problems/utyum/utyum-2024_komol62_8_5_average_degree_friends.yaml`
  - Видно: средняя степень друзей; вероятны несколько независимых подсчетов.
  - Классификация: нужно проверить.

- `utyum-2024_komol63_67_capital_flights_bipartite` — `data/problems/utyum/utyum-2024_komol63_67_capital_flights_bipartite.yaml`
  - Видно: формулировка про столицу и рейсы, двудольность; проверить на две самостоятельные формулировки.
  - Классификация: нужно проверить.

- `utyum-2025_komol64_6_6_odd_degree_game` — `data/problems/utyum/utyum-2025_komol64_6_6_odd_degree_game.yaml`
  - Видно: игра и нечетные степени; вероятны разные стратегии/варианты игроков.
  - Классификация: парный вариант.

- `utyum-2025_komol64_8_7_tree_matchings_path` — `data/problems/utyum/utyum-2025_komol64_8_7_tree_matchings_path.yaml`
  - Видно: дерево, паросочетания и путь; вероятны несколько самостоятельных утверждений в решении.
  - Классификация: нужно проверить.

- `utyum-2025_komol65_7_6_airlines_degree_sum` — `data/problems/utyum/utyum-2025_komol65_7_6_airlines_degree_sum.yaml`
  - Видно: суммы степеней авиалиний; проверить на оценку и пример.
  - Классификация: парный вариант.

- `utyum-2025_komol65_8_6_oriented_graph_bound` — `data/problems/utyum/utyum-2025_komol65_8_6_oriented_graph_bound.yaml`
  - Видно: ориентированный граф и граница; вероятны верхняя оценка плюс конструкция.
  - Классификация: парный вариант.

## Kolmogorov

- `kolmogorov-2004-round2-higher-league-problem-9` — `data/problems/kolmogorov/kolmogorov-2004-round2-higher-league-problem-9.yaml`
  - Видно: высокий тур/номер; проверить на несколько независимых требований или случаев.
  - Классификация: нужно проверить.

- `kolmogorov-2004-round3-higher-league-problem-10` — `data/problems/kolmogorov/kolmogorov-2004-round3-higher-league-problem-10.yaml`
  - Видно: высокий тур/номер 10; вероятна многокомпонентная задача.
  - Классификация: нужно проверить.

- `kolmogorov-2006-round-1-super-high-first-league-problem-1` — `data/problems/kolmogorov/kolmogorov-2006-round-1-super-high-first-league-problem-1.yaml`
  - Видно: объединенная лига `super/high/first`; возможны близкие варианты условий.
  - Классификация: ложный друг.

- `kolmogorov-2006-round-1-super-high-first-league-problem-9` — `data/problems/kolmogorov/kolmogorov-2006-round-1-super-high-first-league-problem-9.yaml`
  - Видно: объединенная лига и поздний номер; проверить на несколько вариантов/случаев.
  - Классификация: нужно проверить.

- `kolmogorov-2007-round-2-high-and-first-league-chromatic-number-problem` — `data/problems/kolmogorov/kolmogorov-2007-round-2-high-and-first-league-chromatic-number-problem.yaml`
  - Видно: явно объединены high and first league; задача о хроматическом числе часто имеет нижнюю оценку и раскраску-пример.
  - Классификация: ложный друг.

- `kolmogorov-2008-round-1-first-league-and-higher-junior-problem-1` — `data/problems/kolmogorov/kolmogorov-2008-round-1-first-league-and-higher-junior-problem-1.yaml`
  - Видно: объединенная лига; возможны два уровня одной формулировки.
  - Классификация: ложный друг.

- `kolmogorov-2008-round-2-first-league-and-higher-junior-problem-1` — `data/problems/kolmogorov/kolmogorov-2008-round-2-first-league-and-higher-junior-problem-1.yaml`
  - Видно: объединенная лига; возможны два уровня одной формулировки.
  - Классификация: ложный друг.

- `kolmogorov-2008-round-4-first-league-and-higher-junior-problem-1` — `data/problems/kolmogorov/kolmogorov-2008-round-4-first-league-and-higher-junior-problem-1.yaml`
  - Видно: объединенная лига; возможны близкие варианты.
  - Классификация: ложный друг.

- `kolmogorov-2009-round1-high-dense-hamiltonian-pancyclic` — `data/problems/kolmogorov/kolmogorov-2009-round1-high-dense-hamiltonian-pancyclic.yaml`
  - Видно: dense/hamiltonian/pancyclic; потенциально два самостоятельных результата: гамильтоновость и панцикличность/циклы разных длин.
  - Классификация: ложный друг.

- `kolmogorov-2009-round2-high-local-vertex-cover-coloring` — `data/problems/kolmogorov/kolmogorov-2009-round2-high-local-vertex-cover-coloring.yaml`
  - Видно: vertex cover + coloring; вероятно дробится на покрытие и раскраску.
  - Классификация: нужно проверить.

- `kolmogorov-2009-round3-high-edge-label-three-edge-path` — `data/problems/kolmogorov/kolmogorov-2009-round3-high-edge-label-three-edge-path.yaml`
  - Видно: метки ребер и пути длины 3; проверить на несколько независимых условий.
  - Классификация: нужно проверить.

- `kolmogorov-2009-round4-high-regular-tournament-hamiltonian-paths` — `data/problems/kolmogorov/kolmogorov-2009-round4-high-regular-tournament-hamiltonian-paths.yaml`
  - Видно: регулярный турнир и гамильтоновы пути; возможны разные варианты/направления подсчета.
  - Классификация: нужно проверить.

- `kolmogorov-2014-round1-complete-graph-orientation-game` — `data/problems/kolmogorov/kolmogorov-2014-round1-complete-graph-orientation-game.yaml`
  - Видно: игра на ориентации полного графа; вероятны отдельные стратегии двух игроков.
  - Классификация: парный вариант.

- `kolmogorov-2014-round1-oriendiriya-road-orientation-game` — `data/problems/kolmogorov/kolmogorov-2014-round1-oriendiriya-road-orientation-game.yaml`
  - Видно: близкая тема ориентации дорог и игра; возможный ложный друг к `complete-graph-orientation-game`.
  - Классификация: ложный друг.

- `kolmogorov-2014-round3-four-regular-two-100-cycles` — `data/problems/kolmogorov/kolmogorov-2014-round3-four-regular-two-100-cycles.yaml`
  - Видно: 4-регулярный граф и два 100-цикла; вероятны две самостоятельные конструкции/леммы.
  - Классификация: нужно проверить.

- `kolmogorov-2014-round4-diameter-cycle-length` — `data/problems/kolmogorov/kolmogorov-2014-round4-diameter-cycle-length.yaml`
  - Видно: диаметр и длина цикла; проверить на два утверждения-оценки.
  - Классификация: нужно проверить.

- `kolmogorov-2015-round-2-graph-coloring-problem` — `data/problems/kolmogorov/kolmogorov-2015-round-2-graph-coloring-problem.yaml`
  - Видно: задача о раскраске графа; вероятны нижняя оценка и раскраска.
  - Классификация: парный вариант.

- `kolmogorov-2015-round-3-missionaries-and-cannibals-problem` — `data/problems/kolmogorov/kolmogorov-2015-round-3-missionaries-and-cannibals-problem.yaml`
  - Видно: прикладная формулировка; проверить, не отделяется ли графовая модель от исходного сюжета.
  - Классификация: нужно проверить.

- `kolmogorov-2015-round-4-spies-and-opergroups-problem` — `data/problems/kolmogorov/kolmogorov-2015-round-4-spies-and-opergroups-problem.yaml`
  - Видно: сюжетная задача со спецгруппами; проверить на несколько независимых требований.
  - Классификация: нужно проверить.

- `kolmogorov-2021-t1-critical-strong-orientation` — `data/problems/kolmogorov/kolmogorov-2021-t1-critical-strong-orientation.yaml`
  - Видно: критичность и сильная ориентация; вероятно две части: существование ориентации и критическое свойство.
  - Классификация: ложный друг.

- `kolmogorov-2021-t2-circulant-rainbow-reachability` — `data/problems/kolmogorov/kolmogorov-2021-t2-circulant-rainbow-reachability.yaml`
  - Видно: точный ответ `20` по скану; нижняя оценка через длину радужного пути и конструкция циркулянта.
  - Классификация: парный вариант.

- `kolmogorov-2021-team-olympiad-seniors-problem-5` — `data/problems/kolmogorov/kolmogorov-2021-team-olympiad-seniors-problem-5.yaml`
  - Видно: в условии явно два требования к "большой Москве": внутренняя связность и ровно `k` внешних соседей; решение через включение/исключение соседа Москвы.
  - Классификация: ложный друг.

- `kolmogorov-2022-individual-seniors-p2-cycle-arrangements` — `data/problems/kolmogorov/kolmogorov-2022-individual-seniors-p2-cycle-arrangements.yaml`
  - Видно: исходная формулировка про циклические расстановки и графовая формулировка через ориентированные циклы/перестановки.
  - Классификация: нужно проверить.

- `kolmogorov-2022-round1-high-edge-count-permutation-nonedges` — `data/problems/kolmogorov/kolmogorov-2022-round1-high-edge-count-permutation-nonedges.yaml`
  - Видно: максимальное `k`; решение начинается с примера, затем должна быть верхняя оценка.
  - Классификация: парный вариант.

- `kolmogorov-2022-round1-third-binary-strings-pairing-graph` — `data/problems/kolmogorov/kolmogorov-2022-round1-third-binary-strings-pairing-graph.yaml`
  - Видно: вопрос "обязательно ли"; исходная формулировка про строки и графовая формулировка через гиперкуб и совершенные паросочетания.
  - Классификация: нужно проверить.

- `kolmogorov-2022-round2-high-colored-integers-infinite-tree` — `data/problems/kolmogorov/kolmogorov-2022-round2-high-colored-integers-infinite-tree.yaml`
  - Видно: условие совмещает бесконечную последовательность, ограниченные разности и одноцветные сдвиги для каждого `n`; решение индукционное с несколькими случаями.
  - Классификация: ложный друг.

- `kolmogorov-2022-round2-juniors-hamiltonian-path-parity` — `data/problems/kolmogorov/kolmogorov-2022-round2-juniors-hamiltonian-path-parity.yaml`
  - Видно: две величины `a` и `b` для красных/синих гамильтоновых путей; решение отдельно нормирует ориентацию пути и сравнивает четности.
  - Классификация: парный вариант.

- `kolmogorov-2022-round2-second-third-red-blue-k10-triangles` — `data/problems/kolmogorov/kolmogorov-2022-round2-second-third-red-blue-k10-triangles.yaml`
  - Видно: вопрос "каким может быть число"; графовая формулировка; решение с ограничениями на степени и подсчетом красных треугольников.
  - Классификация: парный вариант.

- `kolmogorov-2022-round4-high-airport-walk-parity` — `data/problems/kolmogorov/kolmogorov-2022-round4-high-airport-walk-parity.yaml`
  - Видно: вопрос "существуют ли граф и d"; есть исходная аэропортная и графовая формулировки; решение по четности маршрутов.
  - Классификация: нужно проверить.

- `kolmogorov-2022-round4-high-maximum-length-tree-diameter-circles` — `data/problems/kolmogorov/kolmogorov-2022-round4-high-maximum-length-tree-diameter-circles.yaml`
  - Видно: решение явно содержит лемму о замкнутой ломаной и дальнейшее доказательство общей точки окружностей.
  - Классификация: ложный друг.

- `kolmogorov-2022-round4-second-third-even-degree-odd-walks` — `data/problems/kolmogorov/kolmogorov-2022-round4-second-third-even-degree-odd-walks.yaml`
  - Видно: вопрос "существуют ли граф G и n"; условие совмещает четные степени всех вершин и нечетность числа маршрутов для любых пар.
  - Классификация: нужно проверить.

- `kolmogorov-2023-lichol-large-monochromatic-bipartite-component` — `data/problems/kolmogorov/kolmogorov-2023-lichol-large-monochromatic-bipartite-component.yaml`
  - Видно: двудольный граф с параметрами `k,m,n`; решение разбивает доказательство на выбор цвета и отдельный подсчет по суммам степеней.
  - Классификация: нужно проверить.
