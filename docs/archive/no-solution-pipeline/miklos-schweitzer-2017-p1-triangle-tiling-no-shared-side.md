# Miklos Schweitzer 2017/1: разбиение квадрата на треугольники без общей стороны

Карточка: `data/problems/miklos-schweitzer/miklos-schweitzer-2017-p1-triangle-tiling-no-shared-side.yaml`

## Что проверено

- Формат сверялся по `README.md`, `docs/ARCHITECTURE.md`, `docs/AI_CARD_RULES.md` и соседним карточкам с `solutions[]`.
- Официальная англоязычная формулировка уже есть в реестре как `src-miklos-schweitzer-2017-p1-official`: [Problems of the Miklós Schweitzer Memorial Competition, 2017](https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2017-eng.pdf).
- Найден разбор KöMaL A.710: [Problem A. 710](https://www.komal.hu/feladat?a=feladat&f=A710&l=en). Это задача для правильного `n`-угольника, основанная на Schweitzer 2017; решение на венгерском доказывает невозможность при `n >= 4` тем же макроскопическим счетом.
- Найден более общий источник: Kupavskii, Pach, Tardos, [Tilings with noncongruent triangles](https://arxiv.org/abs/1711.04504), Theorem 6. Там доказано, что любой конечный треугольный тайлинг выпуклого `k`-угольника при `k >= 4` содержит две плитки с общей стороной.

## Что внесено

В карточку добавлено полное русское ИИ-решение `sol-ai-plane-graph-counting`. Доказательство самодостаточно: строится плоский граф разбиения, затем используются три счета:

- формула Эйлера дает `e = v + t - 1`;
- сумма углов дает `v <= t + 2`;
- взвешенный счет долей сторон дает `e >= 2t + 2`.

Последние два неравенства противоречат формуле Эйлера, поэтому конечного разбиения квадрата не существует.

## Внешние теоремы

Использована только формула Эйлера для связного плоского графа. Ее доказательство школьное/олимпиадное: можно доказывать удалением рёбер остовного дерева или индукцией по числу граней. Отдельная карточка с формулой Эйлера полезна, если в базе еще нет именно теоремной карточки; как минимум определение `planar_graph` уже существует и указано в решении.

Теорема Kupavskii--Pach--Tardos не используется как черный ящик в карточке; она служит внешней сверкой и более общей версией. Ее Theorem 6 имеет школьно читаемое доказательство, близкое к внесенному решению, и ее стоит добавить отдельной карточкой как обобщение на выпуклые `k`-угольники.

## Источники

Новые `source_id` в карточку не добавлялись, потому что соответствующих записей нет в общем `data/sources/sources.yaml`, а общий реестр редактировать нельзя.

Предлагаемые source entries:

```json
{
  "id": "src-komal-a710-triangle-tiling-no-shared-side",
  "type": "solution_notes",
  "title": "KöMaL Problem A.710, regular n-gon partition into triangles with no shared side",
  "url": "https://www.komal.hu/feladat?a=feladat&f=A710&l=en",
  "browser_openable": true,
  "language": "hu",
  "official": false,
  "status": "source_verified",
  "preference_note": "Secondary version based on Miklós Schweitzer 2017; contains a concise Hungarian solution by planar graph counting."
}
```

```json
{
  "id": "src-kupavskii-pach-tardos-tilings-noncongruent-triangles",
  "type": "research_paper",
  "title": "Andrey Kupavskii, János Pach, Gábor Tardos, Tilings with noncongruent triangles",
  "url": "https://arxiv.org/abs/1711.04504",
  "browser_openable": true,
  "language": "en",
  "official": false,
  "status": "source_verified",
  "preference_note": "Theorem 6 proves the general convex k-gon version; for k=4 it gives the Schweitzer 2017 P1 square case."
}
```

Замечание для будущей чистки: текущий `src-miklos-schweitzer-2017-p1-official` имеет `type: "problem_and_solution"`, но проверенный PDF содержит только условия. Если типы используются строго, лучше заменить на `statement` или аналогичный локальный тип.

## Предложенные связи

Общий `relations.yaml` не редактировался. Если будет создана карточка для общего результата Theorem 6, можно добавить связь:

```json
{
  "id": "rel-schweitzer-2017-p1-convex-polygon-triangle-tiling",
  "from": "miklos-schweitzer-2017-p1-triangle-tiling-no-shared-side",
  "to": "convex-polygon-triangle-tiling-no-shared-side",
  "type": "specialization",
  "distance": 1,
  "forward_text": "Задача о квадрате является случаем k=4 общего утверждения: выпуклый k-угольник при k >= 4 нельзя конечно разбить на треугольники так, чтобы никакие два не имели общей полной стороны.",
  "backward_text": "Общий результат для выпуклых k-угольников содержит Schweitzer 2017/1 как частный случай k=4.",
  "status": "needs_human_review",
  "confidence": 0.86
}
```
