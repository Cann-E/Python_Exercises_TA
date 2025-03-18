class Employee():
    def __init__(self,name,id,salary,department,job_title):
        self.name=name
        self.id=id
        self.salary=salary
        self.department=department
        self.job_title=job_title
        
    def __str__(self):
        return f"Name: {self.name},Id: {self.id}, Salary: {self.salary}$,Department: {self.department},Title: {self.job_title}"
        
    def update_salary(self,new_salary):
        self.salary=new_salary if self.salary<new_salary else self.salary
        
    def update_department(self,new_department):
        self.department=new_department if self.department != new_department else self.department
        
    def update_job_title(self,new_job_title):
        self.job_title=new_job_title if self.job_title != new_job_title else self.job_title
        
    def display_employee(self):
        print(self)
        
class EmployeeDataBase():
    def __init__(self):
        self.employee_list=[]
        
    def add_employee(self,employee):
       print(f"New Employee added in the system.Name:{employee}"); self.employee_list.append(employee)
       
    def remove_employee(self,id):
        found=False
        for employee in self.employee_list:
           if employee.id == id:
               self.employee_list.remove(employee)
               print(f"Employee Found:{employee.name}")
               found=True
               break
        if not found:
            print("No Match.")
            
    def search_employee(self,name):
        found=False
        for employee in self.employee_list:
            if employee.name==name:
                print(employee.display_employee())
                found=True
                break
        if not found:
            print("No Match Found!")
    
    
    def display_employee_all(self):
        for i in self.employee_list:
            print(i)