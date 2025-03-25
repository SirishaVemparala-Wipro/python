def greet(name, msg="Welcome!"):
    print(f"Hello {name}, {msg}")

# Calling the function using positional arguments
greet("Alice")  # Uses default msg

greet("Bob", "Good morning!")  # Custom message

# Calling the function using keyword arguments
greet(name="Charlie")  # Uses default msg

greet(name="David", msg="How are you?")  # Custom message

greet(msg="Have a great day!", name="Eve")  # Order can be changed in keyword arguments
