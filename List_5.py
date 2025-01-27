# 1. Find Unique Elements
# Write a function `find_unique(lst)` that returns a list of elements 
# that appear only once in the input list.
# Test it with: [1, 2, 2, 3, 4, 4, 5].
# Expected Output: [1, 3, 5]

def find_unique(lst):
    return [x for x in lst if lst.count(x) == 1]

x = [1, 2, 2, 3, 4, 4, 5]
unique = find_unique(x)
print(unique)

# 2. Check if a List is Sorted
# Write a function `is_sorted(lst)` that checks whether a list is sorted in ascending order.
# Test it with: [1, 2, 3, 4, 5] and [1, 3, 2, 4, 5].
# Expected Output: True for the first and False for the second.

def is_sorted(lst):
    if lst == sorted(lst):
        return True
    else:
        return False
    
x1=[1, 2, 3, 4, 5]
x2=[1, 3, 2, 4, 5]

print(is_sorted(x1))
print(is_sorted(x2))

# 3. Find Missing Number
# Write a function `find_missing(lst, n)` that finds the missing number 
# in a list of integers from 1 to n.
# Test it with: [1, 2, 4, 5] and n = 5.
# Expected Output: 3.

def find_missing(lst,n):
    total_sum=n*(n+1)//2
    actual_sum=sum(lst)
    return total_sum-actual_sum

lsst=[1, 2, 4, 5]

a=find_missing(lsst,5)
print(a)
        
        
        

# 4. Count Even and Odd Numbers
# Write a function `count_even_odd(lst)` that returns the count of even and odd numbers in a list.
# Test it with: [1, 2, 3, 4, 5, 6].
# Expected Output: (3, 3) (3 even, 3 odd).

# 5. Cumulative Sum of a List
# Write a function `cumulative_sum(lst)` that returns a list where each element is 
# the cumulative sum of the elements so far.
# Test it with: [1, 2, 3, 4].
# Expected Output: [1, 3, 6, 10].

# 6. Find Intersection of Three Lists
# Write a function `common_in_three(lst1, lst2, lst3)` that returns a list 
# of elements common in all three lists.
# Test it with: [1, 2, 3], [2, 3, 4], and [3, 4, 5].
# Expected Output: [3].

# 7. Find Element Closest to Target
# Write a function `find_closest(lst, target)` that returns the number 
# in the list closest to the target.
# Test it with: [10, 20, 30, 40] and target 25.
# Expected Output: 20.

# 8. Check for Palindrome
# Write a function `is_palindrome(lst)` that checks whether a list reads 
# the same forward and backward.
# Test it with: [1, 2, 3, 2, 1] and [1, 2, 3, 4].
# Expected Output: True for the first, False for the second.

# 9. Find Maximum Product of Two Numbers
# Write a function `max_product(lst)` that finds the maximum product of 
# any two numbers in the list.
# Test it with: [1, 10, 2, 6, 5].
# Expected Output: 60 (10 × 6).

# 10. Group Elements by Parity
# Write a function `group_by_parity(lst)` that groups the even and odd numbers 
# together in the same list.
# Test it with: [1, 2, 3, 4, 5, 6].
# Expected Output: [2, 4, 6, 1, 3, 5].
