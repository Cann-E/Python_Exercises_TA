
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
print(copy_==dict_5)



# Use the update() method to update a dictionary with another dictionary’s values.

dict_6={
    "name":"can",
    "age":21,
    "gender":"m"
}

dict_7={"name":"mike","age":99,"gender":"f"}

dict_6.update(dict_7)
print(dict_6)

# Write a program that creates a dictionary, copies it, and checks if they have the same contents but different memory locations.

dict_8={"name":"sarah","age":"30","major":"Cs"}

copy_8=dict_8.copy()

if copy_8 == dict_8 and id(copy_8) != id(dict_8):
    print("Copies have same values but different memory locations.")
else:
    print("Something is wrong!")


# Merge two dictionaries and remove a key from the merged dictionary.

dict_9={
    "name":"can",
    "age":21,
    "gender":"m"
}

dict_10={"name_2":"mike","age_2":99,"gender_2":"f"}

merged_dict= dict_9 | dict_10
merged_dict.pop("name")
print(merged_dict)

# Merge two dictionaries and print only the common keys.

dict_11={"name":"mike","age":25,"gender":"M"}

dict_12={
    "name":"charlie",
    "make":"maserati",
    "model":"ghibli",
    "year":2020
}

common_keys = set(dict_11.keys()) & set(dict_12.keys()) 
print(common_keys)
merged_dict_1=dict_11 | dict_12
print(merged_dict_1)

# Create two dictionaries and find keys that exist in both.

dict_13={"name":"mike","age":25,"gender":"M"}

dict_14={
    "name":"charlie",
    "make":"maserati",
    "model":"ghibli",
    "year":2020
}

common_keys = set(dict_13.keys()) & set(dict_14.keys()) 

if common_keys:
    print(f"Common Keys {common_keys}")
else:
    print("No common!")


# Find the difference between two dictionaries (keys that exist in one but not the other).

dict_15={"name":"mike","age":25,"gender":"M"}

dict_16={
    "name":"charlie",
    "make":"maserati",
    "model":"ghibli",
    "year":2020
}

diff_keys=set(dict_15.keys()) ^ set(dict_16.keys())

print (diff_keys)