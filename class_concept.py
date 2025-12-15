# oop that takes names grade and rollno of few students and displays output
class student:
    def __init__ (self,name,level,rollno):#------------------>>  this is constructor and gets called automatically when object are created
       self.name   = name#----------------------------------->>  self is used to represent current object of a class
       self.level = level#------------------------------------>> self.name ,self.level,self.rollno are instance variables and belongs to specific object
       self.rollno = rollno

    def display(self):
        print(f"name = {self.name}, level ={self.level},rollno={self.rollno}")
s1 = student ("ram",12,1)
s2 = student("sita",12,2)
s1.display()#------------------------------->>>  it is object
s2.display()#------------------------------->>> it is 2nd object