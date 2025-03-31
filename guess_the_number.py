import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game! 🎯")
print("Try to guess the number between 1 and 100.")

while True:
    try:
        # Taking user input
        guess = int(input("Enter your guess: "))

        # Checking conditions
        if guess < random_number:
            print("Too low! Try again. ⬆️")
        elif guess > random_number:
            print("Too high! Try again. ⬇️")
        else:
            print(f"🎉 Congratulations! You guessed the number {random_number} correctly! 🎉")
            break  # Exit loop when guessed correctly

    except ValueError:
        print("⚠️ Invalid input! Please enter a valid number.")

