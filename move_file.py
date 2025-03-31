import shutil
import os

# Ask the user for the source file and destination folder
source_file = input("Enter the full path of the file to move: ")
destination_folder = input("Enter the destination folder path: ")

try:
    # Check if the source file exists
    if not os.path.isfile(source_file):
        print("Error: The file '{}' does not exist.".format(source_file))
    elif not os.path.isdir(destination_folder):
        print("Error: The destination folder '{}' does not exist.".format(destination_folder))
    else:
        # Move the file to the destination folder
        destination_path = shutil.move(source_file, destination_folder)
        print("File moved successfully to '{}'.".format(destination_path))

except Exception as e:
    print("An error occurred:", e)
