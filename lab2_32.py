# TO CHECK GIVEN THREE  NUMBERS ARE SIDES OF TRIANGLES OR NOT
a=float(input("enter the first side: "))
b=float(input("enter the second side: " ))
c=float(input("enter the third side: "))
if a < (b+c) and b<(a+c) and c<(b+a):
    print("sides of triangles")
    print("the perimeter is: ", a+b+c)
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print("the area of triangles is: ", area)
else:
    print("not the sides of triangles")
