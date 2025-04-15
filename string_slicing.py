# Accept a word from the user
word = input("Enter a word: ")

# Print the first 3 characters and the last 3 characters of the word
first_3 = word[:3]
last_3 = word[-3:]

print(f"First 3 characters: {first_3}")
print(f"Last 3 characters: {last_3}")

# Check if the word starts with "Py" (case-insensitive)
if word.lower().startswith("py"):
    print("The word starts with 'Py'.")
else:
    print("The word does not start with 'Py'.")
