import os

# Ask the user for the file name
file_name = input("Enter the file name to delete: ")

# Check if the file exists
if os.path.isfile(file_name):
    try:
        os.remove(file_name)
        print("File '{}' has been deleted successfully.".format(file_name))
    except Exception as e:
        print("An error occurred while deleting the file:", e)
else:
    print("Error: The file '{}' does not exist.".format(file_name))
