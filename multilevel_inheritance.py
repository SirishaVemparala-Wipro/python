class LivingBeing:
    def who(self):
        print("I am a living being.")

class Animal(LivingBeing):
    def type(self):
        print("I am an animal.")

class Dog(Animal):
    def sound(self):
        print("I bark.")

d = Dog()
d.who()
d.type()
d.sound()
