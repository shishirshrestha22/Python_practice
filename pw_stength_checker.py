# This is the program to check the strength of password

def get_password():
    password = input("Enter your password to check the strength: ")
    uppercount = 0
    lowercount = 0
    digitcount = 0
    specialcount = 0
    for i in password:
        if i.isupper():
            uppercount +=1
        elif i.islower():
            lowercount +=1
        elif i.isdigit():
            digitcount += 1
        else:
            specialcount +=1
    if len(password)>=8 and uppercount >0    and lowercount >0 and digitcount>0 and specialcount>0:
        print("Strong password")
    else:
        print("Not a strong password")
get_password()