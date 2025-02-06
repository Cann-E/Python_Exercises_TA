
# Basic Dictionary Operations (1-10)

# Create a dictionary with three key-value pairs and print it.

can_dict={"can":"computer science","mike":"marketing","charlie":"history"}
print(can_dict)

# Access and print a value from a dictionary using square brackets.

dict_1 = {"can":15,"jamal":19,"sarah":55}
print(dict_1["jamal"])

# Access and print a value from a dictionary using the get() method.

dict_2={"make":"maserati","model":"ghibli","year":2018,"mileage":35000}
print(dict_2.get("mileage"))

# Print only the keys of a dictionary using the keys() method.
dict_3={
    "age":21,
    "gender":"M",
    "height":170
}

print(dict_3.keys())

# Print only the values of a dictionary using the values() method.
dict_4 = {
    "age":25,
    "name":"can",
    "weight":185
}

print(dict_4.values())

# Print all key-value pairs of a dictionary using the items() method.
dict_5 = {"gender":"F","name":"Susan"}
print(dict_5.items())

# Check if a specific key exists in a dictionary using an if statement.
dict_6={
    "book":"Harry Potter",
    "author":"JK rowlings"
}

if "author" in dict_6:
    print("Exists!")
else:
    print("Dont Exists!")

# Modify the value of an existing key in a dictionary.

dict_7={"name":"can","age":19}

if "age" in dict_7:
    dict_7["age"]= 25
else:
    print("not found")
    
print(dict_7)

# Add a new key-value pair to an existing dictionary.

dict_8={
    "name":"can",
    "major":"CS",
    "GPA":"3.6"
}

dict_8["class"]="4321"
print(dict_8)

# Remove a key-value pair from a dictionary using the pop() method.

dict_9={"make":"maserati","model":"ghibli","age":2018}

dict_9.pop("age")
print(dict_9)