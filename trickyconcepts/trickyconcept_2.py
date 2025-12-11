for i in range(3):
    pass
print(i)


#In Python, a for loop does not create a new scope.
# Variables created inside the loop belong to the outer scope (same as global/local function scope).
# So this:
# for i in range(3):
# assigns values to i in this order:

# i = 0
# i = 1
# i = 2

# Then the loop finishes.
# After the loop, i still exists!
# After the loop ends, the last assigned value remains in memory.
# So:
# print(i)
# prints: 2


# Because range(3) generates: 0, 1, 2
# and the loop ends after i = 2.