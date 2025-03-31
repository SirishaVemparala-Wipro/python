try:
    # Asking for the filename from the user
    filename = input("Enter the filename to open: ")

    # Trying to open the file in read mode
    with open(filename, "r") as file:
        content = file.read()
        print("File content:\n", content)

except FileNotFoundError:
    # Handling the case where the file does not exist
    print("Error: The file '{}' was not found. Please check the filename and try again.".format(filename))
