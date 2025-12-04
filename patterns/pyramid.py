# This is the program that prints pyramid patterns 
def print_full_pyramid(level,symbol):
    for i in range (1,level+1):
        spaces = level- i
        a = 2*i -1
        print(" "*spaces + a*symbol)
rows = int(input("Enter the no. of rows: "))
pattern = input("Enter the symbol: ")
print_full_pyramid(rows,pattern)
