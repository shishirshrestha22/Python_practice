# THIS PROGRAM HAS BASIC USE OF LOOP AND LIST BUT THE OUPUT IS TRICKIER

mylist = [3,4,5,6,7]
for i in mylist:
    mylist.remove(i)
print(mylist)

# OUTPUT IS [4,6] WHICH SEEMS TO BE UNXPECTED 

# THE REASON BEHIND THE OUTPUT IS:

# This happens because the list gets updated in every iteration

#Iteration 1:
# i = 3
# remove 3
# List becomes: [4, 5, 6, 7]


# Iteration 2:
# Next loop index moves to index 1
# Now i = 5 (because 4 was at index 0)
# remove 5
# List becomes: [4, 6, 7]


# Iteration 3:
# Next index is index 2
# Now i = 7
# remove 7
# List becomes: [4, 6]

# Loop ends