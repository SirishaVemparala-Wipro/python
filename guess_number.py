import random

try:
    # Generate a random number between 1 and 10
    random_number = random.randint(1, 10)

    # Ask the user to guess the number
    user_guess = int(input("Guess a number between 1 and 10: "))

    # Check if the guess is correct
    if user_guess == random_number:
        print("Congratulations! You guessed it!")
    else:
        print("Sorry, the correct number was {}.".format(random_number))

except ValueError:
    # Handle the case where the user enters a non-numeric value
    print("Invalid input! Please enter a number between 1 and 10.")
