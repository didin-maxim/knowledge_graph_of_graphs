# Putnam 2000-2012 graph problems audit

Дата: 2026-05-02.

Зона работы: созданы только новые карточки в `data/problems/putnam/` и этот отчет. `data/sources/sources.yaml`, `data/relations`, `docs`, `viewer`, `tools` не редактировались.

Основные архивы проверки:

- Kedlaya Putnam Archive: https://kskedlaya.org/putnam-archive/
- MAA Putnam Archive: https://maa.org/maa-putnam-archive/

## Созданные карточки

| Файл | source_id | Архивные URL |
| --- | --- | --- |
| `data/problems/putnam/putnam-2002-b2-polyhedron-face-game-four-edge-face.yaml` | `src-putnam-2002-B2-kedlaya` | https://kskedlaya.org/putnam-archive/2002.pdf ; https://kskedlaya.org/putnam-archive/2002s.pdf |
| `data/problems/putnam/putnam-2004-a5-random-checkerboard-components.yaml` | `src-putnam-2004-A5-kedlaya` | https://kskedlaya.org/putnam-archive/2004.pdf ; https://kskedlaya.org/putnam-archive/2004s.pdf |
| `data/problems/putnam/putnam-2005-a2-rook-tours-grid-hamiltonian-paths.yaml` | `src-putnam-2005-A2-kedlaya` | https://kskedlaya.org/putnam-archive/2005.pdf ; https://kskedlaya.org/putnam-archive/2005s.pdf |
| `data/problems/putnam/putnam-2007-a6-admissible-triangulation-bound.yaml` | `src-putnam-2007-A6-kedlaya` | https://kskedlaya.org/putnam-archive/2007.pdf ; https://kskedlaya.org/putnam-archive/2007s.pdf |
| `data/problems/putnam/putnam-2012-b3-round-robin-winners-hall.yaml` | `src-putnam-2012-B3-kedlaya` | https://kskedlaya.org/putnam-archive/2012.pdf ; https://kskedlaya.org/putnam-archive/2012s.pdf |

## Почему добавлены

- Putnam 2002 B2: исходное условие является игрой на гранях полиэдрального графа; решение использует локальную структуру кубического полиэдрального графа и лемму о грани размера хотя бы 4.
- Putnam 2004 A5: стандартное решение из Kedlaya явно строит граф на клетках доски, оценивает число компонент через число ребер и монохромных 4-циклов. Подсказка про 2004 A5 подтвердилась.
- Putnam 2005 A2: ладейные обходы являются гамильтоновыми путями в решеточном графе `P_n square P_3`; Kedlaya solution также ссылается на литературу о Hamiltonian paths in rectangular grid graphs.
- Putnam 2007 A6: триангуляция переводится в плоский граф; ключевые шаги - формула Эйлера, подсчет степеней и удаление граничной цепочки.
- Putnam 2012 B3: хорошее стандартное решение - прямое построение двудольного графа "дни - команды" и применение теоремы Холла.

## Не добавлено / сомнительные случаи

- 2001 A4: раскраска клеток квадратной решетки. Решение алгебраическое, через матричные операции/четность; граф смежности клеток не несет основной идеи.
- 2002 A4: игра в determinant tic-tac-toe. Можно рисовать дерево вариантов игры, но это только дерево перебора, не математическая графовая модель задачи.
- 2003 A5: пути Дика. Это комбинаторика lattice paths; слово path здесь не про графовую структуру в существенном смысле базы.
- 2004 B3: в решении упоминается graph of `f(x)`, то есть график функции; исключено.
- 2006 B3: линейные разбиения конечного множества точек. Есть дуальность к расположению прямых и областям, а также связь с ориентированными матроидами, но графовая модель не является основной и была бы искусственной.
- 2007 A6 был добавлен; задачи 2007 A1/A2 с `graph` в извлеченном тексте не имеют отношения к теории графов.
- 2008 A/B задачи с lattice theory не добавлены: речь о решетках как частично упорядоченных множествах, не о графах.
- 2012 A6 и B5: в текстах решений встречается graph of a function/supporting line to graph; это графики функций, исключено.

## Идеи для relations

- `putnam-2002-b2-polyhedron-face-game-four-edge-face`: связать с `euler-formula-planar`, `planar-edge-bound`, задачами на кубические/полиэдральные графы и стратегические игры на гиперграфах.
- `putnam-2004-a5-random-checkerboard-components`: связать с `grid-boundary-components-coloring-lemma`, `euler-formula-planar`, задачами на компоненты связности в случайной раскраске и подсчет степеней/ребер.
- `putnam-2005-a2-rook-tours-grid-hamiltonian-paths`: связать с задачами на гамильтоновы пути/циклы в решеточных графах и биективное кодирование путей.
- `putnam-2007-a6-admissible-triangulation-bound`: связать с `euler-formula-planar`, `planar-edge-bound`, `planar-large-girth-degree-two-path`, задачами на дискретную кривизну и степень внутренних вершин в плоских триангуляциях.
- `putnam-2012-b3-round-robin-winners-hall`: связать с `hall-marriage-theorem`, `augmenting-path-matching-lemma`, задачами на системы различных представителей и покрытия дней/команд паросочетанием.

## Замечания для главного агента

- Все новые карточки используют `source_id` вида `src-putnam-YYYY-CODE-kedlaya`, поскольку решения брались из открытых Kedlaya PDFs. Записи в `data/sources/sources.yaml` не добавлялись по ограничению зоны работы.
- MAA Putnam Archive сверялся как официальный архивный вход; для лет 2000-2012 текущая страница MAA не дает таких удобных прямых ссылок, как Kedlaya archive.
