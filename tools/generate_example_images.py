import math
import struct
import zlib
from pathlib import Path

from lib import ROOT


ASSETS = ROOT / "data" / "assets" / "examples"

BG = (248, 246, 240)
WHITE = (255, 255, 255)
INK = (37, 50, 56)
MUTED = (110, 120, 126)
LINE = (214, 210, 201)
RED = (199, 62, 29)
BLUE = (27, 99, 187)
GREEN = (50, 125, 91)
ORANGE = (219, 136, 37)
GRAY = (183, 186, 190)
GOLD = (217, 180, 74)
PALE_YELLOW = (255, 249, 176)
PALE_BLUE = (196, 238, 242)
LIGHT_BLUE = (222, 248, 249)
PINK = (247, 154, 154)
DARK_RED = (142, 30, 30)
MAGENTA = (228, 58, 180)
PURPLE = (122, 64, 219)


class Canvas:
    def __init__(self, width, height, bg=BG):
        self.width = width
        self.height = height
        self.pixels = [[bg for _ in range(width)] for _ in range(height)]

    def set_pixel(self, x, y, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.pixels[y][x] = color

    def fill_rect(self, x0, y0, x1, y1, color):
        xa, xb = sorted((int(x0), int(x1)))
        ya, yb = sorted((int(y0), int(y1)))
        for y in range(ya, yb):
            for x in range(xa, xb):
                self.set_pixel(x, y, color)

    def stroke_rect(self, x0, y0, x1, y1, color, thickness=1):
        self.fill_rect(x0, y0, x1, y0 + thickness, color)
        self.fill_rect(x0, y1 - thickness, x1, y1, color)
        self.fill_rect(x0, y0, x0 + thickness, y1, color)
        self.fill_rect(x1 - thickness, y0, x1, y1, color)

    def fill_circle(self, cx, cy, radius, color):
        r2 = radius * radius
        for y in range(int(cy - radius), int(cy + radius) + 1):
            for x in range(int(cx - radius), int(cx + radius) + 1):
                if (x - cx) ** 2 + (y - cy) ** 2 <= r2:
                    self.set_pixel(x, y, color)

    def stroke_circle(self, cx, cy, radius, color, thickness=1):
        outer = radius * radius
        inner = max(radius - thickness, 0) ** 2
        for y in range(int(cy - radius), int(cy + radius) + 1):
            for x in range(int(cx - radius), int(cx + radius) + 1):
                d2 = (x - cx) ** 2 + (y - cy) ** 2
                if inner <= d2 <= outer:
                    self.set_pixel(x, y, color)

    def line(self, x0, y0, x1, y1, color, thickness=1):
        x0, y0, x1, y1 = map(int, (x0, y0, x1, y1))
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy
        while True:
            self.fill_circle(x0, y0, thickness // 2, color)
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy

    def polyline(self, points, color, thickness=1):
        for a, b in zip(points, points[1:]):
            self.line(a[0], a[1], b[0], b[1], color, thickness)

    def save_png(self, path):
        path.parent.mkdir(parents=True, exist_ok=True)
        rows = []
        for row in self.pixels:
            raw = bytearray([0])
            for r, g, b in row:
                raw.extend((r, g, b))
            rows.append(bytes(raw))
        data = zlib.compress(b"".join(rows), level=9)

        def chunk(tag, payload):
            return (
                struct.pack("!I", len(payload))
                + tag
                + payload
                + struct.pack("!I", zlib.crc32(tag + payload) & 0xFFFFFFFF)
            )

        png = [
            b"\x89PNG\r\n\x1a\n",
            chunk(b"IHDR", struct.pack("!IIBBBBB", self.width, self.height, 8, 2, 0, 0, 0)),
            chunk(b"IDAT", data),
            chunk(b"IEND", b""),
        ]
        path.write_bytes(b"".join(png))


def draw_panel_background(canvas, x0, y0, x1, y1):
    canvas.fill_rect(x0, y0, x1, y1, WHITE)
    canvas.stroke_rect(x0, y0, x1, y1, LINE, thickness=2)


def circle_point(cx, cy, radius, angle_deg):
    ang = math.radians(angle_deg)
    return (cx + radius * math.cos(ang), cy + radius * math.sin(ang))


def chord_panel(canvas, box, angles_a, angles_b):
    x0, y0, x1, y1 = box
    draw_panel_background(canvas, x0, y0, x1, y1)
    cx = (x0 + x1) / 2
    cy = (y0 + y1) / 2
    radius = min(x1 - x0, y1 - y0) * 0.33
    canvas.stroke_circle(cx, cy, radius, MUTED, thickness=3)
    pts_a = [circle_point(cx, cy, radius, ang) for ang in angles_a]
    pts_b = [circle_point(cx, cy, radius, ang) for ang in angles_b]
    canvas.line(*pts_a[0], *pts_a[1], RED, thickness=5)
    canvas.line(*pts_b[0], *pts_b[1], BLUE, thickness=5)
    for pt in pts_a + pts_b:
        canvas.fill_circle(pt[0], pt[1], 7, WHITE)
        canvas.stroke_circle(pt[0], pt[1], 7, INK, thickness=2)


def generate_chord_types():
    canvas = Canvas(1080, 360)
    margin = 30
    gap = 24
    width = (canvas.width - 2 * margin - 2 * gap) // 3
    boxes = []
    for i in range(3):
        x0 = margin + i * (width + gap)
        boxes.append((x0, 30, x0 + width, 330))
    chord_panel(canvas, boxes[0], (145, 35), (170, 10))
    chord_panel(canvas, boxes[1], (150, 20), (110, -60))
    chord_panel(canvas, boxes[2], (160, 120), (30, -10))
    canvas.save_png(ASSETS / "imo-2024-c3" / "chord-types.png")


def add_node(canvas, pos, color=WHITE, radius=12):
    canvas.fill_circle(pos[0], pos[1], radius, color)
    canvas.stroke_circle(pos[0], pos[1], radius, INK, thickness=2)


def generate_ferry_operation():
    canvas = Canvas(1000, 420)
    left = (40, 40, 450, 380)
    right = (550, 40, 960, 380)
    draw_panel_background(canvas, *left)
    draw_panel_background(canvas, *right)

    before = {
        "x": (180, 190),
        "y": (310, 190),
        "a": (110, 110),
        "b": (110, 270),
        "c": (380, 110),
        "d": (380, 270),
        "e": (245, 80),
    }
    after = {
        "x": (690, 190),
        "y": (820, 190),
        "a": (620, 110),
        "b": (620, 270),
        "c": (890, 110),
        "d": (890, 270),
        "e": (755, 80),
    }

    edges_before = [("x", "y"), ("x", "a"), ("x", "b"), ("y", "c"), ("y", "d"), ("x", "e"), ("y", "e")]
    edges_after = [("y", "a"), ("y", "b"), ("x", "c"), ("x", "d"), ("x", "e"), ("y", "e")]

    for a, b in edges_before:
        canvas.line(*before[a], *before[b], BLUE if {a, b} == {"x", "y"} else MUTED, thickness=4)
    for a, b in edges_after:
        canvas.line(*after[a], *after[b], GREEN if {a, b} != {"x", "e"} and {a, b} != {"y", "e"} else MUTED, thickness=4)

    for name, pos in before.items():
        add_node(canvas, pos, GOLD if name in {"x", "y"} else WHITE)
    for name, pos in after.items():
        add_node(canvas, pos, GOLD if name in {"x", "y"} else WHITE)

    canvas.line(470, 210, 530, 210, ORANGE, thickness=5)
    canvas.line(530, 210, 515, 200, ORANGE, thickness=5)
    canvas.line(530, 210, 515, 220, ORANGE, thickness=5)
    canvas.save_png(ASSETS / "imo-2016-c6" / "ferry-operation-before-after.png")


def generate_reachability_board():
    canvas = Canvas(720, 720)
    draw_panel_background(canvas, 40, 40, 680, 680)
    x0, y0, cell = 120, 120, 110
    palette = [
        [GREEN, BLUE, ORANGE, GRAY],
        [BLUE, GREEN, ORANGE, GRAY],
        [GREEN, GREEN, ORANGE, GRAY],
        [BLUE, GREEN, ORANGE, GRAY],
    ]
    for row in range(4):
        for col in range(4):
            x = x0 + col * cell
            y = y0 + row * cell
            canvas.fill_rect(x, y, x + cell - 6, y + cell - 6, palette[row][col])
            canvas.stroke_rect(x, y, x + cell - 6, y + cell - 6, WHITE, thickness=3)
    canvas.stroke_rect(x0 + 2 * cell - 6, y0 + cell, x0 + 4 * cell - 6, y0 + 2 * cell - 6, RED, thickness=8)
    canvas.stroke_rect(x0 + 2 * cell - 6, y0 + 2 * cell, x0 + 4 * cell - 6, y0 + 3 * cell - 6, LINE, thickness=2)
    canvas.save_png(ASSETS / "memo-2022-t4" / "reachability-classes-board.png")


def generate_forest_growth():
    canvas = Canvas(960, 360)
    margin = 30
    gap = 18
    width = (canvas.width - 2 * margin - 2 * gap) // 3
    panels = []
    for i in range(3):
        x0 = margin + i * (width + gap)
        panels.append((x0, 30, x0 + width, 330))

    layouts = [
        [(90, 100), (160, 220), (250, 100), (90, 260), (250, 260)],
        [(90, 100), (160, 220), (250, 100), (90, 260), (250, 260)],
        [(90, 100), (160, 220), (250, 100), (90, 260), (250, 260)],
    ]
    edge_sets = [
        [(0, 1)],
        [(0, 1), (2, 4)],
        [(0, 1), (2, 4), (1, 2)],
    ]
    for panel, positions, edges in zip(panels, layouts, edge_sets):
        draw_panel_background(canvas, *panel)
        ox, oy = panel[0] + 20, panel[1] + 20
        translated = [(ox + x, oy + y) for x, y in positions]
        for a, b in edges:
            canvas.line(*translated[a], *translated[b], GREEN, thickness=5)
        for pos in translated:
            add_node(canvas, pos)
    canvas.save_png(ASSETS / "tc-2023-24" / "comparison-forest-growth.png")


def generate_incidence_example():
    canvas = Canvas(1100, 480)
    left = (30, 30, 510, 450)
    right = (590, 30, 1070, 450)
    draw_panel_background(canvas, *left)
    draw_panel_background(canvas, *right)

    x0, y0, cell = 90, 80, 82
    blue_cells = {(0, 0), (0, 2), (1, 1), (2, 0), (2, 3), (3, 2)}
    for row in range(4):
        for col in range(4):
            x = x0 + col * cell
            y = y0 + row * cell
            color = BLUE if (row, col) in blue_cells else WHITE
            canvas.fill_rect(x, y, x + cell - 4, y + cell - 4, color)
            canvas.stroke_rect(x, y, x + cell - 4, y + cell - 4, LINE, thickness=2)

    row_nodes = [(670, 100), (670, 180), (670, 260), (670, 340)]
    col_nodes = [(980, 100), (980, 180), (980, 260), (980, 340)]
    for row, col in blue_cells:
        canvas.line(*row_nodes[row], *col_nodes[col], MUTED, thickness=4)
    for pos in row_nodes:
        add_node(canvas, pos, GREEN)
    for pos in col_nodes:
        add_node(canvas, pos, ORANGE)
    canvas.save_png(ASSETS / "egmo-2016-p3" / "grid-to-incidence-graph.png")


def arrow(canvas, x0, y0, x1, y1, color, thickness=3):
    canvas.line(x0, y0, x1, y1, color, thickness=thickness)
    dx = x1 - x0
    dy = y1 - y0
    length = max((dx * dx + dy * dy) ** 0.5, 1)
    ux, uy = dx / length, dy / length
    px, py = -uy, ux
    size = 12
    back = 18
    left = (x1 - back * ux + size * px, y1 - back * uy + size * py)
    right = (x1 - back * ux - size * px, y1 - back * uy - size * py)
    canvas.line(x1, y1, left[0], left[1], color, thickness=thickness)
    canvas.line(x1, y1, right[0], right[1], color, thickness=thickness)


def special_snake(size, parity_coord):
    cells = []
    for row in range(size, 0, -1):
        if (size - row) % 2 == 0:
            cols = range(1, size + 1)
        else:
            cols = range(size, 0, -1)
        for col in cols:
            cells.append((parity_coord + 2 * (row - 1), parity_coord + 2 * (col - 1)))
    return cells


def blue_snake(m):
    return special_snake(m, 2)


def hopcroft_karp(adj):
    unmatched = None
    left = list(adj)
    pair_left = {u: unmatched for u in left}
    pair_right = {}
    dist = {}

    def bfs():
        queue = []
        found = False
        for u in left:
            if pair_left[u] is unmatched:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = 10**9
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            for v in adj[u]:
                pu = pair_right.get(v, unmatched)
                if pu is unmatched:
                    found = True
                elif dist[pu] == 10**9:
                    dist[pu] = dist[u] + 1
                    queue.append(pu)
        return found

    def dfs(u):
        for v in adj[u]:
            pu = pair_right.get(v, unmatched)
            if pu is unmatched or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_left[u] = v
                pair_right[v] = u
                return True
        dist[u] = 10**9
        return False

    while bfs():
        for u in left:
            if pair_left[u] is unmatched:
                dfs(u)
    return pair_left


def match_dark_to_white(n, dark_cells, available_whites):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    adj = {}
    for cell in sorted(dark_cells):
        r, c = cell
        adj[cell] = sorted(
            (r + dr, c + dc)
            for dr, dc in dirs
            if (r + dr, c + dc) in available_whites
        )
    matching = hopcroft_karp(adj)
    if any(v is None for v in matching.values()):
        raise RuntimeError(f"could not tile remaining cells for n={n}")
    return matching


def blue_small_k_configuration(m, k):
    n = 2 * m + 1
    snake = blue_snake(m)
    used = set()
    dominoes = []

    def midpoint(a, b):
        return ((a[0] + b[0]) // 2, (a[1] + b[1]) // 2)

    for i in range(1, k):
        dark = snake[i]
        target = snake[i - 1]
        white = midpoint(dark, target)
        used.update([dark, white])
        dominoes.append({"dark": dark, "white": white, "target": target, "kind": "blue_prefix"})

    for i in range(k, m * m):
        dark = snake[i]
        if i + 1 < m * m:
            target = snake[i + 1]
            white = midpoint(dark, target)
        else:
            r, c = dark
            if c == 2 * m:
                white = (r, 2 * m + 1)
                target = (r, 2 * m + 2)
            else:
                white = (r, 1)
                target = (r, 0)
        used.update([dark, white])
        dominoes.append({"dark": dark, "white": white, "target": target, "kind": "blue_suffix"})

    red = {(r, c) for r in range(1, n + 1, 2) for c in range(1, n + 1, 2)}
    blue = {(r, c) for r in range(2, n + 1, 2) for c in range(2, n + 1, 2)}
    white = {
        (r, c)
        for r in range(1, n + 1)
        for c in range(1, n + 1)
        if (r, c) not in red and (r, c) not in blue
    }
    matching = match_dark_to_white(n, red, white - used)
    for dark, white_cell in matching.items():
        dominoes.append({"dark": dark, "white": white_cell, "target": None, "kind": "red"})
    return n, snake[0], dominoes


def red_spanning_configuration(m):
    n = 2 * m + 1
    snake = special_snake(m + 1, 1)
    used = set()
    dominoes = []

    def midpoint(a, b):
        return ((a[0] + b[0]) // 2, (a[1] + b[1]) // 2)

    for i in range(1, len(snake)):
        dark = snake[i]
        target = snake[i - 1]
        white = midpoint(dark, target)
        used.update([dark, white])
        dominoes.append({"dark": dark, "white": white, "target": target, "kind": "red_prefix"})

    blue = {(r, c) for r in range(2, n + 1, 2) for c in range(2, n + 1, 2)}
    red = {(r, c) for r in range(1, n + 1, 2) for c in range(1, n + 1, 2)}
    white = {
        (r, c)
        for r in range(1, n + 1)
        for c in range(1, n + 1)
        if (r, c) not in red and (r, c) not in blue
    }
    matching = match_dark_to_white(n, blue, white - used)
    for dark, white_cell in matching.items():
        dominoes.append({"dark": dark, "white": white_cell, "target": None, "kind": "blue_fill"})
    return n, snake[0], dominoes


def verify_component_size(n, empty, dominoes, parity):
    edges = {}
    vertices = {
        (r, c)
        for r in range(1, n + 1)
        for c in range(1, n + 1)
        if r % 2 == parity and c % 2 == parity
    }
    for domino in dominoes:
        dark = domino["dark"]
        target = domino["target"]
        if dark in vertices and target in vertices:
            edges.setdefault(dark, set()).add(target)
            edges.setdefault(target, set()).add(dark)
    seen = {empty}
    stack = [empty]
    while stack:
        cell = stack.pop()
        for nxt in edges.get(cell, set()):
            if nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    return len(seen)


def board_geometry(origin_x, origin_y, cell_size):
    def rect(cell):
        r, c = cell
        x0 = origin_x + (c - 1) * cell_size
        y0 = origin_y + (r - 1) * cell_size
        return x0, y0, x0 + cell_size, y0 + cell_size

    def center(cell):
        x0, y0, x1, y1 = rect(cell)
        return (x0 + x1) / 2, (y0 + y1) / 2

    return rect, center


def draw_domino_board(canvas, n, empty, dominoes, origin_x, origin_y, cell_size, show_suffix_arrows=True):
    rect, center = board_geometry(origin_x, origin_y, cell_size)
    canvas.fill_rect(origin_x, origin_y, origin_x + n * cell_size, origin_y + n * cell_size, PALE_YELLOW)

    color_for = {
        "blue_prefix": PALE_BLUE,
        "blue_suffix": LIGHT_BLUE,
        "red": PINK,
        "red_prefix": PINK,
        "blue_fill": LIGHT_BLUE,
    }
    for domino in dominoes:
        a = domino["dark"]
        b = domino["white"]
        ax0, ay0, ax1, ay1 = rect(a)
        bx0, by0, bx1, by1 = rect(b)
        x0, y0 = min(ax0, bx0) + 2, min(ay0, by0) + 2
        x1, y1 = max(ax1, bx1) - 2, max(ay1, by1) - 2
        canvas.fill_rect(x0, y0, x1, y1, color_for.get(domino["kind"], WHITE))
        canvas.stroke_rect(x0, y0, x1, y1, INK, thickness=1)

    ex0, ey0, ex1, ey1 = rect(empty)
    canvas.fill_rect(ex0 + 3, ey0 + 3, ex1 - 3, ey1 - 3, GRAY)
    canvas.stroke_rect(ex0 + 3, ey0 + 3, ex1 - 3, ey1 - 3, INK, thickness=1)

    for i in range(n + 1):
        x = origin_x + i * cell_size
        y = origin_y + i * cell_size
        canvas.line(x, origin_y, x, origin_y + n * cell_size, LINE, thickness=1)
        canvas.line(origin_x, y, origin_x + n * cell_size, y, LINE, thickness=1)
    canvas.stroke_rect(origin_x, origin_y, origin_x + n * cell_size, origin_y + n * cell_size, INK, thickness=2)

    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if r % 2 == c % 2:
                cx, cy = center((r, c))
                canvas.fill_circle(cx, cy, max(2, cell_size // 9), INK)

    for domino in dominoes:
        target = domino["target"]
        if target is None:
            continue
        if domino["kind"] == "blue_suffix" and not show_suffix_arrows:
            continue
        x0, y0 = center(domino["dark"])
        if 1 <= target[0] <= n and 1 <= target[1] <= n:
            x1, y1 = center(target)
        else:
            x1 = origin_x + (target[1] - 0.5) * cell_size
            y1 = origin_y + (target[0] - 0.5) * cell_size
        color = INK if domino["kind"] in {"blue_prefix", "red_prefix"} else MUTED
        arrow(canvas, x0, y0, x1, y1, color, thickness=max(2, cell_size // 16))


def generate_usamo_2023_p3_small_k_boards():
    m = 3
    n = 2 * m + 1
    cell = 34
    panel = n * cell + 24
    canvas = Canvas(3 * panel + 40, 3 * panel + 40)
    for idx, k in enumerate(range(m * m, 0, -1)):
        row = idx // 3
        col = idx % 3
        ox = 20 + col * panel + 12
        oy = 20 + row * panel + 12
        n, empty, dominoes = blue_small_k_configuration(m, k)
        size = verify_component_size(n, empty, dominoes, 0)
        if size != k:
            raise RuntimeError(f"blue component size {size} != {k}")
        draw_panel_background(canvas, ox - 8, oy - 8, ox + n * cell + 8, oy + n * cell + 8)
        draw_domino_board(canvas, n, empty, dominoes, ox, oy, cell)
    canvas.save_png(ASSETS / "usamo-2023-p3" / "n7-small-k-blue-snake.png")


def generate_usamo_2023_p3_cut_schematic():
    m = 5
    n = 2 * m + 1
    k = 13
    cell = 44
    canvas = Canvas(620, 560)
    ox, oy = 70, 35
    n, empty, dominoes = blue_small_k_configuration(m, k)
    if verify_component_size(n, empty, dominoes, 0) != k:
        raise RuntimeError("schematic blue component check failed")
    draw_domino_board(canvas, n, empty, dominoes, ox, oy, cell, show_suffix_arrows=False)
    rect, center = board_geometry(ox, oy, cell)
    snake = blue_snake(m)
    cut_a = snake[k - 1]
    cut_b = snake[k]
    cut = ((cut_a[0] + cut_b[0]) // 2, (cut_a[1] + cut_b[1]) // 2)
    cx, cy = center(cut)
    canvas.stroke_circle(cx, cy, cell * 0.33, RED, thickness=5)
    for cell_index, special in enumerate(snake):
        sx, sy = center(special)
        color = BLUE if cell_index < k else MUTED
        canvas.stroke_circle(sx, sy, 10, color, thickness=3)
    canvas.save_png(ASSETS / "usamo-2023-p3" / "blue-snake-cut-schematic.png")


def generate_usamo_2023_p3_red_spanning():
    m = 3
    cell = 54
    canvas = Canvas(470, 470)
    n, empty, dominoes = red_spanning_configuration(m)
    size = verify_component_size(n, empty, dominoes, 1)
    if size != (m + 1) * (m + 1):
        raise RuntimeError(f"red component size {size}")
    draw_panel_background(canvas, 35, 35, 435, 435)
    draw_domino_board(canvas, n, empty, dominoes, 46, 46, cell)
    canvas.save_png(ASSETS / "usamo-2023-p3" / "n7-red-spanning-snake.png")


def verify_usamo_2023_p3_samples():
    for m in range(1, 10):
        for k in range(1, m * m + 1):
            n, empty, dominoes = blue_small_k_configuration(m, k)
            if verify_component_size(n, empty, dominoes, 0) != k:
                raise RuntimeError(f"blue snake verification failed for m={m}, k={k}")
        n, empty, dominoes = red_spanning_configuration(m)
        expected = (m + 1) * (m + 1)
        if verify_component_size(n, empty, dominoes, 1) != expected:
            raise RuntimeError(f"red snake verification failed for m={m}")


def main():
    generate_chord_types()
    generate_ferry_operation()
    generate_reachability_board()
    generate_forest_growth()
    generate_incidence_example()
    verify_usamo_2023_p3_samples()
    generate_usamo_2023_p3_small_k_boards()
    generate_usamo_2023_p3_cut_schematic()
    generate_usamo_2023_p3_red_spanning()
    print(f"Generated example images under {ASSETS}")


if __name__ == "__main__":
    main()
