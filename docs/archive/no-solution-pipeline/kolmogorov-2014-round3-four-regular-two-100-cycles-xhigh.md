# kolmogorov-2014-round3-four-regular-two-100-cycles x-high

## Итог

Решение в карточку не добавлено: `solutions: []` оставлено намеренно. Задача помечена как `непросто_для_ИИ` / no-solution: официальная формулировка проверена, но опубликованное олимпиадное решение или авторский разбор не найден, а внешний структурный маршрут не является самодостаточным школьным доказательством для `solutions[]`.

В карточке можно считать проверенными условие, автора, `source_id`, базовые `definition_ids` и текущие теги. `editorial.public_ready` поставлен в `true`, потому что сомнений в формулировке/источниках после x-high сверки не осталось; единственный открытый блокер - отсутствие полного решения.

## Официальная Сверка

- Официальные refs карточки корректны: `src-kolmogorov-2014-official` указывает на `https://turmath.ru/kolm/files/archive/kolm18.zip`, `src-kolmogorov-archive` - на `https://turmath.ru/kolm/archive.php`.
- Официальный `kolm18.zip` скачан во временную папку и просмотрен. Внутри есть `kolm18/tur3_18.doc`; отдельного файла решений для этой задачи в zip-листинге не обнаружено.
- Старый `.doc` был извлечён через `olefile` и piece-table старого Word-документа, потому что Word/LibreOffice/antiword локально не установлены. Извлечённый текст подтверждает: "Третий тур 06.11.14. Высшая лига", задача 10, автор `(Д. Карпов)`.
- Официальное условие совпадает по смыслу с карточкой: связный 4-регулярный граф на 200 вершинах, каждое ребро входит в треугольник, удаление любых трёх вершин сохраняет связность; требуется два непересекающихся простых 100-цикла.

## Поиск Решения

Проверены точные русские запросы по фрагментам условия, запросы с автором `Д. Карпов`, `Дмитрий Карпов`, `Кубок Колмогорова 2014`, `tur3_18`, а также англоязычные запросы про `4-regular graph every edge in a triangle two disjoint cycles`. Отдельно проверялись AoPS, Math StackExchange и MathOverflow. Готового решения задачи не найдено.

Найден релевантный, но не олимпиадный источник: MathOverflow-вопрос Gordon Royle "4-regular graphs with every edge in a triangle" и статья Florian Pfender, Gordon F. Royle, "Quartic graphs with every edge in a triangle", arXiv:1308.0081. Их классификация даёт правдоподобный внешний маршрут: при 4-связности запрещаются замены треугольников на `K_{1,1,3}` из-за 3-вершинного разреза; line-graph случай для кубического графа несовместим с 200 вершинами; остаётся квадрат 200-цикла, где чётные и нечётные вершины дают два 100-цикла. Но этот маршрут опирается на исследовательскую структурную теорему, а не на самодостаточное доказательство в карточке, поэтому в `solutions[]` он не добавлен.

## Tags / Definitions / Sources

- `definition_ids` в statement проверены: `simple_graph`, `cycle`, `degree`, `connected_graph` есть в `data/definitions/definitions.yaml`.
- Текущие теги `connectivity`, `extremal_graph_theory`, `goal_proof` есть в `data/taxonomy/tags.yaml`; новых taxonomy-тегов не добавлялось.
- В `problem_profile.objects` добавлены более явные поисковые объекты `regular_graph`, `triangle`, `vertex_connectivity`, `disjoint_cycles`.
- В `problem_profile.keywords` добавлены `two_disjoint_100_cycles`, `непросто_для_ИИ`, `no_public_solution_found`.
- Новые `source_id` не добавлялись, потому что для Pfender-Royle пришлось бы править общий `data/sources/sources.yaml`, а по задаче разрешены только карточка и этот отчёт.

## Предложения По Связям

Общий файл связей не редактировался.

- Уже существующая связь `rel-kolm-2014-triangle-routes-four-regular-cycles` с `kolmogorov-2014-round3-city-triangle-routes` выглядит уместной как `same_motif`: обе задачи КОЛМ-2014 используют условие "каждое ребро лежит в треугольнике", но методы пока не доказаны общими.
- Если будет заведена отдельная карточка-теорема по Pfender-Royle `quartic-graphs-every-edge-in-triangle-structure`, то для текущей задачи стоит добавить `prerequisite` или `solution_uses` от этой теоремы к `kolmogorov-2014-round3-four-regular-two-100-cycles`.
- Если появится самодостаточная школьная лемма "4-связный простой 4-регулярный граф с triangle property и числом вершин не кратным 3 является квадратом цикла", её лучше завести отдельной карточкой и связать как `prerequisite`; без такой леммы relation уровня `solution_transfer` добавлять рано.

## Проверенные Источники

- Official archive page: https://turmath.ru/kolm/archive.php
- Official 2014 archive zip: https://turmath.ru/kolm/files/archive/kolm18.zip
- MathOverflow related discussion: https://mathoverflow.net/questions/84783/4-regular-graphs-with-every-edge-in-a-triangle
- Pfender-Royle paper: https://arxiv.org/abs/1308.0081
- Royle blog note: https://symomega.wordpress.com/2013/08/02/regular-graphs-triangles-and-mathoverflow/
