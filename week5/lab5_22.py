# PRACTICE PROGRAM FOR DICTIONARY
dic = {'Ogerta':"2003",
       'Sara':'1809',
       'Moad':'1912',
       'Aliyuda':'2003',
       'Kurtis':'9834',
       'Albaarini':'1990',
       'Abdel':'2001',
       'Syed':'1996',
       }
username = input("Enter your username: ").strip()
if username in dic:
    password = input("Enter password: ")
    if dic[username] == password:
        print("You are now logged into the system.")
    else:
        print("Invalid password.")
else:
    print("You are not valid user.")        