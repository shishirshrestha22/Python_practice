#PROGRAM TO CHECK THE NUMBER IS PRIME OR NOT
n=int(input("Enter the number:"))
divisors = []
for i in range (2,n):
    if n % i == 0:
        divisors.append(i)
if len (divisors) == 0:
    print(f"{n} is prime number ")
else:
    print(f"{n} isnot a prime number")
    print(f"The divisors of {n} are :",divisors)

       