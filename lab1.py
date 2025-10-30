# PROGRAM TO CALCULATE THE POPULATION STANDARD DEVIATION
a=float(input("enter the first number : "))
b=float(input("enter the 2nd number : "))
c=float(input("enter the 3rd number : "))
d=float(input("enter the 4rth number: "))
e=float(input ("enter the 5th number "))
sum =a+b+c+d+e
mean= sum/5
print ("the sum is = ",sum)
print("the mean is : ",mean)
#subtraaction of mean from each data point
f=(a-mean)**2
g=(b-mean)**2
h=(c-mean)**2
i=(d-mean)**2
j=(e-mean)**2
#addition of squared deviations
sum1=f+g+h+i+j
#to find variance 
variance=sum1/5
#taking sqr root of the variance(standard deviation)
print("the standard deviation is : ",variance**0.5)
#OUTPUT
# enter the first number : 9
# enter the 2nd number : 8
# enter the 3rd number : 12
# enter the 4rth number: 33
# the 5th number 5
# the sum is =  67.0
# the mean is : 13.4
# the standard deviation is :  10.051865498503252