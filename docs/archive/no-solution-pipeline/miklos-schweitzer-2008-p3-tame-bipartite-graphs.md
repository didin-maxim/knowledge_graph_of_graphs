# miklos-schweitzer-2008-p3-tame-bipartite-graphs

## Итог

Карточка была без решения. Найден опубликованный венгерский разбор в `Matematikai Lapok 2009`: задача 3 указана как предложенная Tardos Gábor, ответ `alpha = 3/2`. В карточку добавлено самостоятельное русское ИИ-решение по этому разбору: конструкция с `Omega(n^{3/2})` рёбрами и верхняя оценка через разбиение рёбер на малые и большие.

## Найденные источники

- Официальная английская формулировка уже была в карточке: `src-miklos-schweitzer-2008-p3-official`, `https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2008-eng.pdf`.
- Опубликованный разбор: `Matematikai Lapok 2009`, PDF `https://real-j.mtak.hu/9404/1/MTA_MatematikaiLapok_2009.pdf`, раздел решений Schweitzer 2008, задача 3, PDF page 52 / printed page 50. В тексте указано: `3. feladat (Tardos Gábor)`, ответ `alpha=3/2`.

## Решение и теоремы

Внешние теоремы не использованы. Доказательство школьно-олимпиадное по технике: конструкция по остаткам и целой части, затем простая экстремальная оценка подсчётом малых и больших рёбер. Отдельную карточку-теорему добавлять не нужно; максимум можно вынести как стандартную идею `small_large_edge_split_for_ordered_extremal_graphs`, если база начнёт собирать такие приёмы.

## Предлагаемый source entry

`data/sources/sources.yaml` не редактировался, потому что он вне зоны разрешённых правок. Точная предлагаемая запись:

```json
{
  "id": "src-matematikai-lapok-2009-schweitzer-2008-solutions",
  "type": "problem_and_solution",
  "title": "Matematikai Lapok 2009, Schweitzer Miklós Matematikai Emlékverseny 2008 solutions",
  "url": "https://real-j.mtak.hu/9404/1/MTA_MatematikaiLapok_2009.pdf",
  "browser_openable": true,
  "language": "hu",
  "official": false,
  "status": "source_verified",
  "preference_note": "Contains the published Hungarian solution of Schweitzer 2008 Problem 3, proposed by Tardos Gábor; answer alpha=3/2. The solution is on PDF page 52 / printed page 50."
}
```

## Предлагаемые relation entries

Новые связи в `relations.yaml` не предлагаю: решение не использует внешнюю теорему и не был найден явный родственный объект в базе. Если позже появится карточка стандартной идеи про разбиение рёбер на малые/большие в упорядоченных экстремальных графах, можно добавить связь:

```json
{
  "from": "small-large-edge-split-ordered-extremal-graphs",
  "to": "miklos-schweitzer-2008-p3-tame-bipartite-graphs",
  "type": "method",
  "confidence": 0.8,
  "status": "needs_human_review",
  "note": "Верхняя оценка в задаче разбивает рёбра на малые и большие относительно упорядочения долей."
}
```

## Изменения в карточке

- Автор заменён с `?` на `Tardos Gábor`, статус `source_verified`.
- Добавлено решение `sol-ai-small-large-edges` со статусом `ai_checked`.
- В `editorial.notes` зафиксирован найденный источник и то, что новый `source_id` не добавлялся.
- `problem_profile.status` и `difficulty.status` переведены в `ai_checked`; `public_ready` оставлен `false`.

## Валидация

Выполнено: `python tools\validate.py`.

Результат: `OK: 565 problems, 673 relations, 9 comments, 591 sources, 29 definitions, 17 standard ideas, 32 import batches.`
