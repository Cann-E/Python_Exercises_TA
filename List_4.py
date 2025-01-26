# 1. Count Occurrences
# Write a function `count_occurrences(lst, element)` that counts and returns 
# the number of times `element` appears in the list.
# Test it with the list: [1, 2, 3, 4, 2, 3, 2] and element 2.

def count_occurence(lst,element):
    return lst.count(element)

test=[1, 2, 3, 4, 2, 3, 2]
print(count_occurence(test,2))

# 2. Remove Duplicates
# Write a function `remove_duplicates(lst)` that takes a list as input 
# and returns a new list with all duplicates removed.
# Test it with the list: [1, 2, 2, 3, 4, 4, 5].

num=[1, 2, 2, 3, 4, 4, 5]

def remove_duplicated(lst):
    new_list=list(set(lst))
    return new_list

num=remove_duplicated(num)
print(num)




# 3. Reverse a List
# Write a function `reverse_list(lst)` that takes a list as input 
# and returns the list in reverse order.
# Test it with the list: [1, 2, 3, 4, 5].

def reverse_list(lst):
    return lst.reverse()

test2=[1, 2, 3, 4, 5]
reverse_list(test2)
print(test2)

# 4. Find Second Largest
# Write a function `find_second_largest(lst)` that returns the second largest 
# number in the list. Assume the list has at least 2 unique numbers.
# Test it with the list: [10, 20, 4, 45, 99].

def find_second_largest(lst):
    largest=max(lst)
    lst.remove(largest)
    second_largest=max(lst)
    return second_largest

test3=[10, 20, 4, 45, 99]
print(find_second_largest(test3))

# 5. Merge and Sort Lists
# Write a function `merge_and_sort(lst1, lst2)` that takes two lists, merges them,
# and returns a new list sorted in ascending order.
# Test it with the lists: [3, 1, 4] and [5, 2, 6].

# 6. Find Common Elements
# Write a function `common_elements(lst1, lst2)` that takes two lists 
# and returns a new list containing only the elements that are present in both lists.
# Test it with the lists: [1, 2, 3, 4] and [3, 4, 5, 6].

# 7. Separate Even and Odd Numbers
# Write a function `separate_even_odd(lst)` that takes a list of numbers 
# and returns two separate lists: one containing even numbers and the other containing odd numbers.
# Test it with the list: [1, 2, 3, 4, 5, 6, 7, 8, 9].

# 8. Find All Pairs That Add Up to a Target
# Write a function `find_pairs(lst, target)` that finds and returns all pairs 
# of numbers in the list that add up to the given target.
# Test it with the list: [1, 2, 3, 4, 5] and target 6.

# 9. Rotate List
# Write a function `rotate_list(lst, k)` that rotates the list to the right by `k` positions.
# Test it with the list: [1, 2, 3, 4, 5] and k = 2.

# 10. Flatten a Nested List
# Write a function `flatten_list(nested_lst)` that takes a nested list as input 
# and returns a single flattened list. Assume the nested list can contain lists within lists.
# Test it with the list: [[1, 2], [3, 4], [5, 6]].
