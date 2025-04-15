import os

# Ask the user for a filename
filename = input("Enter the filename to check: ")

# Check if the file exists
if os.path.isfile(filename):
    print("The file '{}' exists.".format(filename))
else:
    print("The file '{}' does not exist.".format(filename))
