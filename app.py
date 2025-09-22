import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "🎉 You win!"
    else:
        return "❌ You lose!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Choices: rock, paper, scissors")
    
    while True:
        user_choice = input("Enter your choice (or 'quit' to exit): ").lower()
        if user_choice == "quit":
            print("Thanks for playing! 👋")
            break
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Try again!")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        print("-" * 20)  # separator for readability

if __name__ == "__main__":
    play_game()
