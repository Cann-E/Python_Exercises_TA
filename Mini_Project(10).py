
# 1. Define a Student Class

# Attributes:
# name (string) – The student’s full name
# student_id (string) – A unique identifier for each student
# major (string) – The student's major (e.g., Computer Science, Biology)
# gpa (float) – The student's GPA (Grade Point Average)
# courses (dictionary) – Stores course names as keys and grades as values { "Math": 90, "History": 85 }

# Methods:
# update_major(new_major): Updates the student’s major.
# update_gpa(new_gpa): Updates the student’s GPA.
# enroll_course(course_name): Enrolls the student in a course (default grade None).
# update_course_grade(course_name, grade): Updates a student’s grade in a specific course.
# calculate_gpa(): Calculates the GPA dynamically based on course grades.



class Student():
    def __init__(self,name,student_id,major,gpa,):
        self.name=name
        self.student_id=student_id
        self.major=major
        self.gpa=gpa
        self.courses={}
        
    def __str__(self):
        return f"Name: {self.name},Id: {self.student_id},Major: {self.major},Gpa: {self.gpa}\nCourses:{self.courses}"
    
    def update_major(self,new_major):
        old_major=self.major
        self.major=new_major
        print(f"Major Changed from {old_major} to {new_major}")

    def update_gpa(self,new_gpa):
        self.gpa=new_gpa
        print(f"Gpa Updated to {new_gpa}")

    def enroll_course(self,course_name):
        self.courses[course_name]=None
        print(f"Enrolled in new class: {course_name}")


    def update_course_grade(self,course_name,grade):
        if course_name in self.courses:
            self.courses[course_name]=grade
            print(f"Course:{course_name} Grade updated to {grade}")
        else:
            print(f"Course not found: {course_name}")

    def calculate_gpa(self):
        valid_grades=[]
        for grade in self.courses.values():
            if grade is not None:
                valid_grades.append(grade)

        if valid_grades:
            self.gpa=sum(valid_grades)/len(valid_grades)  
            print(f"Gpa is : {self.gpa}")
            return self.gpa
        else:
            print("Gpa not available!")
            return None 

        


# 2. Define a StudentDatabase Class

# Attributes:
# student_list (list of Student objects)

# Methods:
# add_student(student): Adds a new student to the system.
# remove_student(student_id): Removes a student using their unique ID.
# display_students(): Displays all students in the system.
# search_student(name): Searches for a student by name.
# update_student_major(student_id, new_major): Updates a student’s major.
# update_student_gpa(student_id, new_gpa): Updates a student’s GPA.
# enroll_student_in_course(student_id, course_name): Enrolls a student in a course.
# update_student_course_grade(student_id, course_name, grade): Updates a student’s grade.
# sort_students_by_gpa(): Sorts students based on GPA before displaying them.
# filter_students_by_major(major): Filters students based on a specific major.




class StudentDatabase():
    def __init__(self):
        self.student_list=[]

    def add_student(self,student):
        self.student_list.append(student)
        print(f"New Student Added to system: {student}")

    def remove_student(self,student_id):
        found = False
        for id in self.student_list:
            if id.student_id == student_id:
                self.student_list.remove(id)
                print(f"Student Id:{id} removed from the system.Name: {id.name}")
                found =True
                break
        if not found:
            print(f"Student Not Found!Id:{student_id}")

    def display_students(self):
        for i in self.student_list:
            print(f"Name: {i.name},Id: {i.student_id},Major: {i.major},Gpa: {i.gpa}\nCourses:{i.courses}")

    def search_Students(self,name):
        found = False
        for nam in self.student_list:
            if nam.name==name:
                print(f"Student Found: {nam}")
                found =True
                break
        if not found:
            print(f"Student {name} not Found!")

    def update_student_major(self,student_id,new_major):
        found = False
        for id in self.student_list:
            if id.student_id == student_id:
                id.update_major(new_major)
                print(f"Name:{id.name} has changed major to {new_major}")
                found = True
                break
        if not found:
            print("Couldnt Find the student!")


    def update_student_gpa(self,student_id,new_gpa):
        found = False
        for id in self.student_list:
            if id.student_id == student_id:
                id.update_gpa(new_gpa)
                print(f"Student: {id.name} has updated GPA to {new_gpa}")
                found = True
                break
        if not found:
            print(f"Student Not Found!")

    def enroll_student_in_courses(self,student_id,course_name):
        found  = False
        for id in self.student_list:
            if id.student_id == student_id:
                id.enroll_course(course_name)
                print("Student Enrolled!")
                found = True
                break

        if not found:
            print("ID no match!")

    def update_student_course_grade(self,student_id, course_name, grade):
        found = False
        for id in self.student_list:
            if id.student_id == student_id:
                id.update_course_grade(course_name,grade)
                print(f"Course: {course_name},Grade: {grade}")
                found = True
                break
        if not found:
            print("Student not found!")

    def sort_students_by_gpa(self):
        self.student_list.sort(key= lambda student: student.gpa,reverse=True)
        print("Sorted by GPA!")
        print(self.student_list)
    
    def filter_students_by_major(self,major):
        filtered_list=list(filter(lambda student: student.major == major,self.student_list))
        if filtered_list:
            print(f"Filtered with major: {major}")
            for student in filtered_list:
                print(student)
        else:
            print("No students in that major!")

    

# 3. Create a Dynamic Menu for Interaction
# Users can choose from the following options:

# 📌 Add a student
# 📌 Remove a student
# 📌 View all students
# 📌 Search for a student
# 📌 Update a student’s major
# 📌 Update a student’s GPA
# 📌 Enroll a student in a course
# 📌 Update a student’s course grade
# 📌 Sort students by GPA
# 📌 Filter students by major
# 📌 Exit

can_studentdatabase=StudentDatabase()

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
        name=input("Please Enter Your name: ")
        student_id=int(input("Please Enter Student Id: "))
        major=input("Please Enter Students Major: ")
        gpa=float(input("Please Enter Students GPA: "))
        student=Student(name,student_id,major,gpa)
        can_studentdatabase.add_student(student)

    if res1 == "2":
        student_id=int(input("Please Enter Student Id: "))
        can_studentdatabase.remove_student(student_id)

    if res1 == "3":
        can_studentdatabase.display_students()

    if res1 == "4":
        name=input("Please Enter Your name: ")
        can_studentdatabase.search_Students(name)

    if res1 == "5":
       student_id=int(input("Please Enter Student Id: ")) 
       new_major=(input("Please Enter the new Major: "))
       can_studentdatabase.update_student_major(student_id,new_major)

    if res1 == "6":
        student_id=int(input("Please Enter Student Id: ")) 
        new_gpa=float(input("Please Enter the new GPA: "))
        can_studentdatabase.update_student_gpa(student_id,new_gpa)

    if res1 == "7":
        student_id=int(input("Please Enter Student Id: ")) 
        new_course=(input("Please Enter the Course name you want to enroll: "))
        can_studentdatabase.enroll_student_in_courses(student_id,new_course)

    if res1 =="8":
        student_id=int(input("Please Enter The Student ID: "))
        course_name=input("Please Enter the Course Name: ")
        grade=float(input("Please Enter the updated grade: "))
        can_studentdatabase.update_student_course_grade(student_id,course_name,grade)
        

    if res1 =="9":
        can_studentdatabase.sort_students_by_gpa()


    if res1 == "10":
        filter_major=input("Please enter the major you want to filter: ")
        can_studentdatabase.filter_students_by_major(filter_major)

    if res1 == "11":
        print("Thank you for using the Student System!")
        break


