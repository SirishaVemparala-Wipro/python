# Ask the user for source and destination filenames
source_file = "source.txt"
destination_file = "destination.txt"

try:
    # Open source file in read mode and destination file in write mode
    with open(source_file, "r") as src, open(destination_file, "w") as dest:
        # Read content from source and write to destination
        dest.write(src.read())

    print("File content copied successfully from '{}' to '{}'.".format(source_file, destination_file))

except FileNotFoundError:
    print("Error: The source file '{}' does not exist.".format(source_file))
except Exception as e:
    print("An error occurred:", e)
