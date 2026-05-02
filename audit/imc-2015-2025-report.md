# IMC 2015-2025 graph-problem pass

Дата: 2026-05-02.

Зона изменений соблюдена: добавлены только новые карточки в `data/problems/imc/` и этот отчёт. `data/sources/sources.yaml`, `data/relations`, `docs`, `viewer`, `tools` не редактировались.

## Созданные карточки

| Файл | source_id | Официальные URL |
|---|---|---|
| `data/problems/imc/imc-2018-day2-p6-path-orthogonal-representation.yaml` | `src-imc-2018-day2-p6-official` | Problem: https://imc-math.org.uk/?item=prob6q&section=problems&year=2018 ; Solutions PDF: https://imc-math.org.uk/imc2018/imc2018-day2-solutions.pdf |
| `data/problems/imc/imc-2018-day2-p8-frog-lattice-paths.yaml` | `src-imc-2018-day2-p8-official` | Problem: https://imc-math.org.uk/?item=prob8q&section=problems&year=2018 ; Solutions PDF: https://imc-math.org.uk/imc2018/imc2018-day2-solutions.pdf |
| `data/problems/imc/imc-2022-day1-p3-flea-cycle-recurrence.yaml` | `src-imc-2022-day1-p3-official` | Solutions PDF: https://www.imc-math.org.uk/imc2022/imc2022day1solutions.pdf |
| `data/problems/imc/imc-2022-day1-p4-triples-chromatic-loglog.yaml` | `src-imc-2022-day1-p4-official` | Solutions PDF: https://www.imc-math.org.uk/imc2022/imc2022day1solutions.pdf |
| `data/problems/imc/imc-2022-day2-p5-regular-43-coloured-triangles.yaml` | `src-imc-2022-day2-p5-official` | Questions PDF: https://www.imc-math.org.uk/imc2022/imc2022day2questions.pdf ; Solutions PDF: https://www.imc-math.org.uk/imc2022/imc2022day2solutions.pdf |
| `data/problems/imc/imc-2022-day2-p8-random-circle-hulls-colour-changes.yaml` | `src-imc-2022-day2-p8-official` | Questions PDF: https://www.imc-math.org.uk/imc2022/imc2022day2questions.pdf ; Solutions PDF: https://www.imc-math.org.uk/imc2022/imc2022day2solutions.pdf |
| `data/problems/imc/imc-2023-day2-p8-tree-distance-wiener-harary.yaml` | `src-imc-2023-day2-p8-official` | Problem: https://imc-math.org.uk/?item=prob8q&section=problems&year=2023 ; Solutions PDF: https://imc-math.org.uk/imc2023/imc2023-day2-solutions.pdf |
| `data/problems/imc/imc-2024-day2-p9-young-tableaux-friend-graph.yaml` | `src-imc-2024-day2-p9-official` | Problem: https://imc-math.org.uk/?item=prob9q&section=problems&year=2024 ; Solutions PDF: https://imc-math.org.uk/imc2024/imc2024-day2-solutions.pdf |

## Статусы

- `ai_checked`: 2018 D2 P6, 2018 D2 P8, 2022 D1 P3, 2022 D1 P4, 2022 D2 P5, 2022 D2 P8, 2023 D2 P8.
- `needs_human_review`: 2024 D2 P9. Официальное решение очень сжато; карточка раскрывает intended graph/handshaking argument, но обратная биекция между нечётной степенью таблицы и nice-матрицей заслуживает человеческой проверки.
- Для 2023 D2 P8 отдельная graph-theory formulation удалена как дублирующая: исходное условие уже является чистой задачей о дереве и расстояниях.

## Отложенные сомнительные задачи

| Задача | URL | Причина |
|---|---|---|
| IMC 2017 Day 2 P8 | https://imc-math.org.uk/?item=prob8q&section=problems&year=2017 | Матрицы являются матрицами смежности гиперкуба, но официальная карточка потребовала бы аккуратного спектрального доказательства через тензорные/декартовы произведения графов. Не включал без полной русской реконструкции. |
| IMC 2021 Day 2 P8 | https://imc-math.org.uk/?item=prob8q&section=problems&year=2021 | Граф неортогональности естественен, но задача опирается на результат Эрдёша-Розенфельда/геометрическую экстремальную оценку. Не включал как graph_in_solution без надёжной подробной реконструкции. |
| IMC 2025 Day 1 P5 | https://imc-math.org.uk/?item=prob5q&section=problems&year=2025 | Функциональный граф отображения существенен, но решение связано с асимптотикой максимального порядка перестановок/отображений. Отложено, чтобы не делать слабую advanced-карточку. |

## Идеи для родственных связей

- `imc-2018-day2-p6-path-orthogonal-representation`: связать с `data/problems/classical/caro-wei-independent-set-bound.yaml` как мотив независимого множества и с `data/problems/classical/tree-equivalent-properties.yaml` только на уровне path/tree terminology, если нужны терминологические связи.
- `imc-2018-day2-p8-frog-lattice-paths`: связать с решётчатыми/динамическими карточками вроде `data/problems/apmo/apmo-2005-p4-firefighters-grid-spread.yaml` и с классическими путями/инвариантами, если появится отдельная карточка reflection principle/Catalan paths.
- `imc-2022-day1-p3-flea-cycle-recurrence`: связать с `data/problems/classical/eulerian-graph-criterion.yaml` не нужно; лучше мотивная связь с карточками про маршруты/динамику на цикле, например `data/problems/baltic-way/baltic-way-1994-p19-directed-spy-cycles.yaml`.
- `imc-2022-day1-p4-triples-chromatic-loglog`: связать с `data/problems/classical/brooks-theorem.yaml`, `data/problems/classical/digraph-outdegree-greedy-coloring-bound.yaml`, `data/problems/classical/protected-color-recoloring-lemma.yaml` как навигационные связи по chromatic/coloring, но не как prerequisites.
- `imc-2022-day2-p5-regular-43-coloured-triangles`: связать с `data/problems/classical/ramsey-r33.yaml`, `data/problems/classical/ramsey-theorem.yaml`, `data/problems/classical/handshaking-lemma.yaml`; основная связь -- double counting в двухцветном полном графе.
- `imc-2022-day2-p8-random-circle-hulls-colour-changes`: связать с `data/problems/classical/alternating-boundary-pairs-noncrossing-arcs.yaml` и `data/problems/baltic-way/baltic-way-2023-p6-colour-touch-graph.yaml` как cyclic colour-change/adjacency motif.
- `imc-2023-day2-p8-tree-distance-wiener-harary`: связать с `data/problems/classical/tree-equivalent-properties.yaml`, `data/problems/baltic-way/baltic-way-2024-p6-tree-edge-slide-labyrinth.yaml`, `data/problems/classical/tree-total-domination-two-thirds.yaml` как tree-distance/extremal tree navigation.
- `imc-2024-day2-p9-young-tableaux-friend-graph`: связать с `data/problems/classical/handshaking-lemma.yaml` как прямой методический prerequisite; дополнительно с parity-counting карточками вроде `data/problems/imc/imc-2006-day2-p1-polygon-triangulation-parity.yaml`.
