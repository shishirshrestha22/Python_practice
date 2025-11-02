a=int(input("enter the first number "))
b=int(input("enter the 2nd number "))
c=int(input("enter the 3rd number "))
if a>b and a<c or a>c and a<b:
    print("the medium is: " ,a)
elif b>a and b<c or b<a and b>c:
    print("the medium is : ",b)
else:
    print("the medium is :",c)
