
# Advanced Dictionary Operations (41-45)

# Write a function that removes all key-value pairs where the value is None from a dictionary.

def remove_none_values():
    for key in list(dict_can.keys()):
        if dict_can[key] is None:
            dict_can.pop(key)
    print("Updated Dictionary:", dict_can)


dict_can = {"name": "mike", "age": 25, "country": None, "city": "New York"}

remove_none_values()


# Create a dictionary with numbers as values and find the sum of all values.

dict_num={
    "height":170,
    "weight":90,
    "shoesize":45
}
sum_val=0
for i in dict_num.values():
    sum_val+=i
    
print(sum_val)

print(sum(dict_num.values()))  # alternative simpler same result



# Create a dictionary with numbers as values and find the largest value.

dict_num={
    "height":170,
    "weight":90,
    "shoesize":45
}

print(max(dict_num.values()))
    

# Write a program that converts two lists (one of keys and one of values) into a dictionary.

fruits = ["apple", "pear", "strawberry", "raspberry", "watermelon"]
numbers = ["3", "4", "2", "11", "7"]

merged_dict = dict(zip(fruits, numbers))  # Convert two lists into a dictionary

print(merged_dict)


# Write a function that takes a dictionary and returns a new dictionary where the values are squared.

def squared(d):
    new_dict = {}  # Create an empty dictionary
    for key, value in d.items():  # Loop through each key-value pair
        new_dict[key] = value ** 2  # Square the value and store it in new_dict
    return new_dict  # Return the new dictionary

dict_1 = {"make": 1, "model": 2, "year": 3, "mileage": 4}
print(squared(dict_1))
