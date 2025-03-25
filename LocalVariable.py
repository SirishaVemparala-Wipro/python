def my_function():
    
    local_var = "I am local!"  # Local variable
    
    print(local_var)  # Accessible inside the function

# Calling the function
my_function()

# Trying to access the local variable outside the function
print(local_var)  # This will cause an error!
