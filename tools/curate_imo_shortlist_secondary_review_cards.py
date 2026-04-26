#!/usr/bin/env python3
"""Add cards after reviewing the secondary-shortlist needs_review items."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
TODAY = date.today().isoformat()


def dump(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def ensure_sources() -> None:
    path = DATA / "sources" / "sources.yaml"
    payload = json.loads(path.read_text(encoding="utf-8"))
    existing = {item["id"] for item in payload["sources"]}
    additions = [
        {
            "id": "src-kalva-imo-1994-c6-solution",
            "type": "secondary_solution",
            "title": "IMO Shortlist 1994 C6 solution, Kalva archive",
            "url": "https://prase.cz/kalva/short/soln/sh94c6.html",
            "browser_openable": True,
            "language": "en",
            "official": False,
            "status": "source_verified",
        },
        {
            "id": "src-jpsaha-count-two-diff-1995-nc5",
            "type": "secondary_solution",
            "title": "Counting in two different ways, IMOSL 1995 N5/NC5 walkthrough",
            "url": "https://jpsaha.github.io/mop/assets/pdf/Combinatorics/CountTwoDiff.pdf",
            "browser_openable": True,
            "language": "en",
            "official": False,
            "status": "source_verified",
        },
        {
            "id": "src-aops-imo-2004-c3-solution",
            "type": "secondary_solution",
            "title": "AoPS Wiki, 2004 IMO Shortlist C3 solution",
            "url": "https://artofproblemsolving.com/wiki/index.php/2004_IMO_Shortlist_Problems/C3",
            "browser_openable": True,
            "language": "en",
            "official": False,
            "status": "source_verified",
        },
        {
            "id": "src-problem-solving-methods-combinatorics-2005-c3",
            "type": "secondary_solution",
            "title": "Problem-Solving Methods in Combinatorics, board path injection solution",
            "url": "https://www.passeidireto.com/arquivo/133589579/2013-book-problem-solving-methods-in-combin",
            "browser_openable": True,
            "language": "en",
            "official": False,
            "status": "source_verified",
        },
    ]
    payload["sources"].extend(item for item in additions if item["id"] not in existing)
    dump(path, payload)


def stmt(text: str, sid: str, graph: bool = False) -> dict[str, object]:
    item = {
        "id": "stmt-graph" if graph else "stmt-original",
        "text": text,
        "status": "needs_human_review",
        "self_contained": {"status": "ai_checked"},
        "definition_ids": [],
    }
    if graph:
        item["distinct_from"] = ["stmt-original"]
    else:
        item["title"] = "Условие"
        item["source_id"] = sid
        item["distinct_from"] = ["stmt-graph"]
    return item


def idea(i: str, title: str, text: str, tags: list[str]) -> dict[str, object]:
    return {"id": i, "title": title, "text": text, "tags": tags, "status": "needs_human_review"}


def sol(text: str, ideas: list[dict[str, object]], standard: list[str]) -> dict[str, object]:
    return {
        "id": "sol-reviewed-secondary",
        "title": "Сжатое решение после review",
        "text": text,
        "idea_ids": [item["id"] for item in ideas],
        "standard_idea_ids": standard,
        "status": "needs_human_review",
    }


def card(pid: str, title: str, year: int, source: str, original: str, graph: str, ideas: list[dict[str, object]], solution: str, profile: dict[str, list[str]], tags: list[str], extra_sources: list[str]) -> dict[str, object]:
    return {
        "id": pid,
        "title": title,
        "kind": {"primary": "olympiad_problem", "secondary": ["application"]},
        "language": "ru",
        "problem_profile": {
            **profile,
            "keywords": [pid, "early_imo_shortlist", "secondary_review"],
            "status": "needs_human_review",
        },
        "statements": {"original": [stmt(original, source)], "graph_theory": [stmt(graph, source, True)], "olympiad_reformulations": []},
        "ideas": ideas,
        "solutions": [sol(solution, ideas, ["double_counting"] if "double_counting" in profile.get("methods", []) else [])],
        "difficulty": {"main": "imo_p3_plus", "local_score": 12, "comment": f"Ранний IMO Shortlist {year}; источник вторичный, решение сверено по secondary solution.", "status": "needs_human_review"},
        "tags": tags,
        "properties": {"central_method": {"value": profile.get("methods", []), "status": "needs_human_review"}},
        "sources": [{"source_id": source, "role": "secondary_shortlist_statement", "status": "source_verified"}] + [{"source_id": sid, "role": "secondary_solution", "status": "source_verified"} for sid in extra_sources],
        "editorial": {
            "created_by": "ai",
            "created_at": TODAY,
            "review_status": "needs_human_review",
            "public_ready": False,
            "notes": ["Источник решения не официальный IMO PDF; перед public_ready желательно сверить с полным сборником shortlist solutions."],
        },
    }


CARDS = [
    card(
        "imo-1994-c6-infinite-grid-pairing-strategy",
        "Бесконечные крестики-нолики и парная стратегия, IMO Shortlist 1994 C6",
        1994,
        "src-secondary-imo-1994-shortlist",
        "Два игрока по очереди играют на бесконечной квадратной решётке. Первый ставит \\(X\\) в пустую клетку, второй ставит \\(O\\) в пустую клетку. Первый выигрывает, если получает 11 подряд идущих \\(X\\) в одной строке, столбце или диагонали. Докажите, что второй может всегда помешать первому выиграть.",
        "Нужно построить паросочетание на части клеток бесконечного решётчатого графа так, чтобы каждый отрезок из 11 последовательных клеток по горизонтали, вертикали или диагонали содержал пару. Тогда второй отвечает в парную клетку.",
        [
            idea("idea-periodic-pairing", "Периодическое паросочетание клеток", "Повторяется блок \\(10\\times10\\), внутри которого отмечены пары клеток.", ["matching"]),
            idea("idea-threat-line-hit", "Каждая угроза длины 11 задевает пару", "Любая линия из 11 клеток в одном из четырёх направлений содержит две клетки одной пары.", ["coloring"]),
        ],
        "Решение строит периодический шаблон пар клеток на бесконечной решётке. В блоке \\(10\\times10\\) клетки разбиты на специальные пары так, что в каждой строке, каждом столбце и каждой достаточно длинной диагонали блока встречается целая пара; затем блок повторяется по всей плоскости. Стратегия второго: если первый ставит \\(X\\) в клетку пары, второй немедленно ставит \\(O\\) в другую клетку этой пары; остальные клетки шаблона можно игнорировать или обрабатывать согласно той же таблице. Тогда любой потенциальный отрезок из 11 клеток содержит обе клетки некоторой пары, а значит после хода второго не может состоять только из \\(X\\).",
        {"objects": ["infinite_grid", "cell_matching", "threat_lines"], "methods": ["pairing_strategy", "periodic_construction"], "transformations": ["game_board_to_matching"], "goal": ["second_player_draw_strategy"], "auxiliary_graph_type": ["grid_matching"], "invariants": ["paired_response"]},
        ["matching", "coloring"],
        ["src-kalva-imo-1994-c6-solution"],
    ),
    card(
        "imo-1995-nc5-greetings-regular-codegree-graph",
        "Рукопожатия с постоянным числом общих знакомых, IMO Shortlist 1995 NC5",
        1995,
        "src-secondary-imo-1995-shortlist",
        "На встрече \\(12k\\) человек. Каждый обменялся приветствиями ровно с \\(3k+6\\) другими. Для любых двух людей число людей, обменявшихся приветствиями с ними обоими, одно и то же. Сколько людей было на встрече?",
        "Построим регулярный граф на людях; ребро означает приветствие. У любых двух вершин одинаковое число общих соседей. Нужно определить число вершин.",
        [
            idea("idea-codegree-count", "Подсчёт общих соседей", "Считаются тройки: центральная вершина знакома с двумя выбранными людьми.", ["double_counting"]),
            idea("idea-divisibility", "Делимость параметров графа", "Полученная формула для общего кодегри должна быть целым числом, что резко ограничивает \\(k\\).", ["extremal_choice"]),
        ],
        "Пусть общий кодегри любых двух вершин равен \\(\\lambda\\). Считаем тройки \\((a,b,c)\\), где \\(a\\) приветствовал и \\(b\\), и \\(c\\), а \\(b\\ne c\\). С одной стороны, для каждого из \\(12k\\) людей можно выбрать пару его \\(3k+6\\) соседей. С другой стороны, каждая пара людей имеет ровно \\(\\lambda\\) общих соседей. Поэтому \\(12k\\binom{3k+6}{2}=\\lambda\\binom{12k}{2}\\), откуда \\(\\lambda=(3k+5)(3k+6)/(12k-1)\\). Целочисленность даёт, что \\(12k-1\\) делит 525; совместимость с видом \\(12k-1\\) оставляет \\(12k-1=35\\), то есть \\(k=3\\). Значит, людей было \\(36\\).",
        {"objects": ["regular_graph", "constant_codegree"], "methods": ["double_counting", "divisibility"], "transformations": ["greetings_to_graph"], "goal": ["determine_number_of_vertices"], "auxiliary_graph_type": [], "invariants": ["degree", "codegree"]},
        ["double_counting"],
        ["src-jpsaha-count-two-diff-1995-nc5"],
    ),
    card(
        "imo-2004-c3-delete-edge-from-4cycle",
        "Удаление ребра из 4-цикла, IMO Shortlist 2004 C3",
        2004,
        "src-secondary-imo-2004-shortlist",
        "Дан полный граф на \\(n\\ge4\\) вершинах. Разрешено выбрать цикл длины 4 и удалить из него одно ребро. Найдите наименьшее число рёбер графа, которое можно получить повторением таких операций.",
        "Это чистая задача о графовой операции: из \\(K_n\\) удаляются только рёбра, лежащие в текущем 4-цикле.",
        [
            idea("idea-connectivity-preserved", "Связность сохраняется", "Удаляемое ребро лежит в 4-цикле, значит его концы остаются соединены другим путём.", ["connectivity"]),
            idea("idea-odd-cycle-preserved", "Нечётный цикл сохраняется", "Из полного графа нельзя прийти к дереву: после каждой операции остаётся нечётный цикл.", ["trees"]),
        ],
        "Ответ: \\(n\\). Связность сохраняется: если удаляется ребро \\(AB\\) из 4-цикла, то в этом же цикле остаётся путь из \\(A\\) в \\(B\\). Кроме того, граф всегда содержит нечётный цикл. Изначально есть треугольник; если удаляемое ребро лежит на некотором нечётном цикле и одновременно на выбранном 4-цикле, то из симметрической перестройки этих двух циклов остаётся другой нечётный цикл, так что одним удалением нельзя уничтожить все нечётные циклы. Поэтому итоговый граф связен и не является деревом, значит имеет хотя бы \\(n\\) рёбер. Достижимость \\(n\\) рёбер строится индуктивно: почти все рёбра, инцидентные последней вершине, удаляются через подходящие 4-циклы, после чего применяется конструкция для \\(n-1\\) вершин.",
        {"objects": ["complete_graph", "4_cycle", "odd_cycle"], "methods": ["connectivity", "induction", "cycle_invariant"], "transformations": [], "goal": ["minimum_edges_after_operations"], "auxiliary_graph_type": [], "invariants": ["connectedness", "odd_cycle_exists"]},
        ["connectivity", "trees"],
        ["src-aops-imo-2004-c3-solution"],
    ),
    card(
        "imo-2005-c3-black-paths-injection",
        "Чёрные пути на доске и инъекция, IMO Shortlist 2005 C3",
        2005,
        "src-secondary-imo-2005-shortlist",
        "Доска \\(m\\times n\\) раскрашивается в чёрный и белый цвета. Пусть \\(N\\) — число раскрасок, в которых есть чёрный путь из левого края в правый, а \\(M\\) — число раскрасок, в которых есть два непересекающихся таких чёрных пути. Докажите, что \\(N^2\\ge M\\cdot2^{mn}\\).",
        "Рассматривается решётчатый граф клеток доски, где соседние по стороне клетки соединены ребром. Событие — наличие одного или двух непересекающихся чёрных путей между левым и правым краем.",
        [
            idea("idea-lowest-path", "Нижний чёрный путь", "В каждой раскраске с проходом выбирается единственный нижний проход, максимизирующий область над ним.", ["connectivity"]),
            idea("idea-swap-injection", "Инъекция обменом областей", "Для пары раскрасок меняются местами клетки на пути и выше него, что переводит пару в две раскраски с проходом.", ["extremal_choice"]),
        ],
        "Для каждой раскраски с левым-правым чёрным проходом выбираем нижний проход \\(L\\): путь, над которым область максимальна. Такой путь единственен. Рассмотрим пару \\((A,B)\\), где \\(A\\) — раскраска с двумя непересекающимися чёрными проходами, а \\(B\\) — произвольная раскраска. В раскраске \\(A\\) берём нижний проход \\(L\\) и меняем между \\(A\\) и \\(B\\) все клетки, лежащие на \\(L\\) и выше него. После обмена обе полученные раскраски имеют чёрный левый-правый проход: одна сохраняет нижний путь, другая — второй, непересекающийся путь. По нижнему пути операция однозначно обратима, поэтому построена инъекция из множества размера \\(M2^{mn}\\) в множество пар раскрасок с проходом размера \\(N^2\\).",
        {"objects": ["grid_graph", "vertex_disjoint_paths", "colorings"], "methods": ["injection", "extremal_path"], "transformations": ["board_to_grid_graph"], "goal": ["counting_inequality"], "auxiliary_graph_type": [], "invariants": ["lowest_crossing_path"]},
        ["connectivity"],
        ["src-problem-solving-methods-combinatorics-2005-c3"],
    ),
]


SOURCE_TO_PROBLEM = {
    "imo-1994-sl-c6": "imo-1994-c6-infinite-grid-pairing-strategy",
    "imo-1995-sl-c5": "imo-1995-nc5-greetings-regular-codegree-graph",
    "imo-2004-sl-c3": "imo-2004-c3-delete-edge-from-4cycle",
    "imo-2005-sl-c3": "imo-2005-c3-black-paths-injection",
}


def write_cards() -> None:
    for item in CARDS:
        dump(DATA / "problems" / "imo" / f"{item['id']}.yaml", item)


def update_batch() -> None:
    path = DATA / "import_batches" / "imo-shortlist-secondary-graph-curation.yaml"
    batch = json.loads(path.read_text(encoding="utf-8"))
    for item in batch["items"]:
        if item["id"] in SOURCE_TO_PROBLEM:
            item["status"] = "added"
            item["problem_id"] = SOURCE_TO_PROBLEM[item["id"]]
            item["decision_reason"] = "После review найдено устойчивое графовое решение; карточка создана."
        elif item["id"] in {"imo-1998-sl-c6", "imo-1999-sl-c5", "imo-2005-sl-c8"}:
            item["status"] = "needs_review"
            item["decision_reason"] = "Графовая постановка заметна, но в текущем проходе не найдено достаточно надёжного решения/формулы для карточки."
    batch["updated_at"] = TODAY
    dump(path, batch)


def main() -> int:
    ensure_sources()
    write_cards()
    update_batch()
    print(f"wrote {len(CARDS)} reviewed cards")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
