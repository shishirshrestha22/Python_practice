#This is the program that shows sub class inside main class

class Outer:
    def __init__(self):
        self.name = "outer"

    class Inner:
        def __init__(self):
            self.name = "Inner"

        def display (slef):
            print("HEllo from inner class")

# creating an obj of outer class
outer = Outer()
# creating obj of inner  class using outer
inner = outer.Inner()
inner.display()#---------------->>> calling the display method of inner class