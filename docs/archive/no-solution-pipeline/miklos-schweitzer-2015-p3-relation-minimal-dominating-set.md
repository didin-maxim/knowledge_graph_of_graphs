# miklos-schweitzer-2015-p3-relation-minimal-dominating-set

## Что проверено

- Прочитаны `README.md`, `docs/ARCHITECTURE.md`, `docs/AI_CARD_RULES.md` и целевая карточка; формат карточки — JSON-совместимый YAML.
- В карточке уже был источник `src-miklos-schweitzer-2015-p3-official`, указывающий на английский PDF с условиями: `https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2015-eng.pdf`.
- В интернете найден официальный венгерский PDF с решениями: `https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2015-meg.pdf`. В нём эта задача идёт как `43. feladat`; постановщик указан как `Zádori László`, а решение помечено как основанное на решениях нескольких участников.
- Дополнительно найден блог Beni Bogoșel с перепечаткой условий 2015 года: `https://mathproblems123.wordpress.com/2015/10/31/miklos-schweitzer-2015-problems/`. Для решения он не использовался.

## Итог по решению

Решение добавлено в карточку как `sol-ai-private-witnesses-official` с пометкой `ИИ-решение` в заголовке и `review_notes`.

Основная идея: из минимальности `B` для каждого `b_i` получается либо внешний частный свидетель `c_i`, связанный только с `b_i`, либо сам `b_i` не связан ни с одним другим элементом `B`. Для пар с внешними свидетелями выбирается конец направленного ребра; условие задачи запрещает стрелки между выбранными концами, иначе два разных элемента указывали бы в одну цель и вынуждали запрещённую связь с чужим частным свидетелем. Вместе с оставшимися изолированными `b_i` это даёт независимое множество размера `|B|`, поэтому `|B| <= k`.

Внешних тяжёлых теорем не использовано. Лемма о частных свидетелях минимального доминирующего множества школьная: это прямое раскрытие минимальности по включению плюс одно применение условия задачи. Отдельную карточку добавлять не обязательно; если такой мотив начнёт часто повторяться, его можно вынести как стандартную идею `private_witnesses_for_minimal_dominating_set`.

## Источники

В карточке оставлен существующий источник для английского условия:

```yaml
source_id: src-miklos-schweitzer-2015-p3-official
role: official_statement
status: source_verified
```

Для официального PDF с решениями в общем реестре пока нет `source_id`, поэтому `data/sources/sources.yaml` не редактировался. Предлагаемый source entry:

```yaml
{
  "id": "src-miklos-schweitzer-2015-official-solutions-hu",
  "type": "problem_and_solution",
  "title": "A 2015. évi Schweitzer Miklós Matematikai Emlékverseny feladatai és megoldásai",
  "url": "https://www.math.u-szeged.hu/tagok/mmaroti/schweitzer/schweitzer-2015-meg.pdf",
  "browser_openable": true,
  "language": "hu",
  "official": true,
  "status": "source_verified",
  "preference_note": "Official Hungarian statements and solutions for the 2015 Miklós Schweitzer Memorial Competition; Problem 3 appears as 43. feladat, setter Zádori László, solution credited to multiple contestants."
}
```

Опционально стоит проверить существующую запись `src-miklos-schweitzer-2015-p3-official`: сейчас она имеет тип `problem_and_solution`, но URL ведёт на английский PDF только с условиями.

## Предлагаемые связи

`relations.yaml` не редактировался. Возможные слабые связи для ручного ревью:

```yaml
- from: miklos-schweitzer-2015-p3-relation-minimal-dominating-set
  to: spbmo-2014-10-p7-digraph-no-odd-cycles-dominating-independent
  type: same_motif
  confidence: 0.5
  note: "Обе задачи связаны с существованием/оценкой независимого доминирующего множества в ориентированном графе, но условия и техника доказательства разные."
- from: miklos-schweitzer-2015-p3-relation-minimal-dominating-set
  to: spbmo-1997-9-p27-common-acquaintance-dominating-set
  type: same_motif
  confidence: 0.35
  note: "Общий мотив доминирования через отношение смежности/знакомства; связь тематическая, не перенос решения."
```

## Валидация

Выполнено после правки карточки: `python tools\\validate.py`.

Результат: `OK: 565 problems, 673 relations, 9 comments, 591 sources, 29 definitions, 17 standard ideas, 32 import batches.`

После создания отчёта команда `python tools\\validate.py` была запущена ещё раз и упала до проверок source_id на нецелевом файле:

```text
data\problems\miklos-schweitzer\miklos-schweitzer-2017-p1-triangle-tiling-no-shared-side.yaml
Invalid \escape: line 112 column 1346
```

Этот файл не относится к разрешённой зоне правок и не редактировался. Целевая карточка отдельно проверена командой `python -m json.tool data\\problems\\miklos-schweitzer\\miklos-schweitzer-2015-p3-relation-minimal-dominating-set.yaml`.
