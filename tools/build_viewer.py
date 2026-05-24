import json
import os
import shutil

from lib import (
    ROOT,
    load_comments,
    load_definitions,
    load_problems,
    load_relations,
    load_sources,
    load_standard_ideas,
    load_taxonomy,
)


def load_viewer_data():
    return {
        "problems": load_problems(),
        "relations": load_relations(),
        "comments": load_comments(),
        "sources": load_sources(),
        "definitions": load_definitions(),
        "standard_ideas": load_standard_ideas(),
        "taxonomy": {
            "tags": load_taxonomy("tags.yaml", "tags"),
            "statuses": load_taxonomy("statuses.yaml", "statuses"),
            "relation_types": load_taxonomy("relation-types.yaml", "relation_types"),
            "difficulty_levels": load_taxonomy("difficulty.yaml", "difficulty_levels"),
            "properties": load_taxonomy("properties.yaml", "properties"),
            "comment_kinds": load_taxonomy("comment-kinds.yaml", "comment_kinds"),
            "comment_statuses": load_taxonomy("comment-statuses.yaml", "comment_statuses"),
        },
    }


def copy_example_assets():
    source = ROOT / "data" / "assets"
    if not source.exists():
        return
    for target_root in (ROOT / "viewer", ROOT / "docs"):
        target = target_root / "assets"
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source, target)


def feedback_config():
    endpoint = (
        os.environ.get("GRAPH_DB_FEEDBACK_ENDPOINT")
        or os.environ.get("FEEDBACK_ENDPOINT")
        or ""
    ).strip()
    return {
        "endpoint": endpoint,
        "project": "graph-db",
        "subjectPrefix": "[graph-db] Ошибка в карточке",
    }


def build_html(data):
    payload = json.dumps(data, ensure_ascii=False, indent=2)
    feedback_config_js = json.dumps(feedback_config(), ensure_ascii=False, separators=(",", ":"))
    return f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>База графовых задач</title>
  <script>
    window.MathJax = {{
      tex: {{ inlineMath: [['\\\\(', '\\\\)']], displayMath: [['\\\\[', '\\\\]']] }},
      svg: {{ fontCache: 'global' }}
    }};
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f6f5f1;
      --panel: #ffffff;
      --ink: #1f2528;
      --muted: #657076;
      --line: #d9d6cc;
      --accent: #0f766e;
      --soft: #e9f5f2;
      --warn: #fff5d8;
      --bad: #ffe8e4;
      --good: #e9f7e9;
      --code: #253238;
    }}

    * {{ box-sizing: border-box; }}

    body {{
      margin: 0;
      font-family: "Segoe UI", Arial, sans-serif;
      background: var(--bg);
      color: var(--ink);
      line-height: 1.5;
    }}

    button, input, select, textarea {{
      font: inherit;
    }}

    .shell {{
      display: grid;
      grid-template-columns: minmax(300px, 380px) minmax(0, 1fr);
      height: 100vh;
      overflow: hidden;
      transition: grid-template-columns 160ms ease;
    }}

    .shell.sidebar-hidden {{
      grid-template-columns: 0 minmax(0, 1fr);
    }}

    .sidebar {{
      border-right: 1px solid var(--line);
      background: #fbfaf7;
      display: flex;
      flex-direction: column;
      min-width: 0;
      min-height: 0;
      overflow-y: auto;
      overscroll-behavior: contain;
    }}

    .shell.sidebar-hidden .sidebar {{
      border-right: 0;
      visibility: hidden;
    }}

    .brand {{
      padding: 18px 18px 14px;
      border-bottom: 1px solid var(--line);
    }}

    .brand h1 {{
      margin: 0;
      font-size: 24px;
      letter-spacing: 0;
    }}

    .brand .meta {{
      color: var(--muted);
      margin-top: 4px;
      font-size: 14px;
    }}

    .search {{
      padding: 14px 18px;
      border-bottom: 1px solid var(--line);
      display: grid;
      gap: 10px;
    }}

    .mode-toggle {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
    }}

    .mode-button {{
      border: 1px solid var(--line);
      background: #fff;
      color: var(--ink);
      padding: 8px 10px;
      border-radius: 6px;
      cursor: pointer;
    }}

    .mode-button.active {{
      background: var(--soft);
      border-color: #9ccfc5;
    }}

    .small-button {{
      border: 1px solid #8abfb6;
      background: var(--soft);
      color: var(--ink);
      padding: 7px 10px;
      border-radius: 6px;
      min-height: 34px;
      cursor: pointer;
    }}

    .small-button:disabled {{
      opacity: .55;
      cursor: not-allowed;
    }}

    .local-data-actions {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 8px;
    }}

    .search input, .search select, .comment-form textarea {{
      width: 100%;
      border: 1px solid var(--line);
      background: #fff;
      color: var(--ink);
      padding: 10px 12px;
      border-radius: 6px;
    }}

    .list {{
      flex: 1 0 auto;
      min-height: 0;
      padding: 8px;
    }}

    .list-button {{
      display: block;
      width: 100%;
      text-align: left;
      border: 0;
      background: transparent;
      border-radius: 6px;
      padding: 10px;
      cursor: pointer;
      color: var(--ink);
      text-decoration: none;
    }}

    .list-button:hover, .list-button.active {{
      background: var(--soft);
    }}

    .id {{
      color: var(--muted);
      font-size: 12px;
      overflow-wrap: anywhere;
    }}

    main {{
      min-width: 0;
      height: 100vh;
      overflow: auto;
    }}

    .sidebar-toggle {{
      position: fixed;
      top: 10px;
      right: 14px;
      z-index: 20;
      border: 1px solid var(--line);
      background: rgba(255,255,255,.94);
      color: var(--ink);
      border-radius: 6px;
      padding: 7px 10px;
      cursor: pointer;
      box-shadow: 0 2px 10px rgba(0,0,0,.08);
    }}

    .sidebar-toggle:hover {{
      background: var(--soft);
    }}

    .content {{
      max-width: 1120px;
      margin: 0 auto;
      padding: 28px clamp(18px, 4vw, 42px) 64px;
    }}

    .topline {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
      margin-bottom: 12px;
    }}

    h2 {{
      font-size: clamp(28px, 4vw, 44px);
      line-height: 1.1;
      margin: 0 0 6px;
      letter-spacing: 0;
    }}

    h3 {{
      margin: 34px 0 12px;
      font-size: 21px;
      letter-spacing: 0;
    }}

    h4 {{
      margin: 20px 0 8px;
      font-size: 17px;
      letter-spacing: 0;
    }}

    .subtle {{
      color: var(--muted);
    }}

    .pill-row {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-top: 10px;
    }}

    .pill {{
      display: inline-flex;
      align-items: center;
      min-height: 26px;
      padding: 3px 8px;
      border-radius: 999px;
      background: #ece8dc;
      color: #31383c;
      font-size: 13px;
      max-width: 100%;
    }}

    .status-ai_draft, .status-needs_review, .status-needs_human_review {{
      background: var(--warn);
    }}

    .status-human_checked, .status-ai_checked, .status-source_verified, .status-public_ready {{
      background: var(--good);
    }}

    .status-disputed {{
      background: var(--bad);
    }}

    .solution-status {{
      border: 1px solid transparent;
      font-weight: 650;
    }}

    .solution-status-published {{
      background: #e6f4ef;
      border-color: #a8d5c5;
    }}

    .solution-status-official_complete_or_near_complete {{
      background: #e6f4ef;
      border-color: #a8d5c5;
    }}

    .solution-status-official_plan_completed_by_ai {{
      background: #dff6ec;
      border-color: #82c7ad;
    }}

    .solution-status-unofficial_published {{
      background: #edf0f7;
      border-color: #bac4d6;
    }}

    .solution-status-ai {{
      background: #e8f0ff;
      border-color: #b9c9ef;
    }}

    .solution-status-ai_original {{
      background: #e8f0ff;
      border-color: #b9c9ef;
    }}

    .solution-status-heavy {{
      background: #f5ead4;
      border-color: #d8ba78;
    }}

    .solution-status-ai_heavy_external_theorem {{
      background: #f5ead4;
      border-color: #d8ba78;
    }}

    .solution-status-hard_external_theorem_no_proof {{
      background: #f5ead4;
      border-color: #d8ba78;
    }}

    .solution-status-missing {{
      background: #f0e6df;
      border-color: #d0b6a8;
    }}

    .solution-status-no_solution_hard {{
      background: #f4d7d7;
      border-color: #d78b8b;
    }}

    .section {{
      border-top: 1px solid var(--line);
      padding-top: 4px;
      margin-top: 28px;
    }}

    .card {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 14px;
      margin: 10px 0;
    }}

    .reveal {{
      margin: 0 0 10px;
    }}

    .reveal > summary {{
      width: fit-content;
      list-style: none;
      border: 1px solid #8abfb6;
      background: var(--soft);
      color: var(--ink);
      border-radius: 6px;
      padding: 8px 11px;
      cursor: pointer;
      user-select: none;
    }}

    .reveal > summary::-webkit-details-marker {{
      display: none;
    }}

    .reveal[open] > summary {{
      margin-bottom: 10px;
    }}

    .item-title {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      align-items: baseline;
      margin-bottom: 8px;
      font-weight: 650;
    }}

    .text {{
      overflow-wrap: break-word;
    }}

    .text-paragraph {{
      margin: 0 0 0.85em;
    }}

    .text-display-math {{
      margin: 0.9em 0;
      overflow-x: auto;
      overflow-y: hidden;
    }}

    .text > :last-child {{
      margin-bottom: 0;
    }}

    .example-stack {{
      display: grid;
      gap: 12px;
      margin-top: 14px;
    }}

    .example-card {{
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 12px;
      background: #fcfbf8;
    }}

    .example-label {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 10px;
      font-weight: 650;
    }}

    .example-optional {{
      color: var(--muted);
      font-size: 13px;
      font-weight: 400;
    }}

    .example-figure {{
      margin: 0;
      display: grid;
      gap: 10px;
    }}

    .example-image {{
      width: 100%;
      height: auto;
      display: block;
      border-radius: 6px;
      border: 1px solid var(--line);
      background: #fff;
    }}

    .example-caption {{
      color: var(--muted);
      font-size: 14px;
    }}

    a {{
      color: var(--accent);
      text-decoration-thickness: 1px;
      text-underline-offset: 3px;
    }}

    .relation-link {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      color: var(--accent);
      font-weight: 650;
      text-decoration: none;
      border-bottom: 1px solid currentColor;
    }}

    .relation-link:hover {{
      color: #7c2d12;
    }}

    .code {{
      font-family: Consolas, "Cascadia Mono", monospace;
      color: var(--code);
    }}

    .empty {{
      color: var(--muted);
      font-style: italic;
    }}

    .home-hero {{
      min-height: min(70vh, 680px);
      display: grid;
      align-content: center;
      gap: 24px;
      padding: clamp(22px, 5vw, 58px) 0 32px;
      border-bottom: 1px solid var(--line);
    }}

    .home-kicker {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      align-items: center;
      color: var(--muted);
      font-size: 14px;
    }}

    .home-title {{
      max-width: 920px;
      font-size: 76px;
      line-height: 0.98;
      letter-spacing: 0;
      margin: 0;
    }}

    .home-lead {{
      max-width: 760px;
      font-size: 21px;
      color: #425057;
      margin: 0;
    }}

    .home-actions {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      align-items: center;
    }}

    .home-action {{
      border: 1px solid var(--line);
      background: #fff;
      color: var(--ink);
      padding: 10px 13px;
      border-radius: 6px;
      cursor: pointer;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      min-height: 42px;
    }}

    .home-action.primary {{
      background: #113f3b;
      border-color: #113f3b;
      color: #fff;
    }}

    .home-stats {{
      display: grid;
      grid-template-columns: repeat(5, minmax(110px, 1fr));
      gap: 10px;
      max-width: 900px;
    }}

    .home-solution-grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 10px;
      margin-top: 8px;
    }}

    .home-solution-button {{
      width: 100%;
      text-align: left;
      border: 1px solid var(--line);
      background: #fff;
      color: var(--ink);
      border-radius: 8px;
      padding: 12px;
      cursor: pointer;
    }}

    .home-solution-button:hover {{
      background: var(--soft);
      border-color: #9ccfc5;
    }}

    .home-solution-button strong {{
      display: block;
      font-size: 20px;
      line-height: 1.1;
    }}

    .home-solution-button span {{
      display: block;
      color: var(--muted);
      font-size: 13px;
      margin-top: 4px;
    }}

    .home-stat, .home-panel, .home-chip {{
      border: 1px solid var(--line);
      background: #fff;
      border-radius: 8px;
    }}

    .home-stat {{
      padding: 12px;
    }}

    .home-stat strong {{
      display: block;
      font-size: 24px;
      line-height: 1.1;
    }}

    .home-stat span, .home-chip span {{
      color: var(--muted);
      font-size: 13px;
    }}

    .home-band {{
      padding: 30px 0 4px;
    }}

    .home-grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 14px;
    }}

    .home-panel {{
      padding: 16px;
    }}

    .home-panel h3 {{
      margin: 0 0 8px;
      font-size: 18px;
    }}

    .home-panel p, .home-panel li {{
      color: #425057;
    }}

    .home-panel ul {{
      padding-left: 19px;
      margin: 10px 0 0;
    }}

    .home-search-map {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 10px;
    }}

    .home-chip {{
      padding: 11px;
    }}

    .home-chip strong {{
      display: block;
      margin-bottom: 3px;
    }}

    .home-note {{
      border-left: 4px solid #d5a021;
      background: #fff8e5;
      padding: 12px 14px;
      border-radius: 0 8px 8px 0;
      color: #51431f;
    }}

    .comment-form {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 14px;
      margin: 10px 0;
      display: grid;
      gap: 10px;
    }}

    .comment-form button {{
      width: fit-content;
      border: 1px solid #8abfb6;
      background: var(--soft);
      color: var(--ink);
      padding: 8px 12px;
      border-radius: 6px;
      cursor: pointer;
    }}

    .local-panel {{
      display: grid;
      gap: 10px;
      background: #fbfdfb;
    }}

    .local-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      align-items: center;
    }}

    .local-row label {{
      color: var(--muted);
      font-size: 14px;
    }}

    .local-row select, .local-row input, .local-panel textarea {{
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #fff;
      color: var(--ink);
      padding: 8px 10px;
    }}

    .local-row select {{
      min-width: 170px;
    }}

    .local-panel textarea {{
      width: 100%;
      min-height: 96px;
      resize: vertical;
    }}

    .local-muted {{
      color: var(--muted);
      font-size: 13px;
    }}

    .local-save-status {{
      min-width: 92px;
      color: var(--muted);
      font-size: 13px;
    }}

    .report-form {{
      display: grid;
      gap: 10px;
    }}

    .report-form label {{
      display: grid;
      gap: 4px;
      color: var(--muted);
      font-size: 13px;
    }}

    .report-form select, .report-form input, .report-form textarea {{
      width: 100%;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #fff;
      color: var(--ink);
      padding: 8px 10px;
    }}

    .report-output {{
      min-height: 150px;
      font-family: Consolas, "Cascadia Mono", monospace;
      font-size: 13px;
    }}

    textarea {{
      min-height: 150px;
      resize: vertical;
    }}

    .def-link {{
      color: #7c2d12;
      border-bottom: 1px dotted currentColor;
      text-decoration: none;
    }}

    .idea-link {{
      color: #6b4e00;
      border-bottom: 1px dotted currentColor;
      text-decoration: none;
    }}

    @media (max-width: 820px) {{
      .shell {{
        grid-template-columns: 1fr;
        height: 100vh;
      }}

      .sidebar {{
        border-right: 0;
        border-bottom: 1px solid var(--line);
        max-height: 48vh;
      }}

      .shell.sidebar-hidden {{
        grid-template-columns: 1fr;
      }}

      .shell.sidebar-hidden .sidebar {{
        display: none;
      }}

      .home-stats, .home-grid, .home-search-map, .home-solution-grid {{
        grid-template-columns: 1fr;
      }}

      .home-hero {{
        min-height: auto;
      }}

      .home-title {{
        font-size: 40px;
      }}

      .home-lead {{
        font-size: 17px;
      }}
    }}
  </style>
</head>
<body>
  <div class="shell">
    <button class="sidebar-toggle" id="sidebar-toggle" type="button">Скрыть список</button>
    <aside class="sidebar">
      <div class="brand">
        <h1><a href="#home" style="color:inherit;text-decoration:none;">Графы</a></h1>
        <div class="meta" id="db-meta"></div>
      </div>
      <div class="search">
        <button class="mode-button" id="mode-home" type="button">Главная</button>
        <div class="mode-toggle">
          <button class="mode-button active" id="mode-problems" type="button">Задачи</button>
          <button class="mode-button" id="mode-definitions" type="button">Определения</button>
          <button class="mode-button" id="mode-ideas" type="button">Идеи</button>
          <button class="mode-button" id="mode-comments" type="button">Комментарии</button>
        </div>
        <input id="search-input" type="search" placeholder="Поиск">
        <select id="local-progress-filter"></select>
        <div class="local-data-actions" aria-label="Локальные данные">
          <button class="small-button" id="local-export" type="button">Экспорт</button>
          <button class="small-button" id="local-import" type="button">Импорт</button>
          <button class="small-button" id="local-reset" type="button">Сброс</button>
          <input id="local-import-file" type="file" accept="application/json,.json" hidden>
        </div>
        <select id="source-filter"></select>
        <select id="author-filter"></select>
        <select id="year-filter"></select>
        <select id="solution-filter"></select>
        <select id="goal-filter"></select>
        <select id="object-filter"></select>
        <select id="method-filter"></select>
        <select id="type-filter"></select>
      </div>
      <div class="list" id="list"></div>
    </aside>
    <main>
      <div class="content" id="content"></div>
    </main>
  </div>

  <script id="db-data" type="application/json">{payload}</script>
  <script>
    const DB = JSON.parse(document.getElementById('db-data').textContent);
    const problems = DB.problems;
    const relations = DB.relations;
    const comments = DB.comments;
    const sources = DB.sources;
    const definitions = DB.definitions;
    const standardIdeas = DB.standard_ideas;
    const taxonomy = DB.taxonomy;

    function storageGet(key) {{
      try {{ return window.localStorage?.getItem(key) ?? null; }}
      catch (_error) {{ return null; }}
    }}

    function storageSet(key, value) {{
      try {{ window.localStorage?.setItem(key, value); }}
      catch (_error) {{}}
    }}

    function storageRemove(key) {{
      try {{ window.localStorage?.removeItem(key); }}
      catch (_error) {{}}
    }}

    const LOCAL_DATA_KEY = 'graph-db:local-user-data:v1';
    const LOCAL_DATA_VERSION = 1;
    const FEEDBACK_CONFIG = {feedback_config_js};
    const PROGRESS_OPTIONS = [
      {{ value: 'not_started', label: 'не решал' }},
      {{ value: 'tried', label: 'пробовал' }},
      {{ value: 'solved', label: 'решил' }},
      {{ value: 'later', label: 'вернуться позже' }}
    ];
    const PROGRESS_LABELS = Object.fromEntries(PROGRESS_OPTIONS.map(item => [item.value, item.label]));

    function emptyLocalData() {{
      return {{ version: LOCAL_DATA_VERSION, problems: {{}}, updated_at: null }};
    }}

    function normalizeLocalEntry(entry) {{
      if (!entry || typeof entry !== 'object') return {{}};
      const progress = PROGRESS_LABELS[entry.progress] ? entry.progress : 'not_started';
      const note = typeof entry.note === 'string' ? entry.note : '';
      const updated_at = typeof entry.updated_at === 'string' ? entry.updated_at : undefined;
      const result = {{}};
      if (progress !== 'not_started') result.progress = progress;
      if (note) result.note = note;
      if (updated_at && (result.progress || result.note)) result.updated_at = updated_at;
      return result;
    }}

    function loadLocalData() {{
      const raw = storageGet(LOCAL_DATA_KEY);
      if (!raw) return emptyLocalData();
      try {{
        const parsed = JSON.parse(raw);
        const result = emptyLocalData();
        const entries = parsed?.problems && typeof parsed.problems === 'object' ? parsed.problems : {{}};
        for (const [id, entry] of Object.entries(entries)) {{
          const normalized = normalizeLocalEntry(entry);
          if (normalized.progress || normalized.note) result.problems[id] = normalized;
        }}
        result.updated_at = typeof parsed?.updated_at === 'string' ? parsed.updated_at : null;
        return result;
      }} catch (_error) {{
        return emptyLocalData();
      }}
    }}

    let localData = loadLocalData();

    function saveLocalData() {{
      localData.version = LOCAL_DATA_VERSION;
      localData.updated_at = new Date().toISOString();
      storageSet(LOCAL_DATA_KEY, JSON.stringify(localData));
    }}

    function localEntry(problemId) {{
      return localData.problems[problemId] || {{}};
    }}

    function localProgress(problemId) {{
      return localEntry(problemId).progress || 'not_started';
    }}

    function localNote(problemId) {{
      return localEntry(problemId).note || '';
    }}

    function setLocalEntry(problemId, patch) {{
      const current = {{ ...localEntry(problemId), ...patch }};
      const normalized = normalizeLocalEntry({{ ...current, updated_at: new Date().toISOString() }});
      if (normalized.progress || normalized.note) localData.problems[problemId] = normalized;
      else delete localData.problems[problemId];
      saveLocalData();
    }}

    const state = {{
      query: '',
      localProgress: 'all',
      goal: 'all',
      object: 'all',
      method: 'all',
      type: 'all',
      source: 'all',
      author: 'all',
      year: 'all',
      solution: 'all',
      view: 'problems',
      sidebarHidden: storageGet('kg-sidebar-hidden') === '1'
    }};

    const byId = (id) => document.getElementById(id);
    const esc = (value) => String(value ?? '')
      .replaceAll('&', '&amp;')
      .replaceAll('<', '&lt;')
      .replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;')
      .replaceAll("'", '&#039;');

    function applySidebarState() {{
      document.querySelector('.shell').classList.toggle('sidebar-hidden', state.sidebarHidden);
      byId('sidebar-toggle').textContent = state.sidebarHidden ? 'Показать список' : 'Скрыть список';
    }}

    function reveal(summary, html) {{
      if (!html || !html.trim()) return '';
      return `<details class="reveal"><summary>${{esc(summary)}}</summary>${{html}}</details>`;
    }}

    function enhanceReveals() {{
      document.querySelectorAll('details.reveal').forEach(details => {{
        details.addEventListener('toggle', () => {{
          if (details.open && window.MathJax?.typesetPromise) MathJax.typesetPromise([details]);
        }}, {{ once: true }});
      }});
    }}

    function label(map, id) {{
      return map?.[id]?.title || id;
    }}

    function prettyText(value) {{
      return esc(value)
        .replaceAll('&lt;=', '≤')
        .replaceAll('&gt;=', '≥')
        .replaceAll('-&gt;', '→');
    }}

    function escapeRegExp(value) {{
      return value.replace(/[.*+?^${{}}()|[\\]\\\\]/g, '\\\\$&');
    }}

    function isTermChar(char) {{
      return /[А-Яа-яA-Za-z0-9_]/.test(char || '');
    }}

    function linkTerms(html, replacements, className, hrefForId) {{
      replacements.sort((a, b) => b.alias.length - a.alias.length);
      const used = new Set();
      let result = '';
      let index = 0;
      while (index < html.length) {{
        if (html.startsWith('<a ', index)) {{
          const end = html.indexOf('</a>', index);
          if (end !== -1) {{
            result += html.slice(index, end + 4);
            index = end + 4;
            continue;
          }}
        }}
        if (html[index] === '<') {{
          const end = html.indexOf('>', index);
          if (end !== -1) {{
            result += html.slice(index, end + 1);
            index = end + 1;
            continue;
          }}
        }}
        const match = replacements.find(item => {{
          if (used.has(item.id)) return false;
          const alias = esc(item.alias);
          if (html.slice(index, index + alias.length).toLocaleLowerCase('ru') !== alias.toLocaleLowerCase('ru')) return false;
          return !isTermChar(html[index - 1]) && !isTermChar(html[index + alias.length]);
        }});
        if (match) {{
          const alias = esc(match.alias);
          const text = html.slice(index, index + alias.length);
          result += `<a class="${{className}}" href="${{hrefForId(match.id)}}">${{text}}</a>`;
          used.add(match.id);
          index += alias.length;
        }} else {{
          result += html[index];
          index += 1;
        }}
      }}
      return result;
    }}

    function linkDefinitions(html, definitionIds = []) {{
      const replacements = [];
      definitionIds.forEach(id => {{
        const definition = definitions[id];
        if (!definition) return;
        (definition.aliases || []).forEach(alias => {{
          if (!alias.includes('\\\\')) replacements.push({{ id, alias }});
        }});
      }});
      return linkTerms(html, replacements, 'def-link', id => `#def-${{encodeURIComponent(id)}}`);
    }}

    function linkStandardIdeas(html, ideaIds = []) {{
      const replacements = [];
      ideaIds.forEach(id => {{
        const idea = standardIdeas[id];
        if (!idea) return;
        (idea.aliases || []).forEach(alias => replacements.push({{ id, alias }}));
      }});
      return linkTerms(html, replacements, 'idea-link', id => `#stdidea-${{encodeURIComponent(id)}}`);
    }}

    function textSegments(text) {{
      const lines = String(text || '').replace(/\\r\\n?/g, '\\n').split('\\n');
      const segments = [];
      let paragraph = [];
      let displayMath = [];
      let inDisplayMath = false;

      const flushParagraph = () => {{
        if (!paragraph.length) return;
        segments.push({{ type: 'paragraph', text: paragraph.join('\\n') }});
        paragraph = [];
      }};

      const flushDisplayMath = () => {{
        if (!displayMath.length) return;
        segments.push({{ type: 'display-math', text: displayMath.join('\\n') }});
        displayMath = [];
      }};

      lines.forEach(line => {{
        const trimmed = line.trim();
        if (inDisplayMath) {{
          displayMath.push(line);
          if (trimmed.endsWith('\\\\]')) {{
            flushDisplayMath();
            inDisplayMath = false;
          }}
          return;
        }}
        if (trimmed.startsWith('\\\\[')) {{
          flushParagraph();
          displayMath.push(line);
          if (trimmed.endsWith('\\\\]')) {{
            flushDisplayMath();
          }} else {{
            inDisplayMath = true;
          }}
          return;
        }}
        if (!trimmed) {{
          flushParagraph();
          return;
        }}
        paragraph.push(line);
      }});

      flushParagraph();
      flushDisplayMath();
      return segments;
    }}

    function renderTextSegment(segment, definitionIds = [], standardIdeaIds = []) {{
      let html = prettyText(segment.text);
      html = linkDefinitions(html, definitionIds);
      html = linkStandardIdeas(html, standardIdeaIds);
      const className = segment.type === 'display-math' ? 'text-display-math' : 'text-paragraph';
      return `<div class="${{className}}">${{html}}</div>`;
    }}

    function textBlock(text, definitionIds = [], standardIdeaIds = []) {{
      const html = textSegments(text || '')
        .map(segment => renderTextSegment(segment, definitionIds, standardIdeaIds))
        .join('');
      return `<div class="text">${{html}}</div>`;
    }}

    function renderExample(example, definitionIds = [], standardIdeaIds = []) {{
      if (typeof example === 'string') {{
        return `<div class="example-card">${{textBlock(example, definitionIds, standardIdeaIds)}}</div>`;
      }}
      if (!example || typeof example !== 'object') return '';
      const title = example.title || 'Пример';
      const optional = example.optional ? `<span class="example-optional">необязательный блок</span>` : '';
      if (example.type === 'image') {{
        const alt = example.alt || title;
        const caption = example.caption ? `<figcaption class="example-caption">${{textBlock(example.caption, definitionIds, standardIdeaIds)}}</figcaption>` : '';
        return `
          <div class="example-card">
            <div class="example-label">
              <span>${{esc(title)}}</span>
              ${{optional}}
            </div>
            <figure class="example-figure">
              <img class="example-image" src="${{esc(example.path)}}" alt="${{esc(alt)}}">
              ${{caption}}
            </figure>
          </div>
        `;
      }}
      return `
        <div class="example-card">
          <div class="example-label">
            <span>${{esc(title)}}</span>
            ${{optional}}
          </div>
          ${{textBlock(example.text || '', definitionIds, standardIdeaIds)}}
        </div>
      `;
    }}

    function renderExamples(examples, definitionIds = [], standardIdeaIds = []) {{
      if (!examples || !examples.length) return '';
      return `
        <div class="example-stack">
          ${{examples.map(example => renderExample(example, definitionIds, standardIdeaIds)).join('')}}
        </div>
      `;
    }}

    function statusPill(status) {{
      if (!status) return '';
      return `<span class="pill status-${{esc(status)}}">${{esc(label(taxonomy.statuses, status))}}</span>`;
    }}

    function commentStatusPill(status) {{
      if (!status) return '';
      return `<span class="pill">${{esc(label(taxonomy.comment_statuses, status))}}</span>`;
    }}

    function tagPill(tag) {{
      return `<span class="pill">${{esc(label(taxonomy.tags, tag))}}</span>`;
    }}

    function definitionPill(id) {{
      return definitions[id] ? `<a class="pill" href="#def-${{encodeURIComponent(id)}}">${{esc(definitions[id].title)}}</a>` : '';
    }}

    function standardIdeaPill(id) {{
      return standardIdeas[id] ? `<a class="pill" href="#stdidea-${{encodeURIComponent(id)}}">${{esc(standardIdeas[id].title)}}</a>` : '';
    }}

    function renderAuthors(problem) {{
      const authors = problem.authors || [];
      if (!authors.length) return '';
      const items = authors.map(author => {{
        const authorData = typeof author === 'string' ? {{ name: author }} : (author || {{}});
        const name = esc(authorData.name || '?');
        const review = authorData.status && authorData.status !== 'source_verified'
          ? `<span class="pill">${{esc(label(taxonomy.statuses, authorData.status) || authorData.status)}}</span>`
          : '';
        return `<span class="author-entry"><span>${{name}}</span>${{review}}</span>`;
      }}).join('');
      return `
        <div class="section">
          <h3>Авторы</h3>
          <div class="card">
            <div class="pill-row">${{items}}</div>
          </div>
        </div>
      `;
    }}

    function sortedProblems() {{
      return Object.values(problems).sort((a, b) => a.title.localeCompare(b.title, 'ru'));
    }}

    function sortedDefinitions() {{
      return Object.values(definitions).sort((a, b) => a.title.localeCompare(b.title, 'ru'));
    }}

    function sortedStandardIdeas() {{
      return Object.values(standardIdeas).sort((a, b) => a.title.localeCompare(b.title, 'ru'));
    }}

    function sortedComments() {{
      return Object.values(comments).sort((a, b) => {{
        const dateCmp = String(b.created_at || '').localeCompare(String(a.created_at || ''));
        if (dateCmp) return dateCmp;
        return a.id.localeCompare(b.id, 'ru');
      }});
    }}

    function searchBlob(value) {{
      return JSON.stringify(value).toLowerCase();
    }}

    function normalizeCompact(value) {{
      return String(value || '').toLowerCase().replace(/[^a-z0-9а-яё]+/g, '');
    }}

    function firstYear(value) {{
      const match = String(value || '').match(/(19|20)\\d{{2}}/);
      return match ? match[0] : '';
    }}

    function problemYear(problem) {{
      const idMatch = String(problem.id || '').match(/^[a-z0-9-]+-((19|20)\\d{{2}})(?:-|$)/);
      return idMatch ? idMatch[1] : firstYear(problem.id) || firstYear(problem.title);
    }}

    function normalizeAuthor(value) {{
      return normalizeCompact(value);
    }}

    function problemAuthors(problem) {{
      return (problem.authors || [])
        .map(author => String((typeof author === 'string' ? author : author.name) || '').trim())
        .filter(name => name && name !== '?');
    }}

    function problemAuthorKeys(problem) {{
      return problemAuthors(problem).map(normalizeAuthor).filter(Boolean);
    }}

    function sourceFamilies() {{
      return [
        {{ key: 'all-union', prefixes: ['all-union'], label: 'Всесоюзная олимпиада', aliases: ['всесоюзная'] }},
        {{ key: 'apmo', prefixes: ['apmo'], label: 'APMO', aliases: ['apmo'] }},
        {{ key: 'baltic-way', prefixes: ['baltic-way'], label: 'Baltic Way', aliases: ['balticway'] }},
        {{ key: 'bmo', prefixes: ['bmo'], label: 'BMO', aliases: ['bmo'] }},
        {{ key: 'cmo', prefixes: ['cmo'], label: 'CMO', aliases: ['cmo'] }},
        {{ key: 'egmo', prefixes: ['egmo'], label: 'EGMO', aliases: ['egmo'] }},
        {{ key: 'fyum', prefixes: ['fyum'], label: 'ФЮМ', aliases: ['fyum', 'фюм'] }},
        {{ key: 'imc', prefixes: ['imc'], label: 'IMC', aliases: ['imc'] }},
        {{ key: 'imo', prefixes: ['imo'], label: 'IMO Shortlist', aliases: ['imo'] }},
        {{ key: 'inmo', prefixes: ['inmo'], label: 'INMO', aliases: ['inmo'] }},
        {{ key: 'kolmogorov', prefixes: ['kolmogorov'], label: 'Кубок Колмогорова', aliases: ['kolmogorov', 'колмогоров'] }},
        {{ key: 'memo', prefixes: ['memo'], label: 'MEMO', aliases: ['memo'] }},
        {{ key: 'miklos-schweitzer', prefixes: ['miklos-schweitzer'], label: 'Schweitzer', aliases: ['schweitzer', 'миклош'] }},
        {{ key: 'mmo', prefixes: ['mmo'], label: 'ММО', aliases: ['mmo', 'ммо'] }},
        {{ key: 'polish-mo', prefixes: ['polish-mo'], label: 'Польская MO', aliases: ['polishmo', 'польская'] }},
        {{ key: 'putnam', prefixes: ['putnam'], label: 'Putnam', aliases: ['putnam'] }},
        {{ key: 'rmm', prefixes: ['rmm'], label: 'RMM', aliases: ['rmm'] }},
        {{ key: 'school239', prefixes: ['school239'], label: 'Открытая олимпиада ФМЛ 239', aliases: ['239', 'фмл239'] }},
        {{ key: 'simon-marais', prefixes: ['simon-marais'], label: 'Simon Marais', aliases: ['simonmarais'] }},
        {{ key: 'smmc', prefixes: ['smmc'], label: 'SMMC', aliases: ['smmc'] }},
        {{ key: 'spbmo', prefixes: ['spbmo'], label: 'СПбМО', aliases: ['spbmo', 'спбмо'] }},
        {{ key: 'sums', prefixes: ['sums'], label: 'SUMS', aliases: ['sums'] }},
        {{ key: 'tc', prefixes: ['tc'], label: 'Турнир городов', aliases: ['tc', 'турниргородов'] }},
        {{ key: 'usa-tst', prefixes: ['usa-tst'], label: 'USA TST', aliases: ['usatst'] }},
        {{ key: 'usajmo', prefixes: ['usajmo'], label: 'USAJMO', aliases: ['usajmo'] }},
        {{ key: 'usamo', prefixes: ['usamo'], label: 'USAMO', aliases: ['usamo'] }},
        {{ key: 'utyum', prefixes: ['utyum'], label: 'УТЮМ', aliases: ['utyum', 'утюм'] }},
        {{ key: 'vjimc', prefixes: ['vjimc'], label: 'VJIMC', aliases: ['vjimc'] }},
        {{ key: 'vosh', prefixes: ['vosh'], label: 'Всероссийская олимпиада', aliases: ['vosh', 'вош'] }},
        {{ key: 'yumt', prefixes: ['yumt'], label: 'ЮМТ', aliases: ['yumt', 'юмт'] }}
      ];
    }}

    const SOURCE_FAMILIES = sourceFamilies();
    const SOURCE_FAMILY_BY_KEY = Object.fromEntries(SOURCE_FAMILIES.map(item => [item.key, item]));

    function sourceFamilyFromId(problem) {{
      const id = String(problem.id || '').toLowerCase();
      for (const family of SOURCE_FAMILIES) {{
        for (const prefix of family.prefixes) {{
          if (id === prefix || id.startsWith(`${{prefix}}-`) || id.startsWith(`${{prefix}}_`)) return family;
        }}
      }}
      return null;
    }}

    function sourceFamilyFromTitle(problem) {{
      const compactTitle = normalizeCompact(problem.title || '');
      if (compactTitle.includes('турниргородов')) return SOURCE_FAMILY_BY_KEY.tc;
      for (const family of SOURCE_FAMILIES) {{
        if (family.aliases.some(alias => compactTitle.includes(normalizeCompact(alias)))) return family;
      }}
      return null;
    }}

    function fallbackSourceKey(problem) {{
      const idMatch = String(problem.id || '').match(/^([a-z0-9-]+)[-_]((19|20)\\d{{2}})(?:[-_]|$)/);
      if (idMatch) return idMatch[1].split('-')[0];
      return 'misc';
    }}

    function sourceInfo(problem) {{
      const title = String(problem.title || '');
      const family = sourceFamilyFromId(problem) || sourceFamilyFromTitle(problem);
      const key = family?.key || fallbackSourceKey(problem);
      const year = problemYear(problem);
      const aliases = new Set([key, normalizeCompact(title)]);
      (family?.aliases || []).forEach(alias => aliases.add(alias));
      if (year) {{
        aliases.add(`${{key}}${{year}}`);
        (family?.aliases || []).forEach(alias => aliases.add(`${{normalizeCompact(alias)}}${{year}}`));
      }}
      return {{
        key,
        label: family?.label || (key !== 'misc' ? key.toUpperCase() : 'Прочее'),
        year,
        aliases: Array.from(aliases).filter(Boolean)
      }};
    }}

    function realSolutions(problem) {{
      return (problem.solutions || []).filter(solution => {{
        const text = String(solution.text || '').trim();
        const title = String(solution.title || '').trim();
        return text
          && !/^решение пока не найдено[.!]?$/i.test(text)
          && !/близк\\w*\\s+решени\\w*/i.test(title);
      }});
    }}

    function problemHasRealSolution(problem) {{
      return realSolutions(problem).length > 0;
    }}

    function solutionBlob(solution) {{
      return [
        solution.id,
        solution.title,
        solution.text,
        solution.status,
        solution.source_id,
        ...(solution.source_ids || []),
        ...(solution.tags || []),
        ...(solution.review_notes ? [solution.review_notes] : [])
      ].join(' ').toLowerCase();
    }}

    function solutionLooksPublished(solution) {{
      const blob = solutionBlob(solution);
      return solution.status === 'source_verified'
        || Boolean(solution.source_id)
        || (solution.source_ids || []).length > 0
        || /\\b(official|archive|aops|forum|published|source|secondary|reviewed)\\b/i.test(blob)
        || /официальн|архив|опубликован|источник|форум|aops/i.test(blob);
    }}

  function solutionLooksHeavy(solution) {{
     const blob = solutionBlob(solution);
     return /heavy|external|advanced|research|non[- ]?elementary|внешн|тяж[её]л|нешкольн|исследовательск|теорем[ауы]\\s+(ч[еэ]ня|stiebitz|стибиц|kotzig|коциг|tihany|тихани|brooks|брукс|turan|туран|menger|менгер)/i.test(blob);
   }}

  function normalizedSolutionStatusKey(key) {{
    const aliases = {{
      external_published_solution_adapted: 'unofficial_published',
      official_complete: 'official_complete_or_near_complete',
      official_solution: 'official_complete_or_near_complete',
      official_solution_expanded: 'official_plan_completed_by_ai',
      official_solution_restored: 'official_plan_completed_by_ai',
      official_expanded_full_solution: 'official_plan_completed_by_ai',
      official_solution_lemma_extracted: 'official_plan_completed_by_ai',
      published: 'unofficial_published',
      ai: 'ai_original',
      heavy: 'ai_heavy_external_theorem',
      external_theorem_reference: 'hard_external_theorem_no_proof',
      missing: 'missing'
    }};
    return aliases[key] || key;
  }}

  function solutionStatusKey(problem) {{
    const classification = normalizedSolutionStatusKey(problem.editorial?.solution_classification?.type);
    const known = new Set([
      'official_complete_or_near_complete',
      'official_plan_completed_by_ai',
      'unofficial_published',
      'ai_original',
      'ai_heavy_external_theorem',
      'hard_external_theorem_no_proof',
      'missing',
      'no_solution_hard'
    ]);
    if (known.has(classification)) return classification;
    const solutions = realSolutions(problem);
    if (!solutions.length) return 'missing';
    if (solutions.some(solutionLooksHeavy)) return 'ai_heavy_external_theorem';
    if (solutions.some(solutionLooksPublished)) return 'unofficial_published';
    return 'ai_original';
  }}

  function solutionStatusBroadKey(problem) {{
    const key = normalizedSolutionStatusKey(solutionStatusKey(problem));
      if (key === 'no_solution_hard' || key === 'missing') return 'missing';
      if (key === 'ai_original' || key === 'ai') return 'ai';
      if (key === 'ai_heavy_external_theorem' || key === 'heavy') return 'heavy';
      return 'published';
    }}

    function solutionStatusMatches(problem, selected) {{
      if (selected === 'all') return true;
      if (selected === 'with') return problemHasRealSolution(problem);
      if (selected === 'without') return !problemHasRealSolution(problem);
      return selected === solutionStatusKey(problem) || selected === solutionStatusBroadKey(problem);
    }}

    function solutionStatusLabel(key) {{
      const labels = {{
        published: 'опубликованное решение',
        ai: 'ИИ-решение',
        heavy: 'решение с тяжёлыми внешними теоремами',
        missing: 'решения нет',
        official_complete_or_near_complete: 'официальное полное/почти полное',
        official_outline_needs_work: 'официальный план, нужна доработка',
        official_plan_completed_by_ai: 'официальный план, доведённый ИИ',
        unofficial_published: 'опубликованное неофициальное',
        ai_original: 'решение ИИ с нуля',
        ai_heavy_external_theorem: 'ИИ/решение с тяжёлыми внешними теоремами',
        hard_external_theorem_no_proof: 'доказательство не приведено: тяжёлая внешняя теорема',
        no_solution_hard: 'решения нет, гроб',
        with: 'есть решение',
        without: 'решения нет'
      }};
      return labels[key] || key;
    }}

    function solutionStatusPill(problem) {{
      const key = solutionStatusKey(problem);
      const detail = problem.editorial?.solution_classification?.label;
      const title = detail ? ` title="${{esc(detail)}}"` : '';
      return '<span class="pill solution-status solution-status-' + esc(key) + '"' + title + '>' + esc(solutionStatusLabel(key)) + '</span>';
    }}

    function problemSearchBlob(problem) {{
      const info = sourceInfo(problem);
      const solutionState = solutionStatusKey(problem);
      const extra = {{
        source_key: info.key,
        source_label: info.label,
        source_aliases: info.aliases,
        authors: problemAuthors(problem),
        year: info.year,
        solution_state: solutionState,
        solution_state_label: solutionStatusLabel(solutionState),
        has_solution: problemHasRealSolution(problem) ? 'with_solution' : 'without_solution'
      }};
      return searchBlob({{ ...problem, _search_meta: extra }});
    }}

    function tagCategory(tag) {{
      return taxonomy.tags?.[tag]?.category || 'other';
    }}

    function tagInCategories(tag, categories) {{
      return categories.includes(tagCategory(tag));
    }}

    function categoryFilterOk(problem, stateKey) {{
      const selected = state[stateKey];
      return selected === 'all' || (problem.tags || []).includes(selected);
    }}

    function problemTypeKey(problem) {{
      const tags = problem.tags || [];
      if (tags.includes('classical_theorem')) return 'classical_theorem';
      const primary = problem.kind?.primary || 'olympiad_problem';
      if (['theorem', 'lemma', 'corollary', 'problem_family'].includes(primary)) return primary;
      if ((problem.kind?.secondary || []).includes('classical_tool')) return 'classical_tool';
      return 'olympiad_problem';
    }}

    function problemTypeLabel(type) {{
      const labels = {{
        olympiad_problem: 'Задача',
        theorem: 'Теорема',
        lemma: 'Лемма',
        corollary: 'Следствие',
        problem_family: 'Семейство задач',
        classical_theorem: 'Классическая теорема',
        classical_tool: 'Классический инструмент'
      }};
      return labels[type] || type;
    }}

    function problemMatchesFilters(problem, options = {{}}) {{
      const query = state.query.trim().toLowerCase();
      const info = sourceInfo(problem);
      if (!options.excludeLocalProgress && state.localProgress !== 'all' && localProgress(problem.id) !== state.localProgress) return false;
      if (!options.excludeGoal && !categoryFilterOk(problem, 'goal')) return false;
      if (!options.excludeObject && !categoryFilterOk(problem, 'object')) return false;
      if (!options.excludeMethod && !categoryFilterOk(problem, 'method')) return false;
      if (!options.excludeType && state.type !== 'all' && problemTypeKey(problem) !== state.type) return false;
      if (!options.excludeSource) {{
        const sourceOk = state.source === 'all' || info.key === state.source;
        if (!sourceOk) return false;
      }}
      if (!options.excludeAuthor) {{
        const authorOk = state.author === 'all' || problemAuthorKeys(problem).includes(state.author);
        if (!authorOk) return false;
      }}
      if (!options.excludeYear) {{
        const yearOk = state.year === 'all' || info.year === state.year;
        if (!yearOk) return false;
      }}
      if (!options.excludeSolution) {{
        const solutionOk = solutionStatusMatches(problem, state.solution);
        if (!solutionOk) return false;
      }}
      if (!options.excludeQuery) {{
        const compactQuery = normalizeCompact(query);
        const queryWords = query.split(/\\s+/).filter(Boolean);
        const blob = problemSearchBlob(problem);
        const wordsOk = queryWords.every(word => blob.includes(word));
        const queryOk = !query
          || blob.includes(query)
          || wordsOk
          || (compactQuery && info.aliases.some(alias => alias.includes(compactQuery)));
        if (!queryOk) return false;
      }}
      return true;
    }}

    function filteredProblems() {{
      return sortedProblems().filter(problem => problemMatchesFilters(problem));
    }}

    function filteredDefinitions() {{
      const query = state.query.trim().toLowerCase();
      const words = query.split(/\\s+/).filter(Boolean);
      return sortedDefinitions().filter(item => {{
        const blob = searchBlob(item);
        return !query || blob.includes(query) || words.every(word => blob.includes(word));
      }});
    }}

    function filteredStandardIdeas() {{
      const query = state.query.trim().toLowerCase();
      const words = query.split(/\\s+/).filter(Boolean);
      return sortedStandardIdeas().filter(item => {{
        const blob = searchBlob(item);
        return !query || blob.includes(query) || words.every(word => blob.includes(word));
      }});
    }}

    function filteredComments() {{
      const query = state.query.trim().toLowerCase();
      const words = query.split(/\\s+/).filter(Boolean);
      return sortedComments().filter(item => {{
        const blob = searchBlob(item);
        return !query || blob.includes(query) || words.every(word => blob.includes(word));
      }});
    }}

    function currentRoute() {{
      const id = decodeURIComponent(location.hash.replace(/^#/, ''));
      if (!id || id === 'home') return {{ type: 'home', id: 'home' }};
      if (id === 'comments') return {{ type: 'comment', id: null }};
      if (id.startsWith('def-')) {{
        const definitionId = id.slice(4);
        if (definitions[definitionId]) return {{ type: 'definition', id: definitionId }};
      }}
      if (id.startsWith('stdidea-')) {{
        const ideaId = id.slice(8);
        if (standardIdeas[ideaId]) return {{ type: 'idea', id: ideaId }};
      }}
      if (id.startsWith('comment-')) {{
        const commentId = id.slice(8);
        if (comments[commentId]) return {{ type: 'comment', id: commentId }};
      }}
      if (problems[id]) return {{ type: 'problem', id }};
      if (state.view === 'definitions') return {{ type: 'definition', id: sortedDefinitions()[0]?.id }};
      if (state.view === 'ideas') return {{ type: 'idea', id: sortedStandardIdeas()[0]?.id }};
      if (state.view === 'comments') return {{ type: 'comment', id: sortedComments()[0]?.id || null }};
      return {{ type: 'problem', id: sortedProblems()[0]?.id }};
    }}

    function setHome() {{
      location.hash = 'home';
      render();
    }}

    function setProblem(id) {{
      state.view = 'problems';
      location.hash = encodeURIComponent(id);
      render();
    }}

    function setDefinition(id) {{
      state.view = 'definitions';
      location.hash = `def-${{encodeURIComponent(id)}}`;
      render();
    }}

    function setStandardIdea(id) {{
      state.view = 'ideas';
      location.hash = `stdidea-${{encodeURIComponent(id)}}`;
      render();
    }}

    function setComment(id) {{
      state.view = 'comments';
      location.hash = id ? `comment-${{encodeURIComponent(id)}}` : 'comments';
      render();
    }}

    function activateListRoute(link) {{
      const id = link?.dataset?.listId;
      if (!id) return;
      if (link.dataset.listRoute === 'definition') setDefinition(id);
      else if (link.dataset.listRoute === 'idea') setStandardIdea(id);
      else if (link.dataset.listRoute === 'comment') setComment(id);
      else setProblem(id);
    }}

    function routeHash(type, id) {{
      if (!id) return '';
      if (type === 'definition') return `def-${{encodeURIComponent(id)}}`;
      if (type === 'idea') return `stdidea-${{encodeURIComponent(id)}}`;
      if (type === 'comment') return `comment-${{encodeURIComponent(id)}}`;
      return encodeURIComponent(id);
    }}

    function firstVisibleRoute() {{
      if (state.view === 'definitions') return {{ type: 'definition', id: filteredDefinitions()[0]?.id }};
      if (state.view === 'ideas') return {{ type: 'idea', id: filteredStandardIdeas()[0]?.id }};
      if (state.view === 'comments') return {{ type: 'comment', id: filteredComments()[0]?.id }};
      return {{ type: 'problem', id: filteredProblems()[0]?.id }};
    }}

    function selectFirstVisibleRoute() {{
      const route = firstVisibleRoute();
      const nextHash = routeHash(route.type, route.id);
      if (!nextHash) {{
        render();
        return;
      }}
      if (location.hash.replace(/^#/, '') === nextHash) render();
      else location.hash = nextHash;
    }}

    function problemUsesDefinition(problem, definitionId) {{
      const statementsUse = Object.values(problem.statements || {{}}).some(group =>
        (group || []).some(statement => (statement.definition_ids || []).includes(definitionId))
      );
      const solutionsUse = (problem.solutions || []).some(solution =>
        (solution.definition_ids || []).includes(definitionId)
      );
      return statementsUse || solutionsUse;
    }}

    function definitionUsage(definitionId) {{
      return sortedProblems().filter(problem => problemUsesDefinition(problem, definitionId));
    }}

    function solutionUsesStandardIdea(solution, ideaId) {{
      return (solution.standard_idea_ids || []).includes(ideaId);
    }}

    function standardIdeaUsage(ideaId) {{
      const items = [];
      sortedProblems().forEach(problem => {{
        (problem.solutions || []).forEach(solution => {{
          if (solutionUsesStandardIdea(solution, ideaId)) items.push({{ problem, solution }});
        }});
      }});
      return items;
    }}

    function relationsForProblem(problemId) {{
      return relations.filter(rel => rel.from === problemId || rel.to === problemId);
    }}

    function commentsForProblem(problemId) {{
      return sortedComments().filter(comment => comment.target?.type === 'problem' && comment.target?.problem_id === problemId);
    }}

    function architectureComments() {{
      return sortedComments().filter(comment => comment.target?.type === 'architecture');
    }}

    function renderSidebar() {{
      const route = currentRoute();
      state.view = route.type === 'definition' ? 'definitions' : route.type === 'idea' ? 'ideas' : route.type === 'comment' ? 'comments' : 'problems';
      byId('db-meta').textContent = `${{Object.keys(problems).length}} карточек · ${{Object.keys(definitions).length}} определений · ${{Object.keys(standardIdeas).length}} идей · ${{relations.length}} связей · ${{Object.keys(comments).length}} комментариев`;
      byId('mode-home').classList.toggle('active', route.type === 'home');
      byId('mode-problems').classList.toggle('active', state.view === 'problems' && route.type !== 'home');
      byId('mode-definitions').classList.toggle('active', state.view === 'definitions');
      byId('mode-ideas').classList.toggle('active', state.view === 'ideas');
      byId('mode-comments').classList.toggle('active', state.view === 'comments');

      const list = byId('list');
      if (state.view === 'definitions') {{
        list.innerHTML = filteredDefinitions().map(item => `
          <a class="list-button ${{item.id === route.id ? 'active' : ''}}" href="#def-${{encodeURIComponent(item.id)}}" data-list-route="definition" data-list-id="${{esc(item.id)}}">
            <div>${{esc(item.title)}}</div>
            <div class="id">${{esc(item.id)}} · задач: ${{definitionUsage(item.id).length}}</div>
          </a>
        `).join('');
      }} else if (state.view === 'ideas') {{
        list.innerHTML = filteredStandardIdeas().map(item => `
          <a class="list-button ${{item.id === route.id ? 'active' : ''}}" href="#stdidea-${{encodeURIComponent(item.id)}}" data-list-route="idea" data-list-id="${{esc(item.id)}}">
            <div>${{esc(item.title)}}</div>
            <div class="id">${{esc(item.id)}} · задач: ${{standardIdeaUsage(item.id).length}}</div>
          </a>
        `).join('');
      }} else if (state.view === 'comments') {{
        const items = filteredComments();
        list.innerHTML = items.length ? items.map(item => {{
          const targetTitle = item.target?.type === 'problem'
            ? (problems[item.target.problem_id]?.title || item.target.problem_id)
            : 'Архитектура базы';
          return `
            <a class="list-button ${{item.id === route.id ? 'active' : ''}}" href="#comment-${{encodeURIComponent(item.id)}}" data-list-route="comment" data-list-id="${{esc(item.id)}}">
              <div>${{esc(item.title)}}</div>
              <div class="id">${{esc(item.id)}} · ${{esc(targetTitle)}}</div>
            </a>
          `;
        }}).join('') : `<div class="empty" style="padding:10px;">Комментариев пока нет.</div>`;
      }} else {{
        list.innerHTML = filteredProblems().map(item => `
          <a class="list-button ${{item.id === route.id ? 'active' : ''}}" href="#${{encodeURIComponent(item.id)}}" data-list-route="problem" data-list-id="${{esc(item.id)}}">
            <div>${{esc(item.title)}}</div>
            <div class="id">${{[
              item.id,
              solutionStatusLabel(solutionStatusKey(item)),
              localProgress(item.id) !== 'not_started' ? `прогресс: ${{PROGRESS_LABELS[localProgress(item.id)]}}` : '',
              localNote(item.id) ? 'есть заметка' : ''
            ].filter(Boolean).map(esc).join(' · ')}}</div>
          </a>
        `).join('');
      }}
    }}

    function inactiveFilterLabel() {{
      return state.view === 'definitions'
        ? `Определения (${{Object.keys(definitions).length}})`
        : state.view === 'ideas'
        ? `Идеи (${{Object.keys(standardIdeas).length}})`
        : `Комментарии (${{Object.keys(comments).length}})`;
    }}

    function renderTagCategoryFilter(selectId, stateKey, categories, allLabel) {{
      const select = byId(selectId);
      if (state.view !== 'problems') {{
        select.disabled = true;
        select.innerHTML = `<option>${{inactiveFilterLabel()}}</option>`;
        return;
      }}
      select.disabled = false;
      const excludeOption = stateKey === 'goal'
        ? {{ excludeGoal: true }}
        : stateKey === 'object'
        ? {{ excludeObject: true }}
        : {{ excludeMethod: true }};
      const counts = {{}};
      Object.values(problems).forEach(problem => {{
        if (!problemMatchesFilters(problem, excludeOption)) return;
        (problem.tags || []).forEach(tag => {{
          if (!tagInCategories(tag, categories)) return;
          counts[tag] = (counts[tag] || 0) + 1;
        }});
      }});
      const tags = Object.keys(counts).sort((a, b) => label(taxonomy.tags, a).localeCompare(label(taxonomy.tags, b), 'ru'));
      const total = Object.values(problems).filter(problem => problemMatchesFilters(problem, excludeOption)).length;
      select.innerHTML = `<option value="all">${{allLabel}} (${{total}})</option>` + tags.map(tag =>
        `<option value="${{esc(tag)}}">${{esc(label(taxonomy.tags, tag))}} (${{counts[tag]}})</option>`
      ).join('');
      select.value = state[stateKey];
      if (select.value !== state[stateKey]) {{
        state[stateKey] = 'all';
        select.value = 'all';
      }}
    }}

    function renderGoalFilter() {{
      renderTagCategoryFilter('goal-filter', 'goal', ['goal'], 'Все цели');
    }}

    function renderObjectFilter() {{
      renderTagCategoryFilter('object-filter', 'object', ['object', 'topic'], 'Все объекты');
    }}

    function renderMethodFilter() {{
      renderTagCategoryFilter('method-filter', 'method', ['method'], 'Все методы');
    }}

    function renderTypeFilter() {{
      const select = byId('type-filter');
      if (state.view !== 'problems') {{
        select.disabled = true;
        select.innerHTML = `<option>${{inactiveFilterLabel()}}</option>`;
        return;
      }}
      select.disabled = false;
      const counts = {{}};
      Object.values(problems).forEach(problem => {{
        if (!problemMatchesFilters(problem, {{ excludeType: true }})) return;
        const type = problemTypeKey(problem);
        counts[type] = (counts[type] || 0) + 1;
      }});
      const order = ['olympiad_problem', 'problem_family', 'theorem', 'lemma', 'corollary', 'classical_theorem', 'classical_tool'];
      const types = Object.keys(counts).sort((a, b) => {{
        const indexA = order.includes(a) ? order.indexOf(a) : order.length;
        const indexB = order.includes(b) ? order.indexOf(b) : order.length;
        return indexA - indexB || problemTypeLabel(a).localeCompare(problemTypeLabel(b), 'ru');
      }});
      const total = Object.values(problems).filter(problem => problemMatchesFilters(problem, {{ excludeType: true }})).length;
      select.innerHTML = `<option value="all">Все типы (${{total}})</option>` + types.map(type =>
        `<option value="${{esc(type)}}">${{esc(problemTypeLabel(type))}} (${{counts[type]}})</option>`
      ).join('');
      select.value = state.type;
      if (select.value !== state.type) {{
        state.type = 'all';
        select.value = 'all';
      }}
    }}

    function renderLocalProgressFilter() {{
      const select = byId('local-progress-filter');
      if (state.view !== 'problems') {{
        select.disabled = true;
        select.innerHTML = `<option>${{inactiveFilterLabel()}}</option>`;
        return;
      }}
      select.disabled = false;
      const matching = Object.values(problems).filter(problem => problemMatchesFilters(problem, {{ excludeLocalProgress: true }}));
      const counts = Object.fromEntries(PROGRESS_OPTIONS.map(item => [item.value, 0]));
      matching.forEach(problem => {{
        const key = localProgress(problem.id);
        counts[key] = (counts[key] || 0) + 1;
      }});
      select.innerHTML = `<option value="all">Любой локальный прогресс (${{matching.length}})</option>` + PROGRESS_OPTIONS.map(item =>
        `<option value="${{esc(item.value)}}">${{esc(item.label)}} (${{counts[item.value] || 0}})</option>`
      ).join('');
      select.value = state.localProgress;
      if (select.value !== state.localProgress) {{
        state.localProgress = 'all';
        select.value = 'all';
      }}
    }}

    function renderSourceFilter() {{
      const select = byId('source-filter');
      if (state.view !== 'problems') {{
        select.disabled = true;
        select.innerHTML = `<option>Источники</option>`;
        return;
      }}
      select.disabled = false;
      const counts = {{}};
      const labels = {{}};
      Object.values(problems).forEach(problem => {{
        if (!problemMatchesFilters(problem, {{ excludeSource: true }})) return;
        const info = sourceInfo(problem);
        counts[info.key] = (counts[info.key] || 0) + 1;
        labels[info.key] = info.label;
      }});
      const keys = Object.keys(counts).sort((a, b) => labels[a].localeCompare(labels[b], 'ru'));
      const total = Object.values(problems).filter(problem => problemMatchesFilters(problem, {{ excludeSource: true }})).length;
      select.innerHTML = `<option value="all">Все источники (${{total}})</option>` + keys.map(key =>
        `<option value="${{esc(key)}}">${{esc(labels[key])}} (${{counts[key]}})</option>`
      ).join('');
      select.value = state.source;
      if (select.value !== state.source) {{
        state.source = 'all';
        select.value = 'all';
      }}
    }}

    function renderAuthorFilter() {{
      const select = byId('author-filter');
      if (state.view !== 'problems') {{
        select.disabled = true;
        select.innerHTML = `<option>Авторы</option>`;
        return;
      }}
      select.disabled = false;
      const counts = {{}};
      const labels = {{}};
      Object.values(problems).forEach(problem => {{
        if (!problemMatchesFilters(problem, {{ excludeAuthor: true }})) return;
        problemAuthors(problem).forEach(author => {{
          const key = normalizeAuthor(author);
          if (!key) return;
          counts[key] = (counts[key] || 0) + 1;
          labels[key] = author;
        }});
      }});
      const keys = Object.keys(counts).sort((a, b) => labels[a].localeCompare(labels[b], 'ru'));
      const total = Object.values(problems).filter(problem => problemMatchesFilters(problem, {{ excludeAuthor: true }})).length;
      select.innerHTML = `<option value="all">Все авторы (${{total}})</option>` + keys.map(key =>
        `<option value="${{esc(key)}}">${{esc(labels[key])}} (${{counts[key]}})</option>`
      ).join('');
      select.value = state.author;
      if (select.value !== state.author) {{
        state.author = 'all';
        select.value = 'all';
      }}
    }}

    function renderYearFilter() {{
      const select = byId('year-filter');
      if (state.view !== 'problems') {{
        select.disabled = true;
        select.innerHTML = `<option>Годы</option>`;
        return;
      }}
      select.disabled = false;
      const counts = {{}};
      Object.values(problems).forEach(problem => {{
        if (!problemMatchesFilters(problem, {{ excludeYear: true }})) return;
        const year = problemYear(problem);
        if (!year) return;
        counts[year] = (counts[year] || 0) + 1;
      }});
      const years = Object.keys(counts).sort((a, b) => a.localeCompare(b, 'ru'));
      const total = Object.values(problems).filter(problem => problemMatchesFilters(problem, {{ excludeYear: true }})).length;
      select.innerHTML = `<option value="all">Все годы (${{total}})</option>` + years.map(year =>
        `<option value="${{esc(year)}}">${{esc(year)}} (${{counts[year]}})</option>`
      ).join('');
      select.value = state.year;
      if (select.value !== state.year) {{
        state.year = 'all';
        select.value = 'all';
      }}
    }}

    function renderSolutionFilter() {{
      const select = byId('solution-filter');
      if (state.view !== 'problems') {{
        select.disabled = true;
        select.innerHTML = `<option>Решения</option>`;
        return;
      }}
      select.disabled = false;
      const matching = Object.values(problems).filter(problem => problemMatchesFilters(problem, {{ excludeSolution: true }}));
      const counts = {{
        official_complete_or_near_complete: 0,
        official_plan_completed_by_ai: 0,
        unofficial_published: 0,
        ai_original: 0,
        ai_heavy_external_theorem: 0,
        hard_external_theorem_no_proof: 0,
        missing: 0,
        no_solution_hard: 0,
        with: 0,
        without: 0
      }};
      matching.forEach(problem => {{
        const key = solutionStatusKey(problem);
        counts[key] = (counts[key] || 0) + 1;
        if (problemHasRealSolution(problem)) counts.with += 1;
        else counts.without += 1;
      }});
      select.innerHTML = [
        `<option value="all">Все задачи (${{matching.length}})</option>`,
        `<option value="with">Есть решение (${{counts.with}})</option>`,
        `<option value="without">Решения нет (${{counts.without}})</option>`,
        `<option value="official_complete_or_near_complete">Официальное полное/почти полное (${{counts.official_complete_or_near_complete}})</option>`,
        `<option value="official_plan_completed_by_ai">Официальный план, доведённый ИИ (${{counts.official_plan_completed_by_ai}})</option>`,
        `<option value="unofficial_published">Опубликованное неофициальное (${{counts.unofficial_published}})</option>`,
        `<option value="ai_original">Решение ИИ с нуля (${{counts.ai_original}})</option>`,
        `<option value="ai_heavy_external_theorem">Тяжёлые внешние теоремы (${{counts.ai_heavy_external_theorem}})</option>`,
        `<option value="hard_external_theorem_no_proof">Доказательство не приведено: тяжёлая внешняя теорема (${{counts.hard_external_theorem_no_proof}})</option>`,
        `<option value="no_solution_hard">Решения нет, гроб (${{counts.no_solution_hard}})</option>`
      ].join('');
      select.value = state.solution;
      if (select.value !== state.solution) {{
        state.solution = 'all';
        select.value = 'all';
      }}
    }}

    function renderStatements(problem) {{
      const groups = [
        ['original', 'Оригинальные формулировки'],
        ['graph_theory', 'На языке теории графов'],
        ['graph_hint_reformulations', 'Графовые переформулировки-подсказки'],
        ['olympiad_reformulations', 'Олимпиадные переформулировки']
      ];
      return groups.map(([key, title]) => {{
        const items = problem.statements?.[key] || [];
        if (!items.length) return '';
        const content = `<h4>${{title}}</h4>` + items.map(statement => {{
          const sourceIds = [
            ...(statement.source_id ? [statement.source_id] : []),
            ...(statement.source_ids || [])
          ];
          const sourceLinks = sourceIds.map(sourceId => sources[sourceId]).filter(Boolean).map(source =>
            `<a class="subtle" href="${{esc(source.url)}}" target="_blank" rel="noreferrer">${{esc(source.title)}}</a>`
          ).join(' ');
          return `
            <div class="card">
              <div class="item-title">
                <span>${{esc(statement.title || statement.id)}}</span>
                ${{statusPill(statement.status)}}
                ${{statement.self_contained ? `<span class="pill">самодостаточность: ${{esc(label(taxonomy.statuses, statement.self_contained.status))}}</span>` : ''}}
                ${{statement.shared_statement_group ? `<span class="pill">общий источник: ${{esc(statement.shared_statement_group.id)}} / ${{esc(statement.shared_statement_group.case_id)}}</span>` : ''}}
                ${{sourceLinks}}
              </div>
              ${{textBlock(statement.text, statement.definition_ids || [])}}
              <div class="pill-row">${{(statement.definition_ids || []).map(definitionPill).join('')}}</div>
              ${{statement.review_notes ? `<div class="subtle">${{esc(statement.review_notes)}}</div>` : ''}}
            </div>
          `;
        }}).join('');
        return key === 'graph_hint_reformulations' ? reveal('Показать подсказку', content) : content;
      }}).join('');
    }}

    function renderIdeas(problem) {{
      const ideas = problem.ideas || [];
      if (!ideas.length) return '<div class="empty">Идей пока нет.</div>';
      const content = ideas.map(idea => `
        <div class="card">
          <div class="item-title">
            <span>${{esc(idea.title || idea.id)}}</span>
            ${{statusPill(idea.status)}}
          </div>
          ${{textBlock(idea.text)}}
          <div class="pill-row">${{(idea.tags || []).map(tagPill).join('')}}</div>
        </div>
      `).join('');
      return reveal('Показать идеи решения', content);
    }}

    function renderSolutions(problem) {{
      const solutions = problem.solutions || [];
      const classification = problem.editorial?.solution_classification;
      const classificationDetails = classification ? `
        <div class="subtle">
          ${{esc(classification.basis || '')}}
          ${{classification.confidence ? ` · confidence=${{esc(classification.confidence)}}` : ''}}
          ${{classification.notes ? `<br>${{esc(classification.notes)}}` : ''}}
          ${{(classification.external_theorem_ids || []).length ? `<br>Внешние теоремы: ${{classification.external_theorem_ids.map(esc).join(', ')}}` : ''}}
        </div>
      ` : '';
      if (!problemHasRealSolution(problem)) {{
        return `
          <div class="card">
            <div class="pill-row">
              ${{solutionStatusPill(problem)}}
            </div>
            ${{classificationDetails}}
          </div>
        `;
      }}
      if (!solutions.length) return '<div class="empty">Решений пока нет.</div>';
      const statusSummary = `
        <div class="card">
          <div class="pill-row">${{solutionStatusPill(problem)}}</div>
          ${{classificationDetails}}
        </div>
      `;
      const content = solutions.map(solution => `
        <div class="card">
          <div class="item-title">
            <span>${{esc(solution.title || solution.id)}}</span>
            ${{statusPill(solution.status)}}
          </div>
          ${{textBlock(solution.text, solution.definition_ids || [], solution.standard_idea_ids || [])}}
          ${{renderExamples(solution.examples || [], solution.definition_ids || [], solution.standard_idea_ids || [])}}
          <div class="pill-row">
            ${{(solution.definition_ids || []).map(definitionPill).join('')}}
            ${{(solution.idea_ids || []).map(id => `<span class="pill code">${{esc(id)}}</span>`).join('')}}
            ${{(solution.standard_idea_ids || []).map(standardIdeaPill).join('')}}
          </div>
        </div>
      `).join('');
      return statusSummary + reveal('Показать решение', content);
    }}

    function renderRelations(problem) {{
      const items = relationsForProblem(problem.id);
      if (!items.length) return '<div class="empty">Связей пока нет.</div>';
      return items.sort((a, b) => a.distance - b.distance || a.id.localeCompare(b.id)).map(rel => {{
        const forward = rel.from === problem.id;
        const otherId = forward ? rel.to : rel.from;
        const other = problems[otherId];
        const text = forward ? rel.forward_text : rel.backward_text;
        return `
          <div class="card">
            <div class="item-title">
              <a class="relation-link" href="#${{encodeURIComponent(otherId)}}">${{esc(other?.title || otherId)}}</a>
              <span class="pill">${{esc(label(taxonomy.relation_types, rel.type))}}</span>
              <span class="pill">длина ${{esc(rel.distance)}}</span>
              ${{statusPill(rel.status)}}
            </div>
            ${{textBlock(text)}}
          </div>
        `;
      }}).join('');
    }}

    function renderSources(problem) {{
      const items = problem.sources || [];
      if (!items.length) return '<div class="empty">Источники пока не указаны.</div>';
      return items.map(item => {{
        const source = sources[item.source_id];
        if (!source) return '';
        return `
          <div class="card">
            <div class="item-title">
              <a href="${{esc(source.url)}}" target="_blank" rel="noreferrer">${{esc(source.title)}}</a>
              ${{statusPill(item.status)}}
            </div>
            <div class="subtle">${{esc(source.type)}} · ${{esc(source.language)}} · ${{source.official ? 'официальный' : 'справочный'}}</div>
          </div>
        `;
      }}).join('');
    }}

    function renderProperties(problem) {{
      const props = problem.properties || {{}};
      const keys = Object.keys(props);
      if (!keys.length) return '<div class="empty">Динамические признаки пока не указаны.</div>';
      return keys.map(key => {{
        const item = props[key];
        const value = Array.isArray(item.value) ? item.value.join(', ') : String(item.value);
        return `
          <div class="card">
            <div class="item-title">
              <span>${{esc(label(taxonomy.properties, key))}}</span>
              ${{statusPill(item.status)}}
            </div>
            <div class="code">${{esc(value)}}</div>
          </div>
        `;
      }}).join('');
    }}

    function renderCommentCard(comment) {{
      const targetHtml = comment.target?.type === 'problem'
        ? `<a class="relation-link" href="#${{encodeURIComponent(comment.target.problem_id)}}">${{esc(problems[comment.target.problem_id]?.title || comment.target.problem_id)}}</a>`
        : '<span class="pill">Архитектура базы</span>';
      return `
        <div class="card">
          <div class="item-title">
            <span>${{esc(comment.title)}}</span>
            <span class="pill">${{esc(label(taxonomy.comment_kinds, comment.kind))}}</span>
            ${{commentStatusPill(comment.status)}}
          </div>
          <div class="subtle">${{esc(comment.author)}} · ${{esc(comment.created_at || '')}}</div>
          <div style="margin:8px 0 10px;">${{targetHtml}}</div>
          ${{textBlock(comment.text)}}
          ${{comment.response?.notes ? `<div class="subtle" style="margin-top:10px;">Ответ: ${{esc(comment.response.notes)}}</div>` : ''}}
        </div>
      `;
    }}

    function problemCommentKindOptions() {{
      return ['bug_report', 'alternative_solution', 'related_connection']
        .map(kind => `<option value="${{esc(kind)}}">${{esc(label(taxonomy.comment_kinds, kind))}}</option>`)
        .join('');
    }}

    function architectureCommentKindOptions() {{
      return `<option value="architecture">${{esc(label(taxonomy.comment_kinds, 'architecture'))}}</option>`;
    }}

    function renderCommentForm(targetType, problemId = '') {{
      const title = targetType === 'problem' ? 'Новый комментарий к задаче' : 'Новый комментарий по архитектуре';
      const feedbackReady = Boolean(FEEDBACK_CONFIG.endpoint);
      const note = feedbackReady
        ? 'Комментарий будет отправлен в настроенный backend и попадет в data/comments только после подтверждения записи.'
        : 'Автоматическая запись в базу не настроена: статический GitHub Pages не может сам создавать файлы data/comments. Нужен backend endpoint без регистрации пользователя.';
      const options = targetType === 'problem' ? problemCommentKindOptions() : architectureCommentKindOptions();
      return `
        <form class="comment-form" data-comment-form data-target-type="${{esc(targetType)}}" data-problem-id="${{esc(problemId)}}">
          <div class="item-title"><span>${{title}}</span></div>
          <select name="kind">${{options}}</select>
          <input name="author" type="text" placeholder="Автор" required>
          <input name="title" type="text" placeholder="Короткий заголовок" required>
          <textarea name="text" placeholder="Текст комментария" required></textarea>
          <div class="subtle">${{note}}</div>
          <button type="submit" ${{feedbackReady ? '' : 'disabled'}}>Отправить комментарий в базу</button>
          <div class="subtle" data-comment-status></div>
        </form>
      `;
    }}

    function buildCommentPayload(targetType, problemId, formData) {{
      const now = new Date();
      const createdAt = now.toISOString().slice(0, 10);
      const timePart = now.toISOString().slice(11, 19).replaceAll(':', '-');
      const rawTitle = String(formData.get('title') || '').trim().toLowerCase();
      const slug = rawTitle.replace(/[^a-zа-я0-9]+/gi, '-').replace(/^-+|-+$/g, '').slice(0, 40) || 'comment';
      const baseId = targetType === 'problem' ? `${{problemId}}-${{slug}}` : `architecture-${{slug}}`;
      return {{
        id: `comment-${{createdAt}}-${{timePart}}-${{baseId}}`,
        target: targetType === 'problem' ? {{ type: 'problem', problem_id: problemId }} : {{ type: 'architecture' }},
        kind: String(formData.get('kind') || '').trim(),
        title: String(formData.get('title') || '').trim(),
        text: String(formData.get('text') || '').trim(),
        author: String(formData.get('author') || '').trim(),
        created_at: createdAt,
        status: 'open',
        response: {{ status: 'open', notes: '' }},
        editorial: {{ created_by: 'human', notes: [] }}
      }};
    }}

    async function persistCommentPayload(payload) {{
      if (!FEEDBACK_CONFIG.endpoint) {{
        throw new Error('Автоматическая запись в базу не настроена.');
      }}
      const response = await fetch(FEEDBACK_CONFIG.endpoint, {{
        method: 'POST',
        headers: {{ 'Content-Type': 'application/json' }},
        body: JSON.stringify({{ project: FEEDBACK_CONFIG.project || 'graph-db', comment: payload }})
      }});
      if (!response.ok) {{
        const message = await response.text().catch(() => '');
        throw new Error(message || `Endpoint вернул HTTP ${{response.status}}.`);
      }}
    }}

    function attachCommentForms() {{
      document.querySelectorAll('[data-comment-form]').forEach(form => {{
        form.addEventListener('submit', async event => {{
          event.preventDefault();
          const formData = new FormData(form);
          const payload = buildCommentPayload(form.dataset.targetType, form.dataset.problemId || '', formData);
          const status = form.querySelector('[data-comment-status]');
          if (status) status.textContent = 'отправляю...';
          try {{
            await persistCommentPayload(payload);
            form.reset();
            if (status) status.textContent = 'записано в базу';
          }} catch (error) {{
            if (status) status.textContent = error.message || 'не удалось отправить';
          }}
        }});
      }});
    }}

    function renderLocalTools(problem) {{
      const progress = localProgress(problem.id);
      const note = localNote(problem.id);
      const progressOptions = PROGRESS_OPTIONS.map(item => `
        <option value="${{esc(item.value)}}" ${{item.value === progress ? 'selected' : ''}}>${{esc(item.label)}}</option>
      `).join('');
      const reportTypeOptions = [
        ['typo', 'Опечатка или язык'],
        ['statement', 'Проблема в условии'],
        ['solution', 'Проблема в решении'],
        ['source', 'Источник или ссылка'],
        ['relation', 'Связи, метки или тип'],
        ['other', 'Другое']
      ].map(([value, labelText]) => `<option value="${{esc(value)}}">${{esc(labelText)}}</option>`).join('');
      const feedbackReady = Boolean(FEEDBACK_CONFIG.endpoint);
      const feedbackNote = feedbackReady
        ? 'Отчет будет отправлен в настроенный backend и попадет в data/comments только после подтверждения записи.'
        : 'Автоматическая запись в базу не настроена: статический GitHub Pages не может сам создавать файлы data/comments. Нужен backend endpoint без регистрации пользователя.';
      return `
        <div class="card local-panel" data-local-panel data-problem-id="${{esc(problem.id)}}">
          <div class="local-row">
            <label>Локальный прогресс
              <select data-local-progress>${{progressOptions}}</select>
            </label>
            <button class="small-button" type="button" data-toggle-note>Заметка</button>
            <button class="small-button" type="button" data-toggle-report>Сообщить об ошибке</button>
            <span class="local-muted">Хранится только в этом браузере.</span>
          </div>
          <div data-note-block ${{note ? '' : 'hidden'}}>
            <textarea data-local-note placeholder="Личная заметка к карточке">${{esc(note)}}</textarea>
            <div class="local-row">
              <span class="local-save-status" data-local-save-status>${{note ? 'сохранено' : ''}}</span>
              <span class="local-muted">Автосохранение в localStorage.</span>
            </div>
          </div>
          <div data-report-block hidden>
            <div class="report-form">
              <label>Тип проблемы
                <select data-report-type>${{reportTypeOptions}}</select>
              </label>
              <label>Комментарий
                <textarea data-report-comment placeholder="Что именно нужно проверить?"></textarea>
              </label>
              <label>Контакт, необязательно
                <input data-report-contact type="text" placeholder="email или другой способ связи">
              </label>
              <label>Текст отчета
                <textarea class="report-output" data-report-output readonly></textarea>
              </label>
              <div class="local-row">
                <button class="small-button" type="button" data-submit-report ${{feedbackReady ? '' : 'disabled'}}>Отправить в базу</button>
                <span class="local-save-status" data-report-status></span>
              </div>
              <div class="local-muted">${{esc(feedbackNote)}}</div>
            </div>
          </div>
        </div>
      `;
    }}

    function reportProblemUrl(problem) {{
      return `${{window.location.href.split('#')[0]}}#${{encodeURIComponent(problem.id)}}`;
    }}

    function currentReportText(problem, panel) {{
      const typeSelect = panel.querySelector('[data-report-type]');
      const typeLabel = typeSelect?.selectedOptions?.[0]?.textContent || typeSelect?.value || '';
      const comment = panel.querySelector('[data-report-comment]')?.value.trim() || '';
      const contact = panel.querySelector('[data-report-contact]')?.value.trim() || '';
      return [
        'Отчет об ошибке в graph-db',
        '',
        `ID карточки: ${{problem.id}}`,
        `Название: ${{problem.title || ''}}`,
        `URL: ${{reportProblemUrl(problem)}}`,
        `Тип проблемы: ${{typeLabel}}`,
        '',
        'Комментарий:',
        comment || '(не заполнен)',
        '',
        `Контакт: ${{contact || '(не указан)'}}`,
        `Сформировано: ${{new Date().toISOString()}}`
      ].join('\\n');
    }}

    function currentReportPayload(problem, panel) {{
      const typeSelect = panel.querySelector('[data-report-type]');
      const typeLabel = typeSelect?.selectedOptions?.[0]?.textContent || typeSelect?.value || '';
      const comment = panel.querySelector('[data-report-comment]')?.value.trim() || '';
      const contact = panel.querySelector('[data-report-contact]')?.value.trim() || '';
      const createdAt = new Date().toISOString();
      return {{
        project: FEEDBACK_CONFIG.project || 'graph-db',
        kind: typeSelect?.value || 'bug_report',
        title: `${{typeLabel}}: ${{problem.title || problem.id}}`,
        text: comment,
        contact,
        created_at: createdAt,
        page_url: reportProblemUrl(problem),
        user_agent: navigator.userAgent || '',
        target: {{ type: 'problem', problem_id: problem.id }},
        problem: {{ id: problem.id, title: problem.title || '' }},
        report_text: currentReportText(problem, panel)
      }};
    }}

    function updateReportOutput(problem, panel) {{
      const output = panel.querySelector('[data-report-output]');
      if (output) output.value = currentReportText(problem, panel);
    }}

    async function submitReport(problem, panel) {{
      if (!FEEDBACK_CONFIG.endpoint) {{
        throw new Error('Автоматическая запись в базу не настроена.');
      }}
      const payload = currentReportPayload(problem, panel);
      if (!payload.text) {{
        throw new Error('Заполните комментарий перед отправкой.');
      }}
      const response = await fetch(FEEDBACK_CONFIG.endpoint, {{
        method: 'POST',
        headers: {{ 'Content-Type': 'application/json' }},
        body: JSON.stringify(payload)
      }});
      if (!response.ok) {{
        const message = await response.text().catch(() => '');
        throw new Error(message || `Endpoint вернул HTTP ${{response.status}}.`);
      }}
      return response;
    }}

    async function copyText(text) {{
      if (navigator.clipboard?.writeText) {{
        await navigator.clipboard.writeText(text);
        return;
      }}
      const helper = document.createElement('textarea');
      helper.value = text;
      helper.style.position = 'fixed';
      helper.style.left = '-9999px';
      document.body.appendChild(helper);
      helper.focus();
      helper.select();
      document.execCommand('copy');
      helper.remove();
    }}

    function bindProblemLocalControls(problem) {{
      const panel = document.querySelector('[data-local-panel]');
      if (!panel) return;
      const progressSelect = panel.querySelector('[data-local-progress]');
      const noteBlock = panel.querySelector('[data-note-block]');
      const noteTextarea = panel.querySelector('[data-local-note]');
      const noteStatus = panel.querySelector('[data-local-save-status]');
      const reportBlock = panel.querySelector('[data-report-block]');
      const reportStatus = panel.querySelector('[data-report-status]');
      let noteTimer = null;

      progressSelect?.addEventListener('change', event => {{
        setLocalEntry(problem.id, {{ progress: event.target.value }});
        if (state.localProgress !== 'all' && state.localProgress !== event.target.value) selectFirstVisibleRoute();
        else {{
          renderLocalProgressFilter();
          renderSidebar();
        }}
      }});

      panel.querySelector('[data-toggle-note]')?.addEventListener('click', () => {{
        noteBlock.hidden = !noteBlock.hidden;
        if (!noteBlock.hidden) noteTextarea?.focus();
      }});

      noteTextarea?.addEventListener('input', () => {{
        if (noteStatus) noteStatus.textContent = 'сохраняю...';
        window.clearTimeout(noteTimer);
        noteTimer = window.setTimeout(() => {{
          setLocalEntry(problem.id, {{ note: noteTextarea.value }});
          if (noteStatus) noteStatus.textContent = 'сохранено';
          renderLocalProgressFilter();
          renderSidebar();
        }}, 350);
      }});

      panel.querySelector('[data-toggle-report]')?.addEventListener('click', () => {{
        reportBlock.hidden = !reportBlock.hidden;
        if (!reportBlock.hidden) updateReportOutput(problem, panel);
      }});

      for (const field of panel.querySelectorAll('[data-report-type], [data-report-comment], [data-report-contact]')) {{
        field.addEventListener('input', () => updateReportOutput(problem, panel));
        field.addEventListener('change', () => updateReportOutput(problem, panel));
      }}

      panel.querySelector('[data-submit-report]')?.addEventListener('click', async () => {{
        updateReportOutput(problem, panel);
        if (reportStatus) reportStatus.textContent = 'отправляю...';
        try {{
          await submitReport(problem, panel);
          if (reportStatus) reportStatus.textContent = 'записано в базу';
        }} catch (error) {{
          if (reportStatus) reportStatus.textContent = error.message || 'не удалось отправить';
        }}
      }});
    }}

    function exportLocalData() {{
      const payload = {{
        app: 'graph-db',
        version: LOCAL_DATA_VERSION,
        exported_at: new Date().toISOString(),
        local_storage_key: LOCAL_DATA_KEY,
        problems: localData.problems
      }};
      const blob = new Blob([JSON.stringify(payload, null, 2)], {{ type: 'application/json' }});
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = `graph-db-local-${{new Date().toISOString().slice(0, 10)}}.json`;
      document.body.appendChild(link);
      link.click();
      link.remove();
      URL.revokeObjectURL(url);
    }}

    function normalizedImportedProblems(payload) {{
      const rawProblems = payload?.problems && typeof payload.problems === 'object'
        ? payload.problems
        : payload;
      if (!rawProblems || typeof rawProblems !== 'object' || Array.isArray(rawProblems)) return null;
      const result = {{}};
      for (const [id, entry] of Object.entries(rawProblems)) {{
        if (!problems[id]) continue;
        const normalized = normalizeLocalEntry(entry);
        if (normalized.progress || normalized.note) result[id] = normalized;
      }}
      return result;
    }}

    async function importLocalDataFile(file) {{
      let parsed;
      try {{
        parsed = JSON.parse(await file.text());
      }} catch (_error) {{
        window.alert('Не удалось прочитать JSON.');
        return;
      }}
      const imported = normalizedImportedProblems(parsed);
      if (!imported) {{
        window.alert('JSON не похож на экспорт локальных данных.');
        return;
      }}
      const count = Object.keys(imported).length;
      if (!count) {{
        window.alert('В файле нет заметок или прогресса для карточек этой базы.');
        return;
      }}
      const ok = window.confirm(`Импортировать локальные данные для ${{count}} карточек? Записи с теми же id будут заменены.`);
      if (!ok) return;
      localData.problems = {{ ...localData.problems, ...imported }};
      saveLocalData();
      render();
      window.alert('Локальные данные импортированы.');
    }}

    function resetLocalData() {{
      const ok = window.confirm('Удалить весь локальный прогресс и заметки из этого браузера? Это не затронет репозиторий.');
      if (!ok) return;
      localData = emptyLocalData();
      storageRemove(LOCAL_DATA_KEY);
      render();
    }}

    function renderHome() {{
      const problemList = Object.values(problems);
      const solutionCounts = {{
        official_complete_or_near_complete: 0,
        official_plan_completed_by_ai: 0,
        unofficial_published: 0,
        ai_original: 0,
        ai_heavy_external_theorem: 0,
        no_solution_hard: 0
      }};
      problemList.forEach(problem => {{
        const key = solutionStatusKey(problem);
        solutionCounts[key] = (solutionCounts[key] || 0) + 1;
      }});
      const solvedCount = problemList.filter(problemHasRealSolution).length;
      const noSolutionCount = problemList.length - solvedCount;
      const aiAssistedCount = solutionCounts.ai_original + solutionCounts.ai_heavy_external_theorem;
      const graphStatements = problemList.reduce((total, problem) =>
        total + (problem.statements?.graph_theory?.length || 0) + (problem.statements?.graph_hint_reformulations?.length || 0), 0);
      const filteredCount = filteredProblems().length;
      const selectedProblem = filteredProblems()[0] || sortedProblems()[0];
      const selectedHref = selectedProblem ? `#${{encodeURIComponent(selectedProblem.id)}}` : '#home';
      const sourceCount = new Set(problemList.map(problem => sourceInfo(problem).key).filter(Boolean)).size;
      const solutionTypes = [
        'official_complete_or_near_complete',
        'official_plan_completed_by_ai',
        'unofficial_published',
        'ai_original',
        'ai_heavy_external_theorem',
        'no_solution_hard'
      ];
      const solutionButtonHtml = solutionTypes.map(type => `
        <button class="home-solution-button solution-status-${{esc(type)}}" type="button" data-home-solution="${{esc(type)}}">
          <strong>${{solutionCounts[type] || 0}}</strong>
          <span>${{esc(solutionStatusLabel(type))}}</span>
        </button>
      `).join('');
      byId('content').innerHTML = `
        <section class="home-hero">
          <div class="home-kicker">
            <span class="pill">черновая исследовательская база</span>
            <span>${{esc(sourceCount)}} источниковых семейств</span>
            <span>${{esc(relations.length)}} родственных связей</span>
            <span>${{esc(aiAssistedCount)}} ИИ-классифицированных/ИИ-решений</span>
          </div>
          <h2 class="home-title">Графовые задачи, связи и идеи в одном рабочем поле</h2>
          <p class="home-lead">
            Это база олимпиадных и классических задач по теории графов: с оригинальными условиями, графовыми формулировками,
            решениями, идеями, источниками и картой родства между карточками.
          </p>
          <p class="home-note">
            База создаётся при активной помощи ИИ: он помогает извлекать задачи из архивов, переводить и разворачивать решения,
            проставлять теги, искать родственные связи и помечать степень надёжности решений. Эти пометки не заменяют
            человеческую редактуру: спорные решения и тяжёлые внешние теоремы специально выделены отдельными категориями.
          </p>
          <div class="home-actions">
            <a class="home-action primary" href="${{selectedHref}}">Открыть найденные карточки: ${{filteredCount}}</a>
            <button class="home-action" type="button" data-home-view="problems">Все задачи</button>
            <button class="home-action" type="button" data-home-view="definitions">Определения</button>
            <button class="home-action" type="button" data-home-view="ideas">Идеи</button>
            <button class="home-action" type="button" data-home-view="comments">Комментарии</button>
          </div>
          <div class="home-stats">
            <div class="home-stat"><strong>${{problemList.length}}</strong><span>карточек</span></div>
            <div class="home-stat"><strong>${{solvedCount}}</strong><span>с решениями</span></div>
            <div class="home-stat"><strong>${{graphStatements}}</strong><span>графовых формулировок</span></div>
            <div class="home-stat"><strong>${{Object.keys(definitions).length}}</strong><span>определений</span></div>
            <div class="home-stat"><strong>${{noSolutionCount}}</strong><span>без решения</span></div>
          </div>
        </section>

        <section class="home-band">
          <h3>Навигация по типу решения</h3>
          <div class="home-solution-grid">${{solutionButtonHtml}}</div>
          <p class="home-note">
            Эти кнопки выставляют тот же фильтр, что и выпадающий список «Решения» слева: можно быстро отделить полные
            официальные решения от кратких официальных планов, неофициальных публикаций, ИИ-решений, решений с тяжёлыми
            внешними теоремами и задач без решения.
          </p>
        </section>

        <section class="home-band">
          <h3>Как искать</h3>
          <div class="home-search-map">
            <div class="home-chip"><strong>Строка поиска</strong><span>Ищет по названию, условию, решению, источнику, автору и служебным ключам.</span></div>
            <div class="home-chip"><strong>Источник и год</strong><span>Отфильтруйте КОЛМ, ФЮМ, УТЮМ, ЮМТ, IMO, USAMO и другие серии.</span></div>
            <div class="home-chip"><strong>Цель, объект, метод</strong><span>Разделяйте “оценка+пример”, “дерево”, “индукция” и похожие роли задачи.</span></div>
            <div class="home-chip"><strong>Тип и решения</strong><span>Оставьте только задачи, теоремы, леммы или один из шести типов происхождения решения.</span></div>
          </div>
          <p class="home-note">Фильтры слева работают вместе: можно, например, искать задачи КОЛМ про деревья с методом индукции и сразу открыть первую подходящую карточку.</p>
        </section>

        <section class="home-band">
          <h3>Как пользоваться базой</h3>
          <div class="home-grid">
            <div class="home-panel">
              <h3>Читайте карточку слоями</h3>
              <p>Сначала смотрите оригинальное условие, затем графовую формулировку, идеи и решение. Если графовая формулировка не нужна, она намеренно удалена как дубль.</p>
            </div>
            <div class="home-panel">
              <h3>Ходите по связям</h3>
              <p>Родственные связи показывают общий метод, вариант, обобщение или похожий мотив. Это помогает видеть не одну задачу, а семейство приёмов.</p>
            </div>
            <div class="home-panel">
              <h3>Комментируйте как редактор</h3>
              <p>Кнопка комментария отправляет запись в базу только через настроенный backend endpoint. Комментарии экспертов считаются рабочими инструкциями к базе, а не отзывами для модерации.</p>
            </div>
          </div>
        </section>

        <section class="home-band">
          <h3>Как база создавалась</h3>
          <div class="home-grid">
            <div class="home-panel">
              <h3>Сбор источников</h3>
              <p>Карточки импортировались из официальных архивов и проверенных разборов: турниры, списки задач, классические теоремы и локальные подборки.</p>
            </div>
            <div class="home-panel">
              <h3>Редакторский проход</h3>
              <p>Для каждой карточки нормализовались русский текст, самодостаточность условия, графовая постановка, цель задачи, объект и метод решения.</p>
            </div>
            <div class="home-panel">
              <h3>Сеть связей</h3>
              <p>После базовой карточки строились родственные связи: близкие варианты, разные решения одной идеи, частные случаи, обобщения и парные модификации.</p>
            </div>
          </div>
        </section>
      `;
      document.querySelectorAll('[data-home-view]').forEach(button => {{
        button.addEventListener('click', () => {{
          const view = button.dataset.homeView;
          if (view === 'problems') {{
            state.query = '';
            state.localProgress = 'all';
            state.goal = 'all';
            state.object = 'all';
            state.method = 'all';
            state.type = 'all';
            state.source = 'all';
            state.author = 'all';
            state.year = 'all';
            state.solution = 'all';
            byId('search-input').value = '';
            selectFirstVisibleRoute();
          }}
          else if (view === 'definitions') setDefinition(sortedDefinitions()[0]?.id);
          else if (view === 'ideas') setStandardIdea(sortedStandardIdeas()[0]?.id);
          else if (view === 'comments') setComment(sortedComments()[0]?.id || null);
        }});
      }});
      document.querySelectorAll('[data-home-solution]').forEach(button => {{
        button.addEventListener('click', () => {{
          state.solution = button.dataset.homeSolution;
          selectFirstVisibleRoute();
        }});
      }});
    }}

    function renderProblem() {{
      const route = currentRoute();
      const problem = problems[route.id];
      byId('content').innerHTML = `
        <div class="topline">
          <span class="pill code">${{esc(problem.id)}}</span>
          ${{solutionStatusPill(problem)}}
          ${{statusPill(problem.editorial?.review_status)}}
          <span class="pill">${{esc(label(taxonomy.difficulty_levels, problem.difficulty?.main))}}</span>
        </div>
        <h2>${{esc(problem.title)}}</h2>
        ${{renderLocalTools(problem)}}
        <div class="subtle">${{esc(problem.difficulty?.comment || '')}}</div>
        <div class="pill-row">${{(problem.tags || []).map(tagPill).join('')}}</div>

        ${{renderAuthors(problem)}}

        <div class="section">
          <h3>Формулировки</h3>
          ${{renderStatements(problem)}}
        </div>

        <div class="section">
          <h3>Родственные связи</h3>
          ${{renderRelations(problem)}}
        </div>

        <div class="section">
          <h3>Идеи</h3>
          ${{renderIdeas(problem)}}
        </div>

        <div class="section">
          <h3>Решения</h3>
          ${{renderSolutions(problem)}}
        </div>

        <div class="section">
          <h3>Признаки</h3>
          ${{renderProperties(problem)}}
        </div>

        <div class="section">
          <h3>Источники</h3>
          ${{renderSources(problem)}}
        </div>

        <div class="section">
          <h3>Комментарии</h3>
          ${{commentsForProblem(problem.id).length ? commentsForProblem(problem.id).map(renderCommentCard).join('') : '<div class="empty">Комментариев к этой задаче пока нет.</div>'}}
          ${{renderCommentForm('problem', problem.id)}}
        </div>

        <div class="section">
          <h3>Редактура</h3>
          ${{textBlock((problem.editorial?.notes || []).join('\\n') || 'Заметок нет.')}}
        </div>
      `;
      attachCommentForms();
      bindProblemLocalControls(problem);
      if (window.MathJax?.typesetPromise) window.MathJax.typesetPromise([byId('content')]);
    }}

    function renderDefinition() {{
      const route = currentRoute();
      const item = definitions[route.id];
      const usage = definitionUsage(item.id);
      byId('content').innerHTML = `
        <div class="topline">
          <span class="pill code">${{esc(item.id)}}</span>
          ${{statusPill(item.status)}}
          <span class="pill">стандартное определение</span>
        </div>
        <h2>${{esc(item.title)}}</h2>
        <div class="section">
          <h3>Формулировка</h3>
          <div class="card">${{textBlock(item.text)}}</div>
        </div>
        <div class="section">
          <h3>Примеры</h3>
          ${{(item.examples || []).map(example => `<div class="card">${{textBlock(example)}}</div>`).join('')}}
        </div>
        <div class="section">
          <h3>Используется в задачах</h3>
          ${{usage.length ? usage.map(problem => `
            <div class="card">
              <a class="relation-link" href="#${{encodeURIComponent(problem.id)}}">${{esc(problem.title)}}</a>
              <div class="id">${{esc(problem.id)}}</div>
            </div>
          `).join('') : '<div class="empty">Пока не используется.</div>'}}
        </div>
      `;
      if (window.MathJax?.typesetPromise) window.MathJax.typesetPromise([byId('content')]);
    }}

    function renderStandardIdea() {{
      const route = currentRoute();
      const item = standardIdeas[route.id];
      const usage = standardIdeaUsage(item.id);
      byId('content').innerHTML = `
        <div class="topline">
          <span class="pill code">${{esc(item.id)}}</span>
          ${{statusPill(item.status)}}
          <span class="pill">стандартная идея</span>
        </div>
        <h2>${{esc(item.title)}}</h2>
        <div class="section">
          <h3>Описание</h3>
          <div class="card">${{textBlock(item.text)}}</div>
        </div>
        <div class="section">
          <h3>Примеры</h3>
          ${{(item.examples || []).map(example => `<div class="card">${{textBlock(example)}}</div>`).join('')}}
        </div>
        <div class="section">
          <h3>Используется в решениях</h3>
          ${{usage.length ? usage.map(entry => `
            <div class="card">
              <a class="relation-link" href="#${{encodeURIComponent(entry.problem.id)}}">${{esc(entry.problem.title)}}</a>
              <div class="subtle">${{esc(entry.solution.title || entry.solution.id)}} · <span class="code">${{esc(entry.problem.id)}}</span></div>
            </div>
          `).join('') : '<div class="empty">Пока не используется.</div>'}}
        </div>
      `;
      if (window.MathJax?.typesetPromise) window.MathJax.typesetPromise([byId('content')]);
    }}

    function renderCommentPage() {{
      const route = currentRoute();
      const comment = route.id ? comments[route.id] : null;
      if (!comment) {{
        byId('content').innerHTML = `
          <div class="topline">
            <span class="pill">Комментарии</span>
          </div>
          <h2>Комментарии и предложения</h2>
          <div class="section">
            <h3>Комментарии по архитектуре</h3>
            ${{architectureComments().length ? architectureComments().map(renderCommentCard).join('') : '<div class="empty">Архитектурных комментариев пока нет.</div>'}}
            ${{renderCommentForm('architecture')}}
          </div>
        `;
        attachCommentForms();
        return;
      }}
      const target = comment.target?.type === 'problem'
        ? `<a class="relation-link" href="#${{encodeURIComponent(comment.target.problem_id)}}">${{esc(problems[comment.target.problem_id]?.title || comment.target.problem_id)}}</a>`
        : '<span class="pill">Архитектура базы</span>';
      byId('content').innerHTML = `
        <div class="topline">
          <span class="pill code">${{esc(comment.id)}}</span>
          <span class="pill">${{esc(label(taxonomy.comment_kinds, comment.kind))}}</span>
          ${{commentStatusPill(comment.status)}}
        </div>
        <h2>${{esc(comment.title)}}</h2>
        <div class="subtle">${{esc(comment.author)}} · ${{esc(comment.created_at || '')}}</div>
        <div class="section">
          <h3>Цель комментария</h3>
          <div class="card">${{target}}</div>
        </div>
        <div class="section">
          <h3>Текст</h3>
          <div class="card">${{textBlock(comment.text)}}</div>
        </div>
        <div class="section">
          <h3>Текущий ответ</h3>
          <div class="card">
            <div class="pill-row">${{comment.response?.status ? commentStatusPill(comment.response.status) : ''}}</div>
            ${{textBlock(comment.response?.notes || 'Ответ пока не добавлен.')}}
          </div>
        </div>
        <div class="section">
          <h3>Новый комментарий по архитектуре</h3>
          ${{renderCommentForm('architecture')}}
        </div>
      `;
      attachCommentForms();
    }}

    function render() {{
      const route = currentRoute();
      state.view = route.type === 'definition' ? 'definitions' : route.type === 'idea' ? 'ideas' : route.type === 'comment' ? 'comments' : 'problems';
      applySidebarState();
      renderLocalProgressFilter();
      renderSourceFilter();
      renderAuthorFilter();
      renderYearFilter();
      renderSolutionFilter();
      renderGoalFilter();
      renderObjectFilter();
      renderMethodFilter();
      renderTypeFilter();
      renderSidebar();
      if (route.type === 'home') renderHome();
      else if (route.type === 'definition') renderDefinition();
      else if (route.type === 'idea') renderStandardIdea();
      else if (route.type === 'comment') renderCommentPage();
      else renderProblem();
      enhanceReveals();
    }}

    byId('search-input').addEventListener('input', event => {{
      state.query = event.target.value;
      selectFirstVisibleRoute();
    }});

    byId('local-progress-filter').addEventListener('change', event => {{
      state.localProgress = event.target.value;
      selectFirstVisibleRoute();
    }});

    byId('goal-filter').addEventListener('change', event => {{
      state.goal = event.target.value;
      selectFirstVisibleRoute();
    }});

    byId('object-filter').addEventListener('change', event => {{
      state.object = event.target.value;
      selectFirstVisibleRoute();
    }});

    byId('method-filter').addEventListener('change', event => {{
      state.method = event.target.value;
      selectFirstVisibleRoute();
    }});

    byId('type-filter').addEventListener('change', event => {{
      state.type = event.target.value;
      selectFirstVisibleRoute();
    }});

    byId('source-filter').addEventListener('change', event => {{
      state.source = event.target.value;
      selectFirstVisibleRoute();
    }});

    byId('author-filter').addEventListener('change', event => {{
      state.author = event.target.value;
      selectFirstVisibleRoute();
    }});

    byId('year-filter').addEventListener('change', event => {{
      state.year = event.target.value;
      selectFirstVisibleRoute();
    }});

    byId('solution-filter').addEventListener('change', event => {{
      state.solution = event.target.value;
      selectFirstVisibleRoute();
    }});

    byId('local-export').addEventListener('click', exportLocalData);
    byId('local-import').addEventListener('click', () => byId('local-import-file').click());
    byId('local-import-file').addEventListener('change', event => {{
      const file = event.target.files?.[0];
      if (file) importLocalDataFile(file);
      event.target.value = '';
    }});
    byId('local-reset').addEventListener('click', resetLocalData);

    byId('list').addEventListener('pointerdown', event => {{
      if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      const link = event.target.closest('[data-list-route]');
      if (!link) return;
      event.preventDefault();
      activateListRoute(link);
    }});

    byId('list').addEventListener('click', event => {{
      const link = event.target.closest('[data-list-route]');
      if (!link) return;
      event.preventDefault();
      activateListRoute(link);
    }});

    byId('list').addEventListener('keydown', event => {{
      if (event.key !== 'Enter' && event.key !== ' ') return;
      const link = event.target.closest('[data-list-route]');
      if (!link) return;
      event.preventDefault();
      activateListRoute(link);
    }});

    byId('mode-home').addEventListener('click', setHome);
    byId('mode-problems').addEventListener('click', () => {{
      state.view = 'problems';
      selectFirstVisibleRoute();
    }});
    byId('mode-definitions').addEventListener('click', () => {{
      state.view = 'definitions';
      selectFirstVisibleRoute();
    }});
    byId('mode-ideas').addEventListener('click', () => {{
      state.view = 'ideas';
      selectFirstVisibleRoute();
    }});
    byId('mode-comments').addEventListener('click', () => {{
      state.view = 'comments';
      selectFirstVisibleRoute();
    }});

    byId('sidebar-toggle').addEventListener('click', () => {{
      state.sidebarHidden = !state.sidebarHidden;
      storageSet('kg-sidebar-hidden', state.sidebarHidden ? '1' : '0');
      applySidebarState();
    }});

    window.addEventListener('hashchange', render);
    render();
  </script>
</body>
</html>
"""


def main():
    copy_example_assets()
    html = build_html(load_viewer_data())
    for target_dir in (ROOT / "viewer", ROOT / "docs"):
        target_dir.mkdir(exist_ok=True)
        target = target_dir / "index.html"
        target.write_text(html, encoding="utf-8")
        print(f"Built {target}")


if __name__ == "__main__":
    main()
