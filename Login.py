# Simple & Organized Login Form - Example for Nicholas
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys

# Create main window
root = tk.Tk()
root.title("Login Screen")
root.geometry("400x400")
root.configure(bg="#2C3E50")

# Title Label
title_label = tk.Label(
    root,
    text="Welcome Back!",
    font=("Arial", 24, "bold"),
    bg="#2C3E50",
    fg="white"
)
title_label.pack(pady=30)

# Username Section
username_label = tk.Label(
    root,
    text="Username",
    font=("Arial", 12),
    bg="#2C3E50",
    fg="white"
)
username_label.pack(pady=(10, 5))

username_entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 12),
    bg="white",
    fg="black",
    relief="flat",
    borderwidth=2
)
username_entry.pack(pady=5)

# Password Section
password_label = tk.Label(
    root,
    text="Password",
    font=("Arial", 12),
    bg="#2C3E50",
    fg="white"
)
password_label.pack(pady=(10, 5))

password_entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 12),
    bg="white",
    fg="black",
    show="•",
    relief="flat",
    borderwidth=2
)
password_entry.pack(pady=5)


# Login Function
def login():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Error", "Please fill in all fields!")
    else:
        messagebox.showinfo("Success", f"Welcome, {username}!")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        subprocess.Popen([sys.executable, "Drawing_app.py"])
        root.quit()
        root.destroy()


# Login Button
login_button = tk.Button(
    root,
    text="LOGIN",
    command=login,
    font=("Arial", 14, "bold"),
    bg="#3498DB",
    fg="white",
    width=20,
    height=2,
    relief="flat",
    cursor="hand2"
)
login_button.pack(pady=25)

root.mainloop()