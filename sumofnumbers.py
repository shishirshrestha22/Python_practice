#PROGRAM TO FIND TH SUM OF NATURAl NUMBERS 
n=int(input("Enter the number:"))
sum = 0
for i in range (1,n+1):
    sum = sum + i
print(f"The sum upto number {n} from 1  is:",sum)