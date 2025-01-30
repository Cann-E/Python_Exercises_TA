# 1. Define an Employee Class
# Attributes:
# name (string)
# employee_id (unique identifier for each employee)
# position (string)
# salary (float)

# Methods:
# update_salary(new_salary): Updates the employee's salary.

class Employee():
    def __init__(self,name,employee_id,position,salary):
        self.name=name
        self.employee_id=employee_id
        self.position=position
        self.salary=salary

    def __str__(self):
        return (f"Name:{self.name},ID:{self.employee_id},Position:{self.position},Salary:{self.salary}")
    
    def update_salary(self,new_salary):
        self.new_salary=new_salary



# . Define an EmployeeManagement Class
# Attributes:
# employee_list (list of Employee objects)

# Methods:
# add_employee(employee): Adds a new employee to the system.
# remove_employee(employee_id): Removes an employee using their unique ID.
# display_employees(): Displays all employees in the system.
# search_employee(name): Searches for an employee by name.
# update_employee_salary(employee_id, new_salary): Updates an employee's salary.



class EmployeeManagement():
    def __init__(self):
        self.employee_list=[]

    def add_employee(self,employee):
        self.employee_list.append(employee)
        print(f" {employee} named employee is added to the System")

    def remove_employee(self,employee_id):
        found=False
        for employee in self.employee_list:
            if employee.employee_id == employee_id:
                self.employee_list.remove(employee)
                print(f"{employee.name} is removed from the system!")
                found=True
                break
        if not found:
            print(f"id: {employee_id} not found in system!")

    def display_employee(self):
        for employee in self.employee_list:
            print(f"Name:{employee.name},ID:{employee.employee_id},Position:{employee.position},Salary:{employee.salary}")


    def search_employee(self,name):
        found=False
        for employee in self.employee_list:
            if employee.name==name:
                print(f"{employee.name} has been found in the system! ")
                found=True
                break
        if not found:
            print(f"{name} not in the system")


    def update_salaray(self,employee_id,new_salary):
        found=False
        for employee in self.employee_list:
            if employee.employee_id ==employee_id:
                employee.update_salary(new_salary)
                print(f"{employee.name} salary updated to {new_salary}")
                found=True
                break
        if not found:
            print(f"{employee_id} not found cant be updated!")



# 3. Create a Dynamic Menu for Interaction
# Add a command-line menu to interact with the user dynamically. Options include:

# Add an employee.
# Remove an employee.
# View all employees.
# Search for an employee.
# Update an employee's salary.
# Exit.

res_1=input("Welcome To Employee System: \n"
            "1-Add Employee\n"
            "2-Remove an Employee\n"
            "3-View all Employees\n"
            "4-Search for an employee\n"
            "5-Update an employee's salary\n"
            "6-Exit.\n"
            ": "
            
            ).lower()

while res_1 != "6" or res_1=="exit":
    if res_1 =="1" or res_1=="add employee":
        

        