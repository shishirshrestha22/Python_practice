#  Create a class Person with the following features:
# a. In the method (__init__) the name, surname, birthdate, address, telephone and email.
# b. Calculate the age of the person based on the current date (import datetime)
from datetime import datetime
class Person:
    def __init__(self,name,surname,birthdate,address,telephone,email):
        self.name = name
        self.surname = surname
        self.birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()             # Convert input string to datetime.date object
        self.address = address
        self.telephone = telephone
        self.email = email
    
    def cal_age(self):
        today = datetime.today().date()
        age = today.year - self.birthdate.year
        if (today.month,today.day) < (self.birthdate.month,self.birthdate.day):
            age -= 1
            return age
    
    def display(self):
        print(f"Name:  {self.name} {self.surname}")
        print(f"Birthdate: {self.birthdate}")
        print(f"Age: {self.cal_age()} years old")
        print(f"Address: {self.address}")
        print(f"Telephone: {self.telephone}")
        print(f"Email: {self.email}")
    
name = input("Enter your first name:")
surname = input("Enter your surame:")
dob = input("Enter your date of birth (yyyy-mm-dd):")

address = input("Enter your address:")

telephone = input("Enter your telephone:")

email = input("Enter your email:")

p1 =Person(name,surname,dob,address,telephone,email)
p1.display()
print("\n")
        