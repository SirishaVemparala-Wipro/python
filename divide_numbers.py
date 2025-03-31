try:
    # Asking for user input
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))

    # Performing division
    result = num1 / num2

    # Printing the result
    print("Result of division:", result)

except ZeroDivisionError:
    # Handling division by zero
    print("Error: Division by zero is not allowed. Please enter a non-zero denominator.")

except ValueError:
    # Handling invalid input (non-numeric values)
    print("Error: Please enter valid numbers.")
