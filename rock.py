import random

def display_menu():
    print("\nChoose an option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1, 2, or 3): "))
            if choice in [1, 2, 3]:
                return choices[choice - 1]
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    outcomes = {
        ('rock', 'scissors'): 'user',
        ('scissors', 'paper'): 'user',
        ('paper', 'rock'): 'user',
        ('scissors', 'rock'): 'computer',
        ('paper', 'scissors'): 'computer',
        ('rock', 'paper'): 'computer'
    }
    if user_choice == computer_choice:
        return 'tie'
    return outcomes[(user_choice, computer_choice)]

def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("Computer wins!")

def play_again():
    while True:
        again = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if again in ['yes', 'no']:
            return again == 'yes'
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)

        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f"\nScore: You {user_score} - {computer_score} Computer")

        if not play_again():
            break

    print("\nFinal Score:")
    print(f"You: {user_score} - Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
