# OOP practice 

class Area:#-------------------------------->>> creation of class

# Note: Here the constructor (__init__) is not needed,
# since the value of the object is directly passed to the functions

    def area_square(self,l):#----------------------->even though the constuctor is not created (self) should should be passed to track the object
        return l * l
    def area_rectangle(self,l,b):
        return l *b
    def area_circle(self,radius):
        return 3.14*(radius**2)
    
a = Area()#-------------------------------------->> creating a object of area class

print("Area of rectangle = ",a.area_rectangle(12,14))
print("Area of square is : ",a.area_square(5))
print("Area of circle is: ",a.area_circle(3))
        