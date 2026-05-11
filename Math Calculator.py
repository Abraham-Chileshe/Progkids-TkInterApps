import tkinter as tk
from tkinter import ttk


def calculate():
    """Calculate based on selected formula"""
    formula = formula_var.get()
    result_label.config(text="")

    try:
        if formula == "Area of Rectangle":
            length = float(entry1.get())
            width = float(entry2.get())
            result = length * width
            result_label.config(text=f"Area = {result}")

        elif formula == "Area of Triangle":
            base = float(entry1.get())
            height = float(entry2.get())
            result = 0.5 * base * height
            result_label.config(text=f"Area = {result}")

        elif formula == "Area of Circle":
            radius = float(entry1.get())
            result = 3.14159 * radius * radius
            result_label.config(text=f"Area = {result:.2f}")

        elif formula == "Perimeter of Rectangle":
            length = float(entry1.get())
            width = float(entry2.get())
            result = 2 * (length + width)
            result_label.config(text=f"Perimeter = {result}")

        elif formula == "Circumference of Circle":
            radius = float(entry1.get())
            result = 2 * 3.14159 * radius
            result_label.config(text=f"Circumference = {result:.2f}")

        elif formula == "Volume of Cube":
            side = float(entry1.get())
            result = side * side * side
            result_label.config(text=f"Volume = {result}")

        elif formula == "Volume of Rectangular Prism":
            length = float(entry1.get())
            width = float(entry2.get())
            height = float(entry3.get())
            result = length * width * height
            result_label.config(text=f"Volume = {result}")

    except ValueError:
        result_label.config(text="Please enter valid numbers!")


def update_inputs(*args):
    """Update input fields based on selected formula"""
    formula = formula_var.get()

    # Clear all entries
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    result_label.config(text="")

    # Hide all inputs first
    label1.grid_remove()
    entry1.grid_remove()
    label2.grid_remove()
    entry2.grid_remove()
    label3.grid_remove()
    entry3.grid_remove()

    # Show relevant inputs
    if formula == "Area of Rectangle":
        label1.config(text="Length:")
        label1.grid()
        entry1.grid()
        label2.config(text="Width:")
        label2.grid()
        entry2.grid()

    elif formula == "Area of Triangle":
        label1.config(text="Base:")
        label1.grid()
        entry1.grid()
        label2.config(text="Height:")
        label2.grid()
        entry2.grid()

    elif formula == "Area of Circle":
        label1.config(text="Radius:")
        label1.grid()
        entry1.grid()

    elif formula == "Perimeter of Rectangle":
        label1.config(text="Length:")
        label1.grid()
        entry1.grid()
        label2.config(text="Width:")
        label2.grid()
        entry2.grid()

    elif formula == "Circumference of Circle":
        label1.config(text="Radius:")
        label1.grid()
        entry1.grid()

    elif formula == "Volume of Cube":
        label1.config(text="Side:")
        label1.grid()
        entry1.grid()

    elif formula == "Volume of Rectangular Prism":
        label1.config(text="Length:")
        label1.grid()
        entry1.grid()
        label2.config(text="Width:")
        label2.grid()
        entry2.grid()
        label3.config(text="Height:")
        label3.grid()
        entry3.grid()


# Create main window
root = tk.Tk()
root.title("Math Formula Calculator")
root.geometry("400x350")
root.config(bg="#f0f0f0")

# Title
title_label = tk.Label(root, text="🧮 Math Formula Calculator",
                       font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.grid(row=0, column=0, columnspan=2, pady=15)

# Formula selection
formula_label = tk.Label(root, text="Choose a Formula:",
                         font=("Arial", 11), bg="#f0f0f0")
formula_label.grid(row=1, column=0, columnspan=2, pady=5)

formulas = [
    "Area of Rectangle",
    "Area of Triangle",
    "Area of Circle",
    "Perimeter of Rectangle",
    "Circumference of Circle",
    "Volume of Cube",
    "Volume of Rectangular Prism"
]

formula_var = tk.StringVar()
formula_dropdown = ttk.Combobox(root, textvariable=formula_var,
                                values=formulas, state="readonly", width=25)
formula_dropdown.grid(row=2, column=0, columnspan=2, pady=5)
formula_dropdown.current(0)
formula_var.trace('w', update_inputs)

# Input fields
label1 = tk.Label(root, text="Length:", font=("Arial", 10), bg="#f0f0f0")
label1.grid(row=3, column=0, padx=10, pady=10, sticky="e")
entry1 = tk.Entry(root, font=("Arial", 10), width=15)
entry1.grid(row=3, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Width:", font=("Arial", 10), bg="#f0f0f0")
label2.grid(row=4, column=0, padx=10, pady=10, sticky="e")
entry2 = tk.Entry(root, font=("Arial", 10), width=15)
entry2.grid(row=4, column=1, padx=10, pady=10)

label3 = tk.Label(root, text="Height:", font=("Arial", 10), bg="#f0f0f0")
label3.grid(row=5, column=0, padx=10, pady=10, sticky="e")
entry3 = tk.Entry(root, font=("Arial", 10), width=15)
entry3.grid(row=5, column=1, padx=10, pady=10)

# Calculate button
calc_button = tk.Button(root, text="Calculate", font=("Arial", 12, "bold"),
                        bg="#4CAF50", fg="white", command=calculate,
                        width=15, height=1)
calc_button.grid(row=6, column=0, columnspan=2, pady=15)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"),
                        bg="#f0f0f0", fg="#2196F3")
result_label.grid(row=7, column=0, columnspan=2, pady=10)

# Initialize the display
update_inputs()

root.mainloop()