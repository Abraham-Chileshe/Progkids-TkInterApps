# ui_components.py
import tkinter as tk
from constants import *
from shapes_data import SHAPES, draw_shape
from calculator import state, solve, reset_fields

# ─────────────────────────────────────────────
#  HOVER HELPER
# ─────────────────────────────────────────────
def bind_hover(widget, hover_bg, hover_fg, norm_bg, norm_fg):
    widget.bind("<Enter>", lambda e: widget.config(bg=hover_bg, fg=hover_fg))
    widget.bind("<Leave>", lambda e: widget.config(bg=norm_bg,  fg=norm_fg))

# ─────────────────────────────────────────────
#  SOLVER CONTENT BUILDER
# ─────────────────────────────────────────────
def build_solver_content(solver_frame):
    for w in solver_frame.winfo_children():
        w.destroy()
    state["entry_vars"].clear()

    cat   = state["category"]
    shape = state["shape"]
    if not shape or shape not in SHAPES[cat]:
        return
    
    info  = SHAPES[cat][shape]

    # ── Title bar ───────────────────────────
    title_bar = tk.Frame(solver_frame, bg=PANEL)
    title_bar.pack(fill="x", padx=16, pady=(12, 8))
    tk.Label(title_bar, text=f"{shape}  \u2014  {cat}",
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
    tk.Label(right_col, text="ENTER VALUES (supports formulas like pi, sqrt, etc.)", bg=PANEL, fg=MUTED,
             font=("Helvetica", 8, "bold")).pack(anchor="w", pady=(0, 6))

    # Fields
    for label, key in info["fields"]:
        row = tk.Frame(right_col, bg=PANEL)
        row.pack(fill="x", pady=4)

        tk.Label(row, text=label, bg=PANEL, fg=WHITE, font=FONT_BODY,
                 width=22, anchor="w").pack(side="left")

        var = tk.StringVar()
        state["entry_vars"][key] = var

        e = tk.Entry(row, textvariable=var, width=15,
                     bg=CARD, fg=ACCENT2, insertbackground=ACCENT2,
                     font=FONT_RESULT, relief="flat", bd=0)
        e.pack(side="left", ipady=4, padx=(6, 0))

        # underline
        tk.Frame(row, bg=ACCENT, height=2).pack(side="left", fill="x", expand=True, padx=(4, 0))

    # Buttons row
    btn_row = tk.Frame(right_col, bg=PANEL)
    btn_row.pack(anchor="w", pady=(14, 0))

    solve_btn = tk.Button(btn_row, text="  \u25b6  SOLVE  ",
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
             text="\ud83d\udc48  Pick a shape from the left to get started",
             bg=PANEL, fg=MUTED, font=("Helvetica", 13)).place(relx=0.5, rely=0.5, anchor="center")

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
    
    current_cat = state["category"]
    if current_cat not in SHAPES:
        return
        
    for shape in SHAPES[current_cat]:
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
