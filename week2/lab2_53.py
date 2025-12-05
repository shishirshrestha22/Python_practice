#PROGRAM TO FIND DIGITS IN A NUMBER
a=int(input("enter the number :"))
if a>=0 and a<=9 or a<0 and a>=-9:
    print("the number contains 1 digit ")
elif a>=10 and a<=99 or a<=-10 and a>=-99:
    print("the number contains two digits")
elif a>=100 and a<=999 or a<=-100 and a>=-999:
    print("the number contains three digits")
else:
    print("the number contains more than three digits")