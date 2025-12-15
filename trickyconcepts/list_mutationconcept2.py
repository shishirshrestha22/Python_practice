
x = [1,2,3]
y  = x
y = y + [4]
print(x,y)


# output is = [1, 2, 3] [1, 2, 3, 4]

# this is because + creates a new list which means
# x will remains same and y will be new list with a new element 4