# Feedback Endpoint

Статический viewer на GitHub Pages не может сам записывать комментарии в
`data/comments/`: у браузера нет серверного секрета, прав на push и доступа к
файловой системе репозитория. Поэтому комментарии без регистрации пользователя
работают только через отдельный backend endpoint.

Для графовой базы используется тот же Cloudflare Worker, что и для базы задач о
неполной информации:

```text
https://incomplete-info-feedback.maksimdidin4.workers.dev
```

Worker принимает `project: "graph-db"` и пишет комментарии в репозиторий
`didin-maxim/knowledge_graph_of_graphs`, ветка `main`, в папку:

```text
data/comments/inbox/
```

Секрет GitHub token хранится только в Cloudflare. В код, HTML, YAML и историю git
его добавлять нельзя.

## Как включить endpoint при сборке

```powershell
$env:GRAPH_DB_FEEDBACK_ENDPOINT = "https://incomplete-info-feedback.maksimdidin4.workers.dev"
python tools\build_viewer.py
```

Можно использовать общий fallback `FEEDBACK_ENDPOINT`, если один endpoint
обслуживает несколько баз.

## Контракт формы комментария

Форма нового комментария отправляет:

```json
{
  "project": "graph-db",
  "comment": {
    "id": "comment-2026-05-24-12-00-00-problem-id-title",
    "target": {"type": "problem", "problem_id": "problem-id"},
    "kind": "bug_report",
    "title": "Короткий заголовок",
    "text": "Текст комментария",
    "author": "Автор",
    "created_at": "2026-05-24",
    "status": "open",
    "response": {"status": "open", "notes": ""},
    "editorial": {"created_by": "human", "notes": []}
  }
}
```

Для общего комментария по архитектуре используется:

```json
"target": {"type": "architecture"}
```

Форма `Сообщить об ошибке` отправляет плоский report JSON с `project`, `kind`,
`title`, `text`, `contact`, `target`, `problem`, `page_url`, `created_at` и
`report_text`. Worker приводит такой report к записи comment.

Endpoint должен вернуть HTTP 2xx только после реальной записи в GitHub. Ошибка
GitHub API, отсутствие секрета, запрет CORS, пустой комментарий или текст с
явными признаками битой кириллицы должны возвращать ошибку; viewer не должен
показывать их как успешную отправку.

## Чего нельзя делать

`mailto`, копирование текста, прямое открытие GitHub issue из браузера и
сохранение в `localStorage` не являются записью комментария в базу. Их нельзя
показывать как успешную отправку или как основной путь, если требование:
"комментарий должен попасть в базу".
