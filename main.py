from game import get_computer_choice, determine_winner

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Choices: rock,paper,scissors")
    
    while True:
        user_choice = input("Enter your choice (or 'quit' to exit): ").lower()
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
if __name__ == "__main__":
    play_game()