
#1 Finding the index of the item
letters=["a","b","3","c","d"]
print(letters.index("d")) #index of d is 4
print(letters.index("3")) #index of 3 is 2

#2  to check if item is in your list
letters_2=["a","b","3","c","d"]
if "f" in letters_2:
    print(letters.index("f"))
else:
    print("Not in your list")
    
#3 counts how many repeats


letters_3=["a","b","b","c","c","c","d"]
print(letters_3.count("c")) #counts how many reapeats in your list for letter c

#####################################################################################

#4 Takes a List as Input
def list_length(lst):
    return len(lst)  # Return the length of the input list

# Test the function with the given list
fruits = ["apple", "pear", "strawberry", "raspberry", "watermelon"]
print(list_length(fruits))  # Output: 5



#5 List Defined Inside the Function

def list_length():
    lst = ["apple", "pear", "strawberry", "raspberry", "watermelon"]  # Define the list inside the function
    return len(lst)  # Return the length of the list

# Call the function without any arguments
print(list_length())  # Output: 5



#6 Takes a List as Input from the User


def list_length(lst):
    return len(lst)  # Return the length of the input list

# Get a list from the user
user_input = input("Enter list elements separated by commas: ")
fruits = user_input.split(",")  # Split the input string into a list
print("List:", fruits)  # Display the list
print("Number of elements in the list:", list_length(fruits))  # Output the length




#7 List Defined Inside the Function with User Input


def list_length():
    # Get a list from the user inside the function
    user_input = input("Enter list elements separated by commas: ")
    lst = user_input.split(",")  # Split the input string into a list
    return len(lst)  # Return the length of the list

# Call the function
print("Number of elements in the list:", list_length())


#8   average

def calculate_average(self):
    return sum(self.marks)/len(self.marks)  #total sum of the numbers in the list divided by the size of the list

