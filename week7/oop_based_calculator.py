# This program implements the concept of oop for simple calculator
class Calculator:
    def __init__(self,first_var,sec_var):
        self.first_var = first_var
        self.sec_var = sec_var
        
    def add(self):
        print("Result = ",self.first_var + self.sec_var)
    def sub(self):
       print("Result =" ,self.first_var - self.sec_var)
    def prod(self):
        print("Result= ",self.first_var * self.sec_var)
    def division(self):
        if self.sec_var == 0:
            print("Cannot divide by 0 !!")
        else:
            print("Result=",self.first_var / self.sec_var)
    @staticmethod#--------------------------------------------------->>> This is staticmethod inside the class and is used when methods(functions inside class)  
    #---------------------------------------------------------------->>> doesnot need the object or when self is not passed/used.
    def display():
        print("Enter the choices.")
        print("Press 1 for addition")
        print("Press 2 for subtraction")
        print("Press 3 for multiplication")
        print("Press 4 for division")
        print("Press q to exit")
        print("\n")
while True:
    Calculator.display()
    choice = input("\nEnter your choice: ")
    if choice == "q":
        break
    first_var = float(input("Enter the first number: "))
    sec_var = float(input("Enter the second number: "))
    calc = Calculator(first_var,sec_var)
    print("\n")
    if choice == "1":
        calc.add()
    elif choice == "2":
        calc.sub()
    elif choice == "3":
        calc.prod()
    elif choice == "4":
        calc.division()
    else:
        print("Invalid choice!")

        
 


