# first program oop

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Ram", 27)

print(p1.name)
print(p1.age)

p2 = Person("shyam",23)
print(p2.name)
print(p2.age)