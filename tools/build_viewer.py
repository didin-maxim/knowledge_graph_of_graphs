import json
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


def build_html(data):
    payload = json.dumps(data, ensure_ascii=False, indent=2)
    return f"""<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>graphs</title>
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
      min-height: 100vh;
    }}

    .sidebar {{
      border-right: 1px solid var(--line);
      background: #fbfaf7;
      display: flex;
      flex-direction: column;
      min-width: 0;
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

    .search input, .search select, .comment-form textarea {{
      width: 100%;
      border: 1px solid var(--line);
      background: #fff;
      color: var(--ink);
      padding: 10px 12px;
      border-radius: 6px;
    }}

    .list {{
      overflow: auto;
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
      overflow: auto;
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

    .item-title {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      align-items: baseline;
      margin-bottom: 8px;
      font-weight: 650;
    }}

    .text {{
      white-space: pre-wrap;
      overflow-wrap: anywhere;
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
      }}

      .sidebar {{
        border-right: 0;
        border-bottom: 1px solid var(--line);
        max-height: 48vh;
      }}
    }}
  </style>
</head>
<body>
  <div class="shell">
    <aside class="sidebar">
      <div class="brand">
        <h1>graphs</h1>
        <div class="meta" id="db-meta"></div>
      </div>
      <div class="search">
        <div class="mode-toggle">
          <button class="mode-button active" id="mode-problems" type="button">Задачи</button>
          <button class="mode-button" id="mode-definitions" type="button">Определения</button>
          <button class="mode-button" id="mode-ideas" type="button">Идеи</button>
          <button class="mode-button" id="mode-comments" type="button">Комментарии</button>
        </div>
        <input id="search-input" type="search" placeholder="Поиск">
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
    const state = {{
      query: '',
      goal: 'all',
      object: 'all',
      method: 'all',
      type: 'all',
      source: 'all',
      author: 'all',
      year: 'all',
      solution: 'all',
      view: 'problems'
    }};

    const byId = (id) => document.getElementById(id);
    const esc = (value) => String(value ?? '')
      .replaceAll('&', '&amp;')
      .replaceAll('<', '&lt;')
      .replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;')
      .replaceAll("'", '&#039;');

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

    function linkDefinitions(html, definitionIds = []) {{
      const replacements = [];
      definitionIds.forEach(id => {{
        const definition = definitions[id];
        if (!definition) return;
        (definition.aliases || []).forEach(alias => {{
          if (!alias.includes('\\\\')) replacements.push({{ id, alias }});
        }});
      }});
      replacements.sort((a, b) => b.alias.length - a.alias.length);
      let result = html;
      const used = new Set();
      replacements.forEach(item => {{
        if (used.has(item.id)) return;
        const pattern = new RegExp(`(^|[^А-Яа-яA-Za-z0-9_])(${{escapeRegExp(esc(item.alias))}})(?=$|[^А-Яа-яA-Za-z0-9_])`, 'i');
        if (pattern.test(result)) {{
          result = result.replace(pattern, `$1<a class="def-link" href="#def-${{encodeURIComponent(item.id)}}">$2</a>`);
          used.add(item.id);
        }}
      }});
      return result;
    }}

    function linkStandardIdeas(html, ideaIds = []) {{
      const replacements = [];
      ideaIds.forEach(id => {{
        const idea = standardIdeas[id];
        if (!idea) return;
        (idea.aliases || []).forEach(alias => replacements.push({{ id, alias }}));
      }});
      replacements.sort((a, b) => b.alias.length - a.alias.length);
      let result = html;
      const used = new Set();
      replacements.forEach(item => {{
        if (used.has(item.id)) return;
        const pattern = new RegExp(`(^|[^А-Яа-яA-Za-z0-9_])(${{escapeRegExp(esc(item.alias))}})(?=$|[^А-Яа-яA-Za-z0-9_])`, 'i');
        if (pattern.test(result)) {{
          result = result.replace(pattern, `$1<a class="idea-link" href="#stdidea-${{encodeURIComponent(item.id)}}">$2</a>`);
          used.add(item.id);
        }}
      }});
      return result;
    }}

    function textBlock(text, definitionIds = [], standardIdeaIds = []) {{
      let html = prettyText(text || '');
      html = linkDefinitions(html, definitionIds);
      html = linkStandardIdeas(html, standardIdeaIds);
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
        const name = esc(author.name || '?');
        const review = author.status && author.status !== 'source_verified'
          ? `<span class="pill">${{esc(label(taxonomy.statuses, author.status) || author.status)}}</span>`
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
      return firstYear(problem.title) || firstYear(problem.id);
    }}

    function normalizeAuthor(value) {{
      return normalizeCompact(value);
    }}

    function problemAuthors(problem) {{
      return (problem.authors || [])
        .map(author => String(author.name || '').trim())
        .filter(name => name && name !== '?');
    }}

    function problemAuthorKeys(problem) {{
      return problemAuthors(problem).map(normalizeAuthor).filter(Boolean);
    }}

    function sourceAliasMap() {{
      return {{
        yumt: ['yumt', 'юмт'],
        fyum: ['fyum', 'фюм'],
        imo: ['imo'],
        apmo: ['apmo'],
        bmo: ['bmo'],
        egmo: ['egmo'],
        usamo: ['usamo'],
        rmm: ['rmm']
      }};
    }}

    function sourceInfo(problem) {{
      const title = String(problem.title || '');
      const chunks = title.split(',').map(item => item.trim()).filter(Boolean);
      let labelText = '';
      for (const chunk of chunks) {{
        const match = chunk.match(/(19|20)\\d{{2}}/);
        if (!match) continue;
        labelText = chunk.slice(0, match.index).replace(/[-, ]+$/, '').trim();
        if (labelText) break;
      }}
      const idMatch = String(problem.id || '').match(/^([a-z0-9-]+)-((19|20)\\d{{2}})(?:-|$)/);
      const key = idMatch ? idMatch[1].split('-')[0] : normalizeCompact(labelText) || 'misc';
      const labelTextCompact = normalizeCompact(labelText);
      const year = problemYear(problem);
      const aliases = new Set([key, labelTextCompact]);
      (sourceAliasMap()[key] || []).forEach(alias => aliases.add(alias));
      if (year) {{
        aliases.add(`${{key}}${{year}}`);
        if (labelTextCompact) aliases.add(`${{labelTextCompact}}${{year}}`);
        (sourceAliasMap()[key] || []).forEach(alias => aliases.add(`${{alias}}${{year}}`));
      }}
      return {{
        key,
        label: labelText || (key !== 'misc' ? key.toUpperCase() : 'Прочее'),
        year,
        aliases: Array.from(aliases).filter(Boolean)
      }};
    }}

    function problemHasRealSolution(problem) {{
      return (problem.solutions || []).some(solution => {{
        const text = String(solution.text || '').trim();
        const title = String(solution.title || '').trim();
        return text
          && !/^решение пока не найдено[.!]?$/i.test(text)
          && !/близк\\w*\\s+решени\\w*/i.test(title);
      }});
    }}

    function problemSearchBlob(problem) {{
      const info = sourceInfo(problem);
      const extra = {{
        source_key: info.key,
        source_label: info.label,
        source_aliases: info.aliases,
        authors: problemAuthors(problem),
        year: info.year,
        solution_state: problemHasRealSolution(problem) ? 'with_solution' : 'without_solution'
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
      if (['theorem', 'lemma', 'corollary'].includes(primary)) return primary;
      if ((problem.kind?.secondary || []).includes('classical_tool')) return 'classical_tool';
      return 'olympiad_problem';
    }}

    function problemTypeLabel(type) {{
      const labels = {{
        olympiad_problem: 'Задача',
        theorem: 'Теорема',
        lemma: 'Лемма',
        corollary: 'Следствие',
        classical_theorem: 'Классическая теорема',
        classical_tool: 'Классический инструмент'
      }};
      return labels[type] || type;
    }}

    function problemMatchesFilters(problem, options = {{}}) {{
      const query = state.query.trim().toLowerCase();
      const info = sourceInfo(problem);
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
        const hasSolution = problemHasRealSolution(problem);
        const solutionOk = state.solution === 'all'
          || (state.solution === 'with' && hasSolution)
          || (state.solution === 'without' && !hasSolution);
        if (!solutionOk) return false;
      }}
      if (!options.excludeQuery) {{
        const compactQuery = normalizeCompact(query);
        const queryOk = !query
          || problemSearchBlob(problem).includes(query)
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
      return sortedDefinitions().filter(item => !query || searchBlob(item).includes(query));
    }}

    function filteredStandardIdeas() {{
      const query = state.query.trim().toLowerCase();
      return sortedStandardIdeas().filter(item => !query || searchBlob(item).includes(query));
    }}

    function filteredComments() {{
      const query = state.query.trim().toLowerCase();
      return sortedComments().filter(item => !query || searchBlob(item).includes(query));
    }}

    function currentRoute() {{
      const id = decodeURIComponent(location.hash.replace(/^#/, ''));
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
      location.hash = id ? `comment-${{encodeURIComponent(id)}}` : '';
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
      byId('mode-problems').classList.toggle('active', state.view === 'problems');
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
            <div class="id">${{esc(item.id)}}</div>
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
      if (select.value !== state[stateKey]) select.value = 'all';
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
      const order = ['olympiad_problem', 'theorem', 'lemma', 'corollary', 'classical_theorem', 'classical_tool'];
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
      if (select.value !== state.type) select.value = 'all';
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
      if (select.value !== state.author) select.value = 'all';
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
      const withSolution = matching.filter(problem => problemHasRealSolution(problem)).length;
      const withoutSolution = matching.length - withSolution;
      select.innerHTML = [
        `<option value="all">Все задачи (${{matching.length}})</option>`,
        `<option value="with">С решением (${{withSolution}})</option>`,
        `<option value="without">Без решения (${{withoutSolution}})</option>`
      ].join('');
      select.value = state.solution;
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
        return `<h4>${{title}}</h4>` + items.map(statement => {{
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
      }}).join('');
    }}

    function renderIdeas(problem) {{
      const ideas = problem.ideas || [];
      if (!ideas.length) return '<div class="empty">Идей пока нет.</div>';
      return ideas.map(idea => `
        <div class="card">
          <div class="item-title">
            <span>${{esc(idea.title || idea.id)}}</span>
            ${{statusPill(idea.status)}}
          </div>
          ${{textBlock(idea.text)}}
          <div class="pill-row">${{(idea.tags || []).map(tagPill).join('')}}</div>
        </div>
      `).join('');
    }}

    function renderSolutions(problem) {{
      const solutions = problem.solutions || [];
      if (!problemHasRealSolution(problem)) {{
        return `
          <div class="card">
            <div class="pill-row">
              <span class="pill status-needs_human_review">Решение не найдено</span>
            </div>
          </div>
        `;
      }}
      if (!solutions.length) return '<div class="empty">Решений пока нет.</div>';
      return solutions.map(solution => `
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
      const note = targetType === 'problem'
        ? 'Комментарий будет открыт как GitHub issue с привязкой к этой задаче.'
        : 'Комментарий будет открыт как GitHub issue по архитектуре базы.';
      const options = targetType === 'problem' ? problemCommentKindOptions() : architectureCommentKindOptions();
      return `
        <form class="comment-form" data-comment-form data-target-type="${{esc(targetType)}}" data-problem-id="${{esc(problemId)}}">
          <div class="item-title"><span>${{title}}</span></div>
          <select name="kind">${{options}}</select>
          <input name="author" type="text" placeholder="Автор" required>
          <input name="title" type="text" placeholder="Короткий заголовок" required>
          <textarea name="text" placeholder="Текст комментария" required></textarea>
          <div class="subtle">${{note}}</div>
          <button type="submit">Отправить комментарий в базу</button>
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

    function commentIssueBody(payload) {{
      const target = payload.target.type === 'problem'
        ? `problem_id: ${{payload.target.problem_id}}`
        : 'target: architecture';
      return [
        'Комментарий доверенного эксперта к черновой базе.',
        '',
        '```json',
        JSON.stringify(payload, null, 2),
        '```',
        '',
        `Тип: ${{payload.kind}}`,
        target,
        `Автор: ${{payload.author}}`,
        '',
        payload.text
      ].join('\\n');
    }}

    async function persistCommentPayload(payload) {{
      const issueTitle = `[comment] ${{payload.title}}`;
      const params = new URLSearchParams({{
        title: issueTitle,
        body: commentIssueBody(payload),
        labels: 'comment'
      }});
      const url = `https://github.com/didin-maxim/knowledge_graph_of_graphs/issues/new?${{params.toString()}}`;
      const opened = window.open(url, '_blank', 'noopener,noreferrer');
      if (!opened) {{
        window.location.href = url;
      }}
    }}

    function attachCommentForms() {{
      document.querySelectorAll('[data-comment-form]').forEach(form => {{
        form.addEventListener('submit', async event => {{
          event.preventDefault();
          const formData = new FormData(form);
          const payload = buildCommentPayload(form.dataset.targetType, form.dataset.problemId || '', formData);
          try {{
            await persistCommentPayload(payload);
            form.reset();
          }} catch (error) {{
            alert(`Не удалось открыть GitHub issue: ${{error.message || error}}`);
          }}
        }});
      }});
    }}

    function renderProblem() {{
      const route = currentRoute();
      const problem = problems[route.id];
      byId('content').innerHTML = `
        <div class="topline">
          <span class="pill code">${{esc(problem.id)}}</span>
          ${{statusPill(problem.editorial?.review_status)}}
          <span class="pill">${{esc(label(taxonomy.difficulty_levels, problem.difficulty?.main))}}</span>
        </div>
        <h2>${{esc(problem.title)}}</h2>
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
      renderSidebar();
      renderSourceFilter();
      renderAuthorFilter();
      renderYearFilter();
      renderSolutionFilter();
      renderGoalFilter();
      renderObjectFilter();
      renderMethodFilter();
      renderTypeFilter();
      if (route.type === 'definition') renderDefinition();
      else if (route.type === 'idea') renderStandardIdea();
      else if (route.type === 'comment') renderCommentPage();
      else renderProblem();
    }}

    byId('search-input').addEventListener('input', event => {{
      state.query = event.target.value;
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

    byId('mode-problems').addEventListener('click', () => setProblem(sortedProblems()[0]?.id));
    byId('mode-definitions').addEventListener('click', () => setDefinition(sortedDefinitions()[0]?.id));
    byId('mode-ideas').addEventListener('click', () => setStandardIdea(sortedStandardIdeas()[0]?.id));
    byId('mode-comments').addEventListener('click', () => setComment(sortedComments()[0]?.id || null));

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
