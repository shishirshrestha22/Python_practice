# PROGRAM THAT SUMS THE SQUARES UPTO USER INPUT
num=int(input("Enter the number: "))
total=0
for i in range (1,num+1):
    total = total + i*i

print("The total sum of squares is :",total)
