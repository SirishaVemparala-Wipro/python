class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

emp = Employee("Alice", 50000)
emp.display_details()
