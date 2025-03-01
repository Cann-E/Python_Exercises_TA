# 1. Double Each Element
# Write a function `double_elements(lst)` that doubles each element in the list.
# Test it with: [1, 2, 3, 4, 5].
# Expected Output: [2, 4, 6, 8, 10]

def double_elements(lst):
    double_=[]
    for i in lst:
        double_.append(i*2)
    return double_
        

a=[1, 2, 3, 4, 5]
b=double_elements(a)
print(b)


# 2. Create a List of Squares
# Write a function `square_elements(lst)` that returns a list of squares of the elements in the input list.
# Test it with: [1, 2, 3, 4].
# Expected Output: [1, 4, 9, 16]

def square_elements(lst):
    square_=[]
    for i in lst:
        square_.append(i**2)
    return square_

c=[1, 2, 3, 4]
d=square_elements(c)
print(d)


# 3. Combine Two Lists
# Write a function `combine_lists(lst1, lst2)` that combines two lists element by element.
# Assume the lists have the same length.
# Test it with: [1, 2, 3], [4, 5, 6].
# Expected Output: [5, 7, 9]

def combine_(lst1,lst2):
    comb=[]
    for i in range(len(lst1)):       
        comb.append(lst1[i]+lst2[i])
    return comb
            
    
        

x=[1, 2, 3]
y=[4, 5, 6]

print(combine_(x,y))

# 4. Remove Negative Numbers
# Write a function `remove_negatives(lst)` that removes all negative numbers from the list.
# Test it with: [1, -2, 3, -4, 5].
# Expected Output: [1, 3, 5]

def remove_negative(lst):
    for i in lst[:]:   # Use lst[:] to iterate over a copy of the list
        if i<0:
            lst.remove(i)                       
            
ab=[1, -2, 3, -4, 5]

remove_negative(ab)
print(ab)

#########ALTERNATE

def remove_negatives(lst):
    return [i for i in lst if i >= 0]  # Keep only non-negative numbers1

# Test case
ab = [1, -2, 3, -4, 5]
cd = remove_negatives(ab)
print(cd)  # Expected Output: [1, 3, 5]


# 5. Find the Largest Element
# Write a function `find_largest(lst)` that returns the largest number in the list without using `max()`.
# Test it with: [10, 20, 4, 45, 99].
# Expected Output: 99




# 6. Count Vowels in a List of Strings
# Write a function `count_vowels(lst)` that counts the total number of vowels in a list of strings.
# Test it with: ["apple", "banana", "cherry"].
# Expected Output: 8

# 7. Reverse Each String in a List
# Write a function `reverse_strings(lst)` that reverses each string in the list.
# Test it with: ["abc", "def", "ghi"].
# Expected Output: ["cba", "fed", "ihg"]

# 8. Multiply Corresponding Elements
# Write a function `multiply_lists(lst1, lst2)` that multiplies corresponding elements of two lists.
# Assume both lists are of the same length.
# Test it with: [1, 2, 3], [4, 5, 6].
# Expected Output: [4, 10, 18]

# 9. Filter Words of a Specific Length
# Write a function `filter_by_length(lst, length)` that filters out words that are not of the specified length.
# Test it with: ["cat", "dog", "elephant", "ant"], length = 3.
# Expected Output: ["cat", "dog", "ant"]

# 10. Sum of Even Numbers
# Write a function `sum_of_evens(lst)` that calculates the sum of all even numbers in the list.
# Test it with: [1, 2, 3, 4, 5, 6].
# Expected Output: 12

# 11. Add an Element to the Middle
# Write a function `insert_middle(lst, element)` that inserts an element in the middle of the list.
# Test it with: [1, 2, 4, 5], element = 3.
# Expected Output: [1, 2, 3, 4, 5]

# 12. Find Strings That Start With a Specific Letter
# Write a function `starts_with(lst, letter)` that finds all strings that start with the given letter.
# Test it with: ["apple", "banana", "cherry", "apricot"], letter = "a".
# Expected Output: ["apple", "apricot"]

# 13. Rotate List to the Left
# Write a function `rotate_left(lst, k)` that rotates the list to the left by `k` positions.
# Test it with: [1, 2, 3, 4, 5], k = 2.
# Expected Output: [3, 4, 5, 1, 2]

# 14. Find the Index of the First Odd Number
# Write a function `first_odd_index(lst)` that returns the index of the first odd number in the list.
# Test it with: [2, 4, 6, 3, 8].
# Expected Output: 3

# 15. Remove Duplicates Without Using Set
# Write a function `remove_duplicates_no_set(lst)` that removes duplicates from the list 
# without using `set()`.
# Test it with: [1, 2, 2, 3, 4, 4, 5].
# Expected Output: [1, 2, 3, 4, 5]
