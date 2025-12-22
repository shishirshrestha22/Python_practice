#  oop practice 

class Employee:
    def __init__(self,emp_id,name,salary):
        self.name = name 
        self.emp_id = emp_id
        self.salary = salary
    
    def display(self):
        print("\nEmployee id =", self.emp_id)
        print("Employee name is: ",self.name)
        print("Monthly salary is: ",self.salary)
    def annual_salary(self):
        return self.salary*12
        
    def apply_bonus(self,percent):
        bonus = self.salary * percent /100
        self.salary = self.salary +bonus

emp1 = Employee(101,"Karan",100000)
emp1.display()
emp2 = Employee(102,"sagar",15000)
emp2.display()
print("Annual salary: ",emp2.annual_salary())
emp1.apply_bonus(10)
print("\nAfter bonus: ")
emp1.display()
emp2.apply_bonus(12)
emp2.display()