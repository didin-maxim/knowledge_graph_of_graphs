# miklos-schweitzer-2016-p2-complete-graph-collinear-edge-labels

## Краткий итог

Карточка была без решения. Официальный разбор именно Schweitzer 2016 P2 в открытом поиске не найден; найден официальный PDF с условием и школьная адаптация KöMaL A.683 для случая плоскости.

Добавлено ИИ-решение: если образ неколлинеарен, выбираем прямую через две точки образа и перекрашиваем исходные точки в три абстрактных цвета: одна выбранная точка, остальные точки этой прямой, точки вне прямой. Любая исходная коллинеарная тройка дает нерадужный треугольник, а связность исходных прообразов сохраняет связность трех новых цветовых классов. Это противоречит лемме Галлаи: в раскраске полного графа без радужных треугольников не могут быть три связных остовных цветовых класса.

## Найденные источники

- Официальный PDF уже указан в карточке как `src-miklos-schweitzer-2016-p2-official`: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2016-eng.pdf.
- KöMaL A.683, December 2016, формулировка адаптации задачи для `\mathbb R^2`: https://www.komal.hu/feladat?a=feladat&f=A683&l=en.
- Опубликованного решения/официального разбора по точной формулировке в быстром поиске не найдено.

## Внешняя теорема

Использована лемма Галлаи о раскрасках полного графа без радужных треугольников, точнее ее следствие: если каждый использованный цвет образует связный остовный подграф, то использовано не более двух цветов.

Оценка школьности: доказательство леммы через стандартное разбиение Галлаи является элементарным, но не совсем коротким; для школьной базы лучше добавить отдельную карточку-теорему или стандартную идею. Тогда текущее решение станет полностью прозрачным: геометрическая часть короткая, а вся графовая нагрузка будет вынесена в отдельный reusable-факт.

## Предлагаемые source entries

Не редактировал `data/sources/sources.yaml`, потому что это вне зоны разрешенных правок. Для KöMaL можно добавить:

```json
{
  "id": "src-komal-a683-2016",
  "type": "problem_statement",
  "title": "KöMaL Problem A.683, December 2016",
  "url": "https://www.komal.hu/feladat?a=feladat&f=A683&l=en",
  "browser_openable": true,
  "language": "en",
  "official": true,
  "status": "source_verified",
  "preference_note": "KöMaL adaptation based on Miklós Schweitzer 2016 Problem 2; states the planar version and contest statistics, but no solution text is visible."
}
```

Для леммы Галлаи, если будет отдельная карточка:

```json
{
  "id": "src-gallai-transitiv-orientierbare-graphen-1967",
  "type": "research_paper",
  "title": "T. Gallai, Transitiv orientierbare Graphen",
  "url": "https://doi.org/10.1007/BF02020961",
  "browser_openable": true,
  "language": "de",
  "official": false,
  "status": "needs_human_review",
  "preference_note": "Classical source for Gallai colorings / rainbow-triangle-free complete graph colorings; source metadata should be verified before adding."
}
```

## Предлагаемые relation entries

Не редактировал `data/relations/relations.yaml`. После добавления отдельной карточки `gallai-coloring-no-rainbow-triangle-connected-colors` можно добавить:

```json
{
  "id": "rel-gallai-coloring-miklos-schweitzer-2016-p2",
  "from": "gallai-coloring-no-rainbow-triangle-connected-colors",
  "to": "miklos-schweitzer-2016-p2-complete-graph-collinear-edge-labels",
  "type": "prerequisite",
  "distance": 1,
  "forward_text": "Лемма Галлаи исключает трехцветную абстрактную раскраску без радужных треугольников, если все три цветовых класса связны и остовны.",
  "backward_text": "Задача Schweitzer 2016 P2 сводит неколлинеарный образ к такой трехцветной раскраске: одна точка на выбранной прямой, остальные точки этой прямой и точки вне прямой.",
  "anchors": {
    "to_solution_id": "sol-ai-gallai-reduction"
  },
  "status": "ai_draft",
  "confidence": 0.92
}
```

## Изменения в карточке

- Добавлено решение `sol-ai-gallai-reduction` со статусом `ai_checked`.
- В `editorial.notes` зафиксировано, что это ИИ-решение и что лемму Галлаи лучше вынести отдельно.
