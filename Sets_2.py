# Understanding Sets in Python

# What is a Set?
# A set is a collection of unique and unordered elements. Unlike lists, sets do not allow duplicate values, and they do not maintain any specific order.

# Key Features of Sets:

# Unordered – The elements in a set do not have a fixed position.
# Unique Elements – A set automatically removes duplicates.
# Mutable – You can add or remove elements, but you cannot modify existing ones.
# Efficient Membership Check – Checking if an item exists in a set is faster than in a list.



# When to Use a Set?

# When you need a collection of unique values.
# When you frequently check if an element exists in a collection.
# When you need to perform set operations like union, intersection, and difference.


# Common Set Operations:

# Adding Elements – Use .add() to add a single element.

# Removing Elements – Use .remove() (raises error if missing) or .discard() (no error if missing).

# Set Union – Combines two sets and keeps only unique elements.

# Set Intersection – Keeps only the common elements from both sets.

# Set Difference – Returns elements that are in one set but not in the other.

# Symmetric Difference – Returns elements that are in either set, but not both.

# Checking Subset/Superset – Use .issubset() and .issuperset() to compare sets.


# Example Use Cases:

# Removing duplicates from a list.

# Checking common elements between two sets of data.

# Finding unique words in a text file.

# Tracking visited pages in a web application.
