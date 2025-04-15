import math

# Take a mathematical expression as input from the user
expression = input("Enter a mathematical expression (e.g., 3+5*2): ")

try:
    # Evaluate the mathematical expression
    result = eval(expression)
    print(f"Result of the expression: {result}")
    
    # Calculate the square root of the result
    if result >= 0:
        square_root = math.sqrt(result)
        print(f"Square root of the result: {square_root}")
    else:
        print("Cannot calculate the square root of a negative number.")
        
except Exception as e:
    print(f"Error: {e}")