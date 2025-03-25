def outer_function(num):
    
    # Inner function to calculate the square
    def inner_function(n):
        return n * n
    
    # Calling the inner function
    square = inner_function(num)
    
    # Printing the result
    print(f"The square of {num} is: {square}")

# Example usage
outer_function(5)

outer_function(8)
