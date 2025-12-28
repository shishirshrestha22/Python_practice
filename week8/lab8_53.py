# This is the Opp program to perform calculation on rectangle

class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def area(self):
        return self.length *self.breadth
    def display(self):
        print(f"Length = {self.length}")
        print(f"Breadth = {self.breadth}")
        print(f"The perimeter of the rectangle is:",self.perimeter())
        print(f"The area of the rectangle is:",self.area())


while True:
    print("ENter length = 0 to exit")
    length = float(input("Enter the length of the rectangle:"))
    if length == 0:
        break
    breadth = float(input("Enter the breadth of the rectangle:"))
    
    r = Rectangle(length,breadth)
    r.display()
