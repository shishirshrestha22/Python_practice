
a = [0]
for i in range (3):
    a.append(i)
    a = a[i] #--------------->>  since this line converts list into integer 
                                #append() method doesnot work for integer
print(a)

"""This happens because in the first loop iteration,
 the list a is replaced by an integer using a = a[i]. After that, a is no longer a list, so calling append() on it causes an error."""

# BUT if  " a = a[i]" is not used then the list exist so 
# prints [0,0,1,2]
