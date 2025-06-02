class Vehicle:
    def __init__(self, type):
        self.type = type

class Car(Vehicle):
    def __init__(self, type, brand):
        super().__init__(type)
        self.brand = brand

    def display(self):
        print(f"Type: {self.type}, Brand: {self.brand}")

c = Car("Four Wheeler", "Toyota")
c.display()
