
class Bmi:
    def __init__(self,weight,height):
        self.height = height
        self.weight = weight

    def calculate_bmi(self):
        return self.weight/(self.height**2)
    def bmi_status(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Healthy weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    def display(self):
        print("Weight:",self.weight ,"kg")
        print("Height: ",self.height ,"m")
        print("Your BMI (Body mass index) is:",self.calculate_bmi())
        print("BMI Status:", self.bmi_status())
        

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
p1 = Bmi(weight,height)
p1.display()