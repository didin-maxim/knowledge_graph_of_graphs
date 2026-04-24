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
python tools/build_index.py
python tools/build_viewer.py
python tools/search.py query "matching"
python tools/search.py neighbors five-color-theorem --depth 2
python tools/comments.py --status open
```

После сборки viewer можно открыть файл `viewer/index.html` в браузере.
Если в карточках есть рисунки-примеры, `python tools/build_viewer.py` одновременно обновит и `viewer/assets/`, и `docs/assets/`.

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
- [docs/IMPORT_WORKFLOW.md](docs/IMPORT_WORKFLOW.md) — как устроен массовый импорт
- [docs/REVIEW_GUIDE.md](docs/REVIEW_GUIDE.md) — что именно смотреть в этой черновой публикации
- [docs/HANDOFF_FOR_NEW_CHAT.md](docs/HANDOFF_FOR_NEW_CHAT.md) — короткая точка входа для нового чата
- [CONTRIBUTING.md](CONTRIBUTING.md) — правила правок

Рабочие исторические планы вынесены в `docs/archive/working-plans/`, чтобы не мешать чтению актуальной документации.
