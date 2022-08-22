class Employee:
    def __init__(self, name, emp_id, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation
        self.emp_id = emp_id
    def print_detail(self):
        print("Name of of the employee is: ",self.name)
        print("Enter Emloyee ID: ",self.emp_id)
        print("Salary of employee is: ",self.salary)
        print("Designation of the employee:", self.designation)
def menue():
    print('''************Enter your choice**********)
    To add employee's data press: 1:
    To see all list of employees press: 2
    To delet employee press: 3
    To serach employee by name press: 4
    To update an employee press: 5
    To exit program press: 6''')

def get_details():
    name = input("Enter employee name: ")
    emp_id = int(input("Enter employee ID: "))
    salary = int(input("Enter employee salary: "))
    if salary < 0:
        print("salary should be grater then zero")
        salary = input("Enter employee salary: ")
    designation = input("Enter employee designation: ")
    emp_obj = Employee(name,emp_id,salary,designation)
    emp_list.append(emp_obj)
    print(f"\nA new Employee {name} add successfully: ")
def print_info():
    print(f"Current Employee list: \n")
    for emp_obj in emp_list:
        emp_obj.print_detail()
def remove_emloyee():
    del_emp = input("Enter the name of employee to delete: ")
    emp = None
    for item in emp_list:
        if del_emp == item.name:
            emp = item
            if emp:
                emp_list.remove(emp)
                print(f"\nThe Employee {del_emp} is successfully removed. ")
            else:
                print(f"\nRocord not found found {del_emp}: ")
def search_employee():
    search_emp = input("Enter the name of employee to serch : ")
    emp = None
    for item in emp_list:
        if search_emp == item.name:
            emp = item
            if emp:
                print(f"There is a Record found for {search_emp}")
                emp.print_detail()
            else:
                print("records not found!")
def update_employee():
    update_emp = input("Enter the name of employee to update : ")
    emp = None
    for item in emp_list:
        if update_emp == item.name:
            new_name = input(f"Enter new new employee name: ")
            item.name = new_name
            emp = item
            if emp:
                emp.print_detail()
                print(f"\n{update_emp} successfully updates to {new_name}.\n ")
            else:
                print(f"records not found for {update_emp}!")
def contenue_func():
    x = input("Do you want to contenue (yes/no: )")
    if x == 'yes':
        None
        # choice = int(input("Enter choice here: "))
    else:
        exit()
emp_list = []
choice = True

while choice != 0:
    menue()
    choice = int(input("Enter choice here: "))
    if choice == 1:
        get_details()
        contenue_func()
    elif choice == 2:
        print_info()
        contenue_func()
    elif choice == 3:
        remove_emloyee()
        contenue_func()
    elif choice == 4:
        search_employee()
        contenue_func()
    elif choice == 5:
        update_employee()
        contenue_func()
    elif choice == 6:
        exit()
    else:
        print("Wrong entry choice should be 1 to 5")
