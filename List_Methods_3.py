

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


