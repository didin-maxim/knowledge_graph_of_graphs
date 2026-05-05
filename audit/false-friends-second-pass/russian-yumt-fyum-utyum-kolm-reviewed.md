# Второй проход: YUMT/FYUM/UTYUM/Kolmogorov

Источник первого прохода: `audit/false-friends-first-pass/russian-yumt-fyum-utyum-kolm.md`.

Критерий второго прохода был строгим: выживают только случаи, где есть две или более независимые самодостаточные формулировки/варианта. Обычная схема "верхняя оценка + пример", подслучаи одного доказательства, перевод сюжета в графовую модель и технические леммы внутри решения не считаются pair/false relation. Для технических самостоятельных блоков использована метка `lemma_split`.

## Выжившие кандидаты

### false_friend

- `fyum-2009-tur4a-p2` и `fyum-2009-tur4b-p2`
  - Файлы: `data/problems/fyum/fyum-2009-tur4a-p2.yaml`, `data/problems/fyum/fyum-2009-tur4b-p2.yaml`
  - Итог: `false_friend`.
  - Почему: оба выглядят как задачи про ориентированные графы/пути и были отмечены как парные A/B, но содержание и решения принципиально разные. В `tur4a-p2` надо переориентировать произвольный орграф в ациклический с сохранением достижимости/длин через максимальный ациклический подграф. В `tur4b-p2` доказывается одноцветный путь длины `n` в двухцветном ациклическом турнире через инъективные пары длин красного/синего пути.

- `utyum-2023_komol60_6_7_company_departures` и `utyum-2023_komol60_7_7_room_departures`
  - Файлы: `data/problems/utyum/utyum-2023_komol60_6_7_company_departures.yaml`, `data/problems/utyum/utyum-2023_komol60_7_7_room_departures.yaml`
  - Итог: `false_friend`.
  - Почему: внешний сюжет одинаковый - процесс удаления вершины с выделяющейся степенью. Но в первом варианте порог "строго больше всех" на 100 вершинах даёт минимум 3 и короткое локальное рассуждение о последних трёх вершинах. Во втором варианте порог "хотя бы на 2 больше" на 99 вершинах даёт минимум 51, а решение использует убывание степеней на 2 и специальную конструкцию. Это не одна оценка с примером, а две близкие на вид задачи с разной механикой.

- `kolmogorov-2014-round1-complete-graph-orientation-game` и `kolmogorov-2014-round1-oriendiriya-road-orientation-game`
  - Файлы: `data/problems/kolmogorov/kolmogorov-2014-round1-complete-graph-orientation-game.yaml`, `data/problems/kolmogorov/kolmogorov-2014-round1-oriendiriya-road-orientation-game.yaml`
  - Итог: `false_friend`.
  - Почему: обе задачи выглядят как игра ориентации рёбер полного графа с целью создать/избежать ориентированный цикл. Но в первой задаче первый игрок выигрывает, удлиняя ориентированный путь и затем замыкая свободной хордой; во второй выигрывает второй, поддерживая упорядоченное разбиение на блоки. Ключевые стратегии противоположны.

### lemma_split

- `kolmogorov-2021-t1-critical-strong-orientation`
  - Файл: `data/problems/kolmogorov/kolmogorov-2021-t1-critical-strong-orientation.yaml`
  - Итог: `lemma_split`.
  - Почему: это не false_friend и не pair_variant, но решение естественно распадается на самостоятельные леммы: отсутствие мостов из 2-связности по вершинам; применение теоремы Роббинса для сильной ориентации; доказательство, что хордовость циклов заставляет удаление любого ребра разрушать сильную связность. Лучше выносить как леммы/зависимости, а не связывать с другим пунктом.

- `kolmogorov-2022-round4-high-maximum-length-tree-diameter-circles`
  - Файл: `data/problems/kolmogorov/kolmogorov-2022-round4-high-maximum-length-tree-diameter-circles.yaml`
  - Итог: `lemma_split`.
  - Почему: в решении явно есть самостоятельная лемма о замкнутой ломаной: если одно ребро строго короче всех остальных, оно не может принадлежать максимальному по суммарной длине дереву. Затем эта лемма используется в отдельной геометрической части с минимальным охватывающим кругом. Это не пара вариантов, но лемму стоит отделить.

- `utyum-2025_komol64_8_7_tree_matchings_path`
  - Файл: `data/problems/utyum/utyum-2025_komol64_8_7_tree_matchings_path.yaml`
  - Итог: `lemma_split`.
  - Почему: исходная задача про 80 вершин и 820 толстых паросочетаний в решении заменена более общим самостоятельным утверждением о дереве на `2n` вершинах: число паросочетаний из `n-1` рёбер не превосходит `C(n+1,2)`, а равенство при `n>=3` даёт путь. Это лучше оформить как лемму/обобщение, а не как relation между пунктами.

## Приоритетные кандидаты первого прохода, отклонённые

- `yumt-2011-grand-round4-problem9` - `reject`. Обычный точный порог: гарантия при `k <= 1507` и контрпример при `k = 1508`.
- `yumt-2012-start-round2-problem5` - `reject`. Верхняя оценка и достигающий пример для одной экстремальной задачи.
- `yumt-2012-start-team-olympiad-problem5` - `reject`. Графовая формулировка эквивалентна исходной; решение является одной минимизацией числа рёбер.
- `yumt-2014-grand-round4-problem1` - `reject`. Одна задача на максимум числа компаний; оценка через плохую пару плюс конструкция.
- `yumt-2014-start-final-problem1` - `reject`. Одна экстремальная задача для мультиграфа; оценка через остовное дерево плюс пример с двойной звездой.
- `fyum-2009-tur3b-p7` - `reject`. Самостоятельная задача про дерево с корнем; связи с `tur3a-p7` по проверенному содержанию не установлено.
- `fyum-2011-tur1a-p5` и `fyum-2011-tur1b-p5` - `reject`. Это фактически дубликаты одной и той же задачи и одного решения, а не false friend.
- `complete-graph-triangle-edge-weights-minimum-parametric` - `reject`. Параметрическое обобщение `n` и конкретные значения `2000/2019` не образуют независимые варианты; это одна экстремальная задача.
- `utyum-2018_komol_7_red_blue_cycle_game` - `reject`. Стратегии игроков являются частями одного игрового доказательства.
- `utyum-2019_komol_7_airline_costs` - `reject`. Оценка по числу рёбер веса 10/30 и случаи по `L` - обычное доказательство одной нижней границы.
- `utyum-2021_komol_7_no_k5_many_acquaintances` - `reject`. Обычный экстремальный ответ: конструкция через 4-дольный граф и нижняя оценка жадным построением `K5`.
- `utyum-2025_komol64_6_6_odd_degree_game` - `reject`. Верхняя стратегия Пети и нижняя стратегия Васи - две стороны одной игры, не две самостоятельные формулировки.
- `utyum-2025_komol65_7_6_airlines_degree_sum` - `reject`. Классификация возможных `k` через дополнительный граф; чётный/нечётный случаи являются подслучаями одного ответа.
- `utyum-2025_komol65_8_6_oriented_graph_bound` - `reject`. Индукционное доказательство одной нижней оценки.
- `kolmogorov-2006-round-1-super-high-first-league-problem-1` - `reject`. Объединение лиг в названии не даёт разных вариантов; решение одно.
- `kolmogorov-2007-round-2-high-and-first-league-chromatic-number-problem` - `reject`. Одна задача о доведении раскраски до `k` цветов без одноэлементных классов.
- `kolmogorov-2008-round-1-first-league-and-higher-junior-problem-1` - `reject`. Одна задача на максимум числа ходов; путь/звезда и верхняя оценка не являются вариантами.
- `kolmogorov-2008-round-2-first-league-and-higher-junior-problem-1` - `reject`. Одна задача подсчёта раскрасок колеса.
- `kolmogorov-2008-round-4-first-league-and-higher-junior-problem-1` - `reject`. Одно короткое утверждение про красный лист.
- `kolmogorov-2009-round1-high-dense-hamiltonian-pancyclic` - `reject`. Используется единая теорема Бонди; гамильтоновость является условием, а не отдельным результатом задачи.
- `kolmogorov-2015-round-2-graph-coloring-problem` - `reject`. Большое индукционное доказательство с разбором 1- и 2-разделителей, но это подслучаи одной 3-раскраски.
- `kolmogorov-2021-t2-circulant-rainbow-reachability` - `reject`. Точный ответ `20`: нижняя оценка и циркулянтная раскраска являются стандартными половинами одной экстремальной задачи.
- `kolmogorov-2021-team-olympiad-seniors-problem-5` - `reject`. Два требования к большой Москве задают один объект; два приведённых решения альтернативны, но не скрытые варианты задачи.
- `kolmogorov-2022-round1-high-edge-count-permutation-nonedges` - `reject`. Пример и индукционная верхняя оценка для одного максимального `k`.
- `kolmogorov-2022-round2-high-colored-integers-infinite-tree` - `reject`. Случаи по наличию длинных отрезков без цвета и дерево Кёнига - один индукционный переход.
- `kolmogorov-2022-round2-juniors-hamiltonian-path-parity` - `reject`. Нормировка ориентации путей и подсчёт помеченных путей - части одного доказательства делимости.
- `kolmogorov-2022-round2-second-third-red-blue-k10-triangles` - `reject`. Графовая формулировка эквивалентна исходной; подсчёт степеней ведёт к одному числу треугольников.

## Сильные "нужно проверить", просмотренные дополнительно

- `yumt-2014-grand-round1-problem5` - `reject`. В решении есть фундаментальные циклы и тета-графы, но они работают как подшаги одного доказательства существования двух циклов равной длины.
- `kolmogorov-2014-round3-four-regular-two-100-cycles` - `reject/неполно проверено`. В карточке нет решения, а условие само по себе задаёт одно утверждение про два непересекающихся 100-цикла; самостоятельных формулировок в доступном тексте не видно.
- `kolmogorov-2014-round4-diameter-cycle-length` - `lemma_split` слабый кандидат, но relation не нужен. Можно вынести стандартную лемму "2-связность даёт два внутренне непересекающихся пути"; сама задача одна.
- `kolmogorov-2022-individual-seniors-p2-cycle-arrangements` - `reject`. Циклическая и графовая записи являются взаимно однозначным переводом перестановок, не двумя вариантами.
- `kolmogorov-2022-round1-third-binary-strings-pairing-graph` - `reject`. Строковая и гиперкубовая формулировки эквивалентны; решение одно через суммы `A_s`.
- `kolmogorov-2022-round4-high-airport-walk-parity` - `reject`. Исходная и графовая формулировки совпадают по смыслу; два случая по чётности степеней - обычный разбор.
- `kolmogorov-2022-round4-second-third-even-degree-odd-walks` - `reject`. Это частный случай/родственный фрагмент предыдущей parity-задачи, но сам файл содержит одну формулировку.
- `kolmogorov-2009-round2-high-local-vertex-cover-coloring` - `reject/неполно проверено`. В карточке отсутствует решение; условие выглядит как одно локальное условие, из которого требуется одна раскраска.

## Необработанные из "нужно проверить"

Ниже остались кандидаты первого прохода, которые не вошли в качественный второй проход из-за приоритета на уже помеченные `ложный друг`/`парный вариант` и самые сильные дополнительные случаи:

- `yumt-2011-premier-round4-problem1`
- `yumt-2012-start-round3-problem1`
- `yumt-2013-start-round1-problem3`
- `yumt-2013-start-round4-problem8`
- `yumt-2014-start-round4-problem2`
- `yumt-2015-grand-final-problem5`
- `yumt-2015-grand-round3-problem9`
- `yumt-2015-grand-round4-problem10`
- `yumt-2016-team-olympiad-9-11-problem8`
- `yumt-2018-grand-final-problem1`
- `yumt-2021-grand-final-problem7`
- `yumt-2021-grand-round4-problem3`
- `yumt-2023-granda-round2-problem9`
- `yumt-2024-grand-final-problem9`
- `yumt-2025-grand-round1-problem9`
- `fyum-2008-final-p8`
- `fyum-2008-tur1a-p10`
- `fyum-2008-tur4b-p10`
- `fyum-2009-final-p2`
- `fyum-2009-tur3a-p7`
- `fyum-2010-tur3a-p7`
- `fyum-2010-tur3b-p3`
- `fyum-2011-finalb-p4`
- `fyum-2012-tur1a-p10`
- `fyum-2013-tur1b-p10`
- `fyum-2013-tur2b-p7`
- `utyum-1995_final_10_writers_committee`
- `utyum-1996_tur3_10_central_cities`
- `utyum-2001_olymp8_6_countries_route`
- `utyum-2002_carousel_senior_8x8_polyline`
- `utyum-2004_line_acquaintances_endpoints`
- `utyum-2008_tur4_31_6_directed_cities`
- `utyum-2011_tur4_37_8_equal_sums_bipartite_graph`
- `utyum-2012_komol39_8_binary_tree_ordering`
- `utyum-2018_lichol_6_strategic_cities`
- `utyum-2018_lichol_8_tree_cities`
- `utyum-2021_komol_6_archipelago_bridges`
- `utyum-2023_komol61_8_5_yozhgorod_registry`
- `utyum-2024_komol62_6_3_circle_graph_coloring`
- `utyum-2024_komol62_8_5_average_degree_friends`
- `utyum-2024_komol63_67_capital_flights_bipartite`
- `kolmogorov-2004-round2-higher-league-problem-9`
- `kolmogorov-2004-round3-higher-league-problem-10`
- `kolmogorov-2006-round-1-super-high-first-league-problem-9`
- `kolmogorov-2009-round3-high-edge-label-three-edge-path`
- `kolmogorov-2009-round4-high-regular-tournament-hamiltonian-paths`
- `kolmogorov-2015-round-3-missionaries-and-cannibals-problem`
- `kolmogorov-2015-round-4-spies-and-opergroups-problem`
- `kolmogorov-2023-lichol-large-monochromatic-bipartite-component`
