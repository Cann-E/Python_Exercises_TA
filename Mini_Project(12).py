# 1. Define a Student Class

# # Attributes:
# # name (string) – The student’s full name
# # student_id (string) – A unique identifier for each student
# # major (string) – The student's major (e.g., Computer Science, Biology)
# # gpa (float) – The student's GPA (Grade Point Average)
# # courses (dictionary) – Stores course names as keys and grades as values { "Math": 90, "History": 85 }

# # Methods:
# # update_major(new_major): Updates the student’s major.
# # update_gpa(new_gpa): Updates the student’s GPA.
# # enroll_course(course_name): Enrolls the student in a course (default grade None).
# # update_course_grade(course_name, grade): Updates a student’s grade in a specific course.
# # calculate_gpa(): Calculates the GPA dynamically based on course grades.


class Student():
    def __init__(self,name,student_id,major,gpa,courses=None):
        self.name=name
        self.student_id=student_id
        self.major=major
        self.gpa=gpa
        self.courses=courses or {}
        
    def __str__(self):
<<<<<<< HEAD
        return f"Name:{self.name},Id:{self.id},Major:{self.major},Gpa:{self.gpa}\n Courses:{self.courses}"
=======
        return f"Name:{self.name},ID:{self.student_id},Major:{self.major},Gpa:{self.gpa}"
>>>>>>> ff263ffafadedfac74e635dba5d6dfcf32713c67
        
    def update_major(self,new_major):
        old_major=self.major
        self.major=new_major
        print(f"Major changed from {old_major} to {new_major}")
        
    def update_gpa(self,new_gpa):
        old_gpa=self.gpa
        self.gpa=new_gpa
        print(f"Gpa updated from {old_gpa} to {new_gpa}")
        
    def enroll_course(self,course_name):
        if course_name not in self.courses:
            self.courses[course_name]=None
            print(f"Student Enrolled in {course_name}")            
        else:
            print(f"{course_name} already enrolled!")
            
    def update_course_grade(self,course_name,grade):
        if course_name in self.courses:
            self.courses[course_name]=grade
            print(f"Grade updated {course_name}:{grade}")
        else:
            print(f"{course_name} not found")
            
    def calculate_gpa(self):
        valid_grades=[]
        for grades in self.courses.values():
            if grades is not None:
                valid_grades.append(grades)
        
        if valid_grades:
            self.gpa=sum(valid_grades)/len(valid_grades)
            print(f"Gpa is : {self.gpa}")
            return self.gpa
        else:
            print("Gpa not available!")
            return None






# # 2. Define a StudentDatabase Class

# # Attributes:
# # student_list (list of Student objects)

# # Methods:
# # add_student(student): Adds a new student to the system.
# # remove_student(student_id): Removes a student using their unique ID.
# # display_students(): Displays all students in the system.
# # search_student(name): Searches for a student by name.
# # update_student_major(student_id, new_major): Updates a student’s major.
# # update_student_gpa(student_id, new_gpa): Updates a student’s GPA.
# # enroll_student_in_course(student_id, course_name): Enrolls a student in a course.
# # update_student_course_grade(student_id, course_name, grade): Updates a student’s grade.
# # sort_students_by_gpa(): Sorts students based on GPA before displaying them.
# # filter_students_by_major(major): Filters students based on a specific major.


<<<<<<< HEAD
class StudentDatabase():
    def __init__(self):
        self.student_list=[]
        
    def add_student(self,student):
        self.student_list.append(student)
        print(f"{student} added to the system")
        
    def remove_student(self,student_id):
        found=False
        for student in self.student_list:
            if student.student_id==student_id:
                self.student_list.remove(student)
                print(f"Student with id:{student_id},name:{student.name} removed from the system!")
                found=True
                break
        if not found:
                print(f"{student_id} not in the system!")
                
    def display_student(self):
        for stu in self.student_list:
            print(f"Name:{stu.name},Id:{stu.id},Major:{stu.major},Gpa:{stu.gpa}")
        
    def search_student(self,name):
        found=False
        for nam in self.student_list:
            if nam.name==name:
                print(f"{name} has been found in the system!")
                found=False
                break
        if not found:
            print(f"{name} not found in the system")
        
=======
class StudentDatabase:
    def __init__(self):
        self.student_list = []
        
    def add_student(self, student):
        """Adds a new student to the system."""
        self.student_list.append(student)
        print(f"Student {student.name} (ID: {student.student_id}) has been added to the system!")

    def remove_student(self, student_id):
        """Removes a student using their unique ID."""
        for student in self.student_list:
            if student.student_id == student_id:
                self.student_list.remove(student)
                print(f"ID: {student_id}, Name: {student.name} has been removed!")
                return
        print(f"ID: {student_id} not found in the system!")

    def display_students(self):
        """Displays all students in the system."""
        if not self.student_list:
            print("No students in the database.")
            return
        for student in self.student_list:
            print(student)  # Uses the __str__ method of Student

    def search_student(self, name):
        """Searches for a student by name."""
        for student in self.student_list:
            if student.name == name:
                print(f"Student found: {student}")
                return
        print(f"Name: {name} not found!")

    def update_student_major(self, student_id, new_major):
        """Updates a student's major."""
        for student in self.student_list:
            if student.student_id == student_id:
                student.update_major(new_major)
                return
        print(f"ID: {student_id} not found, can't change major.")

    def update_student_gpa(self, student_id, new_gpa):
        """Updates a student's GPA."""
        for student in self.student_list:
            if student.student_id == student_id:
                student.update_gpa(new_gpa)
                return
        print(f"ID: {student_id} not found, can't update GPA.")

    def enroll_student_in_course(self, student_id, course_name):
        """Enrolls a student in a course."""
        for student in self.student_list:
            if student.student_id == student_id:
                student.enroll_course(course_name)
                return
        print(f"ID: {student_id} not found, couldn't enroll.")
        
        
    def update_student_course_grade(self,student_id,course_name,grade):
        """Updates a student grade in a course"""
        for student in self.student_list:
            if student.student_id == student_id:
                student.update_course_grade(course_name,grade)
                return
        print(f"ID:{student_id} not found,{course_name} grade not updated!")
        
    def sort_students_by_gpa(self):
        self.student_list.sort(key=lambda student:student.gpa)
        print("Sorted By Gpa")
        print(self.student_list)
        
    def filter_student_by_major(self,major):
        filtered_list=list(filter(lambda student:student.major==major,self.student_list))
        if filtered_list:
            print(f"Filtered with the major:{major}")
            for student in filtered_list:
                print(student)
            else:
                print("No student in that major!")

   

            
            
>>>>>>> ff263ffafadedfac74e635dba5d6dfcf32713c67





# # 3. Create a Dynamic Menu for Interaction
# # Users can choose from the following options:

# # 📌 Add a student
# # 📌 Remove a student
# # 📌 View all students
# # 📌 Search for a student
# # 📌 Update a student’s major
# # 📌 Update a student’s GPA
# # 📌 Enroll a student in a course
# # 📌 Update a student’s course grade
# # 📌 Sort students by GPA
# # 📌 Filter students by major
# # 📌 Exit


can_studentbase=StudentDatabase()

while True:
    res1 = input(
        "\nWelcome To Student Database:\n"
        "1 - Add a student\n"
        "2 - Remove a student\n"
        "3 - View all students\n"
        "4 - Search for a student\n"
        "5 - Update a student’s major\n"
        "6 - Update a student’s GPA\n"
        "7 - Enroll a student in a course\n"
        "8 - Update a student’s course grade\n"
        "9 - Sort students by GPA\n"
        "10 - Filter students by major\n"
        "11- Exit\n"
        "Enter your choice: "
    ).lower()
    
    if res1 == "1":
        name=input("Please Enter Student Name: ")
        student_id=int(input("Please ENter student id: "))
        major=input("Please Enter Major: ")
        gpa=float(input("Please Enter Student Gpa: "))
        student=Student(name,student_id,major,gpa)
        can_studentbase.add_student(student)
        
    if res1=="2":
        student_id=int(input("Please ENter student id: "))
        can_studentbase.remove_student(student_id)
        
    if res1=="3":
        can_studentbase.display_students()
        
    if res1=="4":
        name=(input("Please Enter Students Nmae: "))
        can_studentbase.search_student(name)
        
    if res1=="5":
        student_id=int(input("Please Enter Student id: "))
        new_major=input("Please Enter the new major you want to change: ")
        can_studentbase.update_student_major(student_id,new_major)