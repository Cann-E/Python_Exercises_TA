# Student Management System - Task Description
# Objective:
# Build a Student Management System using Python’s object-oriented programming concepts.

# Task Breakdown:

# Create a Student Class

# Attributes:
# name (string)
# student_id (integer, unique identifier)
# major (string)
# gpa (float)
# year (string or integer, representing academic year, e.g., Freshman, Sophomore, etc.)

# Methods:
# A method to update the student’s major.
# A method to update the GPA.
# A method to update the academic year.
# Implement the __str__ method to print the student’s details in a well-formatted string.


class Student():
    def __init__(self,name,student_id,major,gpa,year):
        self.name = name
        self.student_id = student_id
        self.major = major
        self.gpa = gpa
        self.year=year
        #---
        
    def __str__(self):
        return f"Name: {self.name}, Student ID: {self.student_id}, Major: {self.major}, GPA: {self.gpa}, Year: {self.year}"
    
    def update_major(self,new_major):
        old_major=self.major
        self.major=new_major
        return f"Major changed from {old_major} to {new_major}"
    
    def update_gpa(self,new_gpa):
        old_gpa=self.gpa
        self.gpa=new_gpa
        return f"Gpa updated from {old_gpa} to {new_gpa}"
    
    def update_academic_year(self,new_academic_year):
        self.gpa=new_academic_year
        return f"Academic Year Updated to {new_academic_year}"
        



# Create a StudentDatabase Class

# Responsibilities:
# Maintain a list of Student objects:

# Required Methods:

# add_student(student): Add a new student to the system.

# remove_student(student_id): Remove a student using their unique student ID.

# display_students(): Display all students currently in the system.

# search_student(name): Search for a student by name and display their information.

# update_student_major(student_id, new_major): Update the major of a specific student.

# update_student_gpa(student_id, new_gpa): Update the GPA of a specific student.

# update_student_year(student_id, new_year): Update the academic year of a specific student.

# sort_students_by_gpa(): Sort the students by GPA in descending order and display them.

# filter_students_by_major(major): Filter and display students who are enrolled in a specific major.




class StudentDatabase():
    def __init__(self):
        self.student_list=[]
        
        
    def add_student(self,student):
        self.student_list.append(student)
        print(f"Success! New Student added to System.Name:{Student}")
        
    
    def remove_student(self,student_id):
        for student in self.student_list:
            if student.student_id == student_id:
                print("Student Found in the System!")
                res1=input("Removing the Student Y/N: ").lower()
                if res1=="y":
                    self.student_list.remove(student)
                    print(f"Student :{student.name} removed From the system!")
                else:
                    print(f"Student :{student.name} not removed!")
                break
        else:
            print("Student not Found!")
            
                
    def display_students(self):
        print(self)
        
            
    def search_students(self,name):
        found=False
        for student in self.student_list:
            if student.name == name:
                print("Student Found!")
                found=True
                res2=input("What would you like to do display or remove student?: ").lower()
                if res2 == "display":
                    print(student)
                    break
                elif res2 == "remove":
                    self.student_list.remove(student)
                    break
        if not found:
            print("Search Unsuccesful Student Not in the System!")    
            
            
    def update_student_major(self, student_id, new_major):
        for student in self.student_list:
            if student.student_id == student_id:
                res3 = input(f"Do you want to update major (Y/N): ").lower()
                if res3 == "y":
                    print("Student major changed!")
                    student.update_major(new_major)
                    return
                elif res3 == "n":
                    print(f"Name: {student.name} major not changed!")
                    return
                else:
                    print("Invalid input. Please enter Y or N.")
                    return
        print("Student not found!")
        

    










# Testing Your Implementation:

# Add multiple students to your database.
# Search for specific students by name.
# Update student details (major, GPA, and year) to test the update methods.
# Display all students, then sort them by GPA to verify the sorting functionality.
# Filter students by a specific major to confirm that the filtering works as expected.
# Deliverables:

# Implement the Student class with the necessary attributes and methods.
# Implement the StudentDatabase class with all the specified functionalities.
# Write a short script to demonstrate the following:
# Adding several Student instances.
# Searching for a student by name.
# Updating student details.
# Sorting the list of students by GPA.
# Filtering the students based on their major.