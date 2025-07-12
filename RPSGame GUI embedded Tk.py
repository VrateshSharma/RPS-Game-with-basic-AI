import tkinter as tk
import random

options = ("rock", "paper", "scissors")
emoji_dict = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

player_history = {
    "rock": 0,
    "paper": 0,
    "scissors": 0
}

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("400x400")
window.resizable(False, False)

frame = tk.Frame(window)
frame.pack(expand=True)

def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()

def get_ai_choice():
    total_moves = sum(player_history.values())
    if total_moves == 0:
        return random.choice(options)
    most_common = max(player_history, key=player_history.get)
    if most_common == "rock":
        return "paper"
    elif most_common == "paper":
        return "scissors"
    else:
        return "rock"

def main_menu():
    clear_frame()
    tk.Label(frame, text="Rock 🪨 Paper 📄 Scissors ✂️", font=("Arial", 18)).pack(pady=20)
    tk.Button(frame, text="Play", font=("Arial", 14), width=20, command=choice_screen).pack(pady=10)
    tk.Button(frame, text="Exit", font=("Arial", 14), width=20, command=window.quit).pack(pady=10)

def choice_screen():
    clear_frame()
    tk.Label(frame, text="Choose your move:", font=("Arial", 16)).pack(pady=20)
    tk.Button(frame, text="🪨 Rock", font=("Arial", 14), width=15, command=lambda: play("rock")).pack(pady=5)
    tk.Button(frame, text="📄 Paper", font=("Arial", 14), width=15, command=lambda: play("paper")).pack(pady=5)
    tk.Button(frame, text="✂️ Scissors", font=("Arial", 14), width=15, command=lambda: play("scissors")).pack(pady=5)

def play(player_choice):
    computer_choice = random.choice(options) or get_ai_choice
    player_history[player_choice] += 1

    if player_choice == computer_choice: 
        result = "🤝 It's a tie!"
    elif player_choice == "rock" and computer_choice == "scissors":
        result = "✅ You win!"
    elif player_choice == "paper" and computer_choice == "rock":
        result = "✅ You win!"
    elif player_choice == "scissors" and computer_choice == "paper":
        result = "✅ You win!"
    else:
        result = "❌ You Lose! Better luck next time."

    result_screen(player_choice, computer_choice, result)

def result_screen(player_choice, computer_choice, result_text):
    clear_frame()
    tk.Label(frame, text=f"You: {emoji_dict[player_choice]}", font=("Arial", 16)).pack(pady=10)
    tk.Label(frame, text=f"Computer: {emoji_dict[computer_choice]}", font=("Arial", 16)).pack(pady=10)
    tk.Label(frame, text=result_text, font=("Arial", 16)).pack(pady=20)
    tk.Label(frame, text="Play again?", font=("Arial", 14)).pack(pady=10)
    tk.Button(frame, text="Yes", font=("Arial", 12), width=10, command=choice_screen).pack(pady=5)
    tk.Button(frame, text="No", font=("Arial", 12), width=10, command=exit_to_menu).pack(pady=5)

def exit_to_menu():
    print("Thanks for playing! 👋")
    main_menu()

main_menu()
window.mainloop()