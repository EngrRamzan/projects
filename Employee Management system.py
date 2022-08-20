class Employee:

    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation

    def print_details(self):
        print("Name of of the employee is: ",self.name)
        print("Salary of employee is: ",self.salary)
        print("Designation of the employee:", self.designation)

    # def __str__(self) -> str:
    #     return self.name
emp_list = []
print("************Enter your choice**********: ")
choice = int(input('''    To add employee's data press: 1:
    To see all list of employees press: 2
    To delet employee press: 3
    To serach employee by name press: 4
    To update an employee press: 5
    To exit program press: 6
    Enter choice: '''))

while choice != 0:
    if choice == 1:
        name = input("Enter employee name: ")
        salary = int(input("Enter employee salary: "))
        if salary < 0:
            print("salary should be grater then zero")
            salary = input("Enter employee salary: ")
        # else:
        #     continue
        designation = input("Enter employee designation: ")
        print(f"\nA new Employee {name} add successfully: ")
        print("\n")
        emp_obj = Employee(name,salary,designation)
        emp_list.append(emp_obj)

    elif choice == 2:
        print(f"Current Employee list: \n")
        for emp_obj in emp_list:
            emp_obj.print_details()
    elif choice == 3:
        del_emp = input("Enter the name of employee to delete: ")
        for item in emp_list:
            if del_emp == item.name:
                emp_list.remove(item)
                print(f"\nThe Employee {del_emp} is successfully removed: ")
        else:
            print(f"\nRocord not found found {del_emp}: ")
        
    elif choice == 4:
        search_emp = input("Enter the name of employee to serch : ")
        for item in emp_list:
            if search_emp == item.name:
                print(f"There is a Record found for {search_emp}")
                item.print_details()
        else:
            print("records not found!")
        # flag = False
        # for item in emp_list:
        #     if search_emp == item.name:
        #         flag = True
        #         print(f"There is a Record found for {search_emp}")
        #         emp_obj.print_details()
        # if not flag:
        #     print("records not found!")
    elif choice == 5:
        update_emp = input("Enter the name of employee to update: ")
        for item in emp_list:
            if update_emp == item.name:
                new_name = input("Enter new employee name: ")
                # salary = int(input("Enter employee salary: "))
                # if salary < 0:
                #     print("salary should be grater then zero")
                #     salary = input("Enter employee salary: ")
                # else:
                #     continue
                # designation = input("Enter employee designation: ")
                print(f"\nEmployee {name}successfully updated to {new_name} : ")
                print("\n")
                emp_obj = Employee(name,salary,designation)
                emp_list.update(new_name)
        else:
            print(f"records not found for {update_emp}!")
    else:
        print("Wrong entry choice should be 1 to 5")
        
    print("************Enter your choice**********: ")
    choice = int(input('''    To add employee's data press: 1:
    To see all list of employees press: 2
    To delet employee press: 3
    To serach employee by name press: 4
    To update an employee press: 5
    To exit program press: 6
    Enter choice: '''))