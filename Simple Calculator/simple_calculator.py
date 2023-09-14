import tkinter as tk
from tkinter import ttk

def button_click(char):
    current_text = entry.get()
    if char == '=':
        try:
            result = str(eval(current_text))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif char == 'Clear':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, char)

def clear_error(event):
    if entry.get() == "Error":
        entry.delete(0, tk.END)

def create_circle_button(parent, text, command):
    button = ttk.Button(parent, text=text, width=7, command=command, style="Circular.TButton")
    return button

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - 500) // 2  # Centered horizontally
y = (screen_height - 310) // 2  # Centered vertically

root.geometry(f"554x375+{x}+{y}")  # Set window position to center
root.resizable(False, False)  # Disable resizing

# Create a style for circular buttons
style = ttk.Style()
style.configure("Circular.TButton", font=("Courier", 18), padding=10)

# Create a frame for the entry and buttons
frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

# Entry field
entry = ttk.Entry(frame, width=20, font=("Courier", 24), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)
entry.bind("<Button-1>", clear_error)  # Clear the error message on click

# Button grid
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'Clear', '=', '+'
]

row_val = 1
col_val = 0

for button_text in buttons:
    if button_text == 'Clear':
        button = create_circle_button(frame, button_text, lambda char=button_text: button_click(char))
    else:
        button = create_circle_button(frame, button_text, lambda char=button_text: button_click(char))
    button.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure padding for the result entry field
entry.grid_configure(pady=20)

# Set the title and background color for the window
root.title("Simple Calculator")

# Start the application
root.mainloop()

