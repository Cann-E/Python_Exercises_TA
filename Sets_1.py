"""
========================================
          Understanding Sets
========================================
"""

# What is a Set?
# --------------
# A set is a collection of unique and unordered elements.
# Unlike lists, sets do not allow duplicate values, and they do not maintain a specific order.

# Key Features:
# -------------
# 1. **Unordered** – Set elements do not have a fixed position.
# 2. **Unique Elements** – A set automatically removes duplicates.
# 3. **Mutable** – You can add or remove elements, but you cannot modify existing ones.
# 4. **Efficient Membership Check** – Checking if an item exists in a set is faster than in a list.

# When to Use a Set?
# ------------------
# - When you need a collection of **unique** values.
# - When you frequently check **if an element exists** in a collection.
# - When performing **set operations** like union, intersection, and difference.

# Common Set Operations:
# ----------------------
# 1. **Adding Elements** – Use `.add()` to add a single element.
# 2. **Removing Elements** – Use `.remove()` (raises error if missing) or `.discard()` (no error if missing).
# 3. **Set Union** – Combines two sets and keeps only unique elements.
# 4. **Set Intersection** – Keeps only the common elements from both sets.
# 5. **Set Difference** – Returns elements that are in one set but not in the other.
# 6. **Symmetric Difference** – Returns elements that are in either set, but not both.
# 7. **Checking Subset/Superset** – Use `.issubset()` and `.issuperset()` to compare sets.

# Example Use Cases:
# ------------------
# - **Removing duplicates** from a list.
# - **Checking common elements** between two sets of data.
# - **Finding unique words** in a text file.
# - **Tracking visited pages** in a web application.


"""
========================================
          Python Learning Sheet:
                 Sets
========================================
"""

# 1. Create a Set
# Create a set called `fruits_set` containing 5 different fruits.

fruits_set = {"apple", "pear", "strawberry", "raspberry", "watermelon"}
print(fruits_set)


# 2. Check if an Element Exists in a Set
# Since sets are unordered, elements cannot be accessed by index.
# Instead, use 'in' to check for membership.

print("apple" in fruits_set)  # True
print("banana" in fruits_set)  # False


# 3. Add Elements to a Set
# Use `.add()` to insert a new element.

fruits_set.add("Mango")
print(fruits_set)


# 4. Remove Elements from a Set
# Use `.remove()` (raises an error if the element is missing).

fruits_set.remove("apple")
print(fruits_set)

# Alternative: Use `.discard()` to avoid an error if the element is missing.
fruits_set.discard("banana")  # No error, even if "banana" is not in the set


# 5. Set Length
# Write a function `set_length(s)` that returns the number of elements in a set.

def set_length(s):
    return len(s)

print(set_length(fruits_set))  # Output depends on set content


# 6. Iterate Over a Set
# Use a loop to iterate through set elements.

for fruit in fruits_set:
    print(fruit)


# 7. Union of Two Sets
# Write a function `union_sets(set1, set2)` that returns the union of two sets.

set1 = {"a", "b", "c"}
set2 = {"c", "d", "e"}

def union_sets(set1, set2):
    return set1.union(set2)

print(union_sets(set1, set2))  # {'a', 'b', 'c', 'd', 'e'}


# 8. Intersection of Two Sets
# Write a function `intersection_sets(set1, set2)` that returns the intersection of two sets.

def intersection_sets(set1, set2):
    return set1.intersection(set2)

print(intersection_sets(set1, set2))  # {'c'}


# 9. Difference of Two Sets
# Write a function `difference_sets(set1, set2)` that returns elements in `set1` but not in `set2`.

def difference_sets(set1, set2):
    return set1.difference(set2)

print(difference_sets(set1, set2))  # {'a', 'b'}


# 10. Symmetric Difference of Two Sets
# Write a function `symmetric_difference_sets(set1, set2)` that returns elements in either set, but not both.

def symmetric_difference_sets(set1, set2):
    return set1.symmetric_difference(set2)

print(symmetric_difference_sets(set1, set2))  # {'a', 'b', 'd', 'e'}


# 11. Check Subset and Superset
# Write functions `is_subset(sub, main)` and `is_superset(main, sub)`.

def is_subset(sub, main):
    return sub.issubset(main)

def is_superset(main, sub):
    return main.issuperset(sub)

small_set = {"a", "b"}
big_set = {"a", "b", "c"}

print(is_subset(small_set, big_set))  # True
print(is_superset(big_set, small_set))  # True


# 12. Convert a List to a Set
# Write a function `list_to_set(lst)` that removes duplicates from a list by converting it to a set.

def list_to_set(lst):
    return set(lst)

print(list_to_set([1, 2, 2, 3, 4, 4, 5]))  # {1, 2, 3, 4, 5}
