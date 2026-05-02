# IMC 2005-2014 graph problems audit

Дата: 2026-05-02.

Зона работы: добавлены только карточки в `data/problems/imc/` и этот отчёт. `data/sources/sources.yaml`, `data/relations`, `docs`, `viewer`, `tools` не редактировались.

## Созданные карточки

| Файл | source_id | Официальный URL |
| --- | --- | --- |
| `data/problems/imc/imc-2006-day2-p1-polygon-triangulation-parity.yaml` | `src-imc-2006-day2-p1-official` | https://www.imc-math.org.uk/imc2006/day2_solutions.pdf |
| `data/problems/imc/imc-2009-day1-p3-friendship-girth-five.yaml` | `src-imc-2009-day1-p3-official` | https://www.imc-math.org.uk/imc2009/imc2009-day1-solutions.pdf |
| `data/problems/imc/imc-2010-day2-p4-f2-adjacency-matrix-zero-entry.yaml` | `src-imc-2010-day2-p4-official` | https://www.imc-math.org.uk/imc2010/imc2010-day2-solutions.pdf |
| `data/problems/imc/imc-2011-day2-p2-tripartite-married-triples.yaml` | `src-imc-2011-day2-p2-official` | https://www.imc-math.org.uk/imc2011/imc2011-day2-solutions.pdf |
| `data/problems/imc/imc-2013-day1-p3-six-trips-cover-pairs.yaml` | `src-imc-2013-day1-p3-official` | https://www.imc-math.org.uk/imc2013/IMC2013-day1-solutions.pdf |
| `data/problems/imc/imc-2013-day2-p5-necklace-good-colorings-odd.yaml` | `src-imc-2013-day2-p5-official` | https://www.imc-math.org.uk/imc2013/IMC2013-day2-solutions.pdf |

## Не добавлено

- IMC 2005 Day 1 P2, https://www.imc-math.org.uk/imc2005/day1_solutions.pdf: это задача о подсчёте слов над трёхбуквенным алфавитом с локальными запретами. Возможна модель через конечный автомат/ориентированный граф переходов, но она выглядит технической оболочкой для рекурсии, а не существенной графовой задачей.
- IMC 2014 Day 1 P5, https://www.imc-math.org.uk/imc2014/IMC2014-day1-solutions.pdf: задача о самопересечениях ломаной с углами 60 градусов. В официальном решении основной объект — геометрическая классификация пересечений и подсчёт пар индексов; граф самопересечений был бы искусственным и не несёт основной идеи.

## Идеи для relations

- `imc-2006-day2-p1-polygon-triangulation-parity`: связать с карточками про планарные графы и триангуляции, особенно `euler-formula-planar` и задачами с индукцией по внешнепланарной структуре.
- `imc-2009-day1-p3-friendship-girth-five`: связать с `apmo-2010-p3-common-acquaintance-extremal`, а также с карточками про подсчёт степеней, диаметр 2, запрет треугольников/четырёхциклов и обхват.
- `imc-2010-day2-p4-f2-adjacency-matrix-zero-entry`: связать с задачами про матрицы смежности, чётность числа маршрутов и инварианты над `F_2`; близка к карточкам с `parity_coloring` и `graph_model`.
- `imc-2011-day2-p2-tripartite-married-triples`: связать с `hall-marriage-theorem`, `augmenting-path-matching-lemma` и задачами о совершенных паросочетаниях/факторах в плотных многодольных графах.
- `imc-2013-day1-p3-six-trips-cover-pairs`: связать с задачами о покрытии рёбер полного графа кликами, блочными конструкциями и двойным счётом.
- `imc-2013-day2-p5-necklace-good-colorings-odd`: связать с карточками о раскрасках циклов, запрете длинных одноцветных отрезков, рекурсиях по путям и периодичности по модулю 2.

## Замечания для главного агента

- Все карточки ссылаются на `source_id` вида `src-imc-YYYY-dayD-pP-official`, как было запрошено; записи в `data/sources/sources.yaml` ожидаются от главного агента.
- Для IMC 2010 Day 2 P4 выставлено `kind.secondary = ["graph_in_solution", "advanced"]`: исходная формулировка линейно-алгебраическая, но симметричная нулевая диагональ — ровно матрица смежности простого графа над `F_2`.
- В извлечённом тексте официального PDF для IMC 2013 Day 1 виден заголовок `IMC 2012`, но ссылка находится в официальном разделе IMC 2013 и сама задача соответствует IMC 2013 Day 1 P3.
