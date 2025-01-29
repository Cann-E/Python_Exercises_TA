# 1. Create a Class for a Person

class Person():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
    def introduce(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old, and I am a {self.gender}.")
        
        
CAN=Person("Can",31,"Male")

CAN.introduce()


# 2. Create a Bank Account Class


class BankAccount():
    def __init__(self,account_holder,balance=0):
        self.account_holder=account_holder
        self.balance=balance
        
    def deposit(self):
        money=float(input(("How Much Money you want to deposit: ")))
        self.balance+=money
        print(f"{money} $ added to account.New Balance is {self.balance} $")
        
    def withdraw(self,amount):
        
        self.balance-=amount
        return self.balance
    
    def get_balance(self):
        print(f"Current Balance is {self.balance} $")
    
        
    
    
can=BankAccount("Can",100)
can.deposit()
print(can.withdraw(50))

can.get_balance()



#  3. Rectangle Class       


class Rectangle():
    def __init__(self,length,width):
        self.length=length
        self.width=width
        
    def area(self):
        area=self.length*self.width
        return area
    
    def perimeter(self):
        perimeter=(self.length+self.width)*2
        return perimeter
    
rectangle_1=Rectangle(18,7)

print(rectangle_1.area())
print(rectangle_1.perimeter())




#4 Car Class


class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        
    def Start(self):
        print(f"The {self.year} {self.make} {self.model} is starting.")
        
        
        
maserati=Car("Maserati","Ghibli","2018")

maserati.Start()





# 5. Student Class
# Create a class `Student` with attributes:
# - `name`
# - `roll_number`
# - `marks` (list of marks in 3 subjects)
# Add methods:
# - `calculate_average()` to calculate and return the average marks.
# - `get_grade()` to return:
#   - `"A"` if average is 90+
#   - `"B"` if 75–89
#   - `"C"` if 50–74
#   - `"F"` otherwise.


class Student:
    def __init__(self, name, roll_number, marks):
        """Initialize student attributes"""
        self.name = name
        self.roll_number = roll_number
        self.marks = marks  # List of marks in 3 subjects

    def calculate_average(self):
        """Calculate and return the average marks"""
        return sum(self.marks) / len(self.marks)

    def get_grade(self):
        """Return the grade based on average marks"""
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "F"

# Test the Student class
student1 = Student("Alice", 101, [85, 90, 78])  # Create a student object

print(f"Name: {student1.name}")
print(f"Roll Number: {student1.roll_number}")
print(f"Average Marks: {student1.calculate_average():.2f}")
print(f"Grade: {student1.get_grade()}")

            



# 6. Book Class
# Create a class `Book` with attributes:
# - `title`
# - `author`
# - `price`
# Add a method `display_info()` that prints:
# "Book: [title], Author: [author], Price: $[price]"


class Book():
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display_info(self):
        print(f"{self.title},Author {self.author},Price:{self.price}")
        
can_book=Book("Dance","Susan",21)
can_book.display_info()

# 7. Dog Class
# Create a class `Dog` with attributes:
# - `name`
# - `breed`
# - `age`
# Add methods:
# - `bark()` that prints: "Woof! Woof!"
# - `description()` that prints: "My name is [name], I am a [age]-year-old [breed]."


class Dog():
    def __init__(self,name,breed,age):
        self.name=name
        self.breed=breed
        self.age=age
    def bark(self):
        print("WOOF,WOOF")
        
    def description(self):
        print(f"My name is {self.name}, I am a {self.age} year old {self.breed}")
        
remy=Dog("Remy","French Bulldog",9)

remy.bark()
remy.description()
         
        

# 8. Employee Class
# Create a class `Employee` with attributes:
# - `name`
# - `id_number`
# - `salary`
# Add methods:
# - `give_raise(amount)` to increase the salary by the given amount.
# - `display_info()` to print the employee’s information.



# 9. Library Class
# Create a class `Library` with attributes:
# - `books` (list of book titles)
# Add methods:
# - `add_book(title)` to add a book to the library.
# - `remove_book(title)` to remove a book if it exists.
# - `display_books()` to print the list of all books.

# 10. Circle Class
# Create a class `Circle` with attributes:
# - `radius`
# Add methods:
# - `area()` to calculate the circle’s area (πr²).
# - `circumference()` to calculate the circle’s circumference (2πr).




            
        