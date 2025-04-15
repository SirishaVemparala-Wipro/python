try:
    # Ask the user to enter a dictionary as a string
    user_input = input("Enter a dictionary (e.g., {'a':1, 'b':2}): ")

    # Convert the input string into an actual dictionary using eval()
    user_dict = eval(user_input)

    # Check if the result is a valid dictionary
    if isinstance(user_dict, dict):
        print("The converted dictionary is:", user_dict)
    else:
        print("Error: Please enter a valid dictionary format (e.g., {'a':1, 'b':2}).")

except (SyntaxError, NameError, TypeError):
    # Handle invalid input
    print("Error: Invalid input! Please enter a proper dictionary format (e.g., {'a':1, 'b':2}).")
