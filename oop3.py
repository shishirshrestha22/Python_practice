# OOP implementationn to calculate the area 

class Area:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def calculation(self):
        area = self.l*self.b
        return area

l = int(input("Enter the length: "))
b = int(input("Enter the breadth: "))
a1 = Area(l,b)
print("The area of the rectangle is :",a1.calculation())