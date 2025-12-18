student1 = {
    "name":"Ram",
     "roll no":"1",
     "level":"high school"
    
}
student2 ={
    "name":"Shyam",
     "roll no":"2",
     "level":"undergrad"
    
}
student3 = {
    "name":"hari",
     "roll no":"3",
     "level":"undergraduate"
}

print(student1)#--------------------------------->>> to print whole dictionary 
print(student1.keys())#--------------------------->>> to print the keys of dictionary
print("\n")
print(student2)
print(student2.keys())
print(student2.values())#---------------------------->>> to print the values of the dictionary
print("\n")
print(student3["name"])#------------------------------>>> to access the single value associated with key
print(student3)
print(student3.get("level"))#--------------------------->>> to access the value if donot exist returns None

print(student2.get("class"))#--------------------------->> returns None since it doest not exist in  the dictionary
