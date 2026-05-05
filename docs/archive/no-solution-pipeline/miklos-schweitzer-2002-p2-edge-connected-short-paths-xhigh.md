# Miklos Schweitzer 2002/2: x-high no-solution pass

Карточка: `data/problems/miklos-schweitzer/miklos-schweitzer-2002-p2-edge-connected-short-paths.yaml`

Дата прохода: 2026-05-05.

## Итог

Полное опубликованное решение задачи 2002/2 не найдено. Автор задачи также не найден: официальный problem PDF, индекс Szeged и страница Bolyai János Mathematical Society не указывают автора для задачи 2.

В карточке оставлено:

- `solutions: []`;
- `ideas: []`, потому что предыдущие идеи были только недоведенными направлениями;
- пометка `no-solution / непросто для ИИ`;
- `editorial.public_ready: true`, потому что единственная выявленная проблема - сложность и отсутствие опубликованного решения, а не сомнительность формулировки.

## Сверка формулировки и источников

- Официальный английский PDF: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2002-eng.pdf. В нем задача 2 формулируется как утверждение о простом `k`-edge-connected графе на `n` вершинах и `k` edge-disjoint `u-v` paths длины не более `20n/k` ребер.
- Индекс Szeged: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/index.html. Для 2002 года есть Hungarian и English PDFs, но нет ссылки на solution; ссылки на решения в индексе появляются только для части более поздних лет.
- Страница Bolyai János Mathematical Society: https://www.bolyai.hu/versenyek-schweitzer-miklos-emlekverseny/. Она содержит задачи/решения и результаты для новых лет, но не дает решения 2002/2.
- Results PDF Bolyai: https://www.bolyai.hu/files/Schweitzer_eredmenyei_osszes_2021-1.pdf. Для 2002 года указаны призеры, но не авторы задач и не решения.

Текущий `source_id` карточки `src-miklos-schweitzer-2002-p2-official` существует в `data/sources/sources.yaml` и указывает на правильный официальный PDF. В общем source registry поле `type` сейчас стоит `problem_and_solution`, хотя проверенный PDF содержит только условия; общий файл не редактировался, но для будущей чистки лучше заменить тип на `statement` / `official_archive` или аналогичный локальный тип.

## Поиск решения

Проверенные направления:

- точные английские фразы: `"20n/k" "edge-disjoint paths"`, `"Let G be a simple k-edge-connected graph"`, `"there exist k edge-disjoint paths from u to v each having at most"`;
- запросы по соревнованию: `"Miklos Schweitzer 2002 problem 2"`, `"Miklos Schweitzer 2002" "edge-disjoint paths"`, `"schweitzer-2002-eng.pdf" solution`;
- форумные/AoPS-запросы: `site:artofproblemsolving.com/community "20n/k"`, `site:artofproblemsolving.com/community "edge-disjoint paths" "Miklos Schweitzer"`;
- венгерские запросы по возможной формулировке: `"k-élösszefüggő"`, `"legfeljebb 20n"`, `"2002. évi Schweitzer" "megoldás"`;
- общий поиск по близким теоремам: `"short edge-disjoint paths" "k-edge-connected"`, `"edge-disjoint paths" "O(n/k)" "k-edge-connected"`.

Результат: найден только официальный problem PDF и нерелевантные материалы по disjoint paths / low-diameter tree packing / expander routing. Эти материалы не являются решением задачи Schweitzer 2002/2 и не дают готового олимпиадного доказательства с константой 20.

## Tags, definitions, source refs

- Tags сокращены до `connectivity` и `goal_existence`: методические теги `augmenting_path` и `cut_counting` были привязаны к недоведенным идеям и удалены.
- `definition_ids` дополнены существующим `connected_graph`; в карточке теперь используются только существующие определения `simple_graph`, `connected_graph`, `graph_cut`, `path`.
- Полезная будущая чистка definitions registry: добавить отдельные определения `k_edge_connected_graph` и `edge_disjoint_paths`, потому что сейчас они есть в `problem_profile.objects`, но не как reusable definitions.
- Source ref в statement корректен: `src-miklos-schweitzer-2002-p2-official`. Новый source entry в карточку не добавлялся.

## Почему решение не добавлено

Задача выглядит как количественное усиление реберной версии теоремы Менгера: обычный Менгер дает `k` реберно-непересекающихся путей, но не ограничивает длину каждого пути.

Публичный разбор не найден, а самостоятельные наброски через BFS-слои, минимальную упаковку путей, потоки/разрезы или диаметр не дают проверенного доказательства одновременного ограничения длины всех `k` путей. Поэтому никакие такие идеи не записаны в базу.

## Предложенные связи

Общий `data/relations/relations.yaml` не редактировался. Конкретная связь для будущего внесения:

```json
{
  "id": "rel-menger-theorem-schweitzer-2002-p2-short-paths",
  "from": "menger-theorem",
  "to": "miklos-schweitzer-2002-p2-edge-connected-short-paths",
  "type": "prerequisite",
  "distance": 2,
  "forward_text": "Теорема Менгера дает базовое существование k реберно-непересекающихся u-v путей при k-рёберной связности; задача Schweitzer 2002/2 требует дополнительного количественного контроля длины каждого пути.",
  "backward_text": "Задача Schweitzer 2002/2 усиливает реберную версию Менгера: нужно выбрать не просто k реберно-непересекающихся путей, а короткую упаковку с верхней оценкой 20n/k.",
  "status": "needs_human_review",
  "confidence": 0.8
}
```

Если позже будет создана отдельная карточка `edge-menger-theorem`, эту связь лучше перенести с `menger-theorem` на нее и поднять confidence.
