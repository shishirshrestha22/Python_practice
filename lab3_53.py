#PROGRAM TO COMPUTE SUM OF ODD DIGITS IN NON NEGATIVE INTEGER
num=int(input("Enter the non negative integer:"))
oddsum = 0
while num > 0:
    a = num % 10  #TO EXTRACT THE DIGITS FROM THE NUMBER
    if a % 2 == 1: #To check the digit is odd or not
       oddsum = oddsum + a
    num =  num //10  # this is floor division which removes the last digit so that the loop runs for each digits
print("the sum of odd digits in the number is ",oddsum)
