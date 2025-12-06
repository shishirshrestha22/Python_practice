#PROGRAM TO MAKE TRANSACTIONS
name=input("Enter your name:")
balance=1000
while True:
 print(f"\nWELCOME {name}")
 print("choose any option to continue:")
 print("Enter 1 to deposit")
 print("Enter 2 to make withdrawal")
 print("Enter 3 to check balance")
 print("Enter 4 to quit")
 option=input("Enter your choice:")
 if option == "1":
     amount=float(input("Enter amount to deposit: "))
     balance += amount
     print("Amount deposited sucessfully.Your new balance is:",balance)
 elif option == "2":
     amount=float(input("Enter amount to withdraw: "))
     if amount>1000:
         print(f"Insufficient balance, your current balance is {balance} ")
     else:
         balance-=amount
         print("Your remaining balance is :",balance)
 elif option =="3":
     print("your current balance is :",balance)
 elif option == "4":
     print("Thanks for choosing our service")
     break
 else:
     print("Invalid option ,please select (1 or 2 or 3 or 4)")

