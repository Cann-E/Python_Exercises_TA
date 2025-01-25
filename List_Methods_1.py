
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

# Test the function
print(find_largest(num))  # Output: 45




