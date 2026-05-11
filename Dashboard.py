import tkinter as tk

screen = tk.Tk()
screen.title("Home page")
screen.geometry("600x400")
screen.minsize(500, 300)
screen.config(bg="white")

is_dark = False
current_page = "home"

def get_theme_color():
    if is_dark:
        return {
            "navbar_bg": "black",
            "sidebar_bg": "#141414",
            "main_bg": "#282828",
            "text_color": "white",
            "sidebar_btn": "#141414",
        }
    else:
        return {
            "navbar_bg": "#34495e",
            "sidebar_bg": "#34495e",
            "main_bg": "white",
            "text_color": "black",
            "sidebar_btn": "#34495e",
        }

colors = get_theme_color()

# ─── Helpers ────────────────────────────────────────────────────────────────

def clear_main():
    for widget in main_frame.winfo_children():
        widget.destroy()

def make_top_section(parent, page_title):
    container = tk.Frame(parent, bg=colors["main_bg"])
    container.pack(fill=tk.BOTH, padx=20, pady=20, expand=True)

    title_frame = tk.Frame(container, bg=colors["main_bg"])
    title_frame.pack(fill=tk.X, pady=20)

    tk.Label(title_frame, text=page_title, bg=colors["main_bg"],
             fg=colors["text_color"], font=("Arial", 10)).pack(side=tk.LEFT)

    tk.Button(title_frame, text="Refresh", bg=colors["sidebar_bg"], fg="white",
              relief="flat", padx=15, pady=5, cursor="hand2",
              font=("Arial", 9)).pack(side=tk.RIGHT)

    return container

# ─── Theme ──────────────────────────────────────────────────────────────────

def change_theme():
    global is_dark, colors
    is_dark = not is_dark
    colors = get_theme_color()
    apply_nav_sidebar()
    # Re-render the active page so every widget is recreated with the right colors
    pages[current_page]()

def apply_nav_sidebar():
    nav_frame.config(bg=colors["navbar_bg"])
    title.config(bg=colors["navbar_bg"])
    sidebar.config(bg=colors["sidebar_bg"])
    sidebar_label.config(bg=colors["sidebar_bg"])
    status_frame.config(bg=colors["navbar_bg"])
    status_label.config(bg=colors["navbar_bg"])
    info_label.config(bg=colors["navbar_bg"])
    main_frame.config(bg=colors["main_bg"])
    for btn in [dashboard_btn, projects_btn, settings_btn]:
        btn.config(bg=colors["sidebar_bg"])

# ─── Nav pages ──────────────────────────────────────────────────────────────

def go_home():
    global current_page
    current_page = "home"
    clear_main()
    main_frame.config(bg=colors["main_bg"])

    container = make_top_section(main_frame, "Home")
    tk.Label(container, text="Welcome to the home page", bg=colors["main_bg"],
             fg=colors["text_color"], font=("Arial", 14)).pack(expand=True)

    status_label.config(text="Ready | current page: Home")
    home_btn.config(bg="green")
    about_btn.config(bg="#3498db")
    help_btn.config(bg="#3498db")

def go_about():
    global current_page
    current_page = "about"
    clear_main()
    main_frame.config(bg=colors["main_bg"])

    container = make_top_section(main_frame, "About")
    tk.Label(container, text="Welcome to the about page", bg=colors["main_bg"],
             fg=colors["text_color"], font=("Arial", 14)).pack(expand=True)

    status_label.config(text="Ready | current page: About")
    about_btn.config(bg="green")
    home_btn.config(bg="#3498db")
    help_btn.config(bg="#3498db")

def go_help():
    global current_page
    current_page = "help"
    clear_main()
    main_frame.config(bg=colors["main_bg"])

    container = make_top_section(main_frame, "Help")
    tk.Label(container, text="Welcome to the help page", bg=colors["main_bg"],
             fg=colors["text_color"], font=("Arial", 14)).pack(expand=True)

    status_label.config(text="Ready | current page: Help")
    help_btn.config(bg="green")
    about_btn.config(bg="#3498db")
    home_btn.config(bg="#3498db")

# ─── Sidebar pages ──────────────────────────────────────────────────────────

def dashboard_function():
    global current_page
    current_page = "dashboard"
    clear_main()
    main_frame.config(bg=colors["main_bg"])
    status_label.config(text="Ready | current page: Dashboard")
    home_btn.config(bg="#3498db")
    about_btn.config(bg="#3498db")
    help_btn.config(bg="#3498db")

    container = tk.Frame(main_frame, bg=colors["main_bg"])
    container.pack(fill=tk.BOTH, padx=20, pady=20, expand=True)

    title_frame = tk.Frame(container, bg=colors["main_bg"])
    title_frame.pack(fill=tk.X, pady=20)

    tk.Label(title_frame, text="Dashboard Overview", bg=colors["main_bg"],
             fg=colors["text_color"], font=("Arial", 10)).pack(side=tk.LEFT)

    tk.Button(title_frame, text="Refresh", bg=colors["sidebar_bg"], fg="white",
              relief="flat", padx=15, pady=5, cursor="hand2",
              font=("Arial", 9)).pack(side=tk.RIGHT)

    stats_frame = tk.Frame(container, bg=colors["main_bg"])
    stats_frame.pack(fill=tk.X, pady=(0, 20))

    def create_stat_card(parent, card_title, value, color, icon):
        card = tk.Frame(parent, bg=color, relief="raised")
        card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        tk.Label(card, text=icon,       bg=color, fg="white", font=("Arial", 24)).pack(pady=(15, 5))
        tk.Label(card, text=value,      bg=color, fg="white", font=("Arial", 18, "bold")).pack()
        tk.Label(card, text=card_title, bg=color, fg="white", font=("Arial", 9)).pack(pady=(0, 15))

    create_stat_card(stats_frame, "Total Projects",  "24", "#3498db", "📁")
    create_stat_card(stats_frame, "Tasks completed", "15", "#2ecc71", "✓")
    create_stat_card(stats_frame, "In Progress",     "6",  "#ff8243", "⏳")
    create_stat_card(stats_frame, "Team Members",    "10", "#e2062c", "👥")

def projects_function():
    global current_page
    current_page = "projects"
    clear_main()
    main_frame.config(bg=colors["main_bg"])
    status_label.config(text="Ready | current page: Projects")
    home_btn.config(bg="#3498db"); about_btn.config(bg="#3498db"); help_btn.config(bg="#3498db")

    container = make_top_section(main_frame, "Projects")
    tk.Label(container, text="Projects page coming soon.", bg=colors["main_bg"],
             fg=colors["text_color"], font=("Arial", 14)).pack(expand=True)

def settings_function():
    global current_page
    current_page = "settings"
    clear_main()
    main_frame.config(bg=colors["main_bg"])
    status_label.config(text="Ready | current page: Settings")
    home_btn.config(bg="#3498db"); about_btn.config(bg="#3498db"); help_btn.config(bg="#3498db")

    container = make_top_section(main_frame, "Settings")
    tk.Label(container, text="Settings page coming soon.", bg=colors["main_bg"],
             fg=colors["text_color"], font=("Arial", 14)).pack(expand=True)

# Map page names to functions for re-rendering on theme change
pages = {
    "home":      go_home,
    "about":     go_about,
    "help":      go_help,
    "dashboard": dashboard_function,
    "projects":  projects_function,
    "settings":  settings_function,
}

# ─── Sidebar button helper ───────────────────────────────────────────────────

def side_bar_btn(parent, text, command):
    btn_frame = tk.Frame(parent, bg=colors["sidebar_btn"])
    btn_frame.pack(fill=tk.X, pady=2)
    btn = tk.Button(btn_frame, text=text, command=command, bg=colors["sidebar_btn"],
                    fg="white", relief="flat", padx=20, pady=12,
                    font=("Arial", 10), cursor="hand2")
    btn.pack(fill=tk.X)

    def on_enter(e): btn.config(bg="#2c3e50")
    def on_leave(e): btn.config(bg=colors["sidebar_btn"])
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

# ─── Build UI ────────────────────────────────────────────────────────────────

# Navigation bar
nav_frame = tk.Frame(screen, bg=colors["navbar_bg"], height=50)
nav_frame.pack(side=tk.TOP, fill=tk.X)

title = tk.Label(nav_frame, text="My App", bg=colors["navbar_bg"], fg="white",
                 font=("Arial", 14, "bold"))
title.pack(side=tk.LEFT, padx=5, pady=10)

home_btn = tk.Button(nav_frame, text="Home", bg="#3498db", fg="white",
                     padx=10, pady=5, relief=tk.FLAT, command=go_home)
home_btn.pack(side=tk.LEFT, padx=5)

about_btn = tk.Button(nav_frame, text="About", bg="#3498db", fg="white",
                      padx=10, pady=5, relief=tk.FLAT, command=go_about)
about_btn.pack(side=tk.LEFT, padx=5)

help_btn = tk.Button(nav_frame, text="Help", bg="#3498db", fg="white",
                     padx=12, pady=5, relief=tk.FLAT, command=go_help)
help_btn.pack(side=tk.LEFT, padx=5)

lighting_btn = tk.Button(nav_frame, text="☀️ Theme", bg="black", fg="white",
                         padx=12, pady=5, relief=tk.FLAT, command=change_theme)
lighting_btn.pack(side=tk.RIGHT, padx=10)

# Sidebar
sidebar = tk.Frame(screen, bg=colors["sidebar_bg"], width=150)
sidebar.pack(side=tk.LEFT, fill=tk.Y)
sidebar.pack_propagate(False)

sidebar_label = tk.Label(sidebar, text="NAVIGATION", bg=colors["sidebar_btn"],
                         fg="white", font=("Arial", 12))
sidebar_label.pack(fill=tk.X, pady=20)

dashboard_btn = side_bar_btn(sidebar, "Dashboard", command=dashboard_function)
projects_btn  = side_bar_btn(sidebar, "Projects",  command=projects_function)
settings_btn  = side_bar_btn(sidebar, "Settings",  command=settings_function)

# Main area
main_frame = tk.Frame(screen, bg=colors["main_bg"])
main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Status bar
status_frame = tk.Frame(screen, bg=colors["navbar_bg"], height=25)
status_frame.pack(side=tk.BOTTOM, fill=tk.X)

status_label = tk.Label(status_frame, text="Ready | current page: Home",
                        bg=colors["navbar_bg"], fg="white")
status_label.pack(side=tk.LEFT, padx=10)

info_label = tk.Label(status_frame, text="User: student",
                      bg=colors["navbar_bg"], fg="white")
info_label.pack(side=tk.RIGHT, padx=10)

# Start on home page
go_home()

screen.mainloop()