
# Nested Dictionaries (31-40)

# Create a dictionary that contains three nested dictionaries and print it.

nest_dict={
    "student1":{"can":20,"major":"CS","GPA":3.75},
    "student2":{"mike":40,"major":"marketing","GPA":4.0},
    "student3":{"sarah":19,"major":"English","GPA":2.5}
}

print(nest_dict)

# Access and print a value from a nested dictionary.

nest_dict={
    "student1":{"can":20,"major":"CS","GPA":3.75},
    "student2":{"mike":40,"major":"marketing","GPA":4.0},
    "student3":{"sarah":19,"major":"English","GPA":2.5}
}

print(nest_dict["student2"])

# Add a new key-value pair inside a nested dictionary.

nest_dict={
    "student1":{"can":20,"major":"CS","GPA":3.75},
    "student2":{"mike":40,"major":"marketing","GPA":4.0},
    "student3":{"sarah":19,"major":"English","GPA":2.5}
}

nest_dict["student4"] = {"name": "TEST"}
print(nest_dict)

# Update a value inside a nested dictionary.

nest_dict={
    "student1":{"can":20,"major":"CS","GPA":3.75},
    "student2":{"mike":40,"major":"marketing","GPA":4.0},
    "student3":{"sarah":19,"major":"English","GPA":2.5}
}

nest_dict["student1"]["can"]=99
nest_dict["student99"]=nest_dict.pop("student3")
print(nest_dict)

# Remove a key-value pair from a nested dictionary.

nest_dict={
    "student1":{"can":20,"major":"CS","GPA":3.75},
    "student2":{"mike":40,"major":"marketing","GPA":4.0},
    "student3":{"sarah":19,"major":"English","GPA":2.5}
}

nest_dict["student1"].pop("can")
print(nest_dict)

# Loop through a nested dictionary and print each key-value pair.

nest_dict={
    "student1":{"can":20,"major":"CS","GPA":3.75},
    "student2":{"mike":40,"major":"marketing","GPA":4.0},
    "student3":{"sarah":19,"major":"English","GPA":2.5}
}

for student in nest_dict:
    for key in nest_dict[student]:
        print(key, ":", nest_dict[student][key])

# Create three separate dictionaries and combine them into a nested dictionary.

nest_dict={
    "student1":{"can":20,"major":"CS","GPA":3.75},
    "student2":{"mike":40,"major":"marketing","GPA":4.0},
    "student3":{"sarah":19,"major":"English","GPA":2.5}
}

nest_dict2={
    "student4":{"jessie":20,"major":"CS","GPA":3.75},
    "student5":{"charlie":40,"major":"marketing","GPA":4.0},
    "student6":{"king":19,"major":"English","GPA":2.5}
}


nest_dict3={
    "student7":{"troy":20,"major":"CS","GPA":3.75},
    "student8":{"leira":40,"major":"marketing","GPA":4.0},
    "student9":{"kenan":19,"major":"English","GPA":2.5}
}

merged_dict=nest_dict | nest_dict2 | nest_dict3
print(merged_dict)


# Write a program to count how many nested dictionaries exist inside a given dictionary.

nest_dict3={
    "student7":{"troy":20,"major":"CS","GPA":3.75},
    "student8":{"leira":40,"major":"marketing","GPA":4.0},
    "student9":{"kenan":19,"major":"English","GPA":2.5}
}

count=0
for i in nest_dict3:
    count+=1
    print(count)
    
    

# Write a function that takes a nested dictionary and returns a list of all values inside it.

nest_dict3 = {
    "student7": {"troy": 20, "major": "CS", "GPA": 3.75},
    "student8": {"leira": 40, "major": "marketing", "GPA": 4.0},
    "student9": {"kenan": 19, "major": "English", "GPA": 2.5}
}

def dict_to_list(nested_dict):
    values_list = []  
    for student in nested_dict.values():  # Loop through the outer dictionary
        for value in student.values():  # Loop through the inner dictionary
            values_list.append(value)  # Append each value to the list
    return values_list

print(dict_to_list(nest_dict3))



# Modify a nested dictionary by adding a new sub-dictionary inside an existing dictionary.

nest_dict2={
    "student4":{"jessie":20,"major":"CS","GPA":3.75},
    "student5":{"charlie":40,"major":"marketing","GPA":4.0},
    "student6":{"king":19,"major":"English","GPA":2.5}
}

nest_dict2["student4"]["country"]="France"
print(nest_dict2)