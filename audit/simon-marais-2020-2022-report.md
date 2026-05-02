# Simon Marais 2020-2022: graph problems audit

Дата проверки: 2026-05-02.

## Официальные архивные страницы

- 2020: https://www.simonmarais.org/20201.html
- 2021: https://www.simonmarais.org/20211.html
- 2022: https://www.simonmarais.org/2022.html

## Официальные PDF

- 2020 Paper A: https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2020-paper-a_1.pdf
- 2020 Paper B: https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2020-paper-b_1.pdf
- 2020 Solutions: https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2020-solutions_1.pdf
- 2021 Paper A: https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-a.pdf
- 2021 Paper B: https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf
- 2021 Solutions: https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-solutions.pdf
- 2022 Paper A: https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2022-paper-a.pdf
- 2022 Paper B: https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2022-paper-b.pdf
- 2022 Paper C: https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2022-paper-c.pdf
- 2022 Solutions: https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2022-solutions.pdf

## Добавлены карточки

- `data/problems/simon-marais/simon-marais-2020-a1-odd-cycle-line-transversal.yaml`
  - `source_id`: `src-simon-marais-2020-A1-official`
  - Основание: в условии задан 2-регулярный граф отрезков на 1001 вершине; официальное решение явно использует граф и нечетный цикл.
- `data/problems/simon-marais/simon-marais-2020-b4-rainbow-distance-clique-polygon.yaml`
  - `source_id`: `src-simon-marais-2020-B4-official`
  - Основание: содержательная графовая формулировка как поиск радужной клики в полном графе на вершинах правильного многоугольника, где цвета ребер задаются расстояниями. Часть (b) в архиве заявлена открытой.
- `data/problems/simon-marais/simon-marais-2021-a3-determinants-cycle-components.yaml`
  - `source_id`: `src-simon-marais-2021-A3-official`
  - Основание: официальное решение прямо строит мультиграф из матрицы: столбцы - вершины, строки с двумя единицами - ребра; после удаления листьев остаются компоненты-циклы.
- `data/problems/simon-marais/simon-marais-2022-c3-random-walk-cycle-five.yaml`
  - `source_id`: `src-simon-marais-2022-C3-official`
  - Основание: блуждание по целым modulo 5 является простым случайным блужданием на цикле C5; это самостоятельная графовая формулировка, не граф состояний решения.

## Просмотренные, но не добавленные

- 2020 A2, A3, A4, B1, B2, B3: не содержат естественной графовой постановки; B3 является задачей преследования в плоскости, не графовой.
- 2021 A1, A2, A4, B1, B2, B3, B4: графовая структура не является содержательной; B2 можно искусственно кодировать как переключательный граф состояний, но это исключено критерием задачи.
- 2022 A1, A2, A3, A4, B1, B2, B4, C1, C2, C4: не содержат самостоятельной графовой постановки по критерию отбора.
- 2022 B3: пропущена как сомнительная. Игру про шоколад можно представить графом позиций, но это именно искусственный state graph игры; официальное решение идет через ним-значения, поэтому задача не включена.

## Замечания

- Общий реестр `data/sources` не изменялся по ограничению задачи; источники указаны внутри карточек через `source_id`.
- Карточка 2020 B4 помечена `needs_human_review`, потому что графовая формулировка не произнесена в официальном решении буквально, хотя она самодостаточна и математически эквивалентна условию о попарных расстояниях.
