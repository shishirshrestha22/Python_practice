# program to calculate the roots of quadratic equation
A=float(input("Enter the coff.. of  x**2 (A) : "))
B=float(input("Enter the coff.. of  x (B) : "))
C=float(input("Enter the constant (C) : " ))
print("The value of A = ", A)
print("The value of B = ",B)
print("The value of C = ", C)
d=(B**2-4*A*C)**0.5
root1=(-B+d)/(2*A)
root2=(-B-d)/(2*A)
print("the first root is: ",root1)
print("the second root is :",root2)
# Sample output

# WHEN A = 1 , B=0 ,C = -4
   # root1 = 2.0
   #root2 = -2.0

#WHEN A=1 ,B=5,C=-36
   #root1 = 4.0 & root2 = -9.0

#WHEN A=2 ,B=7.5,C=6
  #root1= -1.1569296691827464
  #root2= -2.5930703308172536

#WHEN A=0 ,B=3.5,C=8

   # THIS GENERATES ERROR SINCE THE DENOMINATOR BECOMES 0 IN root1 & root2
