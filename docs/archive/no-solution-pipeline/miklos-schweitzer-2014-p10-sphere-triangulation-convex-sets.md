# miklos-schweitzer-2014-p10-sphere-triangulation-convex-sets

## Итог

Карточка была без решения. Найден опубликованный венгерский разбор в `Matematikai Lapok 2015`, в отчёте о Schweitzer Miklós Matematikai Emlékverseny 2014. В карточку добавлено русское ИИ-решение по этому разбору: выбираются точки для треугольных граней, ребрам триангуляции сопоставляются плоские отрезки между точками соседних граней, затем используется экстремальная точка выпуклой оболочки и пересечение луча с ломаной вокруг вершины.

## Найденные источники

- Официальная английская формулировка уже есть в карточке как `src-miklos-schweitzer-2014-p10-official`: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2014-eng.pdf.
- Опубликованный разбор: `Matematikai Lapok 2015`, `ML_15-1-beliv.pdf`, раздел `Jelentés a 2014. évi Schweitzer Miklós-emlékversenyről`, задача 10, PDF pages 84-86 / printed pages 84-86: https://real-j.mtak.hu/6518/2/ML_15-1-beliv.pdf.
- В том же отчёте указаны авторы задачи: Frenkel Péter и Kós Géza. Решение задачи 10 дано "Nagy Dániel megoldása alapján"; также указаны решившие Agoston Péter, Mészáros András, Nagy Dániel, Nagy János и по существу Agoston Tamás.

## Решение и теоремы

В карточку внесено элементарно-геометрическое решение из опубликованного разбора; внешняя теорема в самом решении не используется. В опубликованном тексте после решения есть замечание Csikós Balázs о многомерном обобщении через нерв семейства выпуклых множеств, хорошее покрытие и гомологии над `F_2`.

Оценка школьности: добавленное решение не является стандартной школьной задачей, но его можно читать как олимпиадную плоскую топологию без гомологий. Многомерное замечание через нерв/гомологии не школьное; если база будет собирать такие инструменты, стоит завести отдельную карточку-теорему про нерв хорошего покрытия или `d`-Leray-свойство нервов выпуклых множеств в `R^d`.

## Предлагаемый source entry

`data/sources/sources.yaml` не редактировался, потому что он вне зоны разрешённых правок. Точная предлагаемая запись:

```json
{
  "id": "src-matematikai-lapok-2015-schweitzer-2014-solutions",
  "type": "problem_and_solution",
  "title": "Matematikai Lapok 2015, Schweitzer Miklós Matematikai Emlékverseny 2014 solutions",
  "url": "https://real-j.mtak.hu/6518/2/ML_15-1-beliv.pdf",
  "browser_openable": true,
  "language": "hu",
  "official": false,
  "status": "source_verified",
  "preference_note": "Contains the published Hungarian report and solutions for Schweitzer 2014. Problem 10 is by Frenkel Péter and Kós Géza; the printed solution is based on Nagy Dániel's solution and appears on PDF pages 84-86 / printed pages 84-86."
}
```

## Предлагаемые relation entries

Новые связи в `relations.yaml` не добавлялись. Для текущего элементарного решения обязательной внешней карточки нет. Если позже появится карточка `nerve-theorem-good-cover` или `convex-set-nerves-are-d-leray`, можно добавить связь:

```json
{
  "from": "nerve-theorem-good-cover",
  "to": "miklos-schweitzer-2014-p10-sphere-triangulation-convex-sets",
  "type": "related_method",
  "confidence": 0.8,
  "status": "ai_draft",
  "note": "Опубликованный разбор содержит многомерное замечание: утверждение следует из гомологического рассуждения для нерва семейства выпуклых множеств."
}
```

## Изменения в карточке

- Добавлены авторы задачи `Frenkel Péter` и `Kós Géza`.
- Добавлено решение `sol-ai-published-segment-drawing` со статусом `ai_checked`.
- В `editorial.notes` зафиксированы найденный опубликованный разбор и причина, по которой новый `source_id` не добавлялся в карточку.
