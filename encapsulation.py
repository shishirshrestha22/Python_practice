"""Encapsulation is about protecting data inside a class.
It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.
This prevents accidental changes to your data and hides the internal details of how your class works."""

class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age#--------------->>> the double underscoere creates age as private which cannot be accesed and modified easily 

    def get_age(self):
        return self.__age
    
p1 = Person ("ram",22)
print("The age of ram is:",p1.get_age(),"yrs old")