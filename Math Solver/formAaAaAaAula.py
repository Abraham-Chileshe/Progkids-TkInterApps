import tkinter as tk
from tkinter import messagebox
import math

# ─────────────────────────────────────────────
#  COLORS & FONTS
# ─────────────────────────────────────────────
BG      = "#0f1f2e"
PANEL   = "#162636"
CARD    = "#1e3448"
ACCENT  = "#00c9a7"
ACCENT2 = "#ffd166"
WHITE   = "#e8f1f8"
MUTED   = "#7a9bbf"
RED     = "#ef476f"

FONT_TITLE   = ("Helvetica", 22, "bold")
FONT_HEAD    = ("Helvetica", 13, "bold")
FONT_BODY    = ("Helvetica", 11)
FONT_SMALL   = ("Helvetica", 9)
FONT_RESULT  = ("Courier", 13, "bold")
FONT_FORMULA = ("Courier", 11)

# ─────────────────────────────────────────────
#  SHAPE DATA
# ─────────────────────────────────────────────
SHAPES = {
    "Area": {
        "Circle": {
            "fields":  [("Radius (r)", "r")],
            "formula": "A = π × r²",
            "calc":    lambda v: math.pi * v["r"] ** 2,
            "svg":     "circle",
        },
        "Rectangle": {
            "fields":  [("Length (l)", "l"), ("Width (w)", "w")],
            "formula": "A = l × w",
            "calc":    lambda v: v["l"] * v["w"],
            "svg":     "rectangle",
        },
        "Triangle": {
            "fields":  [("Base (b)", "b"), ("Height (h)", "h")],
            "formula": "A = ½ × b × h",
            "calc":    lambda v: 0.5 * v["b"] * v["h"],
            "svg":     "triangle",
        },
        "Square": {
            "fields":  [("Side (s)", "s")],
            "formula": "A = s²",
            "calc":    lambda v: v["s"] ** 2,
            "svg":     "square",
        },
        "Trapezoid": {
            "fields":  [("Base 1 (a)", "a"), ("Base 2 (b)", "b"), ("Height (h)", "h")],
            "formula": "A = ½ × (a + b) × h",
            "calc":    lambda v: 0.5 * (v["a"] + v["b"]) * v["h"],
            "svg":     "trapezoid",
        },
        "Parallelogram": {
            "fields":  [("Base (b)", "b"), ("Height (h)", "h")],
            "formula": "A = b × h",
            "calc":    lambda v: v["b"] * v["h"],
            "svg":     "parallelogram",
        },
    },
    "Perimeter": {
        "Circle (Circumference)": {
            "fields":  [("Radius (r)", "r")],
            "formula": "C = 2 × π × r",
            "calc":    lambda v: 2 * math.pi * v["r"],
            "svg":     "circle",
        },
        "Rectangle": {
            "fields":  [("Length (l)", "l"), ("Width (w)", "w")],
            "formula": "P = 2 × (l + w)",
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
            "formula": "P = 4 × s",
            "calc":    lambda v: 4 * v["s"],
            "svg":     "square",
        },
    },
    "Volume": {
        "Cube": {
            "fields":  [("Side (s)", "s")],
            "formula": "V = s³",
            "calc":    lambda v: v["s"] ** 3,
            "svg":     "cube",
        },
        "Rectangular Prism": {
            "fields":  [("Length (l)", "l"), ("Width (w)", "w"), ("Height (h)", "h")],
            "formula": "V = l × w × h",
            "calc":    lambda v: v["l"] * v["w"] * v["h"],
            "svg":     "rect_prism",
        },
        "Sphere": {
            "fields":  [("Radius (r)", "r")],
            "formula": "V = (4/3) × π × r³",
            "calc":    lambda v: (4 / 3) * math.pi * v["r"] ** 3,
            "svg":     "sphere",
        },
        "Cylinder": {
            "fields":  [("Radius (r)", "r"), ("Height (h)", "h")],
            "formula": "V = π × r² × h",
            "calc":    lambda v: math.pi * v["r"] ** 2 * v["h"],
            "svg":     "cylinder",
        },
        "Cone": {
            "fields":  [("Radius (r)", "r"), ("Height (h)", "h")],
            "formula": "V = (1/3) × π × r² × h",
            "calc":    lambda v: (1 / 3) * math.pi * v["r"] ** 2 * v["h"],
            "svg":     "cone",
        },
        "Triangular Prism": {
            "fields":  [("Base (b)", "b"), ("Height of triangle (h)", "h"), ("Length (l)", "l")],
            "formula": "V = ½ × b × h × l",
            "calc":    lambda v: 0.5 * v["b"] * v["h"] * v["l"],
            "svg":     "triangle",
        },
    },
}

# ─────────────────────────────────────────────
#  SHAPE CANVAS DRAWING  (compact 180×130)
# ─────────────────────────────────────────────
def draw_shape(canvas, shape_key):
    canvas.delete("all")
    W, H   = 180, 130
    cx, cy = W // 2, H // 2
    fill   = "#00c9a718"
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
        canvas.create_oval(cx-38, cy+18, cx+38, cy+38, outline=line, width=lw, fill=fill)
        canvas.create_line(cx, cy-48, cx-38, cy+28, fill=line, width=lw)
        canvas.create_line(cx, cy-48, cx+38, cy+28, fill=line, width=lw)
        canvas.create_line(cx, cy-48, cx, cy+28, fill=ACCENT2, width=1, dash=(4, 3))
        canvas.create_text(cx + 22, cy - 8,  text="h", fill=ACCENT2, font=FONT_SMALL)
        canvas.create_line(cx, cy+28, cx+38, cy+28, fill=ACCENT2, width=1, dash=(4, 3))
        canvas.create_text(cx + 22, cy + 44, text="r", fill=ACCENT2, font=FONT_SMALL)


# ─────────────────────────────────────────────
#  HOVER HELPER
# ─────────────────────────────────────────────
def bind_hover(widget, hover_bg, hover_fg, norm_bg, norm_fg):
    widget.bind("<Enter>", lambda e: widget.config(bg=hover_bg, fg=hover_fg))
    widget.bind("<Leave>", lambda e: widget.config(bg=norm_bg,  fg=norm_fg))


# ─────────────────────────────────────────────
#  MUTABLE STATE
# ─────────────────────────────────────────────
state = {
    "category":   "Area",
    "shape":      None,
    "entry_vars": {},
    "result_var": None,
    "shape_btns": {},
}


# ─────────────────────────────────────────────
#  SOLVE / RESET
# ─────────────────────────────────────────────
def solve():
    try:
        values = {}
        for key, var in state["entry_vars"].items():
            raw = var.get().strip()
            if raw == "":
                messagebox.showwarning("Missing Input", f"Please enter a value for '{key}'.")
                return
            val = float(raw)
            if val <= 0:
                messagebox.showwarning("Invalid Input", f"'{key}' must be greater than 0.")
                return
            values[key] = val

        cat    = state["category"]
        shape  = state["shape"]
        result = SHAPES[cat][shape]["calc"](values)
        unit_map = {"Area": "units²", "Perimeter": "units", "Volume": "units³"}
        state["result_var"].set(f"✅  Result: {result:,.4f} {unit_map[cat]}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter numeric values only.")


def reset_fields():
    for var in state["entry_vars"].values():
        var.set("")
    if state["result_var"]:
        state["result_var"].set("")


# ─────────────────────────────────────────────
#  RIGHT PANEL  — two columns side by side
#  LEFT  side: shape canvas
#  RIGHT side: formula + input fields + buttons
# ─────────────────────────────────────────────
def build_solver_content(solver_frame):
    for w in solver_frame.winfo_children():
        w.destroy()
    state["entry_vars"].clear()

    cat   = state["category"]
    shape = state["shape"]
    info  = SHAPES[cat][shape]

    # ── Title bar ───────────────────────────
    title_bar = tk.Frame(solver_frame, bg=PANEL)
    title_bar.pack(fill="x", padx=16, pady=(12, 8))
    tk.Label(title_bar, text=f"{shape}  —  {cat}",
             bg=PANEL, fg=ACCENT, font=FONT_HEAD).pack(anchor="w")

    # ── Two-column content row ───────────────
    content_row = tk.Frame(solver_frame, bg=PANEL)
    content_row.pack(fill="both", expand=True, padx=16, pady=(0, 10))

    # LEFT: shape canvas
    left_col = tk.Frame(content_row, bg=CARD, width=190)
    left_col.pack(side="left", fill="y", padx=(0, 14))
    left_col.pack_propagate(False)

    c = tk.Canvas(left_col, width=180, height=130, bg=CARD, highlightthickness=0)
    c.pack(padx=5, pady=20)
    draw_shape(c, info["svg"])

    # RIGHT: formula + inputs + buttons
    right_col = tk.Frame(content_row, bg=PANEL)
    right_col.pack(side="left", fill="both", expand=True)

    # Formula box
    f_box = tk.Frame(right_col, bg="#0a2a1e")
    f_box.pack(fill="x", pady=(0, 12))
    tk.Label(f_box, text="FORMULA", bg="#0a2a1e", fg=ACCENT,
             font=("Helvetica", 8, "bold")).pack(anchor="w", padx=10, pady=(6, 0))
    tk.Label(f_box, text=info["formula"], bg="#0a2a1e", fg=ACCENT2,
             font=FONT_FORMULA).pack(anchor="w", padx=10, pady=(0, 8))

    # Input fields label
    tk.Label(right_col, text="ENTER VALUES", bg=PANEL, fg=MUTED,
             font=("Helvetica", 8, "bold")).pack(anchor="w", pady=(0, 6))

    # Fields
    for label, key in info["fields"]:
        row = tk.Frame(right_col, bg=PANEL)
        row.pack(fill="x", pady=4)

        tk.Label(row, text=label, bg=PANEL, fg=WHITE, font=FONT_BODY,
                 width=22, anchor="w").pack(side="left")

        var = tk.StringVar()
        state["entry_vars"][key] = var

        e = tk.Entry(row, textvariable=var, width=10,
                     bg=CARD, fg=ACCENT2, insertbackground=ACCENT2,
                     font=FONT_RESULT, relief="flat", bd=0)
        e.pack(side="left", ipady=4, padx=(6, 0))

        # underline
        tk.Frame(row, bg=ACCENT, height=2).pack(side="left", fill="x", expand=True, padx=(4, 0))

    # Buttons row
    btn_row = tk.Frame(right_col, bg=PANEL)
    btn_row.pack(anchor="w", pady=(14, 0))

    solve_btn = tk.Button(btn_row, text=" ▶  SOLVE ",
                          font=("Helvetica", 11, "bold"),
                          bg=ACCENT, fg=BG, activebackground=ACCENT2,
                          activeforeground=BG, relief="flat", cursor="hand2",
                          command=solve)
    solve_btn.pack(side="left", ipadx=8, ipady=5)
    bind_hover(solve_btn, ACCENT2, BG, ACCENT, BG)

    clear_btn = tk.Button(btn_row, text=" Clear ",
                          font=("Helvetica", 10),
                          bg=CARD, fg=MUTED, activebackground=RED,
                          activeforeground=WHITE, relief="flat", cursor="hand2",
                          command=reset_fields)
    clear_btn.pack(side="left", padx=(10, 0), ipadx=6, ipady=5)
    bind_hover(clear_btn, RED, WHITE, CARD, MUTED)

    # Result label
    result_var = tk.StringVar(value="")
    state["result_var"] = result_var
    tk.Label(right_col, textvariable=result_var, bg=PANEL, fg=ACCENT2,
             font=FONT_RESULT, wraplength=400, anchor="w").pack(anchor="w", pady=(10, 0))


def clear_solver(solver_frame):
    for w in solver_frame.winfo_children():
        w.destroy()
    tk.Label(solver_frame,
             text="👈  Pick a shape from the left to get started",
             bg=PANEL, fg=MUTED, font=("Helvetica", 13)).place(relx=0.5, rely=0.5, anchor="center")


# ─────────────────────────────────────────────
#  SHAPE LIST
# ─────────────────────────────────────────────
def select_shape(shape, solver_frame):
    state["shape"] = shape
    for s, b in state["shape_btns"].items():
        b.config(bg=ACCENT if s == shape else CARD,
                 fg=BG     if s == shape else WHITE)
    build_solver_content(solver_frame)


def refresh_shapes(shape_list_frame, solver_frame):
    for w in shape_list_frame.winfo_children():
        w.destroy()
    state["shape_btns"].clear()
    for shape in SHAPES[state["category"]]:
        b = tk.Button(shape_list_frame, text=shape,
                      font=FONT_BODY, bg=CARD, fg=WHITE,
                      activebackground=ACCENT2, activeforeground=BG,
                      relief="flat", anchor="w", cursor="hand2",
                      padx=10, pady=6,
                      command=lambda s=shape: select_shape(s, solver_frame))
        b.pack(fill="x", pady=2)
        state["shape_btns"][shape] = b
        bind_hover(b, ACCENT2, BG, CARD, WHITE)


def set_category(cat, shape_list_frame, solver_frame):
    state["category"] = cat
    state["shape"]    = None
    refresh_shapes(shape_list_frame, solver_frame)
    clear_solver(solver_frame)


# ─────────────────────────────────────────────
#  MAIN WINDOW
# ─────────────────────────────────────────────
def build_window():
    window = tk.Tk()
    window.title("📐 Math Shape Solver")
    window.geometry("900x560")
    window.resizable(False, False)
    window.configure(bg=BG)

    # Header
    hdr = tk.Frame(window, bg=ACCENT, height=56)
    hdr.pack(fill="x")
    hdr.pack_propagate(False)
    tk.Label(hdr, text="📐  Math Shape Solver",
             bg=ACCENT, fg=BG, font=FONT_TITLE).pack(side="left", padx=20, pady=8)
    tk.Label(hdr, text="Select category → shape → enter values → solve!",
             bg=ACCENT, fg=BG, font=FONT_SMALL).pack(side="right", padx=20)

    # Body
    body = tk.Frame(window, bg=BG)
    body.pack(fill="both", expand=True, padx=16, pady=12)

    # Left column
    left = tk.Frame(body, bg=BG, width=230)
    left.pack(side="left", fill="y", padx=(0, 12))
    left.pack_propagate(False)

    # Right solver panel
    solver_frame = tk.Frame(body, bg=PANEL)
    solver_frame.pack(side="left", fill="both", expand=True)
    clear_solver(solver_frame)

    # Category label + buttons
    tk.Label(left, text="CATEGORY", bg=BG, fg=MUTED,
             font=("Helvetica", 9, "bold")).pack(anchor="w", pady=(0, 4))
    cat_row = tk.Frame(left, bg=BG)
    cat_row.pack(fill="x", pady=(0, 12))

    # Shape list
    tk.Label(left, text="SHAPES", bg=BG, fg=MUTED,
             font=("Helvetica", 9, "bold")).pack(anchor="w", pady=(0, 4))
    shape_list_frame = tk.Frame(left, bg=BG)
    shape_list_frame.pack(fill="x")

    for cat in SHAPES:
        b = tk.Button(cat_row, text=cat,
                      font=("Helvetica", 10, "bold"),
                      bg=CARD, fg=WHITE,
                      activebackground=ACCENT, activeforeground=BG,
                      relief="flat", cursor="hand2",
                      command=lambda c=cat: set_category(c, shape_list_frame, solver_frame))
        b.pack(side="left", padx=2, ipadx=6, ipady=4)
        bind_hover(b, ACCENT, BG, CARD, WHITE)

    refresh_shapes(shape_list_frame, solver_frame)
    window.mainloop()


build_window()