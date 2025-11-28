# ADVANCED PROGRAM TO CHECK THE YEAR IS LEAP OR NOT
# In this prgram there are 2 functions  i.e is_leap to checkleap year or not
#and another function get_days_of_month to 
def is_leap(year):
    if year % 400 ==0:
        return True
    elif year % 100 ==0:
        return False
    elif year %4 ==0:
        return True
    else:
        return False
def get_days_of_month(month,year):
    if month == 1 or month ==3 or month ==5 or month ==7 or month ==8 or month == 12:
        return 31
    elif month ==4 or month == 6 or month ==9 or month == 11:
        return 30
    elif month ==2:
        if is_leap(year): #..........................function calling 
            return 29
        else:
            return 28
    else:
        return -1
year =int(input("Enter a year: "))
month =int(input("Enter month (1,12): "))
days = get_days_of_month(month,year)
if days == -1:
    print("Invlaid month number !")
else:
    print(f"In {year} year, month {month} has {days} days")