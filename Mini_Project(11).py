


# 1. Define an Employee Class

# Attributes:
# name (string) – The employee’s full name
# employee_id (string) – A unique identifier for each employee
# department (string) – The employee's department (e.g., HR, Engineering, Sales)
# salary (float) – The employee's salary
# projects (dictionary) – Stores project names as keys and assigned hours as values { "Project A": 40, "Project B": 20 }




# Methods:
# update_department(new_department): Updates the employee’s department.
# update_salary(new_salary): Updates the employee’s salary.
# assign_project(project_name, hours): Assigns the employee to a project with given hours.
# update_project_hours(project_name, hours): Updates the hours worked on a specific project.
# calculate_total_hours(): Calculates the total hours assigned across all projects.


class Employee():
    def __init__(self,name,employee_id,department,salary,projects=None):
        self.name=name
        self.employee_id=employee_id
        self.department=department
        self.salary=salary
        self.projects=projects or {}
        
    def update_departments(self,new_department):
        old_department=self.department
        self.department=new_department
        print(f"Department updated to:{new_department} from: {old_department}")
        
    def update_salary(self,new_salary):
        old_salary=self.salary
        self.salary=new_salary
        print(f"Salary got updated from :{old_salary}$ to {new_salary}$")
        
    def assign_project(self, project_name, hours):
        if project_name in self.projects:  
            print(f"Project '{project_name}' already assigned. Updating hours.")
            self.projects[project_name] += hours  
        else:
            self.projects[project_name] = hours  
            print(f"Assigned new project: '{project_name}' with {hours} hours.")
            
    def update_project_hours(self,project_name,hours):
        

            
         











# 2. Define an EmployeeDatabase Class

# Attributes:
# employee_list (list of Employee objects)

# Methods:
# add_employee(employee): Adds a new employee to the system.
# remove_employee(employee_id): Removes an employee using their unique ID.
# display_employees(): Displays all employees in the system.
# search_employee(name): Searches for an employee by name.
# update_employee_department(employee_id, new_department): Updates an employee’s department.
# update_employee_salary(employee_id, new_salary): Updates an employee’s salary.
# assign_employee_to_project(employee_id, project_name, hours): Assigns an employee to a project.
# update_employee_project_hours(employee_id, project_name, hours): Updates an employee’s project hours.
# sort_employees_by_salary(): Sorts employees based on salary before displaying them.
# filter_employees_by_department(department): Filters employees based on a specific department.














# 3. Create a Dynamic Menu for Interaction
# Users can choose from the following options:

# 📌 Add an employee
# 📌 Remove an employee
# 📌 View all employees
# 📌 Search for an employee
# 📌 Update an employee’s department
# 📌 Update an employee’s salary
# 📌 Assign an employee to a project
# 📌 Update an employee’s project hours
# 📌 Sort employees by salary
# 📌 Filter employees by department
# 📌 Exit
