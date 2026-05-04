# Miklos Schweitzer 2012/10: черный граф диаграммы узла

Карточка: `data/problems/miklos-schweitzer/miklos-schweitzer-2012-p10-knot-black-graph-spanning-trees.yaml`

## Что проверено

- Формат карточки сверялся по `README.md`, `docs/ARCHITECTURE.md`, `docs/AI_CARD_RULES.md` и соседним отчётам `docs/archive/no-solution-pipeline/`.
- Официальный PDF с условием уже зарегистрирован как `src-miklos-schweitzer-2012-p10-official`: https://www.math.u-szeged.hu/~mmaroti/schweitzer/schweitzer-2012-eng.pdf.
- В официальном PDF есть только условие задачи 10; опубликованного официального решения в нём нет.
- Дополнительный поиск нашёл перепечатку условия в блоге Beni Bogosel, но без решения: https://mathproblems123.wordpress.com/tag/miklos-schweitzer/.
- Готовый разбор самой задачи не найден. Для пункта (b) найден подходящий внешний результат: Jun Ge, Lianzhu Zhang, "Determinant of links, spanning trees, and a theorem of Shank", Journal of Knot Theory and Its Ramifications 25(09), 2016, DOI 10.1142/S0218216516410054.

## Что добавлено

В карточку добавлено `solution-ai-shank-small-tait-graphs` со статусом `ai_checked` и явной редакционной пометкой "ИИ-решение".

Содержание решения:

- используется теорема Шенка: для Tait-графа связной диаграммы ссылки диаграмма имеет один компонент тогда и только тогда, когда число остовных деревьев Tait-графа нечётно;
- пункт (b) следует сразу, потому что узел имеет ровно один компонент;
- в пункте (a) остаются только случаи `tau = 1` и `tau = 3`;
- `tau = 1` даёт Tait-граф-дерево с nugatory-перекрёстками, то есть тривиальный узел;
- `tau = 3` после удаления мостовых/петельных nugatory-частей даёт ядро: треугольник или две вершины с тремя параллельными рёбрами; соответствующий трёхперекрёстковый twist-shadow задаёт либо тривиальный узел, либо правый/левый трилистник.

Итоговая классификация в карточке: тривиальный узел и два хиральных трилистника; если в локальной конвенции зеркальные трилистники не различаются, это просто "трилистник".

## Внешняя теорема

Использована теорема Шенка о Tait-графах и нечётности числа остовных деревьев. В статье Ge-Zhang она сформулирована как: ссылка имеет один компонент тогда и только тогда, когда число остовных деревьев её Tait-графа нечётно.

Оценка школьности: сама формулировка очень олимпиадно выглядит, но доказательство не совсем школьное, потому что требует либо аккуратной графовой теории плоских медиальных графов/left-right paths, либо базовых инвариантов узлов через Kauffman/Jones/determinant. Для базы стоит добавить отдельную карточку-теорему, потому что она ровно соединяет плоские графы и диаграммы узлов и может понадобиться в других задачах.

Предлагаемый id карточки-теоремы: `shank-tait-graph-spanning-tree-parity`.

## Источники

Новый источник в карточку не добавлялся, потому что подходящего `source_id` для статьи Ge-Zhang в `data/sources/sources.yaml` не найден, а общий реестр источников в рамках этой карточки не редактировался.

Предлагаемый source entry:

```json
{
  "id": "src-ge-zhang-2016-determinant-links-spanning-trees-shank",
  "type": "article",
  "title": "Determinant of links, spanning trees, and a theorem of Shank",
  "url": "https://doi.org/10.1142/S0218216516410054",
  "browser_openable": true,
  "language": "en",
  "official": false,
  "status": "source_verified",
  "preference_note": "Используется для теоремы Шенка: диаграмма ссылки имеет один компонент тогда и только тогда, когда число остовных деревьев Tait-графа нечётно."
}
```

Дополнительный неофициальный источник только для перепечатки условия, если когда-нибудь понадобится:

```json
{
  "id": "src-bogosel-miklos-schweitzer-2012-problems",
  "type": "statement",
  "title": "Beni Bogosel blog, Miklos Schweitzer 2012 Problems",
  "url": "https://mathproblems123.wordpress.com/2013/01/04/miklos-schweitzer-2012-problems/",
  "browser_openable": true,
  "language": "en",
  "official": false,
  "status": "source_verified",
  "preference_note": "Неофициальная перепечатка условий; решения задачи 10 не содержит."
}
```

## Предложенные связи

Общий `relations.yaml` не редактировался. Если будет добавлена отдельная карточка теоремы Шенка, предлагаю связь:

```json
{
  "id": "rel-schweitzer-2012-p10-shank-tait-parity",
  "from": "miklos-schweitzer-2012-p10-knot-black-graph-spanning-trees",
  "to": "shank-tait-graph-spanning-tree-parity",
  "type": "prerequisite",
  "distance": 1,
  "forward_text": "Решение задачи Schweitzer 2012/10 использует теорему Шенка: Tait-граф диаграммы узла имеет нечётное число остовных деревьев.",
  "backward_text": "Задача Schweitzer 2012/10 является прямым применением теоремы Шенка и дополнительно требует классифицировать случаи с 1 или 3 остовными деревьями.",
  "status": "needs_human_review",
  "confidence": 0.9
}
```

## Риски ревью

- Самый чувствительный шаг: соответствие мостов/петель Tait-графа nugatory-перекрёсткам и их удаление без изменения типа узла.
- Второй шаг для человеческой проверки: краткая классификация трёхперекрёсткового ядра как замыкания двухниточной косы `sigma_1^m`.
- Поэтому `editorial.review_status` оставлен `needs_human_review`, несмотря на добавленное ИИ-решение.
