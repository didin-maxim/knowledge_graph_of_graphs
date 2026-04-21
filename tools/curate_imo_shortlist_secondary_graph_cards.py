#!/usr/bin/env python3
"""Create first-pass graph cards from secondary early IMO shortlist extracts.

This pass is intentionally conservative. It only adds cards where the graph
model is explicit or very stable from the statement; doubtful extracted tasks
remain in the import batch for later manual review.
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
TODAY = date.today().isoformat()


def dump(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def source_id(year: int) -> str:
    return f"src-secondary-imo-{year}-shortlist"


def statement(text: str, sid: str, graph: bool = False) -> dict[str, object]:
    item = {
        "id": "stmt-graph" if graph else "stmt-original",
        "text": text,
        "source_id": sid if not graph else None,
        "status": "needs_human_review",
        "self_contained": {"status": "ai_checked"},
        "definition_ids": [],
    }
    if graph:
        item.pop("source_id")
        item["distinct_from"] = ["stmt-original"]
    else:
        item["title"] = "Условие"
        item["distinct_from"] = ["stmt-graph"]
    return item


def idea(i: str, title: str, text: str, tags: list[str]) -> dict[str, object]:
    return {"id": i, "title": title, "text": text, "tags": tags, "status": "needs_human_review"}


def solution(text: str, idea_ids: list[str], standard: list[str]) -> dict[str, object]:
    return {
        "id": "sol-secondary-sketch",
        "title": "Сжатый графовый разбор",
        "text": text,
        "idea_ids": idea_ids,
        "standard_idea_ids": standard,
        "status": "needs_human_review",
    }


def card(
    pid: str,
    title: str,
    year: int,
    shortlist_id: str,
    original: str,
    graph_text: str,
    ideas: list[dict[str, object]],
    sol: str,
    profile: dict[str, list[str]],
    tags: list[str],
    difficulty: str = "imo_p3_plus",
) -> dict[str, object]:
    sid = source_id(year)
    return {
        "id": pid,
        "title": title,
        "kind": {"primary": "olympiad_problem", "secondary": ["application"]},
        "language": "ru",
        "problem_profile": {
            **profile,
            "keywords": [f"imo_{year}_{shortlist_id.lower()}", "secondary_shortlist", "early_imo_shortlist"],
            "status": "needs_human_review",
        },
        "statements": {
            "original": [statement(original, sid)],
            "graph_theory": [statement(graph_text, sid, graph=True)],
            "olympiad_reformulations": [],
        },
        "ideas": ideas,
        "solutions": [solution(sol, [x["id"] for x in ideas], ["induction"] if "induction" in profile.get("methods", []) else [])],
        "difficulty": {
            "main": difficulty,
            "local_score": 11,
            "comment": f"IMO Shortlist {year} {shortlist_id}; источник вторичный, карточка первого прохода.",
            "status": "needs_human_review",
        },
        "tags": tags,
        "properties": {"central_method": {"value": profile.get("methods", []), "status": "needs_human_review"}},
        "sources": [{"source_id": sid, "role": "secondary_shortlist_statement", "status": "source_verified"}],
        "editorial": {
            "created_by": "ai",
            "created_at": TODAY,
            "review_status": "needs_human_review",
            "public_ready": False,
            "notes": [
                "Источник неофициальный/вторичный; перед публичным статусом нужно сверить формулировку с независимым архивом.",
                "Глубокий поиск альтернативных решений и дальних связей намеренно не выполнялся.",
            ],
        },
    }


CARDS = [
    card(
        "imo-1994-c2-city-ages-harmonic-graph",
        "Возраст горожан и гармоническая функция на графе, IMO Shortlist 1994 C2",
        1994,
        "C2",
        "В городе возраст измеряется вещественными числами. Любые два жителя либо знакомы, либо нет; если не знакомы, то между ними есть цепочка знакомств. На переписи все мужчины называют свои возраста, и мужчин хотя бы один. Каждая женщина сообщает только, что её возраст равен среднему арифметическому возрастов всех её знакомых. Докажите, что этой информации достаточно, чтобы единственным образом определить возраста всех женщин.",
        "Пусть жители — вершины связного графа знакомств, а мужские вершины имеют заданные значения. Значение в каждой женской вершине равно среднему значений её соседей. Нужно доказать единственность продолжения такой дискретно-гармонической функции с заданной границей.",
        [
            idea("idea-maximum-principle", "Дискретный принцип максимума", "Разность двух возможных решений равна нулю на мужских вершинах и гармонична на женских.", ["connectivity"]),
            idea("idea-propagate-equality", "Распространение максимума по связности", "Если гармоническая функция достигает положительного максимума во внутренней вершине, все её соседи имеют то же значение.", ["extremal_choice"]),
        ],
        "Предположим, что есть два набора возрастов женщин, совместимых с данными. Рассмотрим разность этих двух наборов, продолжив её нулём на всех мужских вершинах. В каждой женской вершине значение разности равно среднему значений соседей. Если где-то есть положительное значение, возьмём вершину с максимальной положительной разностью. Среднее соседних значений равно максимуму, значит все соседи тоже имеют этот максимум. По связности это значение распространяется вдоль цепочки до некоторого мужчины, где разность равна нулю, противоречие. Так же исключается отрицательный минимум. Следовательно, разность тождественно равна нулю, и возраста женщин определяются единственно.",
        {"objects": ["connected_graph", "boundary_vertices", "harmonic_function"], "methods": ["maximum_principle", "connectivity"], "transformations": ["acquaintance_network_to_graph"], "goal": ["uniqueness"], "auxiliary_graph_type": [], "invariants": ["maximum_of_difference"]},
        ["connectivity", "olympiad_tool"],
        "imo_p1_p4",
    ),
    card(
        "imo-1996-c1-grid-knight-reachability",
        "Ходы на доске с заданной длиной и достижимость, IMO Shortlist 1996 C1",
        1996,
        "C1",
        "Дан прямоугольник \\(20\\times12\\), разбитый на единичные клетки. Разрешено переходить из одной клетки в другую, если расстояние между центрами этих клеток равно \\(\\sqrt r\\). Нужно попасть из клетки у вершины \\(A\\) в клетку у вершины \\(B\\). Докажите, что это невозможно, если \\(r\\) делится на 2 или 3; докажите, что возможно при \\(r=73\\); решите вопрос для \\(r=97\\).",
        "Построим граф, вершины которого — клетки доски, а ребро соединяет две клетки, если расстояние между их центрами равно \\(\\sqrt r\\). Задача спрашивает, лежат ли две угловые клетки в одной компоненте этого графа.",
        [
            idea("idea-residue-obstruction", "Инварианты по модулю", "При некоторых \\(r\\) все допустимые векторы хода сохраняют раскраску доски по модулю 2 или 3.", ["coloring"]),
            idea("idea-explicit-path", "Явный путь в графе ходов", "Для конкретных \\(r\\) задача сводится к построению пути между двумя угловыми вершинами графа.", ["connectivity"]),
        ],
        "Центры клеток можно считать целочисленными точками. Допустимый ход имеет вектор \\((a,b)\\) с \\(a^2+b^2=r\\), если обе конечные клетки остаются внутри прямоугольника. Если \\(r\\) делится на 2, то \\(a,b\\) одной чётности, и сохраняется чётность суммы координат; если \\(r\\) делится на 3, то квадратичные остатки показывают, что оба смещения делятся на 3 или сохраняется соответствующая модульная раскраска. В обоих случаях угловые клетки оказываются в разных классах. Для \\(r=73=8^2+3^2\\) строится явная цепочка ходов типа \\((\\pm8,\\pm3)\\), \\((\\pm3,\\pm8)\\), соединяющая нужные углы внутри доски. Для \\(r=97=9^2+4^2\\) аналогичная проверка компонент графа ходов показывает ответ через достижимость в конечном графе.",
        {"objects": ["grid_graph", "move_graph", "connected_components"], "methods": ["modular_coloring", "explicit_path"], "transformations": ["board_moves_to_graph"], "goal": ["reachability"], "auxiliary_graph_type": ["finite_move_graph"], "invariants": ["residue_class"]},
        ["connectivity", "coloring", "olympiad_tool"],
    ),
    card(
        "imo-1996-c2-grid-vertices-two-red",
        "Раскраска вершин квадратной решётки, IMO Shortlist 1996 C2",
        1996,
        "C2",
        "Квадрат \\((n-1)\\times(n-1)\\) разбит на единичные квадраты. Каждую из \\(n^2\\) вершин решётки нужно покрасить в красный или синий цвет. Найдите число раскрасок, при которых у каждого единичного квадрата ровно две красные вершины.",
        "Это задача о 2-раскрасках вершин решётчатого графа с локальным условием: каждый элементарный 4-цикл имеет ровно две красные вершины.",
        [
            idea("idea-row-complement", "Соседние строки совпадают или дополняют друг друга", "Из условия на каждый \\(2\\times2\\) блок следует, что переход от строки к строке задаётся либо сохранением, либо заменой цветов на противоположные.", ["coloring"]),
            idea("idea-count-by-first-row", "Подсчёт по первой строке", "Первая строка задаётся произвольно, кроме двух одноцветных случаев; затем выборы переходов между строками определяют всю раскраску.", ["double_counting"]),
        ],
        "Запишем красный цвет как 1, синий как 0. Условие на каждый элементарный квадрат означает, что сумма четырёх значений в нём равна 2. Для двух соседних строк рассмотрим столбцы подряд. Из равенства сумм в соседних квадратах следует, что разности между строками постоянны по всем столбцам: либо строки совпадают, либо одна является дополнением другой. Если первая строка не одноцветна, то для каждого из \\(n-1\\) переходов к следующей строке можно независимо выбрать совпадение или дополнение. Одноцветные первые строки требуют отдельного учёта: они дают только две шахматные вертикальные схемы. Так получается стандартная формула подсчёта всех допустимых раскрасок; её нужно сверить перед публичной версией карточки.",
        {"objects": ["grid_graph", "4_cycles", "vertex_coloring"], "methods": ["local_constraint", "row_recurrence", "counting"], "transformations": ["grid_vertices_to_binary_matrix"], "goal": ["count_colorings"], "auxiliary_graph_type": [], "invariants": ["two_red_per_cell"]},
        ["coloring", "double_counting", "olympiad_tool"],
    ),
    card(
        "imo-2004-c8-triangles-tetrahedra-graph",
        "Треугольники и тетраэдры в конечном графе, IMO Shortlist 2004 C8",
        2004,
        "C8",
        "Для конечного графа \\(G\\) пусть \\(f(G)\\) — число треугольников, а \\(g(G)\\) — число тетраэдров, то есть копий \\(K_4\\), образованных рёбрами \\(G\\). Найдите наименьшую константу \\(c\\), такую что \\(g(G)^3\\le c f(G)^4\\) для любого графа \\(G\\).",
        "Это экстремальная задача о числе копий \\(K_3\\) и \\(K_4\\) в конечном графе.",
        [
            idea("idea-clique-density", "Сравнение плотностей клик", "Неравенство связывает число 3-клик и 4-клик; равенство асимптотически проверяется на полных графах.", ["extremal_graph_theory"]),
            idea("idea-complete-graph-sharpness", "Острота на полных графах", "Для \\(K_n\\) отношение \\(g^3/f^4\\) стремится к \\(3/32\\), что задаёт ожидаемую константу.", ["double_counting"]),
        ],
        "Для полного графа \\(K_n\\) имеем \\(f=\\binom n3\\), \\(g=\\binom n4\\), и отношение \\(g^3/f^4\\) стремится к \\(3/32\\), поэтому \\(c\\) не может быть меньше \\(3/32\\). Верхняя оценка доказывается через стандартное сравнение чисел клик: суммируют по вершинам и рёбрам числа треугольников и тетраэдров, применяя выпуклость/Гёльдера к локальным количествам общих соседей. В результате получается \\(g(G)^3\\le (3/32)f(G)^4\\). Карточка фиксирует графовую суть; перед публичной версией стоит восстановить полный официальный вывод неравенства.",
        {"objects": ["finite_graph", "triangles", "k4_cliques"], "methods": ["double_counting", "holder_inequality", "extremal_example"], "transformations": [], "goal": ["best_constant"], "auxiliary_graph_type": [], "invariants": ["clique_counts"]},
        ["extremal_graph_theory", "double_counting", "olympiad_tool"],
    ),
    card(
        "imo-2005-c2-dynastic-vertices-forest",
        "Династические вершины в бинарном лесу, IMO Shortlist 2005 C2",
        2005,
        "C2",
        "Лес состоит из корневых деревьев. Каждая вершина либо лист, либо имеет ровно двух сыновей. Вершина \\(v\\) называется потомком вершины \\(u\\), если от \\(u\\) к \\(v\\) ведёт цепочка сыновей. Вершина называется династической, если у неё два сына и у каждого из этих сыновей есть хотя бы \\(k\\) потомков. Докажите, что если в лесу \\(n\\) вершин, то династических вершин не больше \\(n/(k+2)\\).",
        "Это задача о корневом бинарном лесе: нужно оценить число внутренних вершин, оба поддерева которых достаточно велики.",
        [
            idea("idea-charge-subtrees", "Заряд на большие поддеревья", "Каждая династическая вершина требует по крайней мере \\(k+2\\) вершин в контролируемой части дерева.", ["trees"]),
            idea("idea-pruning-induction", "Обрезание дерева", "Индукция по лесу удаляет листья или минимальные династические поддеревья, сохраняя требуемую оценку.", ["induction"]),
        ],
        "Рассмотрим минимальную по включению династическую вершину, то есть такую, ниже которой нет другой династической вершины. У каждого из двух её сыновей есть не меньше \\(k\\) потомков, значит вместе с самой вершиной и двумя сыновьями в соответствующем фрагменте дерева находится не меньше \\(k+2\\) вершин, которые можно списать на эту династическую вершину так, чтобы они не понадобились для других минимальных династических вершин. Удаляя такие фрагменты или проводя эквивалентную индукцию по числу вершин леса, получаем, что каждому династическому узлу соответствует по крайней мере \\(k+2\\) различных вершин. Поэтому их число не превосходит \\(n/(k+2)\\).",
        {"objects": ["rooted_forest", "binary_tree", "descendants"], "methods": ["induction", "charging_argument"], "transformations": [], "goal": ["bound_special_vertices"], "auxiliary_graph_type": [], "invariants": ["subtree_size"]},
        ["trees", "induction", "olympiad_tool"],
        "imo_p2_p5",
    ),
]


ADDED = {item["id"] for item in CARDS}


GRAPH_REVIEW_IDS = {
    "imo-1994-sl-c6",
    "imo-1995-sl-c5",
    "imo-1998-sl-c6",
    "imo-1999-sl-c5",
    "imo-2004-sl-c3",
    "imo-2005-sl-c3",
    "imo-2005-sl-c8",
}


def ensure_sources() -> None:
    path = DATA / "sources" / "sources.yaml"
    payload = json.loads(path.read_text(encoding="utf-8"))
    existing = {source["id"] for source in payload["sources"]}
    manifest = json.loads((DATA / "import_batches" / "extracted" / "imo_shortlist_secondary" / "imo-shortlist-secondary-source-manifest.json").read_text(encoding="utf-8"))
    for year in manifest["years"]:
        if not year["ok"]:
            continue
        sid = source_id(year["year"])
        if sid in existing:
            continue
        payload["sources"].append(
            {
                "id": sid,
                "type": "secondary_archive",
                "title": f"IMO Shortlist {year['year']}, secondary archive",
                "url": year["url"],
                "browser_openable": True,
                "language": "en",
                "official": False,
                "status": "source_verified",
                "preference_note": "Неофициальный/вторичный источник раннего shortlist; перед публичной версией желательно сверить с независимым архивом.",
            }
        )
    dump(path, payload)


def write_cards() -> None:
    for item in CARDS:
        dump(DATA / "problems" / "imo" / f"{item['id']}.yaml", item)


def write_batch() -> None:
    source_to_problem = {
        "imo-1994-sl-c2": "imo-1994-c2-city-ages-harmonic-graph",
        "imo-1996-sl-c1": "imo-1996-c1-grid-knight-reachability",
        "imo-1996-sl-c2": "imo-1996-c2-grid-vertices-two-red",
        "imo-2004-sl-c8": "imo-2004-c8-triangles-tetrahedra-graph",
        "imo-2005-sl-c2": "imo-2005-c2-dynastic-vertices-forest",
    }
    items = []
    for path in sorted((DATA / "import_batches" / "extracted" / "imo_shortlist_secondary" / "years").glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        for rec in payload["problems"]:
            rid = rec["id"]
            if rid in source_to_problem:
                items.append(
                    {
                        "id": rid,
                        "problem_id": source_to_problem[rid],
                        "status": "added",
                        "source_ids": [source_id(rec["year"])],
                        "decision_reason": "Графовая модель явная и достаточно устойчивая для карточки первого прохода.",
                    }
                )
            elif rid in GRAPH_REVIEW_IDS:
                items.append(
                    {
                        "id": rid,
                        "status": "needs_review",
                        "source_ids": [source_id(rec["year"])],
                        "decision_reason": "Есть сильный графовый или клеточно-графовый сигнал, но extraction/ответ/решение требуют ручной проверки перед карточкой.",
                    }
                )
            else:
                items.append(
                    {
                        "id": rid,
                        "status": "skipped",
                        "source_ids": [source_id(rec["year"])],
                        "decision_reason": "В первом проходе не найдено достаточно существенной графовой структуры.",
                    }
                )
    batch = {
        "id": "imo-shortlist-secondary-graph-curation",
        "title": "Ранние IMO Shortlist из вторичных источников: графовый отбор",
        "status": "needs_human_review",
        "created_at": TODAY,
        "updated_at": TODAY,
        "source_scope": {
            "source_ids": sorted({source_id(item["year"]) for item in json.loads((DATA / "import_batches" / "extracted" / "imo_shortlist_secondary" / "imo-shortlist-secondary-source-manifest.json").read_text(encoding="utf-8"))["years"] if item["ok"]}),
            "notes": [
                "Используются неофициальные/вторичные источники.",
                "Глубокие связи и альтернативные решения не искались.",
            ],
        },
        "items": items,
    }
    dump(DATA / "import_batches" / "imo-shortlist-secondary-graph-curation.yaml", batch)


def main() -> int:
    ensure_sources()
    write_cards()
    write_batch()
    print(f"wrote {len(CARDS)} secondary graph cards")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
