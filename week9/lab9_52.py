#oop concept

class Humanbeing:#--------------------------->> this is parent/ base class
    def __init__(self):
        self.name = ""
        self.gender =""
    
    def set_gender(self,gender):#---------------------methd to set gender
        self.gender = gender
    def get_gender(self):#--------------------------->>method to return gender value
        return self.gender
    def __str__(self):#---------------------------------------------------->>(__str__) is use to print object details
        return f"{self.name.upper()} gender is {self.gender}"
    
class Boy(Humanbeing):#------------------------->> inherits from abse class
    def __init__(self,name):
        super().__init__()
        self.name = name
        self.set_gender("male")

class Girl(Boy):#-------------------------->> this sub class has inherited from boy class to show the multilevel inheritance
    def __init__(self,name):
        super().__init__(name)
        self.set_gender("female")

#creating objects
human = Humanbeing()
human.name = "ram"
human.set_gender("unknwn")

boy =Boy("sam")
girl=Girl("sita")

print(human)
print(boy)
print(girl)
        

        