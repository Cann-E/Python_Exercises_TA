

class Student():
    def __init__(self,name,student_id,major,gpa):
        self.name=name
        self.student_id=student_id
        self.major=major
        self.gpa=gpa
        self.courses={}
        
    def __str__(self):
        return f"Name: {self.name},ID: {self.student_id},Major: {self.major},GPA: {self.gpa}\nCurrent Courses {self.courses}"
    
    def update_gpa(self,new_gpa):
        old_gpa=self.gpa
        self.gpa=new_gpa
        print(f"GPA Updated from {old_gpa} to {new_gpa} !")
        
    def update_major(self,new_major):
        self.major=new_major
        print(f"Student changed Major From {self.major} to {new_major}")
        
    def enroll_course(self,course_name):
        self.courses[course_name]=None  #adding in to the dictionaries!!!!
        print(f"Enrolled in new Course : {course_name}")
        
    def update_course_grade(self,course_name,grade):
        if course_name in self.courses:
            self.courses[course_name]=grade  #like append in the lists it attaches the grade with the course name!!!
            print(f"Grade for {course_name} updated to: {grade}")
        else:
            print(f"Course {course_name} not found!")
            
    def calculate_gpa(self):
        valid_grades = []
        for grade in self.courses.values(): #for values value() for names keys()
            if grade is not None:
                valid_grades.append(grade)

        if valid_grades:
            self.gpa=sum(valid_grades)/len(valid_grades)
            print(f"Updated GPA: {self.gpa}")
            return self.gpa
        else:
            print("No grades available to calculate GPA.")
            return None
        
        
class StudentDatabase():
    def __init__(self):
        self.student_list=[]
        
        
    def add_student(self,student):
        self.student_list.append(student)
        print(f"New Student: {student},added to the system!")
        
        
    def remove_student(self,student_id):
        found=False
        for id in self.student_list:
            if id.student_id == student_id:
                self.student_list.remove(id)
                print(f"ID: {id},Name: {id.name} has been removed from the system!")
                found=True
                break
        if not found:
            print(f"ID: {student_id} is not associated with anyone in the system!")
            
    def display_student(self):
        for student in self.student_list:
            print(f"Name: {student.name},ID: {student.student_id},Major: {student.major},GPA: {student.gpa}\nCurrent Courses {student.courses}")
            
            
    def search_students(self,name):
        found=False
        for student in self.student_list:
            if student.name == name :
                print(f"{student.name} has been found in the system!")
                found=True
                break
        if not found:
            print(f"{name} named student is not found in the system!")
            
            
    def update_student_gpa(self,student_id,new_gpa):
        found=False
        for id in self.student_list:
            if id.student_id == student_id:
                id.update_gpa(new_gpa)
                print(f"ID: {student_id},Name: {id.name} ,GPA has been updated to {new_gpa}")
                found=True
                break
        if not found:
            print(f"{student_id} Not Found!")
            
            
    def update_student_major(self,student_id,new_major):
        found=False
        for id in self.student_list:
            if id.student_id == student_id:
                id.update_major(new_major)
                print(f"Name:{id.name} has changed to major to {new_major}" )
                found=True
                break
        if not found:
            print(f"ID: {student_id} major cant be changed student not found!")
            
    
    def sort_student_by_gpa(self):
        self.student_list.sort(key=lambda student: student.gpa,reverse=True) #Students sorted by GPA!"
        print("Students sorted by GPA!")
        print(f"{self.student_list}")
        
        
    def filter_students_by_major(self, major):
        filtered_list = list(filter(lambda student: student.major == major, self.student_list))
    
        if filtered_list:
            print(f"Students majoring in {major}:")
            for student in filtered_list:
                print(student)
        else:
            print(f"No students found for the major: {major}")
            
            
            
    def enroll_student_in_course(self,student_id,enroll_course):
        found = False
        for id in self.student_list:
            if id.student_id == student_id:
                id.enroll_course(enroll_course)
                print(f"{id.name} has been enrolled in a new class: {enroll_course}")
                found=True
                break
        if not found:
            print(f"{student_id} id not found to enroll!!")
    
    def update_student_course_grade(self,student_id,course_name,update_grade):
        found=False
        for id in self.student_list:
            if id.student_id == student_id:
                id.update_course_grade(course_name,update_grade)
                print(f"{id.name}'s {course_name} course grade is updated to {update_grade}")
                found=True
                break
        if not found:
            print(f"{student_id} id not found to update!")  
    
    def calculate_student_gpa(self,student_id):
        found = False
        for id in self.student_list:
            if id.student_id == student_id:
                avg=id.calculate_gpa()
                print(f"ID: {id},calculated grade is {avg}")
                found =True
                return avg
        if not found:
            print(f"{student_id} id not found to CALCULATE!")  
                

                
student_database=StudentDatabase()

while True:
    res_1 = input(
        "\nWelcome To Student System:\n"
        "1 - Add a student\n"
        "2 - Remove a student\n"
        "3 - View all students\n"
        "4 - Search for a student\n"
        "5 - Update a students GPA \n"
        "6 - Update a students Major\n"
        "7 - Sort students by GPA\n"
        "8 - Filter students by major\n"
        "9 - Enroll a student in a course\n"
        "10 - Update a students course Grade\n"
        "11 - Calculate a students Gpa Dynamically\n"
        "12 - Exit\n"
        "Enter your choice: "
    ).lower()
    
    if res_1 ==  "1"  :
        name=input("Please Enter Name: ")
        student_id=int(input("Please Enter Student ID: "))
        major=input("Please Enter Students Major: ")
        gpa=float(input("Please Enter Students Gpa: "))
        student=Student(name,student_id,major,gpa)
        student_database.add_student(student)  
        
    elif res_1 == "2" :
       student_id=int(input("Please Enter Student ID: "))
       student_database.remove_student(student_id)
    
    elif res_1 == "3":
        student_database.display_student()
        
    elif res_1 == "4":
        name=input("Please Enter Name: ")
        student_database.search_students(name)
        
    elif res_1 == "5":
        student_id=int(input("Please Enter Student ID: "))
        new_gpa=float(input("Please Enter the Updated Gpa: "))
        student_database.update_student_gpa(student_id,new_gpa)
        
    elif res_1 == "6":
        student_id=int(input("Please Enter Student ID: "))
        new_major=input("Please Enter Students New Major: ")
        student_database.update_student_major(student_id,new_major)
        
    elif res_1 == "7":
        student_database.sort_student_by_gpa()
        
    elif res_1 == "8":
        filter_major=input("Please Enter the Major you want to be filtered: ")
        student_database.filter_students_by_major(filter_major)
        
    elif res_1 == "9":
        student_id=int(input("Please Enter Student ID: "))
        enroll_course=input("Please Enter the course you want to be Enrolled: ")
        student_database.enroll_student_in_course(student_id,enroll_course)
        
    elif res_1 == "10":
        student_id=int(input("Please Enter Student ID: "))
        course_name=input("Please Enter the Course Name: ")
        update_grade=int(input("Please Enter the updated Grade: "))
        student_database.update_student_course_grade(student_id,course_name,update_grade)
        
    elif res_1 == "11":
        student_id=int(input("Please Enter Student ID: "))
        student_database.calculate_student_gpa(student_id)
        
    elif res_1 == "12":
        print("Thank you For Using the Student Database System!")
        break
        
        
          