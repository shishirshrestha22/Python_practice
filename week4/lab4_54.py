# THIS IS THE ANOTHER VERSION OF CALCULATOR
def display_menu():
    print("Select an option:")
    print("1 Add")
    print("2 Subtract")
    print("3 Multiply ")
    print("4 Divide")
    print("q Quit")
def run_calculator():
    display_menu()
    choice = input("Enter your choice(1/2/3/4/q):").lower()
    print(f"You selected {choice}.")
    if choice == "1" or choice =="2" or choice =="3" or choice =="4":
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))
        if choice =="1":
            print(f"Result: {num1} + {num2}=",num1+num2)
        elif choice =="2":
            print(f"Result: {num1}-{num2}=",num1-num2)
        elif choice =="3":
            print(f"Result:{num1} * {num2}",num1*num2)
        elif choice =="4":
            if num2 == 0:
                print("Invalid!!,divisor cannot be 0")
            else:
                print(f"Result:{num1}/{num2}=",num1/num2)       
    elif choice == ("q"):
        print("Bye!")
    else:
        print("Please enter valid choice (1/2/3/4/q)")        
run_calculator()
