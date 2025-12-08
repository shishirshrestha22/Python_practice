# PROGRAM THAT READS INTEGERS FROM USER AND STORES THEM IN LIST AND PRINT THEM IN REVERSE
# 0 TO BE USED AS A SENTINEL VALUE TO MARK THE END OF THE INPUT 
list1 =[]
while True:
    user_input = int(input("Enter the integers (0 to Stop): "))
    if user_input == 0:
        break
    
    list1.append(user_input)
print("The original list is: ",list1)
list1.reverse()
print("The reverse ordeer is: ",list1)