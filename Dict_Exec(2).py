# Step 1: Create a Student Class

# Attributes:
# name (string)
# student_id (integer, unique identifier)
# major (string)
# gpa (float)
# year (string, e.g., Freshman, Sophomore, etc.)
# email (string, should be formatted properly)

# Methods:
# update_major(new_major): Updates the student’s major.
# update_gpa(new_gpa): Updates the GPA.
# update_year(new_year): Updates the academic year.
# validate_email(email): Ensures the email is properly formatted.
# __str__(): Returns a formatted string of the student's details.

import re

class Student():
    def __init__(self,name,student_id,major,gpa,year,email):
        self.name=name
        self.student_id=student_id
        self.major=major
        self.gpa=gpa
        self.year=year
        self.email = email if self.validate_email(email) else "Invalid Email"
        
    def __str__(self):
        return f"Name: {self.name},Student ID: {self.student_id},Major: {self.major},Gpa: {self.gpa},Year: {self.year},Email: {self.email}"
        
        
    def update_major(self,new_major):
        old_major=self.major
        self.major=new_major
        print(f"Major changed from {old_major} to {new_major}")
        
    def update_gpa(self,new_gpa):
        old_gpa=self.gpa
        self.gpa=new_gpa
        print(f"Gpa Updated from {old_gpa} to {new_gpa}")
        
    def update_year(self,new_year):
        self.year=new_year
        print(f"Academic Year Updated {new_year}")
        

     
    @staticmethod   
    def validate_email(email):
        pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.match(pattern,email))
        
    # @staticmethod	Makes this function independent (not using self).
    # pattern = r"...regex..."	Defines rules for what an email should look like.
    # re.match(pattern, email)	Checks if email matches the pattern.
    # bool(...)	Converts the result to True (valid) or False (invalid).




# Step 2: Create a StudentDatabase Class
# Responsibilities:
# Maintains a dictionary of Student objects where:

# Keys = student_id
# Values = Student objects
# Required Methods:
# add_student(student): Adds a new student.
# remove_student(student_id): Removes a student by ID.
# display_students(): Displays all students.
# search_student(name): Searches for students by name.
# update_student_major(student_id, new_major): Updates a student's major.
# update_student_gpa(student_id, new_gpa): Updates a student's GPA.
# update_student_year(student_id, new_year): Updates a student's academic year.
# sort_students_by_gpa(): Sorts students by GPA in descending order.
# filter_students_by_major(major): Filters students based on major.
# validate_student_id(student_id): Ensures student ID is unique.


class StudentDatabase():
    def __init__(self):
        self.student_dict={}
        
    def add_students(self,new_student,new_grade):
        self.student_dict[new_student]=new_grade
        print(f"Student added to the system {new_student}")
        
    def remove_student(self,student_id):
        for student in self.student_dict:
            if student.student_id==student_id:
                print(f"Student has been removed from the dictonary {student.name}")
                self.student_dict.pop(student)
                found=True
                break
        if not found:
            print("Student not found!")
            
    def display_students(self):
        print(self)
    
        
        






# Step 3: Testing Your Implementation
# Actions to Perform:
# Add students to the system.
# Search for students by name.
# Update student details (major, GPA, and year).
# Display all students.
# Sort students by GPA.
# Filter students based on their major.
# Remove a student from the system.