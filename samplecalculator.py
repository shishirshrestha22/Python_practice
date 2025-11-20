# SAMPLE CALCULTOR  FOR TWO DIGITS
def addition (userinput1,userinput2):
    return (userinput1+userinput2)
def product (userinput1,userinput2):
    return (userinput1*userinput2)
def subtraction (userinput1,userinput2):
    return (userinput1-userinput2)
def division(userinput1,userinput2):
    return (userinput1/userinput2)
userinput1 = float(input("input number 1:"))
userinput3 = input("Select an operator(* or + or - or /)")
userinput2 = float(input ("input number 2:"))
if userinput3 == "*":
    print(f"Multiplying {userinput1} by {userinput2} = ",product(userinput1,userinput2))
elif userinput3 == "+":
    print(f"Adding {userinput1} with {userinput2} = ",addition(userinput1,userinput2))
elif userinput3 == "-":
    print(f"Subtracting {userinput2} from {userinput1} = ",subtraction(userinput1,userinput2))
elif userinput3 == "/":
    if userinput2 == 0:
        print("Dividing by 0 is not possible")
    else:
     print(f"Dividing {userinput1} by {userinput2} = ",division(userinput1,userinput2))
else:
    print("please enter valid operator and try again!")