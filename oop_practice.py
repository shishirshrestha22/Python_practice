# OOP based  program to calculate the perimeter and area of the rectangle
class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def perimeter(self):
        perimeter = 2*(self.length+self.breadth)
        return perimeter
    def area(self):
        area = self.length *self.breadth
        return area
    def display(self):
        print("Perimeter of rectangle is: ",self.perimeter())
        print("Area of the rectangle is: ",self.area())
l = float(input("Enter the length of the rectangle: "))
b = float(input("Enter the breadth of the rectangle: "))
r1 = Rectangle(l,b)

r1.display()