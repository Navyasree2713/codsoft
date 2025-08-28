import random


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
            (user == "scissors" and computer == "paper") or \
            (user == "paper" and computer == "rock"):
        return "win"
    else:
        return "lose"


def play_game():
    user_score = 0
    computer_score = 0

    print("🎮 Welcome to Rock-Paper-Scissors!")
    print("Instructions: Type rock, paper, or scissors to play.\n")

    while True:
        user_choice = input("👉 Enter your choice (rock/paper/scissors): ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("⚠ Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"🧑 You chose: {user_choice}")
        print(f"💻 Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("😐 It's a tie!")
        elif result == "win":
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("😢 You lose this round!")
            computer_score += 1

        print(f"📊 Score -> You: {user_score} | Computer: {computer_score}\n")

        play_again = input("🔄 Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("👋 Thanks for playing! Final Score:")
            print(f"📊 You: {user_score} | Computer: {computer_score}")
            break


# Run the game
play_game()