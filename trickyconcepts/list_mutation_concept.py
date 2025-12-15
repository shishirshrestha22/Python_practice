# this program gives the concept of list mutation

x = [1,2,3]
y  = x
y += [4]
print(x,y)

#output is = [1, 2, 3, 4] [1, 2, 3, 4]-------------------->> This is because +=  modifes the same object


"""Why does this happens?
 y = x does NOT create a new list
It just creates another reference to the same list in memory.
x ──► [1, 2, 3]
y ──► [1, 2, 3]   (same list!)
So:
x and y are two names

but they point to one single list
 += on lists works in-place
y += [4]
This is equivalent to:

y.extend([4])
It modifies the existing list, not a new one.

Since x and y point to the same list, both see the change.

Now memory looks like:

x ──► [1, 2, 3, 4]
y ──► [1, 2, 3, 4]
"""