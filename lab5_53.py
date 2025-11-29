# WRITE A FUNCTION NAMED find_greater(x_list,x_num) THAT EXPECTS 
# A LIST OF NUMBERS AND A NUMBER AND RETURNS A NEW LIST CONSISTING OF ALL THE NUMBERS IN THE LIST THAT ARE GREATER THAN THE NUMBER X
def find_greater(x_list,x_num):
    new_list =[] #.................................... new empty list to store  greater numbers
    for i in x_list:#..................................i represents the each elements in the list
          if i > x_num:
                new_list.append(i)
    return new_list
# main program
n=int(input("Enter the number of items in the list: "))
my_list =[]
for i in range (n):#.............................................................loop to take elements inn the list
        user_input = int(input("Enter the numbers in the list: "))
        my_list.append(user_input) 
num_input= int(input("enter a number: "))
result = find_greater(my_list,num_input)#...........................................function  calling

# dispaly result
print(f"New list with numbers greater than {num_input} is:",result)
print("\n")