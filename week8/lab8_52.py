"""5.2 Create a Person class with the following features:
a. in the method (__init__) the name attribute (mandatory) and the age attribute (optional, to be set
equal to -1 by default) must be defined
b. it contains a method, called hello, which:
1. receives the name of the friend you want to greet as a mandatory parameter
2. converts the name of the friend to upper case
3. prints the following message: Hello FRIEND, I am XXX and I’m YY years old (the last part
of the sentence must be omitted if the age is not defined, i.e. it is equal to -1)"""

class Person:
    def __init__(self,name,age = -1):
        self.name = name
        self.age = age

    def hello(self,friend_name):
        friend_name = friend_name.upper()
        
        if self.age ==-1:
            print(f"Hello {friend_name}, I am {self.name}")
        else:
            print(f"Hello {friend_name} , I am {self.name} and I'am {self.age} years old")

name = input("Enter your name: ")
friend_name = input ("Enter your friend name: ")
age = int(input("ENter your age:"))
p1 = Person(name,age)
p1.hello(friend_name)

