# Miklos Schweitzer 2005/1: x-high no-solution pass

Карточка: `data/problems/miklos-schweitzer/miklos-schweitzer-2005-p1-high-chromatic-defined-graph.yaml`

Дата прохода: 2026-05-05.

## Итог

Полное опубликованное решение задачи 2005/1 не найдено. Автор задачи также не найден: официальный problem PDF, индекс Szeged и страница Bolyai János Mathematical Society не указывают автора для задачи 1.

В карточке оставлено:

- `solutions: []`;
- `ideas: []`, потому что прежние идеи были только недоведенными направлениями;
- пометка `no-solution / непросто для ИИ` в `difficulty.comment` и `editorial.notes`;
- `editorial.public_ready: true`, потому что формулировка сверена с официальным источником, а единственная выявленная проблема - отсутствие опубликованного решения.

## Сверка формулировки и источников

- Официальный венгерский PDF: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2005.pdf. Задача 1 задает граф `G(a,b)` с вершинами `(i,f)`, где `i in [a]`, `f:[a]->[b]`; две вершины `(i,f)` и `(j,g)` смежны при `i != j`, когда `f(k) != g(k)` ровно для `k`, строго лежащих между `i` и `j`, а на остальных `k` функции совпадают. Требуется доказать, что для любого `c` найдутся `a,b`, при которых вершины `G(a,b)` нельзя правильно раскрасить в `c` цветов.
- Индекс Szeged: https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/index.html. Для 2005 года есть только ссылка `in Hungarian`; ссылки на решения в индексе появляются для 2009 и более новых выбранных лет, но не для 2005.
- Страница Bolyai János Mathematical Society: https://www.bolyai.hu/versenyek-schweitzer-miklos-emlekverseny/. На странице перечислены задачи/решения и результаты для новых лет; отдельного решения 2005/1 на странице не найдено.
- Results PDF Bolyai: https://www.bolyai.hu/files/Schweitzer_eredmenyei_osszes_2021-1.pdf. Для 2005 года указаны призеры, но не авторы задач и не решения.

Текущий `source_id` карточки `src-miklos-schweitzer-2005-p1-official` существует в `data/sources/sources.yaml`, имеет тип `statement`, язык `hu`, официальный статус и правильный URL. Общий source registry не редактировался.

## Поиск решения

Проверенные направления:

- точные фразы из венгерской формулировки: `"G(a,b)" "csúcsai" "színezhetők"`, `"f(k)" "g(k)" "szigorúan i és j között"`, `"csúcsok (i, f) alakúak"`;
- запросы по соревнованию: `"2005. évi Schweitzer Miklós" "1. feladat" megoldás`, `"Schweitzer Miklós" "2005" "1. feladat" "Megoldás"`, `"schweitzer-2005" "solution"`;
- английские/форумные запросы: `"Miklos Schweitzer" "2005" "G(a,b)" chromatic`, `"G(a,b)" "f(k)" "g(k)" "chromatic"`, `site:artofproblemsolving.com/community "G(a,b)" "chromatic"`;
- URL-гипотезы и поиски по возможному файлу решений: `"schweitzer-2005-meg"`, `"schweitzer-2005" "meg"`, `site:math.u-szeged.hu/tagok/mmaroti/schweitzer schweitzer-2005-meg.pdf`.

Результат: найден официальный problem PDF и нерелевантные материалы по хроматическим числам. Полного публичного решения, обсуждения на форумах или указания автора задачи не найдено.

## Tags, definitions, source refs

- Tags оставлены только как проверяемые по условию: `coloring`, `extremal_graph_theory`, `goal_existence`. Удалены `ramsey_theory`, `graph_model`, `goal_impossibility`, потому что они отражали недоведенные идеи или слишком общий методический ярлык.
- `definition_ids` теперь используют существующие определения `simple_graph` и `chromatic_number`.
- `statements.graph_theory` сделана самодостаточной: в ней явно повторена вершина и смежность графа `G(a,b)`, а не только короткая фраза про неограниченное хроматическое число.
- Новый source entry в карточку не добавлялся.

## Почему решение не добавлено

Задача утверждает существование явно заданного семейства треугольник-свободных по структуре графов с неограниченным хроматическим числом. Это похоже на область высокохроматических конструкций и сдвиговых/рамсеевских аргументов, но найденные источники не дают готового доказательства именно для этого `G(a,b)`.

Самостоятельные наброски через сдвиговые графы, интервальное различие функций, Рамсея/компактность или ориентации не доведены до проверенного доказательства. Поэтому они не внесены в базу.

## Предложенные связи

Общий `data/relations/relations.yaml` не редактировался. Убедительной связи уровня prerequisite/solution_transfer пока нет.

Низкоуверенная кандидатная связь для будущей ручной проверки:

```json
{
  "id": "rel-schweitzer-2005-p1-imc-2022-shift-high-chromatic",
  "from": "imc-2022-day1-p4-triples-chromatic-loglog",
  "to": "miklos-schweitzer-2005-p1-high-chromatic-defined-graph",
  "type": "same_motif",
  "distance": 4,
  "forward_text": "Обе задачи используют явно заданные конечные графы с хроматическим числом, растущим за счет сдвигово-интервального кодирования, но прямой перенос решения не установлен.",
  "backward_text": "Schweitzer 2005/1 может быть тематически связан с хроматическими сдвиговыми конструкциями IMC 2022 Day 1 P4, однако для текущего графа G(a,b) опубликованный или проверенный мост не найден.",
  "status": "needs_human_review",
  "confidence": 0.35
}
```

Если позже будет создана отдельная классическая карточка `shift-graphs-high-chromatic` или `explicit-triangle-free-high-chromatic-graphs`, связь лучше вести к ней, а не напрямую к IMC 2022.
