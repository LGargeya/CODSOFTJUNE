from tkinter import *
import random
from tkinter import ttk

# Create an instance of tkinter frame
win = Tk()

# Set the title of the window
win.title("Rock-Paper-Scissors")

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

# Calculate the x and y coordinates to center the window
x = (screen_width - 750) // 2  # 750 is the window width
y = (screen_height - 450) // 2  # 450 is the window height

# Set the geometry of the window with the centered position
win.geometry(f"750x450+{x}+{y}")
win.minsize(750, 450)
win.maxsize(750, 450)

# Default value for Computer
computer_options = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}

# Initialize scores
user_score = 0
computer_score = 0

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissor") or
        (user_choice == "Scissor" and computer_choice == "Paper") or
        (user_choice == "Paper" and computer_choice == "Rock")
    ):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "Computer wins!"

# Function to play a round
def play_round(user_choice):
    computer_choice = computer_options[str(random.randint(0, 2))]
    result = determine_winner(user_choice, computer_choice)
    display_choices(user_choice, computer_choice, result)

# Function to display choices and result
def display_choices(user_choice, computer_choice, result):
    l1.config(text=user_choice)
    l3.config(text=computer_choice)
    label.config(text=result)
    update_scores()

# Function to update and display scores
def update_scores():
    scores_label.config(text=f"User: {user_score}  Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_scores()
    l1.config(text="You")
    l3.config(text="Computer")
    label.config(text="")

# Create a LabelFrame
labelframe = LabelFrame(win, text="Rock Paper Scissors", font=('Century 20 bold'), labelanchor="w", bd=4,
                        bg="#dfa8f0", width=750, height=450, cursor="star")
labelframe.pack(expand=True, fill=BOTH)

# Label for Player
l1 = Label(labelframe, text="You", font=('Lucida 18 bold'))
l1.place(relx=.18, rely=.1)

# Label for VS
l2 = Label(labelframe, text="VS", font=('Lucida 18 bold'), bg="#dfa8f0")
l2.place(relx=.42, rely=.1)

# Label for Computer
l3 = Label(labelframe, text="Computer", font=('Lucida 18 bold'))
l3.place(relx=.62, rely=.1)

# Create a label to display the game result
label = Label(labelframe, text="", font=('Comic Sans MS', 15, 'bold'), bg="#dfa8f0")
label.pack(padx=150, pady=150)

# Create Button Set for Rock, Paper, and Scissor with rounded buttons
button_style = ttk.Style()
button_style.configure("Rounded.TButton", font=("Lucida", 10), borderwidth=0)
button_style.map("Rounded.TButton",
           background=[("active", "#dfa8f0"), ("!active", "#dfa8f0")],
           relief=[("active", "flat"), ("!active", "flat")],
           bordercolor=[("active", "#dfa8f0"), ("!active", "#dfa8f0")],
           highlightthickness=[("active", 0), ("!active", 0)])
b1 = ttk.Button(labelframe, text="Rock", style="Rounded.TButton", width=7, command=lambda: play_round("Rock"))
b1.place(relx=.15, rely=.62)
b2 = ttk.Button(labelframe, text="Paper", style="Rounded.TButton", width=7, command=lambda: play_round("Paper"))
b2.place(relx=.35, rely=.62)
b3 = ttk.Button(labelframe, text="Scissor", style="Rounded.TButton", width=7, command=lambda: play_round("Scissor"))
b3.place(relx=.55, rely=.62)

# Button to reset the game
reset_button = ttk.Button(labelframe, text="Reset", style="Rounded.TButton", width=7, command=reset_game)
reset_button.place(relx=.75, rely=.62)

# Create a label to display scores
scores_label = Label(labelframe, text="", font=('Lucida 16 bold'), bg="#dfa8f0")
scores_label.pack(pady=20)

# Start the tkinter main loop
win.mainloop()
