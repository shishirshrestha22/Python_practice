#this is simple todo list application model using the concept of oop

class TodoList:
    def __init__(self):
        self.tasks = []#--------------------------->> it is empty list to store tasks
    def add_tasks(self,task):#--------------------------------------->>> this is the method to add the new tasks
        self.tasks.append(task)
        print("TAsk added successfully")
    def view_tasks(self):#------------------------------------>>> this is method to view tasks available in the list
        if not self.tasks:
            print("No tasks available")
            return
        print("\n Your tasks: ")
        for index ,task in enumerate(self.tasks,start=1):
            print(f"{index}.{task}")
    

    def remove_task(self,taskno):#-------------------------------->>method to remove the tasks , here taskno is parameter that  
                                #--------------------------------->> recieves arugument value from 3rd conditional staement  ie ('number') is passed to it
        if taskno >= 1 and taskno <= len(self.tasks):
            removed_tasks = self.tasks.pop(taskno -1)#------------------->> removes the task acc to number here taskno -1 because index in py starts from 0
            print(f"removed task:{removed_tasks}")
        
        else:
            print("Invalid task number")


#--------------------MAIN PROGRAM--------------------
todo = TodoList()#------------->> object creation

while True:
    print("\n---- To-Do List----")
    print("1. Add task")
    print("2.View tasks")
    print("3 Remove task")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("ENter task: ")#-------------------------------------->> takes task as input
        todo.add_tasks(task)#---------------------------->> send task as arugument to 'add_tasks' method
    
    elif choice == "2":
        todo.view_tasks()##------------------------------->> calls the view_tasks method
    elif choice == "3":
        todo.view_tasks()
        number = int(input("Enter task no to remove:"))
        todo.remove_task(number)#------------------------------------------->>> receives the number as input and send to remove_task method where taskno recives it
    elif choice == "4":
        print("program exited")
        break
    else:
        print("Invalid choice!, Try Again.")

    

