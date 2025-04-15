try:
    # Ask the user for a mathematical expression
    expression = input("Enter a mathematical expression (e.g., 2+3*5): ")

    # Evaluate the expression using eval()
    result = eval(expression)

    # Print the evaluated result
    print("The result of {} is: {}".format(expression, result))

except (SyntaxError, NameError, ZeroDivisionError):
    # Handle invalid input, undefined variables, or division by zero
    print("Error: Invalid mathematical expression.")
