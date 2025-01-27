# 1. Count Occurrences
# Write a function `count_occurrences(lst, element)` that counts and returns 
# the number of times `element` appears in the list.
# Test it with the list: [1, 2, 3, 4, 2, 3, 2] and element 2.

def count_occurence(lst,element):
    return lst.count(element)

test=[1, 2, 3, 4, 2, 3, 2]
print(count_occurence(test,2))

# 2. Remove Duplicates
# Write a function `remove_duplicates(lst)` that takes a list as input 
# and returns a new list with all duplicates removed.
# Test it with the list: [1, 2, 2, 3, 4, 4, 5].

num=[1, 2, 2, 3, 4, 4, 5]

def remove_duplicated(lst):
    new_list=list(set(lst))
    return new_list

num=remove_duplicated(num)
print(num)




# 3. Reverse a List
# Write a function `reverse_list(lst)` that takes a list as input 
# and returns the list in reverse order.
# Test it with the list: [1, 2, 3, 4, 5].

def reverse_list(lst):
    return lst.reverse()

test2=[1, 2, 3, 4, 5]
reverse_list(test2)
print(test2)

# 4. Find Second Largest
# Write a function `find_second_largest(lst)` that returns the second largest 
# number in the list. Assume the list has at least 2 unique numbers.
# Test it with the list: [10, 20, 4, 45, 99].

def find_second_largest(lst):
    largest=max(lst)
    lst.remove(largest)
    second_largest=max(lst)
    return second_largest

test3=[10, 20, 4, 45, 99]
print(find_second_largest(test3))

# 5. Merge and Sort Lists
# Write a function `merge_and_sort(lst1, lst2)` that takes two lists, merges them,
# and returns a new list sorted in ascending order.
# Test it with the lists: [3, 1, 4] and [5, 2, 6].

def merge_and_sort(lst1,lst2):
    newlist=lst1+lst2
    newlist.sort()
    return newlist

lst_1=[3, 1, 4]
lst_2=[5, 2, 6]

new=merge_and_sort(lst_1,lst_2)
print(new)



# 6. Find Common Elements
# Write a function `common_elements(lst1, lst2)` that takes two lists 
# and returns a new list containing only the elements that are present in both lists.
# Test it with the lists: [1, 2, 3, 4] and [3, 4, 5, 6].

def common_elements(lst1,lst2):
    return list(set(lst1) & set(lst2))

lst_1 = [1, 2, 3, 4]
lst_2 = [3, 4, 5, 6]

common=common_elements(lst_1,lst_2)
print(common)

# 7. Separate Even and Odd Numbers
# Write a function `separate_even_odd(lst)` that takes a list of numbers 
# and returns two separate lists: one containing even numbers and the other containing odd numbers.
# Test it with the list: [1, 2, 3, 4, 5, 6, 7, 8, 9].

lst_5=[1, 2, 3, 4, 5, 6, 7, 8, 9]

def separate_even_odd(lst):
    even=[]
    odd=[]
    for num in lst:
        if num%2==0:
            even.append(num)
        else:
            odd.append(num)
    return even,odd
    
even,odd=separate_even_odd(lst_5)
print(even)
print(odd)
        
    
    

# 8. Find All Pairs That Add Up to a Target
# Write a function `find_pairs(lst, target)` that finds and returns all pairs 
# of numbers in the list that add up to the given target.
# Test it with the list: [1, 2, 3, 4, 5] and target 6.

def find_pairs(lst,target):
    pairs=[]
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==target:
                pairs.append((lst[i],lst[j]))
    return pairs
    
    
numbers_=[1, 2, 3, 4, 5]
result=find_pairs(numbers_,6)
print(result)


# 9. Rotate List
# Write a function `rotate_list(lst, k)` that rotates the list to the right by `k` positions.
# Test it with the list: [1, 2, 3, 4, 5] and k = 2.

def rotate_list(lst,k):
    n=len(lst)
    k=k%n
    return lst[-k:],lst[:-k]

a=[1, 2, 3, 4, 5]
b=rotate_list(a,2)
print(b)
        

# 10. Flatten a Nested List
# Write a function `flatten_list(nested_lst)` that takes a nested list as input 
# and returns a single flattened list. Assume the nested list can contain lists within lists.
# Test it with the list: [[1, 2], [3, 4], [5, 6]].

def flatten_list(nested_lst):
    single_list=[]
    for i in (nested_lst):
        for j in i:
            single_list.append(j)
    return single_list

c=[[1, 2], [3, 4], [5, 6]]
d=flatten_list(c)
print(d)


#11. Write a function find_pairs(lst, target) that finds and returns all pairs of numbers from a list that add up to the given target.
# Test it with the list [10, 20, 30, 40, 50, 60] and target 70.


def find_pairs(lst,target):
    pairs=[]
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==target:
                pairs.append((lst[i],lst[j]))
    return pairs

x=[10, 20, 30, 40, 50, 60]

res=find_pairs(x,70)
print(res)

#12. Write a function find_pairs(lst, target) that finds and returns all pairs of numbers in the list that add up to the given target.

# Test it with the list [3, 8, 12, 15, 7, 5, 10] and target 15.

def find_pairs_1(lst,target):
    pairs=[]
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==target:
                pairs.append((lst[i],lst[j]))
    return pairs

x=[3, 8, 12, 15, 7, 5, 10]
res=find_pairs_1(x,15)
print(res)