students = {}#------------------------------------->>> creating empty dictionary to store students data

def add_student():#---------------------------------->>> function to add students details
    name = input("Name: ")
    marks = int(input("Marks: "))
    students[name] = marks

def show_students():#----------------------------------->>>function to display students details
    for name in students:
        print(f"{name} has got {students[name]} mark")

def main():#---------------------------------------------->>> main function
    while True:
        print("1.Add student:")
        print("2.Display student")
        print("3.Exit")
        choice = input("Enter your Choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()
