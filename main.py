import tkinter as tk
from tkinter import ttk


class SuperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SuperApp")
        self.root.geometry("600x500")
        self.root.configure(bg='white')

        # Remove default window decorations
        self.root.overrideredirect(True)

        # Variables for window dragging
        self.x = 0
        self.y = 0

        # Create custom title bar frame
        title_frame = tk.Frame(root, bg='red', height=40, relief='solid', borderwidth=1)
        title_frame.pack(fill='x', side='top')
        title_frame.pack_propagate(False)

        # Title label
        # title_label = tk.Label(title_frame, text="SuperApp", font=('Arial', 12, 'bold'),
        #                        bg='white', fg='black')
        # title_label.pack(side='left', padx=10, pady=8)

        # Bind dragging events to title frame
        title_frame.bind('<Button-1>', self.start_move)
        title_frame.bind('<B1-Motion>', self.do_move)
        # title_label.bind('<Button-1>', self.start_move)
        # title_label.bind('<B1-Motion>', self.do_move)

        # Window control buttons frame
        controls_frame = tk.Frame(title_frame, bg='white')
        controls_frame.pack(side='right', padx=5)

        # # Minimize button
        # minimize_btn = tk.Label(controls_frame, text="─", font=('Arial', 12),
        #                         bg='white', fg='black', cursor='hand2')
        # minimize_btn.pack(side='left', padx=3)
        # minimize_btn.bind('<Button-1>', lambda e: root.iconify())
        #
        # # Maximize button (drawn as rectangle)
        # maximize_btn = tk.Label(controls_frame, text="☐", font=('Arial', 12),
        #                         bg='white', fg='black', cursor='hand2')
        # maximize_btn.pack(side='left', padx=3)

        # Close button
        # close_btn = tk.Label(controls_frame, text="✕", font=('Arial', 12),
        #                      bg='white', fg='black', cursor='hand2')
        # close_btn.pack(side='left', padx=3)
        # close_btn.bind('<Button-1>', lambda e: root.quit())

        # Main content frame
        content_frame = tk.Frame(root, bg='white')
        content_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Calc button (orange)
        calc_btn = tk.Button(content_frame, text="calc", font=('Arial', 14, 'bold'),
                             bg='#FF8C42', fg='#5856D6', width=12, height=6,
                             relief='flat', cursor='hand2',
                             command=self.open_calc)
        calc_btn.grid(row=0, column=0, padx=30, pady=20)

        # Drawing button (blue)
        drawing_btn = tk.Button(content_frame, text="drawing", font=('Arial', 14, 'bold'),
                                bg='#5856D6', fg='white', width=12, height=6,
                                relief='flat', cursor='hand2',
                                command=self.open_drawing)
        drawing_btn.grid(row=0, column=1, padx=30, pady=20)

    def open_calc(self):
        print("Opening calculator...")

    def open_drawing(self):
        print("Opening drawing app...")

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")


if __name__ == "__main__":
    root = tk.Tk()
    app = SuperApp(root)
    root.mainloop()