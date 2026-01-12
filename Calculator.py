import tkinter as tk

# This variable stores what the user types
current_number = ""

def button_click(number):
    """When a number or symbol is clicked, add it to the screen"""
    global current_number
    current_number = current_number + str(number)
    screen.delete(0, tk.END)
    screen.insert(0, current_number)

def clear_screen():
    """Clear everything on the screen"""
    global current_number
    current_number = ""
    screen.delete(0, tk.END)

def calculate_answer():
    """Calculate the answer when = is pressed"""
    global current_number
    try:
        answer = eval(current_number)
        screen.delete(0, tk.END)
        screen.insert(0, answer)
        current_number = str(answer)
    except:
        screen.delete(0, tk.END)
        screen.insert(0, "Error!")
        current_number = ""

# Create the main window
window = tk.Tk()
window.title("My Calculator")
window.geometry("320x450")
window.config(bg="lightblue")

# Create the screen where numbers appear
screen = tk.Entry(window, font=("Arial", 20), bd=5, justify="right")
screen.pack(pady=20, padx=20, fill="x")

# Create a frame to hold all buttons
button_frame = tk.Frame(window, bg="lightblue")
button_frame.pack()

# Row 1: 7, 8, 9, /
btn7 = tk.Button(button_frame, text="7", width=5, height=2, font=("Arial", 16, "bold"), bg="white", command=lambda: button_click("7"))
btn7.grid(row=0, column=0, padx=5, pady=5)

btn8 = tk.Button(button_frame, text="8", width=5, height=2, font=("Arial", 16, "bold"), bg="white", command=lambda: button_click("8"))
btn8.grid(row=0, column=1, padx=5, pady=5)

btn9 = tk.Button(button_frame, text="9", width=5, height=2, font=("Arial", 16, "bold"), bg="white", command=lambda: button_click("9"))
btn9.grid(row=0, column=2, padx=5, pady=5)

btn_divide = tk.Button(button_frame, text="/", width=5, height=2, font=("Arial", 16, "bold"), bg="orange", command=lambda: button_click("/"))
btn_divide.grid(row=0, column=3, padx=5, pady=5)

# Row 2: 4, 5, 6, *
btn4 = tk.Button(button_frame, text="4", width=5, height=2, font=("Arial", 16, "bold"), bg="white", command=lambda: button_click("4"))
btn4.grid(row=1, column=0, padx=5, pady=5)

btn5 = tk.Button(button_frame, text="5", width=5, height=2, font=("Arial", 16, "bold"), bg="white", command=lambda: button_click("5"))
btn5.grid(row=1, column=1, padx=5, pady=5)

btn6 = tk.Button(button_frame, text="6", width=5, height=2, font=("Arial", 16, "bold"), bg="white", command=lambda: button_click("6"))
btn6.grid(row=1, column=2, padx=5, pady=5)

btn_multiply = tk.Button(button_frame, text="*", width=5, height=2, font=("Arial", 16, "bold"), bg="orange", command=lambda: button_click("*"))
btn_multiply.grid(row=1, column=3, padx=5, pady=5)

# Row 3: 1, 2, 3, -
btn1 = tk.Button(button_frame, text="1", width=5, height=2, font=("Arial", 16, "bold"), bg="white", command=lambda: button_click("1"))
btn1.grid(row=2, column=0, padx=5, pady=5)

btn2 = tk.Button(button_frame, text="2", width=5, height=2, font=("Arial", 16, "bold"), bg="white", command=lambda: button_click("2"))
btn2.grid(row=2, column=1, padx=5, pady=5)

btn3 = tk.Button(button_frame, text="3", width=5, height=2, font=("Arial", 16, "bold"), bg="white", command=lambda: button_click("3"))
btn3.grid(row=2, column=2, padx=5, pady=5)

btn_minus = tk.Button(button_frame, text="-", width=5, height=2, font=("Arial", 16, "bold"), bg="orange", command=lambda: button_click("-"))
btn_minus.grid(row=2, column=3, padx=5, pady=5)

# Row 4: 0, ., =, +
btn0 = tk.Button(button_frame, text="0", width=5, height=2, font=("Arial", 16, "bold"), bg="white", command=lambda: button_click("0"))
btn0.grid(row=3, column=0, padx=5, pady=5)

btn_dot = tk.Button(button_frame, text=".", width=5, height=2, font=("Arial", 16, "bold"), bg="white", command=lambda: button_click("."))
btn_dot.grid(row=3, column=1, padx=5, pady=5)

btn_equals = tk.Button(button_frame, text="=", width=5, height=2, font=("Arial", 16, "bold"), bg="green", fg="white", command=calculate_answer)
btn_equals.grid(row=3, column=2, padx=5, pady=5)

btn_plus = tk.Button(button_frame, text="+", width=5, height=2, font=("Arial", 16, "bold"), bg="orange", command=lambda: button_click("+"))
btn_plus.grid(row=3, column=3, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(button_frame, text="CLEAR", width=23, height=2, font=("Arial", 14, "bold"), bg="red", fg="white", command=clear_screen)
clear_btn.grid(row=4, column=0, columnspan=4, padx=5, pady=5)

# Start the calculator
window.mainloop()