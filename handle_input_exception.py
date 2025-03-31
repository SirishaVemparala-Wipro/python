try:
    # Asking for user input
    user_input = input("Enter a number: ")
    
    # Converting input to integer
    number = int(user_input)
    
    # Printing the valid number
    print("You entered the number:", number)

except ValueError:
    # Handling the case where input is not a number
    print("Invalid input! Please enter a valid number.")
