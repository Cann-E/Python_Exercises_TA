
# 1-append

people=["CAN","ASLI","REMY"]
people.append("Lyndsey")
print(people)



# 2-clear

people=["CAN","ASLI","REMY"]
people.clear()
print(people)

# 3-copy

people=["CAN","ASLI","REMY"]
copy_people=people.copy()
people.append("Lyndsey")
copy_people.remove("ASLI")
print(people)
print(copy_people)


# 4-count

people=["CAN","ASLI","REMY","CAN"]
count_CAN=people.count("CAN")#counts how many CAN repeats in the list
print(count_CAN) 



# 5-extend

people=["CAN","ASLI","REMY"]
cars=["MASERATI","MERCEDES","KIA"]
people.extend(cars)

print(people)


# 6-index

people=["CAN","ASLI","REMY"]  #[0,1,2]
print(people.index("ASLI"))



# 7-insert

people=["CAN","ASLI","REMY","Pasha","Minnak"]
people.insert(1,"Lyndsey")
people.insert(3,"Hina")
print(people)


# 8-pop

people=["CAN","ASLI","REMY","Pasha","Minnak"]
popped=people.pop(3)
print(people)
print(popped)


# 9-remove

people=["CAN","ASLI","REMY","Pasha","Minnak"]
people.remove("REMY")
print(people)


# 10.reverse

people=["CAN","ASLI","REMY","Pasha","Minnak"]
people.reverse()
print(people)



# 11-sort

people=["CAN","ASLI","REMY","Pasha","Minnak"]
people.sort()
print(people)



#12-sorted

numbers = ["3", "4", "2", "11", "7"]

def sort_list(lst):
    return sorted(lst)  # Returns a new sorted list

print(sort_list(numbers))  # Print the sorted list


#13-max

num = [12, 45, 7, 29, 30]

def find_largest(lst):
    return max(lst)  # Use the built-in `max()` function to find the largest number

print(find_largest(num)) 


#14 Set 

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers)) #Removes Duplicates 
print(unique_numbers)

#15 Common Elements

lst_1 = [1, 2, 3, 4]
lst_2 = [3, 4, 5, 6]

def common_elements(lst1,lst2):
    return list(set(lst1) & set(lst2)) #intersection of the set1 & set2

common=common_elements(lst_1,lst_2)
print(common)


#16 For loop is to itirate over items in a collection

numbers = [1, 2, 3, 4]

for num in numbers: #for each number inside the numbers list
    print(num)  #print each number
    
fruits=["apple","pear","watermelon"]

for fruit in fruits:
    print(fruit)
    
name = "Python"

for char in name:
    print(char)







