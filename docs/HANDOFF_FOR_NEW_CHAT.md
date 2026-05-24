# Handoff For New Chat

Этот файл нужен как короткая точка входа для нового чата, который будет править и развивать базу.

## Где лежит база

- Локальный репозиторий:
  `C:\Users\Admin\Documents\Codex\2026-04-20-c-users-admin-documents-codex-2026`
- GitHub:
  [https://github.com/didin-maxim/knowledge_graph_of_graphs](https://github.com/didin-maxim/knowledge_graph_of_graphs)

## Что считать источником истины

Главный источник истины — `data/`.

Особенно важны:

- `data/problems/` — карточки задач, теорем и лемм
- `data/relations/` — связи между карточками
- `data/comments/` — комментарии ревьюеров и архитектурные замечания
- `data/sources/` — нормализованные источники
- `data/definitions/` — стандартные определения
- `data/standard_ideas/` — стандартные идеи решений
- `data/taxonomy/` — статусы, типы связей и другие словари

Производные артефакты:

- `viewer/index.html`
- `index/generated.sqlite`

Их можно пересобирать.

## Как сейчас устроена публикация

- Репозиторий публичный.
- GitHub Pages должен публиковать сайт через `docs/`.
- Для Pages нужен `docs/index.html`.
- Рабочая сборка viewer живёт в `viewer/index.html`.

Если нужно обновить GitHub Pages вручную, самый простой путь:

```powershell
cd C:\Users\Admin\Documents\Codex\2026-04-20-c-users-admin-documents-codex-2026
python tools\build_viewer.py
Copy-Item viewer\index.html docs\index.html -Force
git add viewer\index.html docs\index.html
git commit -m "Refresh viewer for GitHub Pages"
git push origin main
```

## Что уже есть в базе

База уже содержит:

- IMO и IMO Shortlist графовые карточки
- часть задач Турнира городов и ВсОШ
- блоки из EGMO, APMO, RMM, BMO, MEMO
- набор классических теорем и стандартных идей
- relations_status у карточек
- отдельный слой комментариев

## Как устроены комментарии

Комментарии живут отдельно в `data/comments/`.

Поддерживаются два режима:

1. Комментарий к задаче:
   - `target.type = "problem"`
   - `target.problem_id = "..."`
2. Общий комментарий по архитектуре:
   - `target.type = "architecture"`

Основные kinds:

- `bug_report`
- `alternative_solution`
- `related_connection`
- `architecture`

Статусы comments:

- `open`
- `triaged`
- `accepted`
- `declined`
- `resolved`

Viewer умеет показывать comments и сохранять новые comment-файлы.

CLI для просмотра comments:

```powershell
python tools\comments.py --status open
python tools\comments.py --problem vosh-2025-26-final-regions-friendship-coloring
python tools\comments.py --architecture
```

## Минимальный цикл проверки после правок

```powershell
cd C:\Users\Admin\Documents\Codex\2026-04-20-c-users-admin-documents-codex-2026
python tools\validate.py
python tools\check_links.py
python tools\audit_rules.py
python tools\build_index.py
python tools\build_viewer.py
```

## Что важно не ломать

1. Не считать `viewer/` и `index/` источником истины.
2. Не вшивать comments внутрь карточек задач; они отдельная сущность.
3. Не смешивать рабочие import-артефакты с основными problem cards.
4. Не удалять `editorial.relations_status`: он теперь технически важен.
5. Не писать слабые родственные связи без объясняющего текста.
6. Не класть в `solutions[]` пересказ идеи вместо доказательства.
7. Не выдавать `mailto`, копирование отчета, GitHub issue без backend или `localStorage` за запись комментария в базу. Если комментарий должен попадать в `data/comments/` без регистрации пользователя, нужен deployed backend endpoint по `docs/FEEDBACK_ENDPOINT.md`; без него это технический blocker статического GitHub Pages.
8. По комментариям и другим внешним интеграциям различать "подготовлено" и "работает". Агент имеет право отчитаться об успехе только после живой проверки полного пути: frontend отправил запрос, backend с секретом принял его и создал запись/PR/issue в согласованном месте. Если endpoint не развернут или проверка шла только на mock-сервере, финальный статус: "не готово к пользовательскому использованию", с точной причиной.

Для решений действует жёсткое редакторское правило:

- если текст нельзя проверить локально по карточке, это ещё не решение;
- если ключевой шаг спрятан за словами «аналогично», «стандартно» или ссылкой на внешний
  материал, решение надо переписать;
- если красивый аргумент сводится к самостоятельной графовой лемме, лемму лучше вынести в
  отдельную карточку, а не оставлять неявной внутри длинного текста;
- стандартные термины при первом появлении должны быть покрыты `definition_ids`;
- рисунок в `examples` не должен нести скрытую proof load.

## Где смотреть архитектурный контекст

- [README.md](../README.md)
- [AI_CARD_RULES.md](AI_CARD_RULES.md)
- [ARCHITECTURE.md](ARCHITECTURE.md)
- [REVIEW_GUIDE.md](REVIEW_GUIDE.md)
- [CONTRIBUTING.md](../CONTRIBUTING.md)

## Что делать в новом чате в первую очередь

Если новый чат подхватывает работу, ему лучше начать так:

1. Прочитать этот файл.
2. Прочитать `README.md`, `docs/AI_CARD_RULES.md` и `docs/ARCHITECTURE.md`.
3. Прогнать:
   ```powershell
   python tools\validate.py
   python tools\comments.py --status open
   ```
4. Посмотреть, нет ли открытых comments, которые требуют реакции.
5. Только после этого идти в карточки, связи или импорт.

## Если нужно быстро объяснить проект одной фразой

Это файловая база графовых олимпиадных задач и теорем с карточками, решениями, стандартными идеями, родственными связями и отдельным слоем комментариев для ревью и дальнейшей доработки.
