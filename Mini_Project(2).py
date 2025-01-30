

class Student():
    def __init__(self,name,student_id,grades=[]):
        self.name=name
        self.student_id=student_id
        self.grades=grades
        
       
    def __str__(self):
        return f"Student(Name: {self.name}, ID: {self.student_id})" #instead of showing reference pointers it shows the data helper function

        
    def add_grade(self,grade):
        self.grade=grade
        self.grades.append(self.grade)
        
    def calculate_average(self):
        return sum(self.grades)/len(self.grades)
    
    
    
class StudentDatabase():
    def __init__(self):
        self.students_list=[]
        
    def add_student(self,student):
        self.student=student
        self.students_list.append(self.student)
        print(f"{self.student} is added to the Database!")
        
    def remove_student(self, student_id):
        found = False
        for i in self.students_list:
            if i.student_id == student_id:
                self.students_list.remove(i)
                print(f"Student {i.name} (ID: {student_id}) has been removed from the Database!")
                found = True
                break
        if not found: #shouldnt be inside the for loop
            print(f"Student with ID {student_id} is not in the Database!")

            
       
                
    def display_student(self):
        for i in self.students_list:
            print(f"Name:{i.name},ID: {i.student_id}")
            
            
    def search_students(self,name):
        found=False
        self.name=name
        for i in self.students_list:
            if i.name==name:
                print(f"{i.name} named Student Found!")
                found=True
                break
            
        if not found:#shouldnt be inside the for loop
            print(f"{name} named student is not in Database!")
                
                
    def update_student_grade(self,student_id,grade):
        found=False
        self.student_id=student_id
        self.grade=grade
        for i in self.students_list:
            if i.student_id==student_id:
                i.add_grade(grade)
                print(f"Student {i.name} (ID: {student_id}) received a new grade: {grade}. Updated grades: {i.grades}")
                found=True
                break

        if not found:
            print(f"{i.student_id} not found!")   
                
                
                
studentdatabase=StudentDatabase()

student_can=Student("Can",12354,[55,80,93])
student_tolga=Student("Tolga",22145,[80,85,89])
student_asli=Student("Asli",76890,[90,100,35])
student_lyndsey=Student("Lyndsey",101345,[60,75,87])

studentdatabase.add_student(student_can)
studentdatabase.add_student(student_tolga)
studentdatabase.add_student(student_asli)
studentdatabase.add_student(student_lyndsey)

studentdatabase.display_student()

studentdatabase.remove_student(22145)
studentdatabase.remove_student(347568)

studentdatabase.search_students("Can")
studentdatabase.search_students("Tolga")

studentdatabase.update_student_grade(76890,100)




                
                
                

                
        
    
    
    



