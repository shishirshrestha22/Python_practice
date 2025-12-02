#PRACTICE OF DICTIONARY DATA TYPES
car = {"brand":"Ford","model":"Mustang","year":1964}
a=car.keys()
print(a)#.............to print keys before change
car["colour"]="white"
print(a)#..................to print keys after change
x=car.values()
print(x) #....................to print dictionary values before changes
car["year"] = 2020
print(x)#........................to print dictionary vlaues after  year update