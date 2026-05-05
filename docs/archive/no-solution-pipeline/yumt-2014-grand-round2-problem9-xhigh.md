# yumt-2014-grand-round2-problem9: very-high no-solution pass

Дата прохода: 2026-05-05.

## Итог

Полное опубликованное решение не найдено. В карточке оставлено `solutions: []`, а `ideas` очищено до `[]`, чтобы не хранить недоведённые подходы в базе.

Карточка помечена как `no_public_solution_found` / `непросто_для_ИИ`. `editorial.public_ready` поставлен в `true`: официальная формулировка подтверждена, source refs / definitions / tags сверены, и единственный выявленный блокер - отсутствие опубликованного решения или самодостаточного строгого доказательства.

## Официальная сверка

- Официальная страница турнира: https://adygmath.ru/turnir14.html. Она содержит ссылку на `/content/files/smena2014/2turgrand.pdf`.
- Официальный PDF из source registry: `src-yumt-2014-grand-round2-problem9-official`, https://adygmath.ru/content/files/smena2014/2turgrand.pdf.
- PDF заново скачан через `curl`; HTTP-ответ `200 OK`, `Content-Type: application/pdf`, `Content-Length: 123350`, `Last-Modified: Mon, 22 Sep 2014 17:28:57 GMT`.
- Текст извлечён локально через `pypdf`. Страница 1 подтверждает: Девятый Южный математический турнир, ВДЦ "Орлёнок", 20-26.09.2014, Гранд-лига, 2 тур, 22.09.2014, задача 9.
- Формулировка в карточке сверена с PDF. Исправлена мелкая неточность импорта: в официальном тексте "склеил гранями", без слова "их"; смысл не меняется.
- Автор задачи в PDF не указан. Страница жюри 2014 года https://adygmath.ru/turnir14_judge.html перечисляет состав жюри, но не связывает конкретных авторов с задачами; в карточке автор оставлен `unknown` / `not_found_in_checked_sources`.

## Поиск решения, форума и автора

Проверены официальные ссылки страницы турнира: для 2 тура явно опубликовано `2turstartresh.pdf`, но ссылки на решение Гранд-лиги 2 тура на странице нет. Дополнительно проверены типовые URL вроде `2turgrandresh.pdf`, `2turgrand_resh.pdf`, `2tur_grand_resh.pdf`, `resh2turgrand.pdf`, `2turgrand_solution.pdf`, `2turgrand_solutions.pdf`, `2turgrand_ans.pdf`, `2turgrand_reshenia.pdf`; все вернули `404`.

Проверенные веб-запросы включали:

- `"Джо взял 1000 единичных кубиков"`;
- `"склеил гранями так, что получилось связное тело"`;
- `"Полученный граф оказался планарным" "1000"`;
- `"Найдите наименьшее возможное количество отмеченных вершин"`;
- `"Планарный граф рёбер кубиков"`;
- `"1000 единичных кубиков" "планарным" "ЮМТ"`;
- `"Джо" "1000" "кубиков" "Южный математический турнир"`;
- `"Joe" "1000 unit cubes" "planar" "vertices"`;
- `"1000 unit cubes" "planar graph" "edges" "vertices"`;
- `site:math.stackexchange.com "1000 unit cubes" "planar graph"`;
- `site:artofproblemsolving.com "1000 unit cubes" "planar"`;
- `site:mathoverflow.net "unit cubes" "planar graph"`.

Результат: найден официальный PDF с условием и общие/фоновые материалы по планарным графам или решёточным объектам; опубликованного полного решения, форумного разбора или авторского комментария по этой задаче не найдено. Самостоятельный проход не дал строгой нижней оценки, поэтому никакие наброски не внесены в `solutions[]` или `ideas[]`.

## Tags, definitions, source refs

- `definition_ids` проверены: добавлен `planar_graph`, он существует в `data/definitions/definitions.yaml` и соответствует условию.
- Tags `planar_graphs` и `goal_exact_bound` проверены в `data/taxonomy/tags.yaml` и оставлены.
- В `problem_profile.keywords` добавлены только статусные/поисковые метки `no_public_solution_found` и `непросто_для_ИИ`; доказательные маршруты туда не добавлялись.
- Source ref `src-yumt-2014-grand-round2-problem9-official` существует в `data/sources/sources.yaml` и ведёт на официальный PDF с условием. Роль в карточке уточнена до `official_problem_statement`, потому что проверенный PDF содержит условия, но не решение.
- Related source refs `src-grid-graphs-on-surfaces` и `src-minimum-perimeter-lattice-animals` существуют в `data/sources/sources.yaml`; они оставлены как фоновые внешние источники, не как найденное решение.

## Родственные связи

Общий `data/relations/relations.yaml` не редактировался.

Конкретное предложение для будущей ручной проверки, если будет найдено или написано полное решение:

```json
{
  "id": "rel-planar-edge-bound-yumt-2014-cube-edge-graph",
  "from": "planar-edge-bound",
  "to": "yumt-2014-grand-round2-problem9",
  "type": "prerequisite",
  "distance": 2,
  "forward_text": "Классическая оценка числа рёбер планарного графа, вместе с её двудольным вариантом, является естественным инструментом для нижней оценки в задаче о планарном графе рёбер склеенных кубиков.",
  "backward_text": "Задача ЮМТ 2014 о кубиках выглядит как нестандартное применение планарных оценок к графу рёбер пространственной клеточной фигуры; добавлять связь стоит только после проверки полного решения.",
  "status": "needs_human_review",
  "confidence": 0.55
}
```

Пока связь лучше не добавлять автоматически: найденной полной нижней оценки нет, а связь с `planar-edge-bound` остаётся только вероятным инструментальным мотивом.
