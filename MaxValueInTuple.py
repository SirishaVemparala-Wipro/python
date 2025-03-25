def find_max_value(numbers):
    
    # Initialize max_value with the first element
    max_value=numbers[0]
    
     # Iterate through the tuple to find the maximum value
    for num in numbers:
    
        if num>max_value:
    
            max_value=num   # Update max_value if a larger number is found
    
    return max_value

tuple=(10, 25, 8, 32, 15)

print("Maximum Value: ",find_max_value(tuple))