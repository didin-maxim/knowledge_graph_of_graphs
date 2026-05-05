# yumt-2025-unior-round3-problem1: very-high no-solution pass

Дата прохода: 2026-05-05.

## Итог

Полное опубликованное решение не найдено. В карточке оставлено `solutions: []`, а `ideas` очищено до `[]`, чтобы не хранить недоведённые подходы в базе.

Карточка помечена как `no_public_solution_found` / `непросто_для_ИИ`. `editorial.public_ready` поставлен в `true`: официальная формулировка подтверждена, source refs / definitions / tags сверены, и единственный выявленный блокер - отсутствие опубликованного решения или самодостаточного строгого доказательства.

## Официальная сверка

- Официальная страница турнира: https://adygmath.ru/umt2025.html. Она содержит ссылку на `/content/files/umt25/problems/3tur_usl_unior.pdf` в блоке условий III тура.
- Официальный PDF из source registry: `src-yumt-2025-unior-round3-problem1-official`, https://adygmath.ru/content/files/umt25/problems/3tur_usl_unior.pdf.
- PDF заново скачан через `curl`; HTTP-ответ `200 OK`, `Content-Type: application/pdf`, `Content-Length: 126958`, `Last-Modified: Thu, 30 Oct 2025 14:58:37 GMT`.
- Текст извлечён локально через `pypdf`. Страница 1 подтверждает: XX Южный математический турнир, ВДЦ "Орлёнок", тур 3, Юниор-лига, 25.09.2025, задача 1.
- Формулировка в карточке сверена с PDF. В PDF: "Дан граф на n вершинах, все циклы в котором имеют непустое пересечение по вершинам и длину не менее 5. Докажите, что в этом графе не более, чем 2n - 1 ребро." В карточке сохранён тот же смысл; типографские отличия только в пробелах/запятой и записи минуса.
- Карточка трактует условие о пересечении как попарное пересечение циклов по вершинам (`no_two_vertex_disjoint_cycles`), что соответствует уже импортированным метаданным и нетривиальному смыслу задачи. Дословная официальная формулировка сохранена в `statements.original`.
- Автор задачи в PDF не указан. Страница жюри https://adygmath.ru/umt25_jury.html содержит общий состав жюри XX ЮМТ, но не связывает конкретных авторов с задачами; в карточке автор оставлен `unknown` / `not_found_in_checked_sources`.

## Поиск решения, форума и автора

Официальная страница турнира содержит условия, протоколы и результаты боёв, но не содержит раздела решений. Дополнительно проверены типовые URL вроде `3tur_resh_unior.pdf`, `3tur_unior_resh.pdf`, `3tur_usl_unior_resh.pdf`, `3tur_usl_unior_sol.pdf`, `3tur_sol_unior.pdf`, `3tur_unior_solutions.pdf`, `3tur_resheniya_unior.pdf`, `3tur_unior_resheniya.pdf`, `3tur_usl_unior_solution.pdf`, `3tur_usl_unior_res.pdf`, `3tur_unior_ans.pdf`, `3tur_otv_unior.pdf`, `3tur_res_unior.pdf`, `3tur_solutions_unior.pdf`; все вернули `404`.

Проверенные веб-запросы включали:

- `"Дан граф на n вершинах" "2n - 1" "циклы" "длину не менее 5"`;
- `"все циклы" "непустое пересечение" "2n - 1" "ЮМТ"`;
- `"ЮМТ 2025" "Юниор-лига" "третий тур" "Циклы длины не меньше 5"`;
- `"Циклы длины не меньше 5" "ЮМТ"`;
- `"Дан граф на n вершинах, все циклы" "не более, чем 2n"`;
- `"все циклы" "длину не менее 5" "2n−1"`;
- `"graph" "all cycles" "intersect" "girth" "2n-1"`;
- `"no two vertex-disjoint cycles" "girth" "2n"`;
- `"no two disjoint cycles" "girth at least 5" "edges"`;
- `"pairwise intersecting cycles" graph "girth"`;
- `site:adygmath.ru/content/files/umt25/problems/ 3tur_resh_unior`;
- `site:adygmath.ru/content/files/umt25/problems/ unior resh 2025`.

Результат: найден официальный PDF с условием и официальная страница турнира; опубликованного полного решения, форумного разбора или авторского комментария по этой задаче не найдено. Самостоятельный проход не доведён до строгого решения, поэтому никакие наброски не внесены в `solutions[]` или `ideas[]`.

## Tags, definitions, source refs

- `definition_ids` проверены: `simple_graph` и `cycle` существуют в `data/definitions/definitions.yaml`.
- Tags проверены по `data/taxonomy/tags.yaml`: оставлены только существующие `extremal_graph_theory` и `goal_bound`. `minimal_counterexample` удалён из tags и methods, потому что это был недоведённый маршрут, а не проверенный атрибут решения.
- В `problem_profile.keywords` добавлены только статусные/поисковые метки `southern_mathematical_tournament`, `no_public_solution_found` и `непросто_для_ИИ`; доказательные маршруты туда не добавлялись.
- Source ref `src-yumt-2025-unior-round3-problem1-official` существует в `data/sources/sources.yaml` и ведёт на официальный PDF с условием. Роль в карточке оставлена `official_problem_statement`, потому что проверенный PDF содержит условия, но не решение.

## Родственные связи

Общий `data/relations/relations.yaml` не редактировался.

Конкретные предложения для будущей ручной проверки:

```json
{
  "id": "rel-min-degree-girth-two-disjoint-cycles-yumt-2025-unior-round3-problem1",
  "from": "min-degree-three-girth-five-two-vertex-disjoint-cycles",
  "to": "yumt-2025-unior-round3-problem1",
  "type": "prerequisite",
  "distance": 1,
  "forward_text": "Если будет создана и доказана лемма 'минимальная степень хотя бы 3 и обхват хотя бы 5 вынуждают два вершинно непересекающихся цикла', она, вероятно, даст ключевой структурный шаг для оценки 2n - 1 через удаление вершин малой степени.",
  "backward_text": "Задача ЮМТ 2025 выглядит как олимпиадное применение такой леммы к графам без двух вершинно непересекающихся циклов.",
  "status": "needs_human_review",
  "confidence": 0.55
}
```

```json
{
  "id": "rel-degeneracy-motif-yumt-2025-unior-round3-problem1",
  "from": "degeneracy-greedy-coloring",
  "to": "yumt-2025-unior-round3-problem1",
  "type": "method_motif",
  "distance": 3,
  "forward_text": "Техника удаления вершин малой степени является естественным мотивом для сведения плотной контрпримерной конфигурации к подграфу с большой минимальной степенью.",
  "backward_text": "Связь слабая и не должна добавляться без полного решения: текущая карточка не использует раскраску, а только возможный мотив вырожденности.",
  "status": "needs_human_review",
  "confidence": 0.25
}
```

Пока связи лучше не добавлять автоматически: опубликованного решения нет, а ключевая структурная лемма в базе отсутствует как отдельная проверенная карточка.
