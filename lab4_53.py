#PROGRAM TO CHECK WHETHER THE GIVEN  NUMBER IS PERFECT OR NOT. 
num = int(input("Enter the number to check : "))
divisors = 0
for i in range (1,num):
    if num % i == 0:
        divisors += i
if num == divisors :
    print(f"{num} is the perfect number")
else:
    print(f"{num} is not the perfect number ")
