#PROGRAM TO FIND THE MINIMUNM OF THE 3 NUMBERS
a=int((input("enter the first number : ")))
b=int((input("enter the second number : ")))
c=int((input("enter the third number : ")))
if a<b and a<c:
    print("the minimum is : ",a)
elif b<a and b<c:
    print ("the minimum is : ",b)
else:
    print("the minimum is : " ,c)