# This is the program that takes user input in the dictionary
students_marks = { } #------------------------------->> this the empty dictionary to store the students marks
while True:
    print("Enter q to stop")
    key = input("Enter the student names : ")
    if key == "q":
        break
    value = (input("Enter the marks of the student: "))
    if value  == "q":
        break
    students_marks[key] = value
print("The students and their respective marks are: ",students_marks)
