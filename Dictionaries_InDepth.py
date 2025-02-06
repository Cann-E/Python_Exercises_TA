

#1 Dictionaries

dictionary={"can":21,"mike":30,"charlie":35}

dictionary_2 = {
    "brand":"Ford",
    "model":"Mustang",
    "year":2021
    }

print(dictionary)
print(dictionary_2)
print("----------------")


print(dictionary["mike"])
print(dictionary_2["model"])
print("----------------")

print(dictionary.get("charlie"))
print(dictionary_2.get("brand"))
print("----------------")

print(dictionary.keys())   #The keys() method will return a list of all the keys in the dictionary.lest side
print(dictionary.values())#The values() method will return a list of all the values in the dictionary.
print("----------------")

print(dictionary_2.keys()) #The keys() method will return a list of all the keys in the dictionary.
print(dictionary_2.values()) #The values() method will return a list of all the values in the dictionary.Right side
print("----------------")

print(dictionary.items()) #shows as tuples
print(dictionary_2.items()) 
print("----------------")


#2 Access Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
  
#3 Change Values

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018
thisdict.update({"model":"F150"}) #Update the "year" of the car by using the update() method:
print(thisdict["model"])


#4 Add Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#5 Remove Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model") # thisdict.popitem()  popitem() removes the last inserted item  # del thisdict["model"]  del keyword removes the item with the specified key
print(thisdict)

#6 loop through Dictionaries

for x in thisdict:
  print(x)
  
  #Print all values in the dictionary, one by one:

for x in thisdict:
  print(thisdict[x])
  
#You can also use the values() method to return values of a dictionary:

for x in thisdict.values():
  print(x)
  
#Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
  print(x, y)
