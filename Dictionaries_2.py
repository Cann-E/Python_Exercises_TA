
# Looping Through Dictionaries (11-20)

# Loop through a dictionary and print all keys.

dict_1={"name":"can","gender":"male","age":50}

for i in dict_1.keys():
    print(i)

# Loop through a dictionary and print all values.

dict_2={
    "name":"mike",
    "age":31,
    "sex":"M"
}

for i in dict_2.values():
    print(i)

# Loop through a dictionary and print all key-value pairs.

dict_3={"make":"bmw","model":"m5","year":2020}

for i in dict_3.items():
    print(i)

# Create a dictionary with five key-value pairs and use a loop to print only the keys that start with the letter ‘a’.

dict_4={"age":25,"name":"can","alive":"yes","gender":"M","height":"5-7"}
found= False

for i in dict_4:
    if i[0]=="a":
        print(i)
        found = True
if not found:
    print("there is no keys start with a")
    
print("----------------")

# Create a dictionary with names as keys and ages as values. Print only the names of people above 25 years old.

dict_can={
    "can":5,
    "mike":10,
    "sarah":26,
    "jessica":35,
    "cher":56
}

for name,age in dict_can.items():
    if age > 25:
        print(name)


# Print only the values of a dictionary using the values() method inside a loop.

dict_can_1={
    "can":5,
    "mike":10,
    "sarah":26,
    "jessica":35,
    "cher":56
}

for i in dict_can_1.values():
    print(i)


# Print only the keys of a dictionary using the keys() method inside a loop.

dict_can_2={
    "can":5,
    "mike":10,
    "sarah":26,
    "jessica":35,
    "cher":56
}

for i in dict_can_2.keys():
    print(i)

# Loop through a dictionary and print each key along with its length.

dict_can_3={
    "can":5,
    "mike":10,
    "sarah":26,
    "jessica":35,
    "cher":56
}

for i in dict_can_3.keys():
    print(i,len(i))

# Loop through a dictionary and count how many values are greater than 50.

dict_can_4={
    "can":5,
    "mike":10,
    "sarah":26,
    "jessica":35,
    "cher":56
}
count=0
for i in dict_can_4.values():
    if i>50:
       
        count+=1
        print(count)

# Use a loop to check if a dictionary contains a certain key and print its value if it exists.

dict_can_5 = {
    "can": 5,
    "mike": 10,
    "sarah": 26,
    "jessica": 35,
    "cher": 56
}

key_to_find = "mike"  

found = False  

for key in dict_can_5:
    if key == key_to_find:
        print(f"Key found: {key}, Value: {dict_can_5[key]}")
        found = True
        break  

if not found:
    print("Key not found")
