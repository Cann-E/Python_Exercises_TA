#1 List
letters=["a","b","c"]

#2 Matrix
matrix=[[1,0],[1,1],[0,1]]

#3 Multiplying A list
zeros=[0]* 100 #multiplying a list 

#4 Multiplying A list
ones=[1]*5 #multiplying a list
print(ones)

#5 Adding 2 lists
concatinate=letters+ones #adding two lists together
print(concatinate)

#6 Create a list from the range number given
numbers=list(range(20)) #itirate from 0 to 20
print(numbers)

#7 Iitirate Each Char
chars=list("Can Ercan") #itirate each characters
print(chars)

#8 Char lenght
chars=list("Can Ercan") #lenght of how many chartacter iterations
print(len(chars))

# 9 First and Last Element
letters=["a","b","c","d","e"]
print(letters[0]) #index 0 print first element from the list
print(letters[-1])#index last print last element from the list

# 10 Changin Index
letters=["a","b","c","d","e"]
letters[2]="5" #changing index 2 from "c" to 5
print(letters)

# 11 Slicing
letters=["a","b","c","d","e","f","g","h"]
print(letters[3:6]) #from index 3 to 6 slice the list and print out d e f

# 12 Getting every Other element from the list
number=list(range(20))
print(numbers[::2]) #gets every other element from the list
print(numbers[::3]) 
print(numbers[::-1]) #get every element reverse order


# 13 Getting Every Other Char from the list
letters=["a","b","c","d","e","f","g","h"]
print(letters[0::2]) #left side start index right side frequency
print(letters[2::2])


# 14 List Unpacking
letters=["a","b","c"]
first,second,third=letters #matching each element in the list with the variables
print(second)


# 15 List unpacking and packing it in other list
letters=["a","b","c","d","e","f","g","h"]
first,second, *other=letters
print(first)
print(second)
print(other)


# 16 List unpacking and packing it in other list and getting last
letters=["a","b","c","d","e","f","g","h"]
first, *other,last=letters
print (last,first)



# 17 Loop Over lists
letters=["a","b","c","d","e","f","g","h"]
for letter in letters:
    print(letter)


# 18 Getting each index in the list enumerate() function
letters=["a","b","c","d","e","f","g","h"]
for letter in enumerate(letters): #creates tuples read only cant edit  (0, 'a')
    print(letter)


# 19 Tuples
letters=["a","b","c","d","e","f","g","h"]
for letter in enumerate(letters): #creates tuples read only cant add items  (0, 'a')
    # print(letter[0]) #getting the left side of the tuples which means index side (0, 'a') 0 1 2 ETC
    # print(letter[1]) #getting the right side of the tuple (0, 'a') a b c etc
    print(letter[0],letter[1])

# 20 Tuples unpacking way
letters=["a","b","c","d","e","f","g","h"]
for index,letter in enumerate(letters):
    print(index,letter)


