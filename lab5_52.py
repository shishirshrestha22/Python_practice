#THIS PROGRAM GETS TWO LIST AS INPUT AND CHECKS IF THEY HAVE AT LEAT ONE COMMON MEMBER OR NOT
list1 =[]
list2 =[]
print("\n")
n1=int(input("enter the number of elemets in  first list: "))
for i in range(1,n1+1):
    user_input1 = input(f"Enter the {i} elements in the first list: ")
    list1.append(user_input1)
print("...........................................................................")
n2=int(input("Enter the number of elements in second list: "))
for i in range (1,n2+1):
    user_input2 = input(f"Enter the {i} elements the in second list: ")
    list2.append(user_input2)
if set (list1) & set(list2):
    print("There is at least one same element")
else:
    print("There is no any same element")