

class Employee():
    def __init__(self,name,employee_id,department,salary,bonus,deductions):
        self.name=name
        self.employee_id=employee_id
        self.department=department
        self.salary=salary
        self.bonus=bonus
        self.deductions=deductions
        
    def __str__(self):
        return f"name: {self.name},id: {self.employee_id},department: {self.department},salary: {self.salary}$,bonus: {self.bonus}$,deductions: {self.deductions}$"
    
    
    def update_salary(self,new_salary):
        old_salary=self.salary
        self.salary=new_salary
        print(f"Name:{self.name} salary got updated to {new_salary}$ from {old_salary}$")
        
    def update_department(self,new_department):
        old_department=self.department
        self.department=new_department
        print(f"Department changed to {new_department} from {old_department}")
        
    def add_bonus(self,amount):
        self.salary+=amount
        print(f"Bonus: {amount}$ added to you salary!")
        return self.salary
        
        
    def deduct_tax(self,amount):
        self.salary-=amount
        print(f"Tax Deduct: {amount}$ deducted from your salary!")
        return self.salary
        
    def calculate_net_salary(self):
        print(f"Net salary is : {self.salary}$")
        return self.salary
    
class EmployeePayroll():
    def __init__(self):
        self.employee_list=[]
        
    def add_employee(self,employee):
        self.employee_list.append(employee)
        print(f"Name: {employee} added to the Payroll!")
        
    def remove_employee(self,employee_id):
        found = False
        for id in self.employee_list:
            if id.employee_id == employee_id:
                print(f"ID: {employee_id},Name: {id.name} found in the Payroll and Removed from the payroll list!")
                self.employee_list.remove(id)
                found = True
                break
        if not found:
            print(f"Id: {employee_id} not Found in the Payroll System!")
            
    def display_employee(self):
        for i in self.employee_list:
            print(f"name: {i.name},id: {i.employee_id},department: {i.department},salary: {i.salary}$,bonus: {i.bonus}$,deductions: {i.deductions}$")
        
    def search_employee(self,name):
        found = False 
        for name_ in self.employee_list:
            if name_.name == name:
                print(f"Found! Employe Name: {name}")
                found = True
                break
        if not found:
            print(f"Employee: {name} not found in the Payroll!")
            
            
    def update_employee_salary(self,employee_id,new_salary):
        found = False 
        for id in self.employee_list:
            if id.employee_id == employee_id:
                id.update_salary(new_salary)
                print(f"Employee {id} received a new salary!")
                found = True
                break
        if not found:
            print(f"Id not match! Id: {id}")
            
            
    def update_employee_department(self,employee_id,new_department):
        found = False
        for id in self.employee_list:
            if id.employee_id == employee_id:
                id.update_department(new_department)
                print(f"Department Change!")
                found = True
                break
        if not found:
            print(f"ID no match. Department not changed!")
            
    def sort_employees_by_salary(self):
        self.employee_list.sort(key= lambda employee: employee.salary)
        print("Employees sorted by salary!")
        for employee in self.employee_list:
            print(f"{employee}")
        
    def filter_employees_by_department(self,department):
        filtered_list=(list(filter( lambda employee: employee.department == department,self.employee_list)))
        if filtered_list:
            print(f"Employee deparment in: {department}")
            for employee in filtered_list:
                print(employee)
        else:
            print(f"No employees found in the department {department}")
            
    def add_employee_bonus(self,employee_id,amount):
        found = False
        for id in self.employee_list:
            if id.employee_id == employee_id:
                id.add_bonus(amount)
                print(f"Bonus applied! to {id.name}")
                found =True
                break
        if not found:
            print(f"Id {id} no match cant apply bonus")
    
    def deduct_employee_tax(self,employee_id, amount):
        found= False
        for id in self.employee_list:
            if id.employee_id ==employee_id:
                id.deduct_tax(amount)
                print(f"Tax Deducted! from {id.name}")
                found = True
                break
        if not found:
            print(f"Id no match {id} cant deduct tax!")
    
    def process_payroll(self):
        print("Processing payroll for all employees:")
        for employee in self.employee_list:
            employee.calculate_net_salary()
        
        
        
can_payroll=EmployeePayroll()   
        
while True:
    res1 = input(
        "\nWelcome To employee System:\n"
        "1 - Add a employee\n"
        "2 - Remove a employee\n"
        "3 - View all employee\n"
        "4 - Search for an employee\n"
        "5 - Update a employee salary \n"
        "6 - Update a employee department\n"
        "7 - Sort employees by salary\n"
        "8 - Filter employees by department\n"
        "9 - Add a bonus to an employee\n"
        "10 - Deduct tax from an employee's salary\n"
        "11 - Process payroll and calculate net salaries\n"
        "12 - Exit\n"
        "Enter your choice: "
    ).lower()
    
    if res1 == "1":
        name=input("Enter Name: ")
        employee_id=int(input("Enter Employee Id: "))
        department=input("Enter Department: ")
        salary=float(input("Enter Salary: "))
        bonus=float(input("Enter Bonus: "))
        deductions=float(input("Enter Deductions: "))
        employee=Employee(name,employee_id,department,salary,bonus,deductions)
        can_payroll.add_employee(employee)
        
    if res1 == "2":
        employee_id=int(input("Enter Employee Id: "))
        can_payroll.remove_employee(employee_id)
        
    if res1 == "3":
        can_payroll.display_employee()
        
    if res1 == "4":
        name=input("Enter Name: ")
        can_payroll.search_employee(name)
        
    if res1 =="5":
        employee_id=int(input("Enter Employee Id: "))
        new_salary=float(input("Enter a New Salary: "))
        can_payroll.update_employee_salary(employee_id,new_salary)
        
    if res1 == "6":
        employee_id=int(input("Enter Employee Id: "))
        new_department=input("Enter a New Department: ")
        can_payroll.update_employee_department(employee_id,new_department)
        
    if res1 == "7":
        can_payroll.sort_employees_by_salary()
        
    if res1 == "8":
        
        department=input("Enter Department: ")
        can_payroll.filter_employees_by_department(department)
        
    if res1 == "9":
        employee_id=int(input("Enter Employee Id: "))
        _bonus=float(input("Enter Bonus: "))
        can_payroll.add_employee_bonus(employee_id,_bonus)
        
    if res1 == "10":
        employee_id=int(input("Enter Employee Id: "))
        tax_deductions=float(input("Enter Deductions: "))
        can_payroll.deduct_employee_tax(employee_id,tax_deductions)
        
    if res1 == "11":
        
        can_payroll.process_payroll()
        
    if res1 == "12":
        print("Thank you for using the system!")
        break
        
        
            
        
    
    