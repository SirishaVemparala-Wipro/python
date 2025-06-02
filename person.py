class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def show(self):
        super().show()
        print(f"Roll No: {self.roll_no}")

s = Student("Bob", 20, 101)
s.show()
