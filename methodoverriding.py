import math

class Shape:
    def area(self):
        print("Area of shape")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

c = Circle(5)
s = Square(4)

print("Circle Area:", c.area())
print("Square Area:", s.area())
