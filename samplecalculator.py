# SAMPLE CALCULTOR  FOR TWO DIGITS
userinput1 = int(input("input number 1:"))
userinput2 = int(input ("input number 2:"))
userinput3 = input("Select an operator(* or + or - or /)")
if userinput3 == "*":
    print(f"Multiplying {userinput1} by {userinput2} = ",userinput1*userinput2)
elif userinput3 == "+":
    print(f"Adding {userinput1} with {userinput2} = ",userinput1+userinput2)
elif userinput3 == "-":
    print(f"Subtracitng {userinput2} from {userinput1} = ",userinput1-userinput2)
elif userinput3 == "/":
    print(f"Dividing {userinput1} by {userinput2} = ",userinput1/userinput2)
else:
    print("please enter valid operator and try again!")