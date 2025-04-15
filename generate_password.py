import random
import string

try:
    # Ask the user for the desired password length
    length = int(input("Enter the desired password length: "))

    if length <= 0:
        print("Error: Password length should be greater than zero.")
    else:
        # Define characters to include in the password
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate a random password
        password = "".join(random.choice(characters) for _ in range(length))

        # Display the generated password
        print("Your randomly generated password is: {}".format(password))

except ValueError:
    # Handle invalid input (non-numeric values)
    print("Error: Please enter a valid number for the password length.")
