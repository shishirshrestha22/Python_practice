
class Bmi:
    def __init__(self,weight,height):
        self.height = height
        self.weight = weight

    def calculate_bmi(self):
        return self.weight/(self.height**2)

    def display(self):
        print("Weight:",self.weight)
        print("Height: ",self.height)
        print("Your BMI (Boday mass index) is:",self.calculate_bmi())

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
p1 = Bmi(weight,height)
p1.display()