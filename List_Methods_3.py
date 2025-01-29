

#1 ADD
letters=["a","b","c"]
letters.append("5") #add to the end of the list ['a', 'b', 'c', '5']
print(letters)
letters.insert(1,"hey") #insert the exact location you want to add in the list  ['a', 'hey', 'b', 'c', '5']
print(letters)


# Remove
letters=["a","b","c"]
letters.pop() #remove the last item in the list ['a', 'b']
print(letters)

#Remove Specific with index
letters_2=["a","b","c","d"]
letters_2.pop(2) #removes the item using the index of the item whichever item index you want to ['a', 'b', 'd']
print(letters_2)

#Remove if you dont know the index of the item
letters_3=["a","b","c","d","e"]
letters_3.remove("d") #if you dont know the index you can specify the item ['a', 'b', 'c', 'e']
print(letters_3)

#Remove using del if you want to remove multiple items
letters_4=["a","b","c","d","e"]
del letters_4[1:3] #deleting range of items ['a', 'd', 'e']
print(letters_4)

#Remove clear() to empty the list



#List Comprehension
#Conver a list of string to Uppercase

words = ["hello", "world", "python"]

uppercase_words = []
for word in words:
    uppercase_words.append(word.upper())

print(uppercase_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']

#####SHORTER WAY

words = ["hello", "world", "python"]

uppercase_words = [word.upper() for word in words]

print(uppercase_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']



#GET ONLY NUMBERS GREATER THAN 5


numbers = [2, 5, 8, 1, 10, 3]

greater_than_five = []
for num in numbers:
    if num > 5:
        greater_than_five.append(num)

print(greater_than_five)  # Output: [8, 10]

####ALTERNATE SHORTER 


numbers = [2, 5, 8, 1, 10, 3]

greater_than_five = [num for num in numbers if num > 5]

print(greater_than_five)  # Output: [8, 10]













