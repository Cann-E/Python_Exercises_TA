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