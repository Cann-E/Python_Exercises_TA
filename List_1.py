# 1. Create a List
# Create a list called `fruits` containing the names of 5 different fruits.
# Print the list.

fruits=["apple","pear","strawbeery","raspberry","watermelon"]
print(fruits)

# 2. Access List Elements
# From the `fruits` list, print the first fruit and the last fruit using indexing.


fruits=["apple","pear","strawbeery","raspberry","watermelon"]
print(fruits[0],fruits[-1])


# 3. Modify List Elements
# Change the second fruit in the `fruits` list to "Mango".
# Print the updated list.

fruits_2=["apple","pear","strawbeery","raspberry","watermelon"]
fruits_2.pop(1)
fruits_2.insert(1,"Mango")
fruits_2[2]="CAN" #TO DIRECTLY MODIFY
print(fruits_2)

# 4. Add and Remove Elements
# Add "Pineapple" to the `fruits` list.
# Remove the first fruit from the list.
# Print the updated list.

fruits_3=["apple","pear","strawbeery","raspberry","watermelon"]
fruits_3.append("Pineapple")
fruits_3.pop(0) #or fruits_3.remove("apple")
print(fruits_3)


# 5. List Length
# Write a function `list_length(lst)` that takes a list as input
# and returns the number of elements in the list.
# Test it with the `fruits` list.

fruits=["apple","pear","strawbeery","raspberry","watermelon"]
def list_length(lst):
    return len(lst)

print(list_length(fruits))
    
    

    

# 6. Check If Element Exists
# Write a function `check_element(lst, element)` that takes a list and an element.
# Return True if the element exists in the list, otherwise return False.
# Test it with the `fruits` list and the element "Mango".

fruits=["apple","pear","strawbeery","raspberry","watermelon"]

def check_element(lst,element):
    if element in lst:
        return True
    else:
        return False
        
print(check_element(fruits,"Mango"))

# 7. Iterate Over a List
# Write a function `print_list(lst)` that takes a list as input and prints each element
# on a separate line. Test it with the `fruits` list.

fruits=["apple","pear","strawbeery","raspberry","watermelon"]

def print_list(lst):
    for fruit in lst:
        print(fruit)
    
print_list(fruits)

# 8. Sort a List
# Write a function `sort_list(lst)` that sorts a list in ascending order.
# Test it with a list of numbers: [5, 3, 8, 1, 4].

numbers=["3","4","2","11","7"]


def sort_list(lst):
    lst.sort() 
   
sort_list(numbers) 
print(numbers)

# 9. Find the Largest Number
# Write a function `find_largest(lst)` that takes a list of numbers
# and returns the largest number in the list.
# Test it with a list of numbers: [12, 45, 7, 29, 30].

num = [12, 45, 7, 29, 30]

def find_largest(lst):
    return max(lst)  # Use the built-in `max()` function to find the largest number


print(find_largest(num))  

#################Alternate
# num=[12, 45, 7, 29, 30]


# def find_largest(lst):
#     lst.sort()
#     print(lst[-1])

# find_largest(num)
####################



# 10. Combine Two Lists
# Write a function `combine_lists(lst1, lst2)` that takes two lists and
# returns a new list containing all elements from both lists.
# Test it with the lists: [1, 2, 3] and [4, 5, 6].

list_1=[1, 2, 3]
list_2=[4, 5, 6]


def combine_list(lst1,lst2):
    concatinate=lst1+lst2
    return concatinate

print(combine_list(list_1,list_2))
