def display_main_menu():
    print("Welcome to your To Do List ")
    print("1. Task Management ")
    print("2. Task Display ")
    print("3. End Program ")

display_main_menu()   
option = input("What option would you like to choose? ")

tasks = []

if option == "1":
    print("Add tasks ")
    task = input("Enter ")
    tasks.append(task)
if option == "2":
    print(tasks)

if option == "3":
    quit()



while True:
    display_main_menu()
    option = input("What option would you like to choose? ")
    
    
    if option == "1":
        print("Add tasks ")
        task = input("Enter ")
        tasks.append(task)
    if option == "2":
        print(tasks)
    if option == "3":
        quit()
     
       

    


