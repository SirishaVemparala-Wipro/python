class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

def compare_volume(box1, box2):
    v1 = box1.volume()
    v2 = box2.volume()
    if v1 > v2:
        print("Box1 is bigger")
    elif v1 < v2:
        print("Box2 is bigger")
    else:
        print("Both boxes are equal")

b1 = Box(2, 3, 4)
b2 = Box(3, 2, 2)
compare_volume(b1, b2)
