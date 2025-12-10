# Create in Python the program containing the tuple: tuplex = (4, 9, ['a','b'], 123.45, 0)
# At the end of the program the tuple must be changed in the following way, applying the changes in the exact
# order given below (remember: tuples cannot be modified, they can only be reassigned, thus a list must be
# used to perform the transition from the initial tuple to the final one):
# 1. add value 7 at the end of the sequence
# 2. add tuple (10, 100, 1000) in the fourth position
# 3. add the string "bob" stored in the position with index 2
# 4. add number 3.5 in first position
# 5. add False in position -1
# 6. delete value 9
# 7. delete the element stored in the position with index -4
# Display each change on the screen (printing each time the intermediate list) and, at last, print the final tuple 

tuplex =(4,9,['a','b'],123.45,0)
list1 = list(tuplex)
list1.append(7)
print(list1)
print("\n")
list1.insert(3,(10,100,1000))
print(list1)
print("\n")
list1.insert(2,"bob")
print(list1)
print("\n")
list1.insert(0,3.5)
print(list1)
print("\n")
list1.insert(-1,False)
print(list1)
print("\n")
list1.remove(9)
print(list1)
print("\n")
del list1[-4]
print(list1)
print("\n")
print("final tuple = ", tuple(list1))