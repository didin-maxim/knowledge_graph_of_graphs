# Putnam 2013-2025 graph-problem pass

Дата: 2026-05-02.

Зона изменений соблюдена: добавлены только новые карточки в `data/problems/putnam/` и этот отчёт. `data/sources/sources.yaml`, `data/relations`, `docs`, `viewer`, `tools` не редактировались.

## Созданные карточки

| Файл | source_id | URL |
|---|---|---|
| `data/problems/putnam/putnam-2013-a1-icosahedron-face-labels.yaml` | `src-putnam-2013-A1-kedlaya` | Problem: https://kskedlaya.org/putnam-archive/2013.pdf ; Solutions: https://kskedlaya.org/putnam-archive/2013s.pdf |
| `data/problems/putnam/putnam-2013-b5-functions-iterate-into-roots.yaml` | `src-putnam-2013-B5-kedlaya` | Problem: https://kskedlaya.org/putnam-archive/2013.pdf ; Solutions: https://kskedlaya.org/putnam-archive/2013s.pdf |
| `data/problems/putnam/putnam-2014-b3-prime-entries-bipartite-cycle.yaml` | `src-putnam-2014-B3-kedlaya` | Problem: https://kskedlaya.org/putnam-archive/2014.pdf ; Solutions: https://kskedlaya.org/putnam-archive/2014s.pdf |
| `data/problems/putnam/putnam-2016-a5-cayley-digraph-short-words.yaml` | `src-putnam-2016-A5-kedlaya` | Problem: https://kskedlaya.org/putnam-archive/2016.pdf ; Solutions: https://kskedlaya.org/putnam-archive/2016s.pdf |
| `data/problems/putnam/putnam-2017-a6-icosahedron-edge-colorings.yaml` | `src-putnam-2017-A6-kedlaya` | Problem: https://kskedlaya.org/putnam-archive/2017.pdf ; Solutions: https://kskedlaya.org/putnam-archive/2017s.pdf |
| `data/problems/putnam/putnam-2021-b5-very-odd-matrices-dag.yaml` | `src-putnam-2021-B5-official` | Official: https://maa.org/wp-content/uploads/2024/10/Putnam-2021-problems-and-solutions.pdf |
| `data/problems/putnam/putnam-2025-a3-ternary-string-game-perfect-matching.yaml` | `src-putnam-2025-A3-official` | Official: https://maa.org/wp-content/uploads/2026/02/2025OfficialSolutions.pdf |
| `data/problems/putnam/putnam-2025-a4-cycle-commutation-graph-matrices.yaml` | `src-putnam-2025-A4-official` | Official: https://maa.org/wp-content/uploads/2026/02/2025OfficialSolutions.pdf |

## Статусы

- `ai_checked`: 2013 A1, 2014 B3, 2021 B5, 2025 A3.
- `needs_human_review`: 2013 B5, 2016 A5, 2017 A6, 2025 A4.
- Причины `needs_human_review`: в 2013 B5 карточка разворачивает стандартную лесную интерпретацию из замечания Kedlaya; в 2016 A5 нужно проверить крайний случай представления единицы непустым словом; в 2017 A6 стоит проверить краткую аргументацию сюръективности отображения рёбра-граням; в 2025 A4 стоит проверить детали выбора 2025 векторов в общем положении и запрет размерности 2.

## Просмотренные, но не добавленные

| Задача | URL | Причина |
|---|---|---|
| Putnam 2013 A4 | https://kskedlaya.org/putnam-archive/2013.pdf | Круговые дуги/строки; можно нарисовать циклический порядок, но графовая модель не является содержательной. |
| Putnam 2013 B6 | https://kskedlaya.org/putnam-archive/2013.pdf | Игра на позициях допускает граф состояний, но решение использует инвариант/эндшпиль, а полный граф состояний был бы искусственным. |
| Putnam 2014 B5 | https://kskedlaya.org/putnam-archive/2014.pdf | Игра на коммутирующих матрицах; граф коммутирования можно ввести, но стандартное решение алгебраическое, граф не даёт естественного ядра. |
| Putnam 2015 | https://kskedlaya.org/putnam-archive/2015.pdf | Не найдено задач, где графы/гиперграфы являются существенной моделью. |
| Putnam 2016 A4 | https://kskedlaya.org/putnam-archive/2016.pdf | Замощение прямоугольника: возможен граф клеток, но официальная модель геометрическая/площадная, не графовая. |
| Putnam 2017 A1 | https://kskedlaya.org/putnam-archive/2017.pdf | Можно построить бесконечный направленный граф переходов для множества чисел, но это слабее прямого модульного решения. |
| Putnam 2018 | https://kskedlaya.org/putnam-archive/2018.pdf | Существенно графовых задач не обнаружено. |
| Putnam 2019 | https://kskedlaya.org/putnam-archive/2019.pdf | Существенно графовых задач не обнаружено. |
| Putnam 2020 | https://kskedlaya.org/putnam-archive/2020.pdf | Существенно графовых задач не обнаружено; слово graph встречается только в нерелевантных/геометрических контекстах. |
| Putnam 2021 A1 | https://maa.org/wp-content/uploads/2024/10/Putnam-2021-problems-and-solutions.pdf | Решётчатый граф ходов возможен, но решение сводится к метрике/линейной оценке; графовая оболочка не нужна. |
| Putnam 2022 | https://kskedlaya.org/putnam-archive/2022.pdf | Существенно графовых задач не обнаружено. |
| Putnam 2023 | https://kskedlaya.org/putnam-archive/2023.pdf | Существенно графовых задач не обнаружено. |
| Putnam 2024 | https://maa.org/maa-putnam-archive/ | Существенно графовых задач не обнаружено; в архивном тексте встречалось edge только как геометрический край/граница. |
| Putnam 2025 A4 alternative | https://maa.org/wp-content/uploads/2026/02/2025OfficialSolutions.pdf | Добавлена как граф коммутирования; не добавлялись отдельные варианты решения как отдельные карточки. |

## Идеи для родственных связей

- `putnam-2013-a1-icosahedron-face-labels`: связать с `data/problems/classical/handshaking-lemma.yaml`, если нужна общая карточка по double counting/incidence; также с 2017 A6 как пара задач об икосаэдре.
- `putnam-2013-b5-functions-iterate-into-roots`: связать с карточками про формулу Кэли, rooted forests, functional digraphs, если они есть/появятся.
- `putnam-2014-b3-prime-entries-bipartite-cycle`: связать с `data/problems/classical/tree-equivalent-properties.yaml` или лесной оценкой `e<=v-1`, а также с задачами про двудольный цикл и ранг.
- `putnam-2016-a5-cayley-digraph-short-words`: связать с карточками про достижимость в ориентированных графах и кратчайшие пути.
- `putnam-2017-a6-icosahedron-edge-colorings`: связать с `putnam-2013-a1-icosahedron-face-labels`, с задачами на раскраску рёбер и с линейной алгеброй над конечными полями.
- `putnam-2021-b5-very-odd-matrices-dag`: связать с классическими DAG/topological ordering и с задачами, где цикл даёт вырожденность/паритетную линейную зависимость.
- `putnam-2025-a3-ternary-string-game-perfect-matching`: связать с карточками на pairing strategy и perfect matching.
- `putnam-2025-a4-cycle-commutation-graph-matrices`: связать с задачами про представления графов матрицами/ортогональностью и с `graph_symmetry`/cycle graph motifs.
