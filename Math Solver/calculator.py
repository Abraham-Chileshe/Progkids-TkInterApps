# calculator.py
import math
from tkinter import messagebox
from shapes_data import SHAPES

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

def safe_eval(expr):
    """
    Evaluates a math expression safely using the math module's namespace.
    """
    # Allow only math functions and numbers
    allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    allowed_names.update({"abs": abs, "min": min, "max": max, "round": round})
    
    # Pre-process common symbols if needed (e.g., replace ^ with **)
    expr = expr.replace("^", "**").replace("\u03c0", "pi").replace("\u00d7", "*").strip()
    
    try:
        # evaluate the expression with no access to builtins for security
        return eval(expr, {"__builtins__": {}}, allowed_names)
    except Exception:
        raise ValueError("Invalid math expression")

def solve():
    try:
        values = {}
        for key, var in state["entry_vars"].items():
            raw = var.get().strip()
            if raw == "":
                messagebox.showwarning("Missing Input", f"Please enter a value for '{key}'.")
                return
            
            # Use safe_eval instead of float() to support math formulas
            try:
                val = safe_eval(raw)
            except ValueError:
                messagebox.showerror("Invalid Input", f"Could not evaluate formula for '{key}'. Please enter a valid number or math expression.")
                return
                
            if val <= 0:
                messagebox.showwarning("Invalid Input", f"'{key}' result ({val}) must be greater than 0.")
                return
            values[key] = val

        cat    = state["category"]
        shape  = state["shape"]
        result = SHAPES[cat][shape]["calc"](values)
        unit_map = {"Area": "units\u00b2", "Perimeter": "units", "Volume": "units\u00b3"}
        state["result_var"].set(f"\u2705  Result: {result:,.4f} {unit_map[cat]}")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def reset_fields():
    for var in state["entry_vars"].values():
        var.set("")
    if state["result_var"]:
        state["result_var"].set("")
