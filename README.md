# graphs

Черновая база графовых олимпиадных задач, теорем и связей между ними.

Сейчас это не финальный релиз, а рабочая публикация для архитектурного ревью: базу уже можно читать, искать и просматривать в статическом viewer, но схема и редакторские правила еще могут меняться.

## Что внутри

- `data/problems/` — карточки задач, теорем и лемм
- `data/relations/` — связи между карточками
- `data/sources/` — источники
- `data/definitions/` — стандартные определения
- `data/standard_ideas/` — стандартные идеи решений
- `data/taxonomy/` — служебные словари и статусы
- `data/import_batches/` — журналы массовых импортов
- `tools/` — проверка, поиск, сборка индекса и viewer
- `viewer/index.html` — статическая сборка для чтения базы
- `data/assets/` — исходные рисунки и другие ассеты для карточек

Источник истины — YAML-файлы в `data/`. Файлы сейчас записаны в JSON-совместимом подмножестве YAML, чтобы инструменты работали без внешних Python-зависимостей.

## Быстрый старт

```powershell
python tools/validate.py
python tools/check_links.py
python tools/audit_rules.py
python tools/build_index.py
python tools/build_viewer.py
python tools/build_agent_access.py
python tools/search.py query "matching"
python tools/search.py neighbors five-color-theorem --depth 2
python tools/comments.py --status open
```

После сборки viewer можно открыть файл `viewer/index.html` в браузере.
Если в карточках есть рисунки-примеры, `python tools/build_viewer.py` одновременно обновит и `viewer/assets/`, и `docs/assets/`.

Viewer хранит личный прогресс и заметки только в браузере пользователя
(`localStorage`, ключ `graph-db:local-user-data:v1`). Эти данные не попадают в
репозиторий; их можно экспортировать/importировать JSON-файлом или сбросить в
интерфейсе. Кнопки комментариев и `Сообщить об ошибке` отправляют данные в базу
только через настроенный backend endpoint (`GRAPH_DB_FEEDBACK_ENDPOINT` или
`FEEDBACK_ENDPOINT` при сборке viewer). Без endpoint статический GitHub Pages
не может создавать файлы в `data/comments/`.

## Доступ для внешних браузерных агентов

Для агентов, которым неудобно читать большой JavaScript viewer или пользоваться GitHub code search,
генерируется отдельный лёгкий слой в `docs/agent/`:

- `docs/agent/README.md` — правила работы с базой как с источником информации;
- `docs/agent/catalog.json` — компактные метаданные и список чанков;
- `docs/agent/problems.jsonl` — одна задача на строку JSON;
- `docs/agent/problems-by-source/*.jsonl` — меньшие чанки по источникам;
- `docs/agent/problems.md` — простой Markdown-каталог.

Эти файлы предназначены только для поиска и навигации. Источник истины остаётся в `data/`.

## Текущее состояние

- база уже пригодна для чтения и ручной правки;
- покрытие неравномерное: сильнее всего заполнены IMO/IMO Shortlist и несколько официальных международных архивов;
- у карточек есть редакторские статусы, в том числе `review_status` и `editorial.relations_status`;
- комментарии хранятся отдельными файлами в `data/comments/`;
- часть контента все еще помечена как `needs_human_review`, это нормально для текущей черновой публикации.

## Что имеет смысл смотреть при ревью

1. Достаточно ли удачна схема карточки как единицы знания.
2. Удобно ли разделены задачи, решения, стандартные идеи, определения и связи.
3. Не перегружен ли `problem_profile`.
4. Достаточно ли понятны статусы и редакторские поля.
5. Не стоит ли иначе организовать `relations`, `import_batches` или `taxonomy`.

Короткий гайд для ревью лежит в [docs/REVIEW_GUIDE.md](docs/REVIEW_GUIDE.md).

## Документация

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — актуальная схема репозитория
- [docs/AI_CARD_RULES.md](docs/AI_CARD_RULES.md) — компактные правила для ИИ-правок карточек
- [docs/IMPORT_WORKFLOW.md](docs/IMPORT_WORKFLOW.md) — как устроен массовый импорт
- [docs/REVIEW_GUIDE.md](docs/REVIEW_GUIDE.md) — что именно смотреть в этой черновой публикации
- [docs/HANDOFF_FOR_NEW_CHAT.md](docs/HANDOFF_FOR_NEW_CHAT.md) — короткая точка входа для нового чата
- [CONTRIBUTING.md](CONTRIBUTING.md) — правила правок

Рабочие исторические планы вынесены в `docs/archive/working-plans/`, чтобы не мешать чтению актуальной документации.
