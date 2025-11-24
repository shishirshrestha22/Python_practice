# THIS PROGRAM PRINTS THE  RECTANGLE PATTERN
def pattern():
    rows = int(input("enter the no of rows"))
    columns=int(input("enter column"))
    for i in range (rows):#.....................................outer loop for rows
        for j in range (columns):#...............................inner loop for columns
            print("*",end = " ")#.......................print star in same  line in inner loop
        print()#..................................to print in new line after inner loop
pattern()    