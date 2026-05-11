# shapes_data.py
import math
from constants import *

# ─────────────────────────────────────────────
#  SHAPE DATA
# ─────────────────────────────────────────────
SHAPES = {
    "Area": {
        "Circle": {
            "fields":  [("Radius (r)", "r")],
            "formula": "A = \u03c0 \u00d7 r\u00b2",
            "calc":    lambda v: math.pi * v["r"] ** 2,
            "svg":     "circle",
        },
        "Rectangle": {
            "fields":  [("Length (l)", "l"), ("Width (w)", "w")],
            "formula": "A = l \u00d7 w",
            "calc":    lambda v: v["l"] * v["w"],
            "svg":     "rectangle",
        },
        "Triangle": {
            "fields":  [("Base (b)", "b"), ("Height (h)", "h")],
            "formula": "A = \u00bd \u00d7 b \u00d7 h",
            "calc":    lambda v: 0.5 * v["b"] * v["h"],
            "svg":     "triangle",
        },
        "Square": {
            "fields":  [("Side (s)", "s")],
            "formula": "A = s\u00b2",
            "calc":    lambda v: v["s"] ** 2,
            "svg":     "square",
        },
        "Trapezoid": {
            "fields":  [("Base 1 (a)", "a"), ("Base 2 (b)", "b"), ("Height (h)", "h")],
            "formula": "A = \u00bd \u00d7 (a + b) \u00d7 h",
            "calc":    lambda v: 0.5 * (v["a"] + v["b"]) * v["h"],
            "svg":     "trapezoid",
        },
        "Parallelogram": {
            "fields":  [("Base (b)", "b"), ("Height (h)", "h")],
            "formula": "A = b \u00d7 h",
            "calc":    lambda v: v["b"] * v["h"],
            "svg":     "parallelogram",
        },
    },
    "Perimeter": {
        "Circle (Circumference)": {
            "fields":  [("Radius (r)", "r")],
            "formula": "C = 2 \u00d7 \u03c0 \u00d7 r",
            "calc":    lambda v: 2 * math.pi * v["r"],
            "svg":     "circle",
        },
        "Rectangle": {
            "fields":  [("Length (l)", "l"), ("Width (w)", "w")],
            "formula": "P = 2 \u00d7 (l + w)",
            "calc":    lambda v: 2 * (v["l"] + v["w"]),
            "svg":     "rectangle",
        },
        "Triangle": {
            "fields":  [("Side a", "a"), ("Side b", "b"), ("Side c", "c")],
            "formula": "P = a + b + c",
            "calc":    lambda v: v["a"] + v["b"] + v["c"],
            "svg":     "triangle",
        },
        "Square": {
            "fields":  [("Side (s)", "s")],
            "formula": "P = 4 \u00d7 s",
            "calc":    lambda v: 4 * v["s"],
            "svg":     "square",
        },
    },
    "Volume": {
        "Cube": {
            "fields":  [("Side (s)", "s")],
            "formula": "V = s\u00b3",
            "calc":    lambda v: v["s"] ** 3,
            "svg":     "cube",
        },
        "Rectangular Prism": {
            "fields":  [("Length (l)", "l"), ("Width (w)", "w"), ("Height (h)", "h")],
            "formula": "V = l \u00d7 w \u00d7 h",
            "calc":    lambda v: v["l"] * v["w"] * v["h"],
            "svg":     "rect_prism",
        },
        "Sphere": {
            "fields":  [("Radius (r)", "r")],
            "formula": "V = (4/3) \u00d7 \u03c0 \u00d7 r\u00b3",
            "calc":    lambda v: (4 / 3) * math.pi * v["r"] ** 3,
            "svg":     "sphere",
        },
        "Cylinder": {
            "fields":  [("Radius (r)", "r"), ("Height (h)", "h")],
            "formula": "V = \u03c0 \u00d7 r\u00b2 \u00d7 h",
            "calc":    lambda v: math.pi * v["r"] ** 2 * v["h"],
            "svg":     "cylinder",
        },
        "Cone": {
            "fields":  [("Radius (r)", "r"), ("Height (h)", "h")],
            "formula": "V = (1/3) \u00d7 \u03c0 \u00d7 r\u00b2 \u00d7 h",
            "calc":    lambda v: (1 / 3) * math.pi * v["r"] ** 2 * v["h"],
            "svg":     "cone",
        },
        "Triangular Prism": {
            "fields":  [("Base (b)", "b"), ("Height of triangle (h)", "h"), ("Length (l)", "l")],
            "formula": "V = \u00bd \u00d7 b \u00d7 h \u00d7 l",
            "calc":    lambda v: 0.5 * v["b"] * v["h"] * v["l"],
            "svg":     "tri_prism",
        },
    },
}

# ─────────────────────────────────────────────
#  SHAPE CANVAS DRAWING
# ─────────────────────────────────────────────
def draw_shape(canvas, shape_key):
    canvas.delete("all")
    W, H   = 180, 130
    cx, cy = W // 2, H // 2
    # Fix: Removed invalid alpha value 18 from hex color, using 6-digit hex
    fill   = "#1a3a4a" # Solid variant of previous translucent color
    line   = ACCENT
    lw     = 2

    if shape_key == "circle":
        r = 42
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline=line, width=lw, fill=fill)
        canvas.create_line(cx, cy, cx+r, cy, fill=ACCENT2, width=1, dash=(4, 3))
        canvas.create_text(cx + r//2 + 4, cy - 10, text="r", fill=ACCENT2, font=FONT_SMALL)

    elif shape_key == "rectangle":
        x1, y1, x2, y2 = cx-55, cy-28, cx+55, cy+28
        canvas.create_rectangle(x1, y1, x2, y2, outline=line, width=lw, fill=fill)
        canvas.create_text(cx, y1 - 9, text="l", fill=ACCENT2, font=FONT_SMALL)
        canvas.create_text(x2 + 9, cy, text="w", fill=ACCENT2, font=FONT_SMALL)

    elif shape_key == "square":
        s = 45
        canvas.create_rectangle(cx-s, cy-s, cx+s, cy+s, outline=line, width=lw, fill=fill)
        canvas.create_text(cx, cy-s-9, text="s", fill=ACCENT2, font=FONT_SMALL)

    elif shape_key == "triangle":
        pts = [cx, cy-48, cx-48, cy+40, cx+48, cy+40]
        canvas.create_polygon(pts, outline=line, width=lw, fill=fill)
        canvas.create_text(cx, cy - 58, text="h↕", fill=ACCENT2, font=FONT_SMALL)
        canvas.create_text(cx, cy + 50, text="b",  fill=ACCENT2, font=FONT_SMALL)

    elif shape_key == "trapezoid":
        pts = [cx-30, cy-28, cx+30, cy-28, cx+55, cy+28, cx-55, cy+28]
        canvas.create_polygon(pts, outline=line, width=lw, fill=fill)
        canvas.create_text(cx, cy - 38, text="a", fill=ACCENT2, font=FONT_SMALL)
        canvas.create_text(cx, cy + 38, text="b", fill=ACCENT2, font=FONT_SMALL)

    elif shape_key == "parallelogram":
        pts = [cx-30, cy-28, cx+55, cy-28, cx+30, cy+28, cx-55, cy+28]
        canvas.create_polygon(pts, outline=line, width=lw, fill=fill)
        canvas.create_text(cx, cy + 38, text="b", fill=ACCENT2, font=FONT_SMALL)

    elif shape_key == "cube":
        canvas.create_rectangle(cx-35, cy-15, cx+28, cy+42, outline=line, width=lw, fill=fill)
        pts = [cx-35, cy-15, cx-12, cy-42, cx+50, cy-42, cx+28, cy-15]
        canvas.create_polygon(pts, outline=line, width=lw, fill=fill)
        pts = [cx+28, cy-15, cx+50, cy-42, cx+50, cy+15, cx+28, cy+42]
        canvas.create_polygon(pts, outline=line, width=lw, fill=fill)
        canvas.create_text(cx - 46, cy + 15, text="s", fill=ACCENT2, font=FONT_SMALL)

    elif shape_key == "rect_prism":
        canvas.create_rectangle(cx-40, cy-15, cx+22, cy+38, outline=line, width=lw, fill=fill)
        pts = [cx-40, cy-15, cx-16, cy-40, cx+46, cy-40, cx+22, cy-15]
        canvas.create_polygon(pts, outline=line, width=lw, fill=fill)
        pts = [cx+22, cy-15, cx+46, cy-40, cx+46, cy+14, cx+22, cy+38]
        canvas.create_polygon(pts, outline=line, width=lw, fill=fill)
        canvas.create_text(cx - 5,  cy + 50, text="l",  fill=ACCENT2, font=FONT_SMALL)
        canvas.create_text(cx + 58, cy - 12, text="w",  fill=ACCENT2, font=FONT_SMALL)
        canvas.create_text(cx + 34, cy + 6,  text="h",  fill=ACCENT2, font=FONT_SMALL)

    elif shape_key == "sphere":
        r = 42
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline=line, width=lw, fill=fill)
        canvas.create_oval(cx-r, cy-12, cx+r, cy+12, outline=MUTED, width=1, dash=(3, 3))
        canvas.create_line(cx, cy, cx+r, cy, fill=ACCENT2, width=1, dash=(4, 3))
        canvas.create_text(cx + r//2 + 4, cy - 9, text="r", fill=ACCENT2, font=FONT_SMALL)

    elif shape_key == "cylinder":
        canvas.create_oval(cx-38, cy-42, cx+38, cy-26, outline=line, width=lw, fill=fill)
        canvas.create_oval(cx-38, cy+22, cx+38, cy+38, outline=line, width=lw, fill=fill)
        canvas.create_line(cx-38, cy-34, cx-38, cy+30, fill=line, width=lw)
        canvas.create_line(cx+38, cy-34, cx+38, cy+30, fill=line, width=lw)
        canvas.create_line(cx, cy-34, cx+38, cy-34, fill=ACCENT2, width=1, dash=(4, 3))
        canvas.create_text(cx + 22, cy - 44, text="r", fill=ACCENT2, font=FONT_SMALL)
        canvas.create_text(cx + 46, cy - 4,  text="h", fill=ACCENT2, font=FONT_SMALL)

    elif shape_key == "cone":
      
        # Base (parallelogram in perspective)
        base = [cx-35, cy+20, cx+15, cy+20, cx+40, cy+5, cx-10, cy+5]
        canvas.create_polygon(base, outline=line, width=lw, fill=fill)
        # Left face (triangle)
        left = [cx-35, cy+20, cx-10, cy+5, cx, cy-25]
        canvas.create_polygon(left, outline=line, width=lw, fill=fill)
        # Right face (triangle)
        right = [cx+15, cy+20, cx+40, cy+5, cx, cy-25]
        canvas.create_polygon(right, outline=line, width=lw, fill=fill)
        # Front face (triangle)
        front = [cx-35, cy+20, cx+15, cy+20, cx, cy-25]
        canvas.create_polygon(front, outline=line, width=lw, fill=fill)
        # Height dashed line (apex down to base center)
        canvas.create_line(cx, cy-25, cx-10, cy+12, dash=(3,3), fill=line, width=lw)
        # Labels
        canvas.create_text(cx+5, cy+30, text="b", fill=ACCENT2, font=FONT_SMALL)
        canvas.create_text(cx+2, cy-1, text="h", fill=ACCENT2, font=FONT_SMALL)

    elif shape_key == "tri_prism":
        pts = [cx-40, cy+20, cx+10, cy+20, cx-15, cy-20]
        canvas.create_polygon(pts, outline=line, width=lw, fill=fill)
        pts2 = [cx+10, cy+20, cx+45, cy, cx+20, cy-40, cx-15, cy-20]
        canvas.create_polygon(pts2, outline=line, width=lw, fill=fill)
        canvas.create_text(cx-15, cy+30, text="b", fill=ACCENT2, font=FONT_SMALL)
