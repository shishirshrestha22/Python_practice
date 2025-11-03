def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def prod(a,b):
    return a*b
def div(a,b):
    return a/b

a=int(input("enter the 1st num:"))
b=int(input("enter the 2nt num:"))

print("PRESS 1 for addtion")
print("PRESS 2. for subtraction")
print("PRESS 3. for product")
print("PRESS 4. for division")
s=int(input("enter the choice (1,2,3,4)"))

if s==1:
    print("the sum is =",add(a,b))
elif s==2:
    print("the subtraction is =",sub(a,b))
elif s==3:
    print("the product is =",prod(a,b))
elif s==4:
    print("the division is =",div(a,b))
else:
    print("invalid choice ")     
