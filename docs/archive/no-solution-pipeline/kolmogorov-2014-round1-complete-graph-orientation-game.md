# kolmogorov-2014-round1-complete-graph-orientation-game

## Что проверено

- Прочитаны `README.md`, `docs/ARCHITECTURE.md` и карточка задачи; формат карточки — JSON-совместимый YAML.
- Официальный `src-kolmogorov-2014-official` указывает на `https://turmath.ru/kolm/files/archive/kolm18.zip`. Архив был скачан во временную папку; в `kolm18/tur1_18.doc` найдена задача 7 высшей лиги с пометкой первоисточника `(Turkey JBMO TST 2014)`.
- В официальном архивном файле первого тура найдено условие, но не найден официальный разбор этой задачи.
- Внешний поиск нашел обсуждение задачи на Math StackExchange: `https://math.stackexchange.com/questions/842767/a-game-on-a-graph`. Там есть источник Turkey JBMO TST 2014 и несколько набросков; наиболее близкий к полному решению ответ использует рост ориентированной цепочки и подсчет вынужденных хорд.

## Итог по решению

Решение добавлено в карточку как `sol-ai-longest-chain-counting` с явной пометкой `ИИ-решение` в заголовке и `review_notes`.

Идея: первый игрок каждый ход может удлинить максимальную ориентированную цепочку, пока она не стала гамильтоновой. После 2002-го хода первого есть цепочка минимум на 2003 вершинах. Чтобы первый не замкнул цикл обратной хордой, второй должен был бы ориентировать все `C(2003,2)=2005003` ребра между вершинами этой цепочки. Но всего за 2002 раунда ориентировано не более `2002 + 1000*2002 = 2004002` ребер. Значит, свободная хорда остается, и первый следующим ходом замыкает ориентированный цикл.

Внешних тяжелых теорем не использовано. Лемма об удлинении цепочки является школьной: это тот же тип вставки вершины, что в стандартном доказательстве существования гамильтонова пути в турнире, но адаптированный к частично ориентированному полному графу. Отдельную новую карточку добавлять не обязательно: в базе уже есть близкая классическая карточка `tournament-hamiltonian-path`; если выносить, то скорее как короткую стандартную идею "вставка вершины в ориентированную цепочку".

## Источники

В карточке уже есть подходящий официальный источник:

```yaml
source_id: src-kolmogorov-2014-official
role: problem_statement_official
status: source_verified
```

Новый source entry для Math StackExchange можно добавить отдельно, если база допускает вторичные разборы:

```yaml
{
  "id": "src-math-stackexchange-842767-graph-orientation-game",
  "type": "secondary_solution",
  "title": "A game on a graph",
  "url": "https://math.stackexchange.com/questions/842767/a-game-on-a-graph",
  "browser_openable": true,
  "language": "en",
  "official": false,
  "status": "needs_human_review",
  "preference_note": "Community discussion of the Turkey JBMO TST 2014 graph orientation game; useful for the longest-chain counting idea, not an official source."
}
```

## Предлагаемые связи

`relations.yaml` не редактировался. Возможные связи:

```yaml
- from: kolmogorov-2014-round1-complete-graph-orientation-game
  to: kolmogorov-2014-round1-oriendiriya-road-orientation-game
  type: paired_variant
  confidence: 0.9
  note: "Обе задачи из КОЛМ 2014 про игру в ориентацию полного графа; в младшем варианте второй успевает поддерживать транзитивную ориентацию, а в варианте на 2014 вершинах первый выигрывает подсчетом хорд длинной цепочки."
- from: kolmogorov-2014-round1-complete-graph-orientation-game
  to: tournament-hamiltonian-path
  type: same_motif
  confidence: 0.65
  note: "Лемма решения использует ту же вставку вершины в ориентированную цепочку, что и стандартное доказательство гамильтонова пути в турнире."
```

## Валидация

Выполнено: `python tools\\validate.py`.

Результат: `OK: 565 problems, 673 relations, 9 comments, 591 sources, 29 definitions, 17 standard ideas, 32 import batches.`
