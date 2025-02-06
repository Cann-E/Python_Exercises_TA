
# Looping Through Dictionaries (11-20)

# Loop through a dictionary and print all keys.

dict_1={"name":"can","gender":"male","age":50}

for i in dict_1:
    print(dict_1.keys())

# Loop through a dictionary and print all values.

dict_2={
    "name":"mike",
    "age":31,
    "sex":"M"
}

for i in dict_2:
    print(dict_2.values())

# Loop through a dictionary and print all key-value pairs.

dict_3={"make":"bmw","model":"m5","year":2020}

for i in dict_3:
    print(dict_3.items())

# Create a dictionary with five key-value pairs and use a loop to print only the keys that start with the letter ‘a’.

dict_4={"age":25,"name":"can","alive":"yes","gender":"M","height":"5-7"}
found= False

for i in dict_4:
    if i[0]=="a":
        print(i)
        found = True
if not found:
    print("there is no keys start with a")

# Create a dictionary with names as keys and ages as values. Print only the names of people above 25 years old.

# Print only the values of a dictionary using the values() method inside a loop.

# Print only the keys of a dictionary using the keys() method inside a loop.

# Loop through a dictionary and print each key along with its length.

# Loop through a dictionary and count how many values are greater than 50.

# Use a loop to check if a dictionary contains a certain key and print its value if it exists.