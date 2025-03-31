import os
import shutil

file_name = "data.txt"
backup_file = "data_backup.txt"

# Check if data.txt exists
if not os.path.isfile(file_name):
    # Create and write default text if it doesn't exist
    with open(file_name, "w") as file:
        file.write("This is the default text inside data.txt.\n")
    print(f"'{file_name}' was not found, so it has been created with default content.")

# Read and print the content of data.txt
with open(file_name, "r") as file:
    content = file.read()
    print("\nContent of 'data.txt':\n")
    print(content)

# Copy data.txt to data_backup.txt
shutil.copy(file_name, backup_file)
print(f"\nFile '{file_name}' has been copied to '{backup_file}'.")

# Ask user if they want to delete the backup file
delete_backup = input("\nDo you want to delete 'data_backup.txt'? (yes/no): ").strip().lower()

if delete_backup in ["yes", "y"]:
    os.remove(backup_file)
    print("'data_backup.txt' has been deleted.")
else:
    print("'data_backup.txt' has been kept.")

