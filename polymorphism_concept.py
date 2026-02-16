#THIS IS THE PROGWAM TO UNDER STAND THE CONCEPT OF POLYMORPHISM
class Shape:#------------------------>>> Base class i.e parent class
    def area(self):
        print("Area formula not defined for generic shape")
        
"""The base class method executes when an object of the base class is created, 
or when the child class does not override the method, or when the parent method is explicitly called using super()."""
class Rectangle(Shape):#--------------->> child class
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    
class Circle(Shape):#--------->>2nd child class
    def __init__(self,radius):
        self.radius = radius
    
    def area(self):
        return 3.14* self.radius*self.radius

def calculate_area(shapes):
    for shape in shapes:
        print(f"Area:{shape.area()}")

#main program

shapes=[
    Rectangle(12,14),Circle(9)
]
calculate_area(shapes)
