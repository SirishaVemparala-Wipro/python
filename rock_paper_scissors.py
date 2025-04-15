import random

# Function to get computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "win"
    else:
        return "lose"

# Function to display the final score and save to a file
def save_score(wins, losses, ties):
    with open("game_score.txt", "w") as file:
        file.write(f"Final Score:\nWins: {wins}\nLosses: {losses}\nTies: {ties}\n")
    print("\nFinal score saved in 'game_score.txt'. Thank you for playing!")

# Main game loop
def play_game():
    wins = losses = ties = 0  # Initialize scores

    print("🎮 Welcome to Rock-Paper-Scissors! 🎮")
    print("Enter 'rock', 'paper', or 'scissors'. Type 'quit' to exit.")

    while True:
        try:
            # Get user input
            user_choice = input("\nYour choice: ").strip().lower()

            if user_choice == "quit":
                break  # Exit the game

            if user_choice not in ["rock", "paper", "scissors"]:
                raise ValueError("Invalid input! Please enter 'rock', 'paper', or 'scissors'.")

            # Get computer's choice
            computer_choice = get_computer_choice()
            print(f"Computer chose: {computer_choice}")

            # Determine the winner
            result = determine_winner(user_choice, computer_choice)

            if result == "win":
                print("🎉 You win!")
                wins += 1
            elif result == "lose":
                print("😢 You lose!")
                losses += 1
            else:
                print("🤝 It's a tie!")
                ties += 1

            # Display score
            print(f"Score → Wins: {wins}, Losses: {losses}, Ties: {ties}")

        except ValueError as e:
            print(e)  # Handle invalid input

    # Save the final score
    save_score(wins, losses, ties)

# Run the game
if __name__ == "__main__":
    play_game()
