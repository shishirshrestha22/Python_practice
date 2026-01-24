# this is the program about the concept of try and except

try:
    print(y)
except:
    print("Exception error occured")

# Since y is not defined it may have generate the error but 
#without generting error the program flows inside the except code block and executes

try:
    print("hello")#------------------>>> this prints hello 
except:
    print("something wrong happened")#-------------->>> this block doesnot get print since try block executes
else:
    print("all code is right")#----------------------->> this block also gets excutes and
