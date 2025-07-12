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

running = True

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

while running:
    player = None
    computer = get_ai_choice()

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    player_history[player] += 1

    print(f"Player: {player} {emoji_dict[player]}")
    print(f"Computer: {computer} {emoji_dict[computer]}")

    if player == computer: 
        print("🤝 It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("✅ You win!")
    elif player == "paper" and computer == "rock":
        print("✅ You win!")
    elif player == "scissors" and computer == "paper":
        print("✅ You win!")
    else:
        print("❌ You Lose! Better luck next time.")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        running = False

print("👋 Thanks for playing!")