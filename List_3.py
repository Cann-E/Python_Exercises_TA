# 1. Create a List with a Range
# Create a list called nums with all integers from 1 to 10 (inclusive) using the range() function.
# Print the list.

nums=list(range(1,11))
print(nums)



# 2. Reverse a List
# Create a list called words with the elements: "sun", "moon", "stars".
# Reverse the list using the reverse() method and print the updated list.
words=["sun", "moon", "stars"]
words.reverse()
print(words)

# 3. Check Membership
# Create a list called items with the elements: "pen", "notebook", "eraser", "ruler".
# Check if "pen" is in the list using the in keyword and print the result.

items=["pen", "notebook", "eraser", "ruler"]
if "pen" in items:
    print("Pen Found")

# 4. Concatenate Two Lists
# Create two lists:
# list_a = [10, 20, 30]
# list_b = [40, 50, 60].
# Concatenate the two lists using the + operator and print the resulting list.

list_a = [10, 20, 30]
list_b = [40, 50, 60]
new_=list_a+list_b
print(new_)

# 5. Find the Maximum and Minimum
# Create a list called temperatures with the elements: [25, 30, 28, 22, 35, 31].
# Find and print the maximum and minimum values using max() and min().

temperature=[25, 30, 28, 22, 35, 31]
print(max(temperature))
print(min(temperature))

# 6. Sort a List
# Create a list called ages with the elements: [25, 22, 30, 18, 27].
# Sort the list in ascending order using the sort() method and print the sorted list.

ages=[25, 22, 30, 18, 27]
ages.sort()
print(ages)

# 7. Copy a List
# Create a list called cities with the elements: "New York", "Paris", "Tokyo".
# Create a copy of the list using the copy() method and print the copied list.

cities=["New York", "Paris", "Tokyo"]
cities_copy=cities.copy()
print(cities_copy)

# 8. Find the Length of a List
# Create a list called pets with the elements: "dog", "cat", "fish", "hamster", "bird".
# Find and print the length of the list using the len() function.

pets=["dog", "cat", "fish", "hamster", "bird"]
print(len(pets))

# 9. Multiply a List
# Create a list called letters with the elements: "a", "b", "c".
# Multiply the list by 3 using the * operator and print the resulting list.

letters=["a", "b", "c"]
print(letters*3)

# 10. Insert an Element
# Create a list called books with the elements: "Harry Potter", "The Hobbit", "1984".
# Insert the element "Pride and Prejudice" at the second position using the insert() method.
# Print the updated list.


books=["Harry Potter", "The Hobbit", "1984"]
books.insert(1,"Pride and Prejudice")
print(books)

