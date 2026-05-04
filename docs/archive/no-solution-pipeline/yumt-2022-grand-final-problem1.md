# yumt-2022-grand-final-problem1

## Краткий итог

Карточка была без решения. Официальный источник с условием найден в уже подключённой записи `src-yumt-2022-grand-final-problem1-official`, но публичный официальный разбор и автор задачи по точной формулировке не найдены.

Добавлено ИИ-решение: если граф не 3-раскрашиваем, берём 4-критический подграф. По теореме Крусенстьерна-Хафстрёма и Тофта в нём есть индуцированный нечётный цикл `C`, для которого удаление вершин `C` оставляет связный граф. Так как в 4-критическом графе минимальная степень не меньше 3, удаление только рёбер `C` связность не нарушает, что противоречит условию задачи.

## Найденные источники

- Официальная формулировка ЮМТ 2022, Гранд-лига, финал: `https://adygmath.ru/content/files/umt22/uslovie/umt22_uslovie_final_grand.pdf`.
- В открытом поиске найдена близкая тренировочная версия ЦПМ/Хамовников с более слабым утверждением `χ(G) <= 4`, но это не официальный разбор данной карточки: `https://math.mosolymp.ru/upload/files/2019/khamovniki/9/1/2019-05-13-graph-coloring.pdf`.
- Использованная внешняя теорема упоминается в статье J. Gao et al., "A Unified Proof of Conjectures on Cycle Lengths in Graphs": `https://par.nsf.gov/servlets/purl/10055175`.
- Справочная формулировка результата также есть в книге T. R. Jensen, B. Toft, "Graph Coloring Problems", раздел "Nonseparating Odd Cycles in 4-Critical Graphs": `https://djvu.online/file/sNID8jjCqAw5z`.

## Внешняя теорема

Использована теорема Крусенстьерна-Хафстрёма и Тофта: каждый 4-критический граф содержит индуцированный нечётный цикл `C`, такой что `G - V(C)` связен.

Оценка школьности: теорема тяжёлая и не является стандартным олимпиадным инструментом. Для базы решение полезно как закрывающее направление, но карточку лучше держать `public_ready: false`, пока не будет найден официальный/элементарный разбор или не будет заведена отдельная карточка-теорема с доказательством. Без этой теоремы задача выглядит непросто для ИИ.

## Предлагаемые source entries

Не редактировал `data/sources/sources.yaml`, потому что это вне зоны разрешённых правок. Возможная запись для внешней теоремы:

```json
{
  "id": "src-krusenstjerna-hafstrom-toft-nonseparating-odd-cycle",
  "type": "research_paper",
  "title": "Krusenstjerna-Hafstrom and Toft, Non-separating induced odd cycles in 4-critical graphs",
  "url": "https://par.nsf.gov/servlets/purl/10055175",
  "browser_openable": true,
  "language": "en",
  "official": false,
  "status": "source_verified",
  "preference_note": "Secondary accessible reference: Gao et al. cite the theorem and state that every 4-critical graph contains a non-separating induced odd cycle."
}
```

## Изменения в карточке

- Добавлено решение `sol-ai-critical-nonseparating-odd-cycle` со статусом `ai_checked`.
- Добавлена идея `idea-critical-graph-nonseparating-odd-cycle`.
- Обновлены профильные поля; словарные теги карточки оставлены как `coloring`, `goal_proof`.
- В `editorial.notes` зафиксировано, что официальное решение/автор не найдены, а ИИ-решение зависит от тяжёлой внешней теоремы.
