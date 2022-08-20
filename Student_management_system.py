std_list = []
def menue():

    print("********************Menue***************: ")
    print("************Enter your choice**********: ")
choice = int(input('''  
                To add a new Student press: 1
                To see all list of Student press: 2
                To delet Student press: 3
                To serach Student by name press: 4
                To update stdent name press: 5
                To exit program press: 6
                Enter choice: '''))
def get_info():
    name = input("Enter student name: ")
    # roll_no = input("Enter student roll number: ")
    # std_fee = input("Enter student fee: ")
    print(f"\nA new student {name} add successfully: ")
    std_list.append(name)
    # std_list.append(roll_no)
    # std_list.append(std_fee)

def print_details():
    print("Current student list:")
    for students in std_list:
        print(students)
def delete_student():
    del_std = input("Enter name to remove: ")
    if del_std in std_list:
        a = std_list.index(del_std)
        std_list.remove(del_std)
        print(f"{del_std} sucesfuly removed") 
        # print(f"There is a record found for {search_std}")
        # print(f"Name of student {search_std}")
    else:
        print(f"No record found for {del_std}")
    # del_std = input("Enter student name to delete: ")
    # std_list.remove(del_std)
    # print(f"{del_std} succesfuly remove")
def search_student():
    search_std = input("Enter name to find: ")
    if search_std in std_list:
        x = std_list.index(search_std)
        print(f"{std_list[x]} preasent in the list")
        # print(f"There is a record found for {search_std}")
        # print(f"Name of student {search_std}")
    else:
                print(f"No record found for {search_std}")
def updade_new_student():
    update_std = input("Enter name of student to update: ")
    if update_std in std_list:
        x = std_list.index(update_std)
        new_std = input("Enter new student: ")
        std_list[x] = new_std
        print(f"{update_std} sucesfuly updated to {new_std}")
    else:
        print(f"No record found for {update_std}")
while choice != 0:
    if choice == 1:
        get_info()
    elif choice == 2:
        print_details()
    elif choice == 3:
        delete_student()
    elif choice == 4:
        search_student()
    elif choice == 5:
        updade_new_student()
    elif choice == 6:
        exit()
    else:
        print("Invalid intry")
    #menue()
    #print()
    choice = int(input('''  
            To add a new Student press: 1
                To see all list of Student press: 2
                To delet Student press: 3
                To serach Student by name press: 4
                To update stdent name press: 5
                To exit program press: 6
                Enter choice: '''))