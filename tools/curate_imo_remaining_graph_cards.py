#!/usr/bin/env python3
"""Create graph cards from the remaining early IMO combinatorics extract."""

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
            "id": "src-imomath-imo-1964",
            "type": "statement",
            "title": "IMOmath, IMO 1964 problems",
            "url": "https://imomath.com/othercomp/I/Imo1964.pdf",
            "browser_openable": True,
            "language": "en",
            "official": False,
            "status": "source_verified",
        },
        {
            "id": "src-imomath-imo-1979",
            "type": "statement",
            "title": "IMOmath, IMO 1979 problems",
            "url": "https://imomath.com/othercomp/I/Imo1979.pdf",
            "browser_openable": True,
            "language": "en",
            "official": False,
            "status": "source_verified",
        },
        {
            "id": "src-imomath-imo-1986",
            "type": "statement",
            "title": "IMOmath, IMO 1986 problems",
            "url": "https://imomath.com/othercomp/I/Imo1986.pdf",
            "browser_openable": True,
            "language": "en",
            "official": False,
            "status": "source_verified",
        },
        {
            "id": "src-imomath-imo-1991",
            "type": "statement",
            "title": "IMOmath, IMO 1991 problems",
            "url": "https://imomath.com/othercomp/I/Imo1991.pdf",
            "browser_openable": True,
            "language": "en",
            "official": False,
            "status": "source_verified",
        },
        {
            "id": "src-imomath-imo-1992",
            "type": "statement",
            "title": "IMOmath, IMO 1992 problems",
            "url": "https://imomath.com/othercomp/I/Imo1992.pdf",
            "browser_openable": True,
            "language": "en",
            "official": False,
            "status": "source_verified",
        },
        {
            "id": "src-imomath-imo-1997",
            "type": "statement",
            "title": "IMOmath, IMO 1997 problems",
            "url": "https://imomath.com/othercomp/I/Imo1997.pdf",
            "browser_openable": True,
            "language": "en",
            "official": False,
            "status": "source_verified",
        },
        {
            "id": "src-kalva-imo-1985-shortlist",
            "type": "secondary_shortlist_statement",
            "title": "Kalva archive, IMO Shortlist 1985",
            "url": "https://prase.cz/kalva/short/sh85.html",
            "browser_openable": True,
            "language": "en",
            "official": False,
            "status": "source_verified",
        },
        {
            "id": "src-kalva-imo-1986-shortlist",
            "type": "secondary_shortlist_statement",
            "title": "Kalva archive, IMO Shortlist 1986",
            "url": "https://prase.cz/kalva/short/sh86.html",
            "browser_openable": True,
            "language": "en",
            "official": False,
            "status": "source_verified",
        },
        {
            "id": "src-kalva-imo-1989-shortlist",
            "type": "secondary_shortlist_statement",
            "title": "Kalva archive, IMO Shortlist 1989",
            "url": "https://prase.cz/kalva/short/sh89.html",
            "browser_openable": True,
            "language": "en",
            "official": False,
            "status": "source_verified",
        },
        {
            "id": "src-kalva-imo-1991-shortlist",
            "type": "secondary_shortlist_statement",
            "title": "Kalva archive, IMO Shortlist 1991",
            "url": "https://prase.cz/kalva/short/sh91.html",
            "browser_openable": True,
            "language": "en",
            "official": False,
            "status": "source_verified",
        },
        {
            "id": "src-imo-compendium-solutions-1959-2004",
            "type": "secondary_solution",
            "title": "IMO Compendium / early IMO solution collection",
            "url": "https://www.imomath.com/",
            "browser_openable": True,
            "language": "en",
            "official": False,
            "status": "source_verified",
        },
    ]
    payload["sources"].extend(item for item in additions if item["id"] not in existing)
    dump(path, payload)


def stmt(text: str, source_id: str, graph: bool = False) -> dict[str, object]:
    item = {
        "id": "stmt-graph" if graph else "stmt-original",
        "text": text,
        "status": "needs_human_review",
        "self_contained": {"status": "ai_checked"},
        "definition_ids": [],
        "distinct_from": ["stmt-original"] if graph else ["stmt-graph"],
    }
    if not graph:
        item["title"] = "Условие"
        item["source_id"] = source_id
    return item


def idea(i: str, title: str, text: str, tags: list[str]) -> dict[str, object]:
    return {"id": i, "title": title, "text": text, "tags": tags, "status": "needs_human_review"}


def card(
    pid: str,
    title: str,
    source_id: str,
    original: str,
    graph_text: str,
    ideas: list[dict[str, object]],
    solution: str,
    profile: dict[str, object],
    tags: list[str],
    source_role: str = "statement",
) -> dict[str, object]:
    return {
        "id": pid,
        "title": title,
        "kind": {"primary": "olympiad_problem", "secondary": ["application"]},
        "language": "ru",
        "problem_profile": {
            **profile,
            "keywords": [pid, "early_imo_remaining", "graph_review"],
            "status": "needs_human_review",
        },
        "statements": {
            "original": [stmt(original, source_id)],
            "graph_theory": [stmt(graph_text, source_id, True)],
            "olympiad_reformulations": [],
        },
        "ideas": ideas,
        "solutions": [
            {
                "id": "sol-graph-review",
                "title": "Сжатое графовое решение",
                "text": solution,
                "idea_ids": [item["id"] for item in ideas],
                "standard_idea_ids": profile.get("standard_idea_ids", []),
                "status": "needs_human_review",
            }
        ],
        "difficulty": {
            "main": "imo_p3_plus",
            "local_score": profile.get("local_score", 11),
            "comment": "Добавлено из оставшегося early IMO/shortlist extraction после проверки существенности графовой модели.",
            "status": "needs_human_review",
        },
        "tags": tags,
        "properties": {"central_method": {"value": profile.get("methods", []), "status": "needs_human_review"}},
        "sources": [
            {"source_id": source_id, "role": source_role, "status": "source_verified"},
            {"source_id": "src-imo-compendium-solutions-1959-2004", "role": "secondary_solution_crosscheck", "status": "source_verified"},
        ],
        "editorial": {
            "created_by": "ai",
            "created_at": TODAY,
            "review_status": "needs_human_review",
            "public_ready": False,
            "notes": [
                "Graph significance checked against the problem statement and standard official/compendium-style solution. Early shortlist source is secondary when no official shortlist PDF is available online."
            ],
        },
    }


CARDS = [
    card(
        "imo-1964-p4-three-topic-ramsey",
        "Три темы разговора и одноцветный треугольник, IMO 1964 P4",
        "src-imomath-imo-1964",
        "Каждая пара из 17 учеников поговорила ровно на одну из трёх тем. Докажите, что найдутся трое учеников, которые попарно говорили между собой на одну и ту же тему.",
        "Это раскраска рёбер полного графа K_17 в три цвета; нужно найти одноцветный K_3.",
        [
            idea("idea-ramsey-from-one-vertex", "Одна вершина даёт шесть рёбер одного цвета", "Из выбранной вершины выходит 16 рёбер трёх цветов, значит хотя бы 6 из них одного цвета.", ["ramsey_theory"]),
            idea("idea-close-or-complement", "Либо замыкаем треугольник, либо остаётся двухцветный K_6", "Если среди шести соседей есть ребро того же цвета, всё готово; иначе их полный граф раскрашен двумя цветами и содержит одноцветный треугольник.", ["coloring"]),
        ],
        "Выберем ученика A. Среди 16 разговоров от A хотя бы 6 имеют одну тему, скажем первую; пусть это множество B. Если две вершины из B также говорили на первую тему, вместе с A они дают нужную тройку. Если нет, то все рёбра внутри B окрашены только двумя оставшимися цветами. По R(3,3)=6 в K_6 найдётся одноцветный треугольник. Значит в любом случае есть трое учеников, попарно говоривших на одну тему.",
        {"objects": ["complete_graph", "edge_coloring", "monochromatic_triangle"], "methods": ["ramsey_theory", "pigeonhole"], "transformations": ["students_to_complete_graph"], "goal": ["force_monochromatic_triangle"], "auxiliary_graph_type": [], "invariants": ["color_degree"], "standard_idea_ids": ["pigeonhole_principle"], "local_score": 8},
        ["ramsey_theory", "coloring", "olympiad_tool"],
    ),
    card(
        "imo-1979-p6-octagon-walks-cycle-graph",
        "Пути фишки по восьмиугольнику, IMO 1979 P6",
        "src-imomath-imo-1979",
        "В регулярном восьмиугольнике фишка стартует из вершины S и каждую секунду переходит в одну из двух соседних вершин. Процесс заканчивается в противоположной вершине F. Пусть a_n — число различных путей длительности n из S в F. Докажите заданную формулу для a_n.",
        "Это подсчёт числа прогулок длины n между противоположными вершинами в цикле C_8.",
        [
            idea("idea-fold-cycle", "Сложить C_8 по симметрии", "По расстоянию от S противоположные вершины имеют одинаковое число путей, поэтому задача сводится к линейной рекурсии на четырёх состояниях.", ["graph_symmetry"]),
            idea("idea-characteristic-roots", "Рекурсия для чётных длин", "Для b_n=a_{2n} получается линейная рекурсия с корнями 2+sqrt(2) и 2-sqrt(2).", ["double_counting"]),
        ],
        "Нечётная длина невозможна, потому что C_8 двудолен и S,F лежат в одной доле: a_{2n-1}=0. Для чётных длин сложим вершины цикла по симметрии относительно оси SF и будем считать числа путей в зависимости от расстояния до S. Переходы между четырьмя расстояниями дают линейную систему; исключая промежуточные состояния, получаем для b_n=a_{2n} рекурсию b_n=4b_{n-1}-2b_{n-2} с начальными значениями b_1=0, b_2=2. Поэтому b_n=((2+sqrt(2))^{n-1}-(2-sqrt(2))^{n-1})/sqrt(2).",
        {"objects": ["cycle_graph", "walks", "recurrence"], "methods": ["graph_symmetry", "linear_recurrence"], "transformations": ["octagon_moves_to_cycle_graph"], "goal": ["count_walks"], "auxiliary_graph_type": ["cycle_graph"], "invariants": ["parity"], "standard_idea_ids": [], "local_score": 9},
        ["graph_symmetry", "double_counting", "olympiad_tool"],
    ),
    card(
        "imo-1985-sl5-lattice-perfect-code",
        "Совершенное независимое множество в кубической решётке, IMO Shortlist 1985",
        "src-kalva-imo-1985-shortlist",
        "В множестве всех целочисленных точек пространства две точки называются соседними, если две координаты совпадают, а третья отличается на 1. Докажите, что существует подмножество S, в котором никакие две соседние точки не лежат вместе, а каждая точка вне S имеет ровно одного соседа из S.",
        "Это построение совершенного 1-кода в бесконечном 6-регулярном решёточном графе Z^3.",
        [
            idea("idea-mod-seven-label", "Метка по модулю 7", "Функция x+2y+3z mod 7 меняется на шесть разных ненулевых остатков при переходе к шести соседям.", ["coloring"]),
            idea("idea-perfect-code", "Один сосед каждого внешнего узла", "Класс нулевого остатка независим, а у любой другой вершины ровно один сосед попадает в нулевой класс.", ["extremal_graph_theory"]),
        ],
        "Положим S={(x,y,z): x+2y+3z ≡ 0 (mod 7)}. У шести соседей точки значение этой линейной формы отличается на ±1, ±2, ±3, то есть на все ненулевые остатки по модулю 7. Поэтому две соседние точки не могут обе лежать в S. Если же значение в точке равно r≠0, то среди шести изменений ±1,±2,±3 ровно одно равно -r mod 7; соответствующий сосед и только он лежит в S.",
        {"objects": ["infinite_grid_graph", "perfect_code", "independent_set"], "methods": ["modular_coloring", "construction"], "transformations": ["lattice_to_grid_graph"], "goal": ["construct_perfect_independent_dominating_set"], "auxiliary_graph_type": ["grid_graph"], "invariants": ["residue_class"], "standard_idea_ids": [], "local_score": 10},
        ["coloring", "extremal_graph_theory", "olympiad_tool"],
        "secondary_shortlist_statement",
    ),
    card(
        "imo-1986-sl12-increasing-edge-trail",
        "Возрастающая цепь рёбер в размеченном графе, IMO Shortlist 1986",
        "src-kalva-imo-1986-shortlist",
        "В графе n вершин и q рёбер; рёбра помечены числами 1,2,...,q. Докажите, что найдётся последовательность по крайней мере 2q/n рёбер, в которой метки возрастают, а соседние рёбра имеют общую вершину.",
        "Нужно найти длинный ориентированный путь в линейном графе L(G), где рёбра исходного графа стали вершинами, упорядоченными по меткам.",
        [
            idea("idea-line-graph-path", "Перейти к линейному графу", "Последовательность рёбер с общей вершиной — это путь в L(G), а возрастание меток задаёт ациклическую ориентацию.", ["extremal_choice"]),
            idea("idea-average-degree-bound", "Средняя степень заставляет длинный путь", "В размеченном графе можно выбрать вершину большой степени и продолжать возрастающую цепь через ранги инцидентных рёбер.", ["extremal_choice"]),
        ],
        "Рассматриваем каждое ребро исходного графа как вершину линейного графа L(G); две такие вершины смежны, если соответствующие рёбра имеют общий конец. Направим каждое ребро L(G) от меньшей метки к большей. Требуется длинный ориентированный путь. Стандартное доказательство берёт для каждого ребра наибольшую длину возрастающей цепи, заканчивающейся в нём, и суммирует эти величины по инцидентным рёбрам у каждой вершины исходного графа. Из выпуклости/средней степени получается, что максимальная длина не меньше средней степени исходного графа, то есть 2q/n.",
        {"objects": ["graph", "edge_labels", "line_graph", "directed_path"], "methods": ["longest_path", "average_degree"], "transformations": ["edges_to_line_graph_vertices"], "goal": ["find_long_increasing_trail"], "auxiliary_graph_type": ["line_graph"], "invariants": ["edge_label_order"], "standard_idea_ids": ["longest_path"], "local_score": 12},
        ["extremal_graph_theory", "extremal_choice", "olympiad_tool"],
        "secondary_shortlist_statement",
    ),
    card(
        "imo-1986-p6-axis-line-balanced-coloring",
        "Баланс красных и белых точек на строках и столбцах, IMO 1986 P6",
        "src-imomath-imo-1986",
        "Дано конечное множество точек с целыми координатами на плоскости. Можно ли раскрасить часть точек в красный цвет, а остальные в белый так, чтобы на каждой прямой, параллельной одной из координатных осей, числа красных и белых точек отличались не более чем на 1?",
        "Построим двудольный граф: строки и столбцы — вершины, каждая точка — ребро между своей строкой и своим столбцом. Нужно 2-раскрасить рёбра так, чтобы в каждой вершине числа двух цветов отличались не более чем на 1.",
        [
            idea("idea-row-column-bipartite-graph", "Точки как рёбра двудольного графа", "Ограничения по горизонтальным и вертикальным прямым становятся локальным балансом цветов рёбер в каждой вершине.", ["coloring"]),
            idea("idea-alternate-on-trails", "Чередование на эйлеровых кусках", "Разбиваем рёбра каждой компоненты на циклы и пути и красим их попеременно.", ["eulerian_graphs"]),
        ],
        "Создадим двудольный граф: слева все занятые горизонтали, справа все занятые вертикали, а точка (x,y) даёт ребро между своей горизонталью и вертикалью. Достаточно раскрасить рёбра графа в два цвета так, чтобы у каждой вершины разность чисел инцидентных рёбер двух цветов была не больше 1. В каждой компоненте добавим при необходимости фиктивные рёбра, чтобы все степени стали чётными, разложим на эйлеровы циклы и покрасим рёбра каждого цикла попеременно. После удаления фиктивных рёбер баланс в каждой вершине нарушается не более чем на 1. Возвращаясь к точкам, получаем требуемую раскраску.",
        {"objects": ["bipartite_graph", "edge_coloring", "eulerian_circuits"], "methods": ["graph_modeling", "alternating_coloring", "eulerian_decomposition"], "transformations": ["points_to_row_column_bipartite_graph"], "goal": ["balanced_two_coloring"], "auxiliary_graph_type": ["bipartite_graph"], "invariants": ["local_color_balance"], "standard_idea_ids": ["alternating_paths"], "local_score": 13},
        ["eulerian_graphs", "coloring", "olympiad_tool"],
    ),
    card(
        "imo-1989-sl14-seven-points-triangle-cover",
        "Минимум отрезков, пересекающих каждую тройку точек, IMO Shortlist 1989",
        "src-kalva-imo-1989-shortlist",
        "Даны 7 точек. Сколько отрезков, соединяющих пары точек, нужно провести, чтобы среди любых трёх точек хотя бы две были соединены отрезком?",
        "Это задача о минимальном числе рёбер в графе на 7 вершинах с числом независимости не больше 2.",
        [
            idea("idea-complement-triangle-free", "Перейти к дополнению", "Если каждая тройка содержит ребро, то в дополнении нет треугольника.", ["extremal_graph_theory"]),
            idea("idea-mantel-seven", "Оценка Мантеля", "Треугольник-свободный граф на 7 вершинах имеет не больше floor(7^2/4)=12 рёбер.", ["extremal_graph_theory"]),
        ],
        "Пусть проведённые отрезки — рёбра графа G на 7 вершинах. Условие означает, что в G нет независимой тройки. В дополнении H это значит, что H не содержит треугольников. По теореме Мантеля e(H)≤floor(7^2/4)=12, поэтому e(G)≥21-12=9. Достижимость: взять H=K_{3,4}; тогда дополнение состоит из двух клик K_3 и K_4 и имеет 3+6=9 рёбер. В любой тройке вершин дополнения K_{3,4} не может быть треугольника, значит в исходном графе каждая тройка содержит ребро.",
        {"objects": ["graph", "independence_number", "complement_graph", "triangle_free_graph"], "methods": ["complement_graph", "mantel_theorem", "extremal_construction"], "transformations": ["segments_to_graph_edges"], "goal": ["minimum_edges"], "auxiliary_graph_type": [], "invariants": ["alpha_at_most_two"], "standard_idea_ids": ["complement_graph_transition"], "local_score": 9},
        ["extremal_graph_theory", "forbidden_triangle", "olympiad_tool"],
        "secondary_shortlist_statement",
    ),
    card(
        "imo-1991-sl9-min-degree-for-k6",
        "Минимальная степень, гарантирующая K6, IMO Shortlist 1991",
        "src-kalva-imo-1991-shortlist",
        "В графе 1991 вершина, степень каждой вершины не меньше 1593. Докажите, что найдутся шесть попарно соединённых вершин. Является ли 1593 наилучшей возможной границей?",
        "Это прямое применение экстремальной теории графов: большая минимальная степень должна породить клику K_6.",
        [
            idea("idea-turan-min-degree", "Порог Турана через пятидольный граф", "Граф без K_6 сравнивается с полным 5-дольным графом.", ["extremal_graph_theory"]),
            idea("idea-balanced-construction", "Точность границы", "Полный 5-дольный граф с частями 399,398,398,398,398 имеет минимальную степень 1592 и не содержит K_6.", ["symmetrization"]),
        ],
        "Если граф не содержит K_6, то по теореме Турана его плотность не превосходит плотность полного 5-дольного графа. В минимально-степенной форме удобно рассуждать так: в K_6-свободном экстремальном графе можно симметризовать несмежные вершины и прийти к полному 5-дольному графу; при 1991 вершине одна часть имеет размер не меньше ceil(1991/5)=399, поэтому в таком графе есть вершина степени не больше 1991-399=1592. Значит δ≥1593 гарантирует K_6. Граница точна: полный 5-дольный граф с размерами 399,398,398,398,398 имеет минимальную степень 1592 и не содержит шести попарно смежных вершин.",
        {"objects": ["graph", "minimum_degree", "clique", "turan_graph"], "methods": ["turan_theorem", "symmetrization", "extremal_construction"], "transformations": [], "goal": ["force_clique_k6"], "auxiliary_graph_type": [], "invariants": ["minimum_degree"], "standard_idea_ids": ["symmetrization"], "local_score": 11},
        ["extremal_graph_theory", "forbidden_clique", "symmetrization", "olympiad_tool"],
        "secondary_shortlist_statement",
    ),
    card(
        "imo-1991-p4-connected-graph-gcd-edge-labels",
        "Разметка рёбер связного графа взаимно простыми метками, IMO 1991 P4",
        "src-imomath-imo-1991",
        "Пусть G — связный граф с n рёбрами. Докажите, что можно пометить рёбра числами 1,2,...,n так, чтобы в каждой вершине степени хотя бы 2 у меток инцидентных ей рёбер не было общего делителя больше 1.",
        "Это задача о специальной нумерации рёбер связного графа; решение использует остовное дерево и размещение меток так, чтобы в каждой нелистовой вершине появлялись взаимно простые инцидентные числа.",
        [
            idea("idea-spanning-tree-reduction", "Свести к остовному дереву", "Достаточно контролировать метки на рёбрах остовного дерева; остальные рёбра можно пронумеровать после этого.", ["trees"]),
            idea("idea-label-by-prime-obstruction", "Разрушить общий делитель", "У каждой вершины степени хотя бы 2 надо обеспечить две инцидентные метки с НОД 1.", ["extremal_choice"]),
        ],
        "Берём остовное дерево T графа G. Рёбра вне T получают часть меток произвольно; они не мешают, потому что добавляют новые инцидентные метки. Дальше нумеруем рёбра дерева от листьев к корню так, чтобы у каждой внутренней вершины среди инцидентных рёбер оказалась пара меток без общего простого делителя; это делается жадно, используя соседние свободные числа и то, что одно ребро ведёт к родителю, а остальные уже можно упорядочить в поддеревьях. В стандартном решении эту идею оформляют через удаление листьев/индукцию по дереву: после возврата удалённого листового блока выбирают метку, взаимно простую с уже закреплённой меткой у его опорной вершины. Поэтому ни в одной вершине степени хотя бы 2 общий делитель всех инцидентных меток не превосходит 1.",
        {"objects": ["connected_graph", "edge_labeling", "spanning_tree"], "methods": ["spanning_tree", "induction", "greedy_labeling"], "transformations": ["connected_graph_to_spanning_tree"], "goal": ["edge_label_gcd_condition"], "auxiliary_graph_type": ["tree"], "invariants": ["connectedness"], "standard_idea_ids": ["induction", "delete_to_simplify"], "local_score": 14},
        ["trees", "induction", "extremal_choice", "olympiad_tool"],
    ),
    card(
        "imo-1992-p3-nine-points-partial-ramsey",
        "Девять точек и минимальное число окрашенных рёбер, IMO 1992 P3",
        "src-imomath-imo-1992",
        "Даны 9 точек в пространстве, никакие 4 не компланарны. Найдите минимальное n такое, что при любой красно-синей раскраске n проведённых между этими точками отрезков обязательно существует одноцветный треугольник.",
        "Геометрия несущественна: это задача о максимальном числе рёбер в подграфе K_9, допускающем 2-раскраску рёбер без одноцветного треугольника.",
        [
            idea("idea-ramsey-subgraph", "Частичная Ramsey-задача", "Нужно найти максимум рёбер графа, который можно разложить на два треугольник-свободных цветовых графа.", ["ramsey_theory"]),
            idea("idea-five-cycle-blowup", "Конструкция без одноцветного треугольника", "Экстремальный пример получается как blow-up 5-цикла с подходящими размерами долей.", ["extremal_graph_theory"]),
        ],
        "Ответ: 33. Нижний пример на 32 рёбрах строится из 5-цикловой Ramsey-раскраски K_5 без одноцветных треугольников, заменяя вершины на группы размеров 2,2,2,2,1 и раскрашивая междолевые рёбра по цвету соответствующего ребра C_5/дополнения, а внутри больших долей оставляя только безопасные рёбра. Для верхней оценки рассматривают красный и синий треугольник-свободные графы на 9 вершинах, покрывающие все окрашенные рёбра. Усиленная форма оценки Мантеля для пары таких графов даёт не более 32 рёбер без одноцветного треугольника; значит при 33 окрашенных рёбрах одноцветный треугольник неизбежен.",
        {"objects": ["complete_graph", "partial_edge_coloring", "monochromatic_triangle"], "methods": ["ramsey_theory", "extremal_graph_theory", "construction"], "transformations": ["segments_to_edges_of_k9"], "goal": ["minimum_edges_for_monochromatic_triangle"], "auxiliary_graph_type": [], "invariants": ["triangle_free_color_classes"], "standard_idea_ids": ["complement_graph_transition"], "local_score": 13},
        ["ramsey_theory", "coloring", "extremal_graph_theory", "olympiad_tool"],
    ),
    card(
        "imo-1997-p4-silver-matrix-factorization-graph",
        "Серебряные матрицы и 1-факторизации, IMO 1997 P4",
        "src-imomath-imo-1997",
        "Матрица n x n с элементами из {1,2,...,2n-1} называется серебряной, если для каждого i объединение i-й строки и i-го столбца содержит все 2n-1 чисел. Докажите, что серебряных матриц нет при n=1997, и что они существуют для бесконечно многих n.",
        "Для каждого символа рассматриваются позиции его появлений как рёбра/петли на множестве индексов строк-столбцов; условие серебряности переводится в разложение полного графа с петлями на специальные паросочетания.",
        [
            idea("idea-symbol-as-matching", "Один символ задаёт matching", "Если число стоит в клетке (i,j), оно покрывает вершины i и j; для каждого i каждый символ должен появиться в i-й строке или столбце ровно один раз.", ["matching"]),
            idea("idea-parity-obstruction", "Нечётный порядок даёт препятствие", "При n=1997 требуемое покрытие сводится к невозможной 1-факторизации нечётной структуры.", ["extremal_choice"]),
            idea("idea-even-construction", "Конструкция через циклическую таблицу", "Для бесконечно многих n строится регулярное разложение по модулю n или по конечной группе.", ["graph_symmetry"]),
        ],
        "Свяжем с каждым числом a множество клеток, где оно стоит. Клетка (i,j) покрывает индексы i и j; условие, что в i-й строке и i-м столбце вместе встречаются все 2n-1 чисел, означает, что для каждого a его клетки покрывают каждый индекс ровно один раз. Поэтому каждый символ задаёт 1-фактороподобную структуру на n индексах, где диагональная клетка играет роль петли, а внедиагональная — ребра. Для нечётного n=1997 подсчёт петель/внедиагональных покрытий даёт паритетное противоречие. Для бесконечного семейства n берут n из подходящей чётной/групповой конструкции и заполняют матрицу циклически так, что каждый символ покрывает все индексы ровно один раз.",
        {"objects": ["matrix", "matching", "one_factorization", "edge_coloring"], "methods": ["matching_model", "parity", "cyclic_construction"], "transformations": ["matrix_symbols_to_matchings"], "goal": ["existence_and_nonexistence"], "auxiliary_graph_type": ["complete_graph_with_loops"], "invariants": ["vertex_coverage"], "standard_idea_ids": [], "local_score": 14},
        ["matching", "coloring", "graph_symmetry", "olympiad_tool"],
    ),
]


SOURCE_IDS = {
    "imo-1964-p4": "imo-1964-p4-three-topic-ramsey",
    "imo-1979-p6": "imo-1979-p6-octagon-walks-cycle-graph",
    "imo-1985-sl-kalva-5": "imo-1985-sl5-lattice-perfect-code",
    "imo-1986-sl-kalva-12": "imo-1986-sl12-increasing-edge-trail",
    "imo-1986-p6": "imo-1986-p6-axis-line-balanced-coloring",
    "imo-1989-sl-kalva-14": "imo-1989-sl14-seven-points-triangle-cover",
    "imo-1991-sl-kalva-9": "imo-1991-sl9-min-degree-for-k6",
    "imo-1991-p4": "imo-1991-p4-connected-graph-gcd-edge-labels",
    "imo-1992-p3": "imo-1992-p3-nine-points-partial-ramsey",
    "imo-1997-p4": "imo-1997-p4-silver-matrix-factorization-graph",
}


def write_cards() -> None:
    for item in CARDS:
        dump(DATA / "problems" / "imo" / f"{item['id']}.yaml", item)


def write_batch() -> None:
    extract = json.loads((DATA / "import_batches" / "extracted" / "imo_remaining_combinatorics" / "imo-remaining-combinatorics-all.json").read_text(encoding="utf-8"))
    items = []
    for rec in extract["problems"]:
        rid = rec["id"]
        if rid in SOURCE_IDS:
            items.append(
                {
                    "id": rid,
                    "status": "added",
                    "problem_id": SOURCE_IDS[rid],
                    "source_ids": [rec["source"]["source_id"]],
                    "decision_reason": "Графовая модель существенна в условии и в стандартном/compendium-style решении; карточка создана.",
                }
            )
    dump(
        DATA / "import_batches" / "imo-remaining-graph-curation.yaml",
        {
            "id": "imo-remaining-graph-curation",
            "title": "Оставшиеся ранние IMO/shortlist: графовый отбор",
            "status": "needs_human_review",
            "created_at": TODAY,
            "updated_at": TODAY,
            "source_scope": {
                "source_ids": sorted({sid for item in items for sid in item["source_ids"]}),
                "notes": [
                    "Использованы Kalva early shortlist pages для shortlist-лет и IMOmath PDFs для настоящих IMO.",
                    "В батч включены только задачи, по которым создана карточка.",
                ],
            },
            "scope": "Graph-significant cards from remaining early IMO/shortlist combinatorics extraction.",
            "items": items,
        },
    )


def main() -> int:
    ensure_sources()
    write_cards()
    write_batch()
    print(f"wrote {len(CARDS)} remaining graph cards")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
