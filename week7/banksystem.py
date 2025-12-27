# OOP program that implements simple banking system

class BankAccount:#----------------------------------------------------------->> class declaration
    def __init__(self,accno,money ):#----------------------------------------->> This is constructor and gets called when object is created
        self.__acc_number = accno
        self.__balance = money

    def get_balance(self):#---------------------------------------------------->> This is the method or a function inside the class tocheck the balance
        return self.__balance 
    def deposit(self,amount):
        self.__balance += amount
        print(f"{amount} has been deposited to your account ")
        print(f"your new balance is {self.__balance}")
        
    def withdraw(self,amount):
        self.__balance -= amount
        print(f"{amount} has been withdrawn")
        print(f"Your  remianing balance is {self.__balance}")
    def transfer(self,amount,acc):
        self.__balance -= amount
        acc.deposit(amount)
        print(f"{amount} has been transferd successfully.")
        print(f"Your remaining balance is { self.__balance}")
        

acc1 = BankAccount(100101,10000)#--------------------------------------------->> This is the object in the class and it represents account no1
acc2 =BankAccount(102000,5000)#--------------------------------------------->> This is another the object in the class and it represents account no2
print("\n")
while True:

    print("CHoose the opertaion to perform.")
    print("Presss 1 to deposit")
    print("Press 2 to withdraw")
    print("Press 3 to transfer money")
    print("Press 4 to check the balance")
    print("Press 5 to exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        choose_acc = int(input("Choose acc 1 or 2: "))
        deposit_amount = float(input("Enter the amount to deposit: "))
        if choose_acc == 1:
            acc1.deposit(deposit_amount)#-------------------------------------------------------->>> This is the way to call the function inside the class 
        #------------------------------------------------------------------------------------->>> and is done by object_name follwed by (.) operator and passing the arguments
        elif choose_acc ==2:
            acc2.deposit(deposit_amount)
        else:
            print("Account doesnot exist")
        

    elif choice == 2:
        choose_acc = int(input("Choose acc 1 or 2: "))
        amount = float(input("Enter the amount to withdraw: "))
        if choose_acc == 1:
            acc1.withdraw(amount)
        elif choose_acc ==2:
            acc2.withdraw(amount)
        else:
            print("Account doesnot exist")
    elif choice == 3:
        amount = int(input("Enter the amount to transfer: "))
        acc1.transfer(amount,acc2)
    elif choice == 4:
        print(f"Your current balance in accountno 1 is {acc1.get_balance()}")
        print(f"Your current balance in accno 2 is:{acc2.get_balance()}")
    elif choice == 5:
        print("Thank you for choosing our service")
        break
    else:
        print("Invalid choice!")
print("\n")


