class Trapezium:
    def __init__(self,B,b,h):
        self.majorBase = B
        self.minorBase = b
        self.height = h
    def area(self):
        try:#--------------------------------------------->> Try to convert values into numbers and calculate area
            majorBase = float(self.majorBase)
            minorBase = float(self.minorBase)
            height = float(self.height)

            return (majorBase + minorBase)*height/2
        
        except ValueError:
            return "Enter the numeric value only ,non numeric value cannot be calculated"
    def __str__(self):#------------------------------------------------------------------>>>t0 define how an object should look when printed 
        shape = "triangle" if isinstance(self.minorBase,(int,float)) and self.minorBase <=0 else "trapezium"

        area_value = self.area()

        if isinstance(area_value ,(int,float)):#-------------------------------->>> isinstance is use to check the value is numeric or not
            area_text =f"{area_value:,.3f}"
        else:
            area_text = area_value  

        return (
            f"the object created is {shape}\n"
            f"-Major Base (B) = {self.majorBase}\n"
            f"-Minor Base (b) = {self.minorBase}\n"
            f"-Height (h) = {self.height}\n"
        f"-Area = {area_text}"
    )     

Tr1 = Trapezium(300, 100, 250)
Tr2 = Trapezium(21.36, 0, 9.7)
Tr3 = Trapezium("twenty", 12, 5)
Tr4 = Trapezium(20, "twelve", 5)

print(Tr1)
print()
print(Tr2)
print()
print(Tr3)
print()
print(Tr4)
