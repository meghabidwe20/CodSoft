import tkinter as tk
from tkinter import messagebox
import random
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

root.geometry("400x300")
frame = tk.Frame(root)
frame.pack(pady=20)

user_choice_label = tk.Label(frame, text="Your choice: ", font=('Helvetica', 12))
user_choice_label.grid(row=0, column=0, padx=10)

computer_choice_label = tk.Label(frame, text="Computer's choice: ", font=('Helvetica', 12))
computer_choice_label.grid(row=1, column=0, padx=10)

result_label = tk.Label(frame, text="", font=('Helvetica', 14))
result_label.grid(row=2, columnspan=3, pady=20)

user_score_label = tk.Label(root, text="Your score: 0", font=('Helvetica', 12))
user_score_label.pack(side=tk.LEFT, padx=20)

computer_score_label = tk.Label(root, text="Computer's score: 0", font=('Helvetica', 12))
computer_score_label.pack(side=tk.RIGHT, padx=20)

user_score = 0
computer_score = 0

def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        user_score += 1
        user_score_label.config(text=f"Your score: {user_score}")
        return "You win!"
    else:
        computer_score += 1
        computer_score_label.config(text=f"Computer's score: {computer_score}")
        return "You lose!"
    
def user_choice(choice):
    computer_choice = get_computer_choice()
    user_choice_label.config(text=f"Your choice: {choice}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")
    result = determine_winner(choice, computer_choice)
    result_label.config(text=result)

rock_button = tk.Button(frame, text="Rock", width=10, command=lambda: user_choice('Rock'))
rock_button.grid(row=0, column=1, padx=10)

paper_button = tk.Button(frame, text="Paper", width=10, command=lambda: user_choice('Paper'))
paper_button.grid(row=0, column=2, padx=10)

scissors_button = tk.Button(frame, text="Scissors", width=10, command=lambda: user_choice('Scissors'))
scissors_button.grid(row=0, column=3, padx=10)

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_score_label.config(text="Your score: 0")
    computer_score_label.config(text="Computer's score: 0")
    user_choice_label.config(text="Your choice: ")
    computer_choice_label.config(text="Computer's choice: ")
    result_label.config(text="")
    
reset_button = tk.Button(root, text="Play Again", command=reset_game)
reset_button.pack(pady=10)

root.mainloop()
