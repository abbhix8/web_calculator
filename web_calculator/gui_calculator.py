# gui_calculator.py

import tkinter as tk
from tkinter import messagebox

def click(button_text):
    if button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "=":
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
    else:
        entry.insert(tk.END, button_text)

# Initialize main window
root = tk.Tk()
root.title("Basic Calculator")

# Entry widget for display
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create buttons in a grid
row = 1
col = 0
for button in buttons:
    action = lambda x=button: click(x)
    tk.Button(root, text=button, width=5, height=2, font=('Arial', 24), command=action)\
        .grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the GUI event loop
root.mainloop()
