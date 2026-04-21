#!/usr/bin/env python3
"""Add cards for the remaining secondary-shortlist graph review items."""

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
            "id": "src-kalva-imo-1998-c6-solution",
            "type": "secondary_solution",
            "title": "IMO Shortlist 1998 C6 solution, Kalva archive",
            "url": "https://prase.cz/kalva/short/soln/sh98c6.html",
            "browser_openable": True,
            "language": "en",
            "official": False,
            "status": "source_verified",
        },
        {
            "id": "src-aops-imo-1999-p3-statement",
            "type": "statement",
            "title": "AoPS Wiki, 1999 IMO Problems/Problem 3",
            "url": "https://wiki.artofproblemsolving.com/wiki/index.php/1999_IMO_Problems/Problem_3",
            "browser_openable": True,
            "language": "en",
            "official": False,
            "status": "source_verified",
        },
        {
            "id": "src-olympiad-combinatorics-1999-p3",
            "type": "secondary_solution",
            "title": "Olympiad Combinatorics, IMO 1999 Problem 3 solution",
            "url": "https://1library.net/document/zkomjopy-olympiad-combinatorics.html",
            "browser_openable": True,
            "language": "en",
            "official": False,
            "status": "source_verified",
        },
        {
            "id": "src-imomath-compendium-2005-c8-solution",
            "type": "secondary_solution",
            "title": "IMO Compendium excerpt, 2005 Shortlist C8 solution",
            "url": "https://www.imomath.com/pcpdf/f1/f38.pdf",
            "browser_openable": True,
            "language": "en",
            "official": False,
            "status": "source_verified",
        },
    ]
    payload["sources"].extend(item for item in additions if item["id"] not in existing)
    dump(path, payload)


def statement(text: str, source_id: str | None = None, graph: bool = False) -> dict[str, object]:
    item: dict[str, object] = {
        "id": "stmt-graph" if graph else "stmt-original",
        "text": text,
        "status": "needs_human_review",
        "self_contained": {"status": "ai_checked"},
        "definition_ids": [],
        "distinct_from": ["stmt-original"] if graph else ["stmt-graph"],
    }
    if source_id:
        item["source_id"] = source_id
    if not graph:
        item["title"] = "Условие"
    return item


def idea(i: str, title: str, text: str, tags: list[str]) -> dict[str, object]:
    return {"id": i, "title": title, "text": text, "tags": tags, "status": "needs_human_review"}


def make_card(
    pid: str,
    title: str,
    source_id: str,
    original: str,
    graph_text: str,
    ideas: list[dict[str, object]],
    solution: str,
    profile: dict[str, object],
    tags: list[str],
    extra_sources: list[tuple[str, str]],
    note: str,
) -> dict[str, object]:
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
        "statements": {
            "original": [statement(original, source_id)],
            "graph_theory": [statement(graph_text, graph=True)],
            "olympiad_reformulations": [],
        },
        "ideas": ideas,
        "solutions": [
            {
                "id": "sol-reviewed-web",
                "title": "Сжатое решение после web review",
                "text": solution,
                "idea_ids": [item["id"] for item in ideas],
                "standard_idea_ids": profile.get("standard_idea_ids", []),
                "status": "needs_human_review",
            }
        ],
        "difficulty": {
            "main": "imo_p3_plus",
            "local_score": 13,
            "comment": "Ранний IMO/IMO Shortlist; добавлено после отдельной проверки AoPS, Kalva и/или сборника решений.",
            "status": "needs_human_review",
        },
        "tags": tags,
        "properties": {"central_method": {"value": profile.get("methods", []), "status": "needs_human_review"}},
        "sources": [{"source_id": source_id, "role": "secondary_shortlist_statement", "status": "source_verified"}]
        + [{"source_id": sid, "role": role, "status": "source_verified"} for sid, role in extra_sources],
        "editorial": {
            "created_by": "ai",
            "created_at": TODAY,
            "review_status": "needs_human_review",
            "public_ready": False,
            "notes": [note],
        },
    }


CARDS = [
    make_card(
        "imo-1998-c6-complete-graph-rainbow-edges",
        "Раскраска рёбер K10 и разноцветные рёбра, IMO Shortlist 1998 C6",
        "src-secondary-imo-1998-shortlist",
        "Даны 10 точек общего положения на плоскости; каждый отрезок между парой точек окрашен в один из k цветов. Требуется, чтобы для любых k из 10 точек среди отрезков с концами в этих k точках нашлись k отрезков попарно разных цветов. Найти все k, 1 <= k <= 10, для которых это возможно.",
        "Это задача о раскраске рёбер полного графа K10. Для каждого k нужно, чтобы любой индуцированный K_k содержал k рёбер разных цветов; существенная часть решения для k=4 использует локальные степени цвета и R(3,3)=6.",
        [
            idea("idea-five-color-construction", "Пятицветная конструкция через разбиения", "Для каждого цвета задаются группы вершин, внутри которых все рёбра имеют этот цвет; из любых пяти вершин две попадают в одну группу каждого цвета.", ["coloring"]),
            idea("idea-four-color-ramsey-obstruction", "Запрет четырёх цветов через R(3,3)", "Если четыре цвета работали бы для любых четырёх вершин, то анализ цветовых степеней в одной вершине и Ramsey R(3,3)=6 дают одноцветный или безданногоцветный треугольник, что приводит к противоречию.", ["ramsey_theory"]),
        ],
        "Ответ: возможны все k, кроме k=4; нетривиальна проверка k=5 и невозможность k=4, остальные значения следуют проще из монотонных/элементарных соображений. Для k=5 строится явная 5-раскраска рёбер K10: каждый цвет задаётся несколькими кликами-группами так, что любые пять вершин содержат ребро каждого из пяти цветов. Для k=4 предположим, что раскраска четырьмя цветами существует. В одной вершине не может быть четырёх рёбер одного цвета, иначе вместе с подходящим ребром среди четырёх соседей получаются четыре ребра одного цвета на четырёх вершинах. Значит для некоторого цвета из вершины выходят ровно три ребра AB, AC, AD. Тогда BC, BD, CD не имеют этого цвета. На оставшихся шести вершинах по R(3,3)=6 есть либо треугольник этого цвета, либо треугольник без этого цвета. В обоих случаях, добавляя A или одну из B,C,D, получаем четыре вершины, где невозможно иметь четыре разных цвета.",
        {
            "objects": ["complete_graph", "edge_coloring", "rainbow_subgraph", "ramsey_triangle"],
            "methods": ["explicit_coloring", "ramsey_theory", "degree_counting"],
            "transformations": ["points_to_complete_graph"],
            "goal": ["determine_possible_number_of_colors"],
            "auxiliary_graph_type": [],
            "invariants": ["color_degree_constraints"],
            "standard_idea_ids": ["pigeonhole_principle"],
        },
        ["coloring", "ramsey_theory", "olympiad_tool"],
        [("src-kalva-imo-1998-c6-solution", "secondary_solution")],
        "AoPS printable collection gives the statement; Kalva supplies a complete solution. The graph method is essential, especially the K10 edge-colouring and R(3,3) obstruction.",
    ),
    make_card(
        "imo-1999-c5-grid-total-domination",
        "Минимальное доминирующее множество на доске, IMO 1999 Problem 3 / Shortlist C5",
        "src-secondary-imo-1999-shortlist",
        "Пусть n — чётное положительное число. На доске n x n нужно отметить минимальное число клеток так, чтобы каждая клетка, отмеченная или нет, имела отмеченную соседнюю по стороне клетку. Найти этот минимум.",
        "Это точное вычисление total domination number для решёточного графа n x n: вершины — клетки, рёбра соединяют клетки с общей стороной, и каждая вершина должна иметь отмеченного соседа.",
        [
            idea("idea-layer-coloring-lower-bound", "Слоистая раскраска для нижней оценки", "Доска раскрашивается слоями так, что каждая клетка соседствует ровно с двумя выделенными клетками цвета-свидетеля; один отмеченный сосед может покрыть не больше двух таких свидетелей.", ["coloring"]),
            idea("idea-alternating-construction", "Конструкция через чередование в слоях", "Отмечаются чередующиеся клетки в выбранных слоях; каждая клетка получает отмеченного соседа, и достигается нижняя оценка.", ["extremal_choice"]),
        ],
        "Пусть n=2k. Ответ равен k(k+1)=n^2/4+n/2. Для нижней оценки используют специальную слоистую раскраску клеток-свидетелей: каждая клетка доски соседствует ровно с двумя такими клетками. Поэтому одна отмеченная клетка может обеспечить соседство не более чем для двух свидетелей, а число свидетелей равно 2k(k+1); нужно хотя бы k(k+1) отмеченных клеток. Конструкция достигает этой оценки: в каждом слое выбираются чередующиеся клетки так, чтобы каждая невыбранная и выбранная клетка имела выбранного соседа. В терминах графов это ровно построение минимального множества вершин, тотально доминирующего решёточный граф.",
        {
            "objects": ["grid_graph", "total_dominating_set", "board_cells"],
            "methods": ["coloring", "construction", "lower_bound"],
            "transformations": ["board_to_grid_graph"],
            "goal": ["minimum_total_dominating_set_size"],
            "auxiliary_graph_type": [],
            "invariants": ["neighbor_coverage"],
            "standard_idea_ids": [],
        },
        ["coloring", "extremal_graph_theory", "olympiad_tool"],
        [
            ("src-aops-imo-1999-p3-statement", "statement_crosscheck"),
            ("src-olympiad-combinatorics-1999-p3", "secondary_solution"),
        ],
        "AoPS has the official IMO statement but no solution on the wiki page. The graph interpretation is substantial as total domination in a grid graph, though the standard olympiad proof is usually phrased as a board colouring argument.",
    ),
    make_card(
        "imo-2005-c8-noncrossing-diagonals-crossings",
        "Пересечения двух триангуляционных наборов диагоналей, IMO Shortlist 2005 C8",
        "src-secondary-imo-2005-shortlist",
        "В выпуклом n-угольнике некоторые n-3 диагонали окрашены в чёрный цвет, а другие n-3 диагонали — в красный. Диагонали одного цвета не пересекаются строго внутри многоугольника, хотя могут иметь общую вершину. Найти максимальное число внутренних точек пересечения диагоналей разных цветов.",
        "Каждый цвет задаёт максимальное непересекающееся множество диагоналей, то есть триангуляцию. Задача ищет максимальное число пересечений между двумя плоскими диагональными графами на одних и тех же вершинах.",
        [
            idea("idea-pair-ears", "Попарное снятие ушных диагоналей", "В любой триангуляции есть две диагонали, отсекающие треугольники; их последовательно объединяют в пары, уменьшая оставшийся многоугольник.", ["planar_graphs"]),
            idea("idea-crossing-sum-bound", "Оценка суммы пересечений по парам", "Для двух зелёных диагоналей оценивается сумма чисел красных пересечений через размер части многоугольника между ними.", ["double_counting"]),
        ],
        "Ответ: ceil(3(n-3)^2/4). Пусть C_d — число пересечений красных диагоналей с зелёной диагональю d. Для двух зелёных диагоналей d_i,d_j, между которыми лежит часть многоугольника с m вершинами, красных диагоналей, пересекающих обе, не больше n-m-1, а остальные relevant диагонали пересекают не более одной из них; отсюда C_{d_i}+C_{d_j} <= 2n-m-4. Затем зелёные диагонали упорядочивают попарно: сначала две ушные диагонали, отсекающие два треугольника, затем две такие же в оставшемся (n-2)-угольнике, и так далее. Для k-й пары соответствующий m не меньше n-2k, поэтому сумма по парам даёт верхнюю оценку ceil(3(n-3)^2/4). Конструкция из официального решения берёт две веерные семьи диагоналей одного цвета и две веерные семьи другого цвета около четырёх подходящих вершин; она достигает этой оценки.",
        {
            "objects": ["convex_polygon", "noncrossing_diagonals", "triangulation", "crossing_number"],
            "methods": ["ear_decomposition", "double_counting", "extremal_construction"],
            "transformations": ["diagonal_sets_to_plane_graphs"],
            "goal": ["maximize_bichromatic_crossings"],
            "auxiliary_graph_type": ["outerplanar_graph"],
            "invariants": ["triangulation_size"],
            "standard_idea_ids": ["double_counting"],
        },
        ["planar_graphs", "double_counting", "extremal_graph_theory", "olympiad_tool"],
        [("src-imomath-compendium-2005-c8-solution", "published_solution")],
        "The solution in the IMO Compendium excerpt is explicitly about noncrossing diagonal graphs/triangulations; graph structure is central.",
    ),
]


SOURCE_TO_PROBLEM = {
    "imo-1998-sl-c6": "imo-1998-c6-complete-graph-rainbow-edges",
    "imo-1999-sl-c5": "imo-1999-c5-grid-total-domination",
    "imo-2005-sl-c8": "imo-2005-c8-noncrossing-diagonals-crossings",
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
            item["decision_reason"] = "После web/AoPS review графовая структура признана существенной; карточка создана."
    batch["updated_at"] = TODAY
    dump(path, batch)


def main() -> int:
    ensure_sources()
    write_cards()
    update_batch()
    print(f"wrote {len(CARDS)} remaining reviewed cards")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
