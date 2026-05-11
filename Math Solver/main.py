# main.py
import tkinter as tk
from constants import *
from shapes_data import SHAPES
from calculator import state
from ui_components import set_category, refresh_shapes, clear_solver, bind_hover

def build_window():
    window = tk.Tk()
    window.title("\ud83d\udcd0 Math Shape Solver")
    window.geometry("900x560")
    window.resizable(False, False)
    window.configure(bg=BG)

    # Header
    hdr = tk.Frame(window, bg=ACCENT, height=56)
    hdr.pack(fill="x")
    hdr.pack_propagate(False)
    tk.Label(hdr, text="\ud83d\udcd0  Math Shape Solver",
             bg=ACCENT, fg=BG, font=FONT_TITLE).pack(side="left", padx=20, pady=8)
    tk.Label(hdr, text="Supports math formulas in input boxes! (e.g. pi*2, sqrt(16))",
             bg=ACCENT, fg=BG, font=FONT_SMALL).pack(side="right", padx=20)

    # Body
    body = tk.Frame(window, bg=BG)
    body.pack(fill="both", expand=True, padx=16, pady=12)

    # Left column (Categories and Shapes)
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

    # Build Category buttons
    for cat in SHAPES:
        b = tk.Button(cat_row, text=cat,
                      font=("Helvetica", 10, "bold"),
                      bg=CARD, fg=WHITE,
                      activebackground=ACCENT, activeforeground=BG,
                      relief="flat", cursor="hand2",
                      command=lambda c=cat: set_category(c, shape_list_frame, solver_frame))
        b.pack(side="left", padx=2, ipadx=6, ipady=4)
        bind_hover(b, ACCENT, BG, CARD, WHITE)

    # Initial load
    refresh_shapes(shape_list_frame, solver_frame)
    
    window.mainloop()

if __name__ == "__main__":
    build_window()
