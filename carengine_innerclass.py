#THIS IS THE PROGRAM THAT SHOWS THE CAR ENGINE USING INNER CLASS CONCEPT
#outer class
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()#----------->>>self.Engine()
#                            This is creating a new object of the inner Engine class.
    
    class Engine:
        def __init__(self):
            self.status = "Off"
        
        def start(self):
            self.status = "running"
            print("ENgine started")
        def stop(self):
            self.status = "Off"
            print("ENgine stopped ")
    def drive (self):
        if self.engine.status == "running":
            print(f"Driving the {self.brand} {self.model}")
        else:
            print("Start the engine first")  

car = Car("Toyota","Corolla")
car.drive()
car.engine.start()
car.drive()