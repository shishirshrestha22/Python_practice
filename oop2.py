class animals:
    def __init__(self,name,sound,types):
        self.name = name
        self.sound = sound
        self.types = types

a1 = animals("cow","moo","domestic")
print(a1.name,a1.sound,a1.types)    

a2 = animals("dog","bark","pet")
print(a2.name,a2.sound,a2.types)

a3= animals("lion","roar","wild")
print(a3.name,a3.sound,a3.types)