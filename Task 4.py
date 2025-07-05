import random

# Initialize scores
user_score = 0
computer_score = 0

# Choices
choices = ['Rock', 'Paper', 'Scissors']

while True:
    # Computer makes a random choice
    computer = random.choice(choices)
    
    # User input
    user = input("User Chose (Rock, Paper, Scissors or Quit): ").capitalize()
    
    # Quit condition
    if user == 'Quit':
        print("\n Exiting Game...")
        break

    # Validate user input
    if user not in choices:
        print(" Invalid choice. Please try again.\n")
        continue

    print("Computer chose:", computer)
    print("You chose:", user)

    # Game logic
    if user == computer:
        print(" It's a tie!\n")
    elif (user == 'Rock' and computer == 'Scissors') or \
         (user == 'Paper' and computer == 'Rock') or \
         (user == 'Scissors' and computer == 'Paper'):
        print("You win this round!\n")
        user_score += 1
    else:
        print(" Computer wins this round!\n")
        computer_score += 1

    # Show scoreboard
    print(f" Scoreboard => You: {user_score} | Computer: {computer_score}\n")

    # Ask to continue
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != 'yes':
        print("\n Final Score => You: {} | Computer: {}".format(user_score, computer_score))
        if user_score > computer_score:
            print(" You won the game!")
        elif user_score < computer_score:
            print(" Computer won the game!")
        else:
            print(" It's a tie overall!")
        break
