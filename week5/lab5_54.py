# WRITE A FUNCTION NAMED sum (list_x,list_y) THAT
#EXPECTS  TWO LISTS OF NUMBERS AND RETURNS A NEW LIST CONTAINNING THE SUMS OF THOSE LISTS 
def sum_lists(list_x,list_y):
    newlist = []
    min_len = min(len(list_x),len(list_y)) 
    for i in range (min_len):
        newlist.append(list_x[i]+list_y[i])
    return  newlist
n1=int(input("Enter the size of first list: "))
list_x = []
for i in range(n1):
    userinput1 = int(input("Enter the elements in first the list: "))
    list_x.append(userinput1)
print("--------------------------------------------------------------")
n2=int(input("Enter the size of second list: "))
list_y = []
for i in range (n2):
    userinput2 = int(input("Enter the elements in second list: "))
    list_y.append(userinput2)
result = sum_lists(list_x,list_y)
print("The new list is ", result)
print("\n")