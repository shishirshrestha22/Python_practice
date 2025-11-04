import random 
a=random.randint(1,100)
i=0
while i !=5:
   i=i+1
print("WELCOME TO NUMBER GUESSSING GAME😊")
print("Guess the number between 1 to 100")
b=0
attempt=0
while (b!=a):
 attempt=attempt+1
 b=int(input("enter  your guess:"))
 if b==a:
    print(" congrats!!,you made a correct guess")
 elif b>a:
    print(" your guess is high ")
 elif b<a:
    print("your guess is low ")
 
print("the correct number is:",a)
print("you made correct guess in",attempt,"times")

