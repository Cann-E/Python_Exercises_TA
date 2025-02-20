# Employee Management System - Task Description
# You are tasked with building an Employee Management System using Python's object-oriented programming concepts.

# 1. Create an Employee Class
# The Employee class should have the following attributes:
# name (string)
# employee_id (integer, unique identifier)
# department (string)
# salary (float)
# job_title (string)

# Implement methods to:
# Update the department.
# Update the salary.
# Update the job title.
# Print the employee’s details using the __str__ method.

class  Employee():
    def __init__(self,name,employee_id,department,salary,job_title):
        self.name=name
        self.employee_id=employee_id
        self.department=department
        self.salary=salary
        self.job_title=job_title
        
    def __str__(self):
        return f"Name:{self.name},ID:{self.employee_id},Department:{self.department},Salary:{self.salary}$,Job Title:{self.job_title}"
        
    def update_department(self,new_department):
        old_department=self.department
        self.department=new_department
        print(f"Department updated from {old_department} to {new_department}")
        
    def update_salary(self,new_salary):
        old_salary=self.salary
        self.salary=new_salary
        print(f"Salary updated from {old_salary}$ to {new_salary}$")
        
    def update_job_title(self,new_job_title):
        old_job_title=self.job_title
        self.job_title=new_job_title
        print(f"Job title changed from {old_job_title} to {new_job_title}")
        
    def show_employees(self):
        print(self)
        
        
        
        
        
        
        

# 2. Create an EmployeeDatabase Class
# This class should maintain a list of Employee objects.
# Implement the following methods:
# add_employee(employee): Adds a new employee to the system.
# remove_employee(employee_id): Removes an employee using their unique ID.
# display_employees(): Displays all employees in the system.
# search_employee(name): Searches for an employee by name.
# update_employee_department(employee_id, new_department): Updates an employee’s department.
# update_employee_salary(employee_id, new_salary): Updates an employee’s salary.
# update_employee_job_title(employee_id, new_title): Updates an employee’s job title.
# sort_employees_by_salary(): Sorts employees by salary in descending order and displays them.
# filter_employees_by_department(department): Filters and displays employees by a specific department.

class EmployeeDatabase():
    def __init__(self):
        self.employee_list=[]
        
    def add_employee(self,employee):
        #Add Employe
        self.employee_list.append(employee)
        print(f"New Employee added to system.Employee {employee}")
        
    def remove_employee(self,employee_id):
        #Remove Employee
        for employee in self.employee_list:
            if employee.employee_id == employee_id:
                self.employee_list.remove(employee)
                print(f"Employee {employee.name} removed from the system!")
                return
        print(f"Employee ID:{employee_id} not found!")
        
    def display_employee(self):
        for employee in self.employee_list:
            print(employee.show_employees())
            
    def search_employee(self,name):
        #Search Employee
        for employee in self.employee_list:
            if employee.name == name:
                print(f"Employee Found,Name:{employee}")    
                return
        print(f"{employee} not Found!")
        



# Deliverables
# Implement the Employee class with the required attributes and methods.
# Implement the EmployeeDatabase class with the specified functionality.
# Test your implementation by:
# Adding multiple employees.
# Searching for employees.
# Updating their details.
# Sorting and filtering based on salary and department.
