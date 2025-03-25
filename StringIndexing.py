# Input string
string = "Python"

# First character
first_char = string[0]

# Last character
last_char = string[-1]

# Middle character(s)
mid_index = len(string) // 2

if len(string) % 2 == 0:
    middle_chars = string[mid_index - 1 : mid_index + 1]  # Two middle characters for even length

else:
    middle_chars = string[mid_index]  # Single middle character for odd length

print("String:", string)
print("First character:", first_char)
print("Last character:", last_char)
print("Middle character(s):", middle_chars)

