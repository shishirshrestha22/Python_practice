""" Even though the tuple is immutable and if "list" is used as tuple element 
 then the list operation is possible """

#for example

t = (1, [2, 3], 4)
print("Original tuple: ",t)
t[1].append(5)
print("After change: ",t)