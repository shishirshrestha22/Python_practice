"""his program demonstrates polymorphism where the same method sound()
 behaves differently for different objects through inheritance and method overriding, resolved using dynamic binding."""

class Animal:
    def sound (self):
        print("All animals makes differnt sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("CAt Meows") 

class Cow(Animal):
    def sound(self):
        print("Cows moos")

#Polymorphism 

animals = [Dog(),Cat(),Cow()]
for animal in animals:
    animal.sound()