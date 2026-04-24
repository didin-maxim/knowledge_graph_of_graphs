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


def main():
    generate_chord_types()
    generate_ferry_operation()
    generate_reachability_board()
    generate_forest_growth()
    generate_incidence_example()
    print(f"Generated example images under {ASSETS}")


if __name__ == "__main__":
    main()
