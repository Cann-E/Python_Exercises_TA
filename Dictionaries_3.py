
# Copying and Merging Dictionaries (21-30)

# Copy a dictionary using the copy() method and print the copy.
dict_1={"make":"bmw","model":"m6","year":2021,"mileage":13500}
copy_dict=dict_1.copy()
print(copy_dict)

# Copy a dictionary using the dict() function and print the copy.

dict_2={
    "name":"can",
    "age":40,
    "sex":"M"
}

copy_=dict(dict_2)
print(copy_)

# Merge two dictionaries into one dictionary and print the result.

dict_3={"name":"mike","age":25,"gender":"M"}

dict_4={
    "make":"maserati",
    "model":"ghibli",
    "year":2020
}

merged_=dict_3 | dict_4
print(merged_)

# Create a dictionary and make two separate copies. Modify one copy and compare it to the original dictionary.

dict_5={"hey":"wave","kick":"dance","shout":"yell"}

copy_=dict(dict_5)
copy_2=dict_5.copy()


copy_["age"]=20
print(copy_)
print(dict_5)


# Use the update() method to update a dictionary with another dictionary’s values.



# Write a program that creates a dictionary, copies it, and checks if they have the same contents but different memory locations.

# Merge two dictionaries and remove a key from the merged dictionary.

# Merge two dictionaries and print only the common keys.

# Create two dictionaries and find keys that exist in both.

# Find the difference between two dictionaries (keys that exist in one but not the other).