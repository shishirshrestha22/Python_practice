# this program has the concept of the inheritance 

class Vechile:#-------------------------------------------------->> parent Class
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed 
    def display(self):
        print(f"Brand: {self.brand}")
        print(f"Speed: {self.speed} km/h")
    
# creating sub class
class Car(Vechile):
    def __init__(self, brand, speed,doors):
        super().__init__(brand, speed)#---------------------------------------------->> super() inherits the parent properties in sub class
        self.doors = doors             #--------------------------------------------->> specific features of  derived class

    def display(self):#-------------------------------------------------------------->> it is called function overriding 
        super().display()#----------------------------------------------------------->> this calls the parent class's display to reuse 
        print(f"Doors: {self.doors}")
    
class Bus(Vechile):#---------------------------->> sub class
    def __init__(self,brand ,speed,capacity):
        super().__init__(brand,speed)#----------------------------------------------->> super() inherits the parent properties in sub class
        self.capacity = capacity
    def display(self):
        super().display()
        print(f"Passenger Capacity: {self.capacity}")

car = Car("Toyota",180,4)#----------------------------------------------------------->> creating object for Car sub class
bus = Bus("Tata",100,50)#----------------------------------------------------------->> creating object for Bus sub class

print("Car Details:")
car.display()

print("\nBus Details:")
bus.display()