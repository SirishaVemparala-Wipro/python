import random
import os

# Write 5 random numbers to the file "numbers.txt"
with open("numbers.txt", "w") as file:
    random_numbers = [random.randint(1, 100) for _ in range(5)]
    file.write("\n".join(map(str, random_numbers)) + "\n")

# Read the content of the file and print it
with open("numbers.txt", "r") as file:
    content = file.read()
    print("Content of 'numbers.txt':")
    print(content)

# Delete the file after reading
os.remove("numbers.txt")
print("\nThe file 'numbers.txt' has been deleted.")
