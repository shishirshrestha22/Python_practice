#this is the program to show the use of multiple inner class
class Computer:
    def __init__(self):
        self.cpu = self.CPU()#----------------------->>> self.CPU() calls the inner class CPU
        self.ram = self.RAM()#----------------------->>>> self.RAM calss the inner class RAM
    class CPU:
        def process(self):
            print("Processing data")
    class RAM:
        def store(self):
            print("Storing data")

computer = Computer()
computer.cpu.process()
computer.ram.store()