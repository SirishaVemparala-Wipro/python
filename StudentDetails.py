def student_details(**kwargs):
    
    print("\n--- Student Details ---")
    
    # Loop through each key-value pair in kwargs
    for key, value in kwargs.items():
    
        print(f"{key.capitalize()}: {value}")# Print formatted key-value pair

student_details(name="Alice", age=20, course="Computer Science", grade="A")

student_details(name="Bob", age=22, university="MIT", major="Mathematics")
