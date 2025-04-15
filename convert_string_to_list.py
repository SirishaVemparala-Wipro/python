try:
    # Ask the user to enter a Python list as a string
    user_input = input("Enter a list (e.g., [1,2,3,4]): ")

    # Convert the input string into an actual list using eval()
    user_list = eval(user_input)

    # Check if the result is a valid list
    if isinstance(user_list, list):
        print("The converted list is:", user_list)
    else:
        print("Error: Please enter a valid list format (e.g., [1,2,3,4]).")

except (SyntaxError, NameError, TypeError):
    # Handle invalid input
    print("Error: Invalid input! Please enter a proper list format (e.g., [1,2,3,4]).")
