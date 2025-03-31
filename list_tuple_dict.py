# Creating a list of 5 numbers
num_list = [2, 4, 6, 8, 10]

# Converting the list into a tuple
num_tuple = tuple(num_list)

# Creating a dictionary where numbers are keys and their squares are values
num_dict = {num: num**2 for num in num_tuple}

# Printing the dictionary
print("Dictionary of numbers and their squares:", num_dict)
