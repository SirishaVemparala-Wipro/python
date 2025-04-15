# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handling division operations with exception handling
try:
    division = num1 / num2
    floor_division = num1 // num2
    modulus = num1 % num2
except ZeroDivisionError:
    division = "Undefined (Cannot divide by zero)"
    floor_division = "Undefined (Cannot divide by zero)"
    modulus = "Undefined (Cannot divide by zero)"

exponentiation = num1 ** num2

# Displaying results using formatted strings
print(f"\nResults for numbers {num1} and {num2}:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Floor Division: {floor_division}")
print(f"Modulus: {modulus}")
print(f"Exponentiation: {exponentiation}")
