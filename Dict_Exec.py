#1- Create a Dictionary Attribute
# Create a class Student that stores student names and grades in a dictionary.
# Implement a method to add a new student and their grade.
class Student():
    def __init__(self):
        self.names_dict={}
    
    def add_student(self,new_student,grade):
        self.names_dict[new_student]=grade
        print(f"Student added:Name{new_student},Grade:{grade}")
        
student=Student()
student.add_student("can",95)
student.add_student("asli",85)
print(student.names_dict)
    


#2- Retrieve a Value from a Dictionary
# Modify the Student class to add a method get_grade(name) that returns the grade of a student.
# If the student is not found, return "Student not found".

class Student():
    def __init__(self):
        self.names_dict={}
        
    def add_student(self,new_student,grade):
        self.names_dict[new_student]=grade
        print(f"Student added:Name{new_student},Grade:{grade}")
        
    def get_grade(self,name):
        found=False
        for student in self.names_dict:
            if student == name:
                found=True
                return self.names_dict[student]
        if not found:
            print("Student not found!")
                
student=Student()
student.add_student("can",95)
student.add_student("asli",85)
print(student.get_grade("can"))
print(student.get_grade("asli"))
    

# 3-Check if a Key Exists in the Dictionary
# Add a method has_student(name) to check if a student exists in the records.
# Return True if they exist, otherwise False.

class Student():
    def __init__(self):
        self.names_dict={}
        
    def add_student(self,new_student,grade):
        self.names_dict[new_student]=grade
        print(f"Student added:Name{new_student},Grade:{grade}")
        
    def get_grade(self,name):
        found=False
        for student in self.names_dict:
            if student == name:
                found=True
                return self.names_dict[student]
        if not found:
            print("Student not found!")
    
    def has_student(self,name):
        for student in self.names_dict:
            if student == name:
                return True
        else:
            return False
                
student=Student()
student.add_student("can",95)
student.add_student("asli",85)

print(student.get_grade("can"))
print(student.get_grade("asli"))

print(student.has_student("can"))
print(student.has_student("mike"))

# 4-Update a Dictionary Value
# Add a method update_grade(name, new_grade) to update the grade of an existing student.
# If the student does not exist, return "Student not found".

class Student():
    def __init__(self):
        self.names_dict={}
        
    def add_student(self,new_student,grade):
        self.names_dict[new_student]=grade
        print(f"Student added:Name{new_student},Grade:{grade}")
        
    def get_grade(self,name):
        found=False
        for student in self.names_dict:
            if student == name:
                found=True
                return self.names_dict[student]
        if not found:
            print("Student not found!")
    
    def has_student(self,name):
        for student in self.names_dict:
            if student == name:
                return True
        else:
            return False
        
    def update_grade(self,name,new_grade):
        for student in self.names_dict:
            if student ==name:
                self.names_dict[student]=new_grade
                print(f"Student:{student} new grade:{new_grade}")
                found=True
                break
        if not found:
            print(f"Student:{student} not found")
         
                
student=Student()
student.add_student("can",95)
student.add_student("asli",85)

print(student.get_grade("can"))
print(student.get_grade("asli"))

print(student.has_student("can"))
print(student.has_student("mike"))

student.update_grade("asli",100)


# 5-Delete a Key from the Dictionary
# Implement a method remove_student(name) that removes a student from the dictionary.
# If the student does not exist, return "Student not found".



# 6-Count the Number of Entries in the Dictionary
# Add a method count_students() that returns the number of students in the dictionary.

# 7-Return All Keys and Values
# Implement a method get_all_students() that returns all student names and grades as a dictionary.

# 8-Find the Student with the Highest Grade
# Implement a method top_student() that returns the name of the student with the highest grade.
# If no students are present, return "No students available".

# 9-Reverse a Dictionary (Swap Keys and Values)
# Implement a method reverse_records() that swaps the student names with their grades, making the grades the keys and names the values.

# 10-Merge Two Dictionary Attributes
# Create a second class Classroom that stores another dictionary of students.
# Implement a method merge_students(classroom_obj) that merges the two dictionaries into one.