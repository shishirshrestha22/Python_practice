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
while True:
    key = input("Enter the student name to see the marks: ",)
    if key == "q":
        break
    if key in students_marks:
        print(f"{key} has got {students_marks[key]} marks")
    else:
        print("Student not found !")
print("\n")
