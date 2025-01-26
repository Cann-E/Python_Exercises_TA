# 1. Create an Empty List
# Create an empty list called `my_list`.
# Add three different elements to the list using the `append()` method.
# Print the final list.

my_list=[]
my_list.append("apple")
my_list.append("pencil")
my_list.append("coke")
print(my_list)

# 2. Access Multiple Elements
# Create a list called `colors` with the elements: "red", "blue", "green", "yellow".
# Print the second and third elements using indexing.

colors=["red","blue","green","yellow"]
print(colors[2],colors[3])

# 3. Slice a List
# Create a list called `numbers` with the elements: [10, 20, 30, 40, 50, 60, 70].
# Print the first three elements and the last two elements using slicing.

numbers=[10, 20, 30, 40, 50, 60, 70]
print(numbers[0:3],numbers[4:6])

# 4. Replace an Element
# Create a list called `animals` with the elements: "cat", "dog", "rabbit".
# Replace "dog" with "elephant" and print the updated list.

animals=["cat", "dog", "rabbit"]
animals[1]="elephant"
print(animals)

# 5. Extend a List
# Create two lists: `list1` with [1, 2, 3] and `list2` with [4, 5, 6].
# Use the `extend()` method to add all elements of `list2` to `list1`.
# Print the extended list.

list1=[1, 2, 3]
list2=[4, 5, 6]
list1.extend(list2)
print(list1)


# 6. Remove an Element
# Create a list called `fruits` with the elements: "apple", "banana", "cherry", "date".
# Remove "cherry" from the list using the `remove()` method and print the updated list.

fruits=["apple", "banana", "cherry", "date"]
fruits.remove("cherry")
print(fruits)

# 7. Pop an Element
# Create a list called `tasks` with the elements: "clean", "cook", "shop", "study".
# Use the `pop()` method to remove the last element and print the updated list.

tasks=["clean", "cook", "shop", "study"]
tasks.pop()
print(tasks)

# 8. Count Elements in a List
# Create a list called `numbers` with the elements: [1, 2, 3, 2, 4, 2, 5].
# Use the `count()` method to find how many times `2` appears in the list.

numbers=[1, 2, 3, 2, 4, 2, 5]
print(numbers.count(2))


# 9. Find the Index of an Element
# Create a list called `names` with the elements: "Alice", "Bob", "Charlie", "David".
# Use the `index()` method to find the index of "Charlie".

names=["Alice", "Bob", "Charlie", "David"]
print(names.index("Charlie"))

# 10. Clear a List
# Create a list called `shopping_cart` with the elements: "milk", "eggs", "bread", "butter".
# Use the `clear()` method to remove all elements from the list and print the empty list.

shopping_cart=["milk", "eggs", "bread", "butter"]
shopping_cart.clear()
print(shopping_cart)
