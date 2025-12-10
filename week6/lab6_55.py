#Create in Python a program which receives a positive integer number from the user and displays the list
# of prime numbers smaller than the given value. The program must follow these guidelines:
# a. it must manage the entry of invalid inputs
# b. even numbers should be excluded from the check, since they cannot be prime numbers

def get_input():
    my_list = []
    num = int(input("Enter a positive integer: "))
    if num <=0:
        print("Please enter number greater than 0.")
    else:
        for i in range(num):
            if i % 2 != 0:
                for j in range(3,int(i**0.5)+1,2):
                    if i % j == 0:
                        break
                else:
                    my_list.append(i)
        print(my_list)
get_input()
             

            
        
