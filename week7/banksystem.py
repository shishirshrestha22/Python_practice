# OOP program that implements simple banking system

class BankAccount:
    def __init__(self,accno,money ):
        self.__acc_number = accno
        self.__balance = money
    def get_account(self):
        return self.__acc_number
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        self.__balance += amount
        print(f"{amount} has been deposited to your account ")
        print(f"your new balance is {self.__balance}")
        
    def withdraw(self,amount):
        self.__balance -= amount
        print(f"{amount} has been withdrawn")
    def transfer(self,amount,acc):
        self.__balance -= amount
        acc.deposit(amount)
        print(f"{amount} has been transferd successfully.")
        print(f"Your remaining balance is { self.__balance}")
        

acc1 = BankAccount(100101,10000)
acc2 =BankAccount(102000,5000)
acc1.transfer(1000,acc2)

