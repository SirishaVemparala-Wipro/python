# Global variable
count = 10

def modify_global():
    
    global count  # Declare that we are using the global variable
    
    count += 5  # Modify the global variable
    
    print("Inside function, count =", count)

# Calling the function
modify_global()

# Printing the modified global variable outside the function
print("Outside function, count =", count)
