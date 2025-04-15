# Ask the user for the filename
filename = input("Enter the filename to read: ")

try:
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read and print the file contents line by line
        for line in file:
            print(line.strip())  # strip() removes any extra spaces or newline characters

except FileNotFoundError:
    print("Error: The file '{}' does not exist.".format(filename))
except Exception as e:
    print("An error occurred:", e)
