# 1. Create a Set
# Create a set called `fruits_set` containing the names of 5 different fruits.
# Print the set.

fruits_set = {"apple", "pear", "strawberry", "raspberry", "watermelon"}
print(fruits_set)


# 2. Access Set Elements
# Since sets are unordered, elements cannot be accessed by index.
# Instead, check if a specific element exists in the set.

fruits_set = {"apple", "pear", "strawberry", "raspberry", "watermelon"}

print("apple" in fruits_set)  # True
print("banana" in fruits_set)  # False


# 3. Add Elements to a Set
# Add "Mango" to the `fruits_set`.
# Print the updated set.

fruits_set.add("Mango")
print(fruits_set)


# 4. Remove Elements from a Set
# Remove "apple" from the `fruits_set`.
# Print the updated set.

fruits_set.remove("apple")  # Raises error if element is not found
print(fruits_set)

# Alternative: Use discard() to avoid an error if the element is missing.
fruits_set.discard("banana")  # No error, even if "banana" is not in the set


# 5. Set Length
# Write a function `set_length(s)` that takes a set as input and returns the number of elements in the set.
# Test it with the `fruits_set`.

def set_length(s):
    return len(s)

print(set_length(fruits_set))


# 6. Check If Element Exists
# Write a function `check_element(s, element)` that takes a set and an element.
# Return True if the element exists in the set, otherwise return False.
# Test it with "Mango".

def check_element(s, element):
    return element in s

print(check_element(fruits_set, "Mango"))  # True
print(check_element(fruits_set, "Banana"))  # False


# 7. Iterate Over a Set
# Write a function `print_set(s)` that takes a set as input and prints each element on a separate line.

def print_set(s):
    for item in s:
        print(item)

print_set(fruits_set)


# 8. Union of Two Sets
# Write a function `union_sets(set1, set2)` that returns the union of two sets.
# Test it with: {"a", "b", "c"} and {"c", "d", "e"}.

set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}

def union_sets(set1, set2):
    return set1.union(set2)

print(union_sets(set1, set2))  # {'a', 'b', 'c', 'd', 'e'}


# 9. Intersection of Two Sets
# Write a function `intersection_sets(set1, set2)` that returns the intersection of two sets.
# Test it with: {"a", "b", "c"} and {"c", "d", "e"}.

def intersection_sets(set1, set2):
    return set1.intersection(set2)

print(intersection_sets(set1, set2))  # {'c'}


# 10. Difference of Two Sets
# Write a function `difference_sets(set1, set2)` that returns elements in `set1` but not in `set2`.
# Test it with: {"a", "b", "c"} and {"c", "d", "e"}.

def difference_sets(set1, set2):
    return set1.difference(set2)

print(difference_sets(set1, set2))  # {'a', 'b'}


# 11. Symmetric Difference of Two Sets
# Write a function `symmetric_difference_sets(set1, set2)` that returns elements that are in either set, but not both.
# Test it with: {"a", "b", "c"} and {"c", "d", "e"}.

def symmetric_difference_sets(set1, set2):
    return set1.symmetric_difference(set2)

print(symmetric_difference_sets(set1, set2))  # {'a', 'b', 'd', 'e'}


# 12. Check Subset and Superset
# Write functions `is_subset(sub, main)` and `is_superset(main, sub)` to check if one set is a subset or superset of another.
# Test with: {"a", "b"} and {"a", "b", "c"}.

def is_subset(sub, main):
    return sub.issubset(main)

def is_superset(main, sub):
    return main.issuperset(sub)

small_set = {"a", "b"}
big_set = {"a", "b", "c"}

print(is_subset(small_set, big_set))  # True
print(is_superset(big_set, small_set))  # True


# 13. Convert a List to a Set
# Write a function `list_to_set(lst)` that removes duplicates from a list by converting it to a set.
# Test it with: [1, 2, 2, 3, 4, 4, 5].

def list_to_set(lst):
    return set(lst)

print(list_to_set([1, 2, 2, 3, 4, 4, 5]))  # {1, 2, 3, 4, 5}
