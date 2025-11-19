#PROGRAM THAT LOADS INTEGER AND PRINTS ITS SECOND DIGITS FROM  LEFT , THIRD DIGIT FROM THE RIGHT 
user_input= (input("Enter integers with 3 or more digits: "))
a=user_input[1]
b=user_input[-3]
print("the second digit from left is: ",a)
print("The third digit from right is: ",b)