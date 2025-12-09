# program that shows contents of math module 
import math
print("CONTENTS OF MATH MODULE ARE")
print(dir(math))
print("Help for reqired math function ")
help(math.ceil)
help(math.pow)
help(math.log)
help(math.sqrt)
help(abs)

print("\n------------------------------------\n")

num = int(input("Enter any integer (positive,zero, or negative):"))
print("Entered value: ",num)
print("# Calculations #")
print("Absolute value: ",abs(num))
print("Squared: ",num**2)
print("Cube: ",num**3)
if num < 0:
    print("Square root not possible")
else:
    print("Square root:",math.sqrt(num))
if num <=0 :
    print("Natural logarithm not posible for number < 0")
else:
    print("Natural logarithm:",math.log(num))
if num <=0:
    print("Base 10 logarithm not possible for number <= 0")
else:
    print("Base 10 logarithm: ",math.log10(num))  