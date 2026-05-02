# Miklos Schweitzer 2009-2016 graph audit

Дата: 2026-05-02.

Основной индекс: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/index.html

## Добавленные карточки

- `miklos-schweitzer-2009-p1-k17-edge-coloring-cards.yaml` - 2009 P1, раскраски ребер `K_17`; источник: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2009-eng.pdf
- `miklos-schweitzer-2009-p2-smooth-difference-graphs.yaml` - 2009 P2, граф разностей на целых числах; источник: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2009-eng.pdf
- `miklos-schweitzer-2010-p2-infinite-vertex-transitive-perfect-matching.yaml` - 2010 P2, совершенное паросочетание в счетном вершинно-транзитивном графе; источник: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2010-eng.pdf
- `miklos-schweitzer-2011-p2-min-degree-monochromatic-connected-subgraph.yaml` - 2011 P2, большая одноцветная связная компонента; источники: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2011-meg.pdf и английский перевод https://mathproblems123.wordpress.com/2012/03/06/miklos-schweitzer-2011/
- `miklos-schweitzer-2012-p3-two-colored-k-chromatic-tree.yaml` - 2012 P3, одноцветное дерево в 2-раскрашенном `k`-хроматическом графе; источник: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2012-eng.pdf
- `miklos-schweitzer-2012-p10-knot-black-graph-spanning-trees.yaml` - 2012 P10, черный граф диаграммы узла и остовные деревья; источник: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2012-eng.pdf
- `miklos-schweitzer-2014-p10-sphere-triangulation-convex-sets.yaml` - 2014 P10, триангуляция сферы и выпуклые множества; источник: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2014-eng.pdf
- `miklos-schweitzer-2015-p2-van-der-corput-rectangle-graph-coloring.yaml` - 2015 P2, геометрический граф на последовательности Ван дер Корпута; источник: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2015-eng.pdf
- `miklos-schweitzer-2015-p3-relation-minimal-dominating-set.yaml` - 2015 P3, бинарное отношение как ориентированный граф; источник: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2015-eng.pdf
- `miklos-schweitzer-2016-p2-complete-graph-collinear-edge-labels.yaml` - 2016 P2, метки ребер полного графа; источник: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2016-eng.pdf

## Пропущенные и сомнительные

- 2009 P6 про системы Штейнера не добавлена: это естественная инцидентная структура/гиперграф, но задача в основном групповая, без самодостаточной графовой постановки.
- 2013: по английскому PDF содержательных графовых задач не найдено.
- 2014 P1 про разделяющие семейства и P3 про пустые треугольники не добавлены: возможны вспомогательные графовые модели, но они выглядят искусственными для базы графовых задач.
- 2015 P6 про группы перестановок не добавлена: графовые модели возможны, но условие не графовое и не дает самостоятельной графовой задачи.
- 2016 P8 про разбиение прямоугольника не добавлена: можно построить граф смежности/электрическую сеть, но в условии граф не задан явно, а графовая модель не является самодостаточной без существенной новой теории.

## Замечания по языку и решениям

- Английские PDF доступны для 2009, 2010, 2012, 2013, 2014, 2015, 2016. Для 2011 в индексе есть венгерское условие и венгерский отчет с решениями; английская формулировка 2011 P2 взята из публичного перевода Beni Bogosel и сверена с венгерским отчетом.
- Для большинства карточек добавлены только формулировка и идеи со статусом `needs_human_review`, потому что официальные решения отсутствуют в английском виде или требуют уверенного чтения венгерского отчета.
- Полное решение добавлено для 2011 P2, так как венгерский отчет содержит короткое решение через разрез и подсчет степеней.
- Для 2012 P3 добавлена стандартная идея решения, но карточка оставлена `needs_human_review` до сверки с официальным решением.
- Для 2016 P2 требуется ручная проверка фразы о прообразе точки: в карточке она интерпретирована как связность соответствующего остовного подграфа на всем множестве вершин.
