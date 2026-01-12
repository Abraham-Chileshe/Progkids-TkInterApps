# Simple Drawing App - Drawing_app.py
import tkinter as tk
from tkinter import colorchooser, messagebox

# Create main window
root = tk.Tk()
root.title("Drawing App")
root.geometry("800x650")
root.configure(bg="#34495E")

# Drawing settings
pen_color = "black"
pen_size = 2
old_x = None
old_y = None

# Header
header = tk.Label(
    root,
    text="🎨 My Drawing App",
    font=("Arial", 20, "bold"),
    bg="#2C3E50",
    fg="white",
    height=2
)
header.pack(fill=tk.X)

# Toolbar Frame
toolbar = tk.Frame(root, bg="#34495E")
toolbar.pack(pady=10)

# Choose Color Function
def choose_color():
    global pen_color
    color = colorchooser.askcolor(title="Choose a color")
    if color[1]:
        pen_color = color[1]

# Clear Canvas Function
def clear_canvas():
    canvas.delete("all")

# Change to Eraser
def use_eraser():
    global pen_color
    pen_color = "white"

# Change to Black Pen
def use_black():
    global pen_color
    pen_color = "black"

# Increase Pen Size
def increase_size():
    global pen_size
    if pen_size < 20:
        pen_size += 1
        size_label.config(text=f"Size: {pen_size}")

# Decrease Pen Size
def decrease_size():
    global pen_size
    if pen_size > 1:
        pen_size -= 1
        size_label.config(text=f"Size: {pen_size}")

# Drawing Function - UPDATED FOR SMOOTH LINES
def paint(event):
    global old_x, old_y
    if old_x and old_y:
        canvas.create_line(
            old_x, old_y, event.x, event.y,
            width=pen_size * 2,
            fill=pen_color,
            capstyle=tk.ROUND,
            smooth=True
        )
    old_x = event.x
    old_y = event.y

# Reset function when mouse is released
def reset(event):
    global old_x, old_y
    old_x = None
    old_y = None

# Buttons
color_btn = tk.Button(
    toolbar,
    text="Choose Color",
    command=choose_color,
    font=("Arial", 12),
    bg="#3498DB",
    fg="white",
    width=12,
    height=2
)
color_btn.pack(side=tk.LEFT, padx=5)

black_btn = tk.Button(
    toolbar,
    text="Black Pen",
    command=use_black,
    font=("Arial", 12),
    bg="#2C3E50",
    fg="white",
    width=12,
    height=2
)
black_btn.pack(side=tk.LEFT, padx=5)

eraser_btn = tk.Button(
    toolbar,
    text="Eraser",
    command=use_eraser,
    font=("Arial", 12),
    bg="#E74C3C",
    fg="white",
    width=12,
    height=2
)
eraser_btn.pack(side=tk.LEFT, padx=5)

clear_btn = tk.Button(
    toolbar,
    text="Clear All",
    command=clear_canvas,
    font=("Arial", 12),
    bg="#E67E22",
    fg="white",
    width=12,
    height=2
)
clear_btn.pack(side=tk.LEFT, padx=5)

# Size control frame
size_frame = tk.Frame(root, bg="#34495E")
size_frame.pack(pady=5)

decrease_btn = tk.Button(
    size_frame,
    text="−",
    command=decrease_size,
    font=("Arial", 16, "bold"),
    bg="#95A5A6",
    fg="white",
    width=3,
    height=1
)
decrease_btn.pack(side=tk.LEFT, padx=5)

size_label = tk.Label(
    size_frame,
    text=f"Size: {pen_size}",
    font=("Arial", 12, "bold"),
    bg="#34495E",
    fg="white",
    width=10
)
size_label.pack(side=tk.LEFT, padx=5)

increase_btn = tk.Button(
    size_frame,
    text="+",
    command=increase_size,
    font=("Arial", 16, "bold"),
    bg="#95A5A6",
    fg="white",
    width=3,
    height=1
)
increase_btn.pack(side=tk.LEFT, padx=5)

# Canvas for drawing
canvas = tk.Canvas(
    root,
    bg="white",
    width=750,
    height=450
)
canvas.pack(pady=10)

# Bind mouse movement to drawing
canvas.bind("<B1-Motion>", paint)
canvas.bind("<ButtonRelease-1>", reset)

root.mainloop()