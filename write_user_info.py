# Ask the user for input
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

# Open the file in write mode
with open("user_info.txt", "w") as file:
    file.write("Name: {}\n".format(name))
    file.write("Age: {}\n".format(age))
    file.write("City: {}\n".format(city))

print("User information has been saved to 'user_info.txt'.")
