"""
========================================
          Understanding Booleans
========================================
"""

# What is a Boolean?
# ------------------
# A Boolean is a data type that represents one of two values:
# - True
# - False
# Booleans are commonly used for decision-making in programming.

# Key Features:
# -------------
# 1. Only Two Values: True and False.
# 2. Used in Conditional Statements: Commonly found in if statements.
# 3. Result of Comparisons: Comparisons return Boolean values.
# 4. Used in Logical Operations: 'and', 'or', 'not' are common Boolean operators.

# Boolean Values in Python:
# -------------------------
# - Python uses 'True' and 'False' (Capitalized).
# - Some values are considered "truthy" (evaluate to True).
# - Some values are "falsy" (evaluate to False).

# Truthy and Falsy Values:
# ------------------------
# Truthy: Non-zero numbers, non-empty strings, lists, sets, dictionaries.
# Falsy: 0, None, empty strings "", empty lists [], empty sets set(), empty dictionaries {}.

# Common Boolean Operations:
# --------------------------
# 1. Comparison Operators: ==, !=, <, >, <=, >=
# 2. Logical Operators: and, or, not
# 3. Checking Truthiness with bool()
# 4. Using Booleans in if statements

# Example Use Cases:
# ------------------
# - Checking conditions in if statements.
# - Validating user input (e.g., checking if a field is empty).
# - Controlling loops (e.g., while True: for infinite loops).
# - Filtering data based on conditions.


"""
========================================
          Python Learning Sheet:
              Booleans
========================================
"""

# 1. Boolean Values
# Assign True and False to variables and print them.

is_sunny = True
is_raining = False

print(is_sunny)   # True
print(is_raining) # False


# 2. Boolean from Comparisons
# Use comparison operators to get Boolean values.

print(10 > 5)    # True
print(3 == 3)    # True
print(7 < 2)     # False
print(5 != 5)    # False


# 3. Boolean Operators: and, or, not
# Use logical operators to combine Boolean expressions.

a = True
b = False

print(a and b)   # False
print(a or b)    # True
print(not a)     # False


# 4. Boolean in an If Statement
# Use a Boolean expression in an if condition.

age = 20

if age >= 18:
    print("You are an adult.")  # This will print because age is 20


# 5. Boolean in a Function
# Write a function `is_even(n)` that returns True if a number is even.

def is_even(n):
    return n % 2 == 0

print(is_even(4))  # True
print(is_even(7))  # False


# 6. Check Truthiness with bool()
# Convert different values to Boolean using `bool()`.

print(bool(0))      # False
print(bool(1))      # True
print(bool(""))     # False
print(bool("Hello"))  # True
print(bool([]))     # False
print(bool([1, 2, 3]))  # True


# 7. Using Boolean in a While Loop
# A while loop that runs until a Boolean variable becomes False.

running = True
counter = 0

while running:
    print("Loop is running...")
    counter += 1
    if counter == 3:
        running = False  # Stops the loop after 3 iterations


# 8. Short-Circuiting with and/or
# Python stops evaluating as soon as it knows the result.

x = False and print("This won't print")
y = True or print("This won't print either")

print(x, y)  # False True


# 9. Boolean as Return Value in a Function
# Write a function `is_adult(age)` that returns True if age is 18 or older.

def is_adult(age):
    return age >= 18

print(is_adult(20))  # True
print(is_adult(15))  # False


# 10. Using Boolean with Lists
# Check if a list is empty using a Boolean condition.

names = []

if names:  # This is False since the list is empty
    print("List is not empty")
else:
    print("List is empty")  # This will print
