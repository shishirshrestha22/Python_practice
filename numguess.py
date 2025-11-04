import random 
a=random.randint(1,100)
i=0
while i !=5:
   i=i+1
print("WELCOME TO NUMBER GUESSSING GAME😊")
b=0
attempt=0
while (b!=a):
 attempt=attempt+1
 b=int(input("enter  your guess:"))
 if b==a:
    print(" congrats!!,correct guess")
 elif b>a:
    print("high guess")
 elif b<a:
    print("low guess")
 
print("the correct number is:",a)
print("you made correct guess in",attempt,"times")
