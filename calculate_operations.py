def calculate(*args, **kwargs):
    operation = kwargs.get("operation", "sum")  # Default operation is "sum"
    
    if operation == "sum":
        return sum(args)  # Return the sum of all numbers
    elif operation == "product":
        product = 1
        for num in args:
            product *= num
        return product  # Return the product of all numbers
    else:
        return "Invalid operation! Please use 'sum' or 'product'."

# Example usage
print(calculate(1, 2, 3, 4, operation="sum"))       # Output: 10
print(calculate(2, 3, 4, operation="product"))      # Output: 24
print(calculate(2, 3, 4, operation="average"))      # Output: Invalid operation! Please use 'sum' or 'product'.
