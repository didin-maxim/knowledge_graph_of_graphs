# yumt-2023-granda-final-problem6: very-high pass

## Итог

Решение в карточку не добавлено: `solutions: []` оставлен пустым. Недоведённая идея удалена из `ideas`, чтобы база не хранила невалидированный набросок.

Официальная формулировка подтверждена, автор найден: задача 6 финала Гранд-лиги A ЮМТ-2023, автор `В. Дольников`. При этом `editorial.public_ready` оставлен `false`: проблема не только в сложности и отсутствии опубликованного решения, а в том, что точная задача близка к сильным утверждениям Erdős-Lovász-Tihany о хроматических разбиениях; без официального/авторского решения или отдельной ручной проверки публиковать как готовую карточку рискованно.

Карточка помечена как `no_solution_hard` / `непросто для ИИ`, `review_status: needs_human_review`.

## Проверка источников

- Официальная страница ЮМТ-2023: `https://adygmath.ru/umt2023.html`. Через `curl` страница доступна; она содержит ссылку на условия финала Гранд-лиги A, но не содержит открытой ссылки на решения финала.
- Официальный PDF условий: `https://adygmath.ru/content/files/umt23/final/final_usl_granda.pdf`. PDF доступен, `Content-Type: application/pdf`, `Last-Modified: Sun, 08 Oct 2023 13:03:15 GMT`. Извлечённый текст подтверждает: `XVIII Южный математический турнир. ВДЦ «Орленок». Гранд-лига. Финал. 25.09.2023.`; задача 6 совпадает с текстом карточки; после условия указано `(В. Дольников)`.
- Проверены вероятные неиндексированные имена файлов решений в `/content/files/umt23/final/`: `final_resh_granda.pdf`, `final_reshenie_granda.pdf`, `final_resheniya_granda.pdf`, `final_sol_granda.pdf`, `final_solution_granda.pdf`, `final_solutions_granda.pdf`, `final_otv_granda.pdf`, `final_otvet_granda.pdf`, `final_otvety_granda.pdf`, `resh_granda.pdf`, `resheniya_granda.pdf`, `solutions_granda.pdf`, `final_usl_granda_resh.pdf`, `final_granda_resh.pdf`, `granda_resh.pdf`; все дали `404`.
- В `data/sources/sources.yaml` source id `src-yumt-2023-granda-final-problem6-official` существует и ведёт на официальный PDF. Замечание для будущего общего source-аудита: `access_note` в общем файле пишет `Page: 2`, но фактический PDF извлекается как одностраничный; общий файл источников не редактировался по ограничению задачи.
- В карточке роль официального source-ref уточнена до `official_problem_statement`, потому что найденный PDF содержит условия, а не решения.
- Внешний источник `src-elt-claw-free-arxiv` существует и релевантен только как фон по Erdős-Lovász-Tihany; в карточке явно отмечено, что он не является решением задачи ЮМТ.

## Поиск решения

Опубликованное полное решение, форумный разбор или авторский комментарий по точной формулировке не найдены.

Проверенные запросы включали точные и близкие фразы:

- `"Дано натуральное число n ≥ 3" "χ(G) = n" "больше чем n вершин"`
- `"Докажите, что в G найдутся два" "χ(G1)" "χ(G2)"`
- `"больше чем n вершин" "χ(G1) + χ(G2)"`
- `"В. Дольников" "хроматическое число" "два" "подграфа"`
- `"ЮМТ" "2023" "Гранд-лига A" "финал" "задача 6" "хроматическим числом"`
- `site:math.stackexchange.com "chromatic numbers" "disjoint subgraphs" "Tihany"`
- `site:mathoverflow.net "Erdős-Lovász Tihany" "disjoint subgraphs"`
- `"χ(G1) + χ(G2)" "χ(G)+1" graph`

Найдены только нерешающие материалы:

- Math StackExchange по более слабой стандартной задаче о разбиении с суммой `χ(G)`, а не `χ(G)+1`.
- Erdős Problems #628: `https://www.erdosproblems.com/628`, открытая постановка Erdős-Lovász Tihany для графа с `χ(G)=k`, без `K_k`, и любых `a,b >= 2`, `a+b=k+1`, спрашивающая о двух непересекающихся подграфах с хроматическими числами хотя бы `a` и `b`.
- arXiv `https://arxiv.org/abs/1309.1020`, Chudnovsky-Fradkin-Plumettaz, `On the Erdös-Lovász Tihany Conjecture for Claw-Free Graphs`; источник подтверждает, что общий ELT-контекст открыт, а известные результаты являются частичными по классам графов или малым параметрам.

## Карточка

- `authors`: заменено `?` на `В. Дольников`, `status: source_verified`.
- `ideas`: очищено до `[]`; недоведённый набросок про выделение части из раскраски не оставлен в базе.
- `solutions`: оставлено `[]`.
- `tags`: проверены и оставлены валидные `coloring`, `goal_existence`.
- `definition_ids`: `chromatic_number` существует в `data/definitions/definitions.yaml` и соответствует условию. Отдельных definitions для `подграф` или `не пересекающиеся по вершинам` в текущем файле не найдено, поэтому неизвестные definition ids не добавлялись.
- `sources`: оба `source_id` существуют; официальный source-ref ограничен `statement_ids: ["stmt-original"]`.
- `editorial.public_ready`: оставлен `false`.
- `editorial.manual_review`: добавлен запрос на авторское/официальное решение или ручную математическую проверку слабой формы задачи.

## Родственные связи

Общий файл relations не редактировался.

Конкретные предложения для будущей ручной правки:

- `yumt-2023-granda-final-problem6` -- `yumt-2015-grand-final-problem5`: `same_motif`. Обе задачи про разбиение графа на непересекающиеся части с контролем хроматических чисел; задача 2015 года соответствует близкому ELT/двойно-критическому сюжету для 5-хроматических графов без `K5`, но не даёт автоматического решения текущей задачи.
- `yumt-2023-granda-final-problem6` -- `stiebitz-double-critical-k5`: `same_motif` или осторожно `prerequisite` только для частного `n=5`/edge-deletion направления. Не помечать как `solution_transfer` без нового полного доказательства.
- Если будет создана отдельная классическая карточка по Erdős-Lovász Tihany conjecture, связать текущую задачу с ней как `same_motif` или `specialization_candidate`, но не как доказанную `specialization`, пока не проверена точная слабая форма `exists a,b`.
