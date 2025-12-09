# PROGRAM T0 MAKE SIMPLE CONATCTS APPLICATIONS
def main():
    contacts =[]
    while True:
        print("Select an operation:")
        print("v  view contacts")
        print("a  add contacts")
        print("d  delete contacts")
        print("q  quit")
        choice= input("Enter choice(v/a/d/q) - to quit:")
        if choice.lower() == "a":
            add_contacts(contacts)
        elif choice.lower() == "v":
            view_contacts(contacts)
        elif choice.lower()== "d":
            delete_contact(contacts)
        elif choice.lower() == "q":
            print("----------goodbye---------")
            break
        else:
            print("--------invalid_choice---------")
            print("Try again...")
            print("\n")
def view_contacts(contacts):
    print("------------view _contacts----------")
    print(contacts)
    print("\n")
def add_contacts(contacts):
    print("--------------add_contacts--------------")
    name=input("Enter contact name: ")
    contact=int(input("Enter contact number: "))
    contacts.append((name,contact))
    print(f"{name}- {contact} has been added into the contact.")
    print("\n")
def delete_contact(contacts):
    print("------------- delete_contacts--------------")
    if len(contacts) == 0:
        print("No contacts to delete.")
        return
    print(contacts)
    index= int(input("Enter the index to delete (0,1,2....)"))
    if 0 <= index <len(contacts):
        del contacts[index]
        print("Contact deleted.")
    else:
        print("Invalid index.")
    print("\n")
main()