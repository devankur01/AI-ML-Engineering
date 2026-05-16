# 1). Write a program to find the largest and smallest elements in a list.
'''
nums = [4, 8, 1, 9, 2]    

largest = nums[0]   
smallest = nums[0]

for i in nums : 
    if i > largest :    
        largest = i

    if i < smallest :   
        smallest = i

print("Largest:", largest)
print("Smallest:", smallest)
'''

# 2). Write a program to remove duplicate elements form a list.     
'''
values = [1111,222,33,33,2222,222,4444]    
unique = [] 
for i in values:    
    if i not in unique:    # mtlb agr isme i ki value nhi h to hi ye append krega list ke item ko nhi to nhi krega.
        unique.append(i)    

print(unique)
'''

# 3). Write a program to reverse a list without using built-in reverse method.
'''
mylist = [1,2,3,4,5,6]  
print(mylist[::-1])    
'''

# 4). Write a program to count even and odd numbers in a list.
'''
mylist = [1,2,3,4,5,6,7,8]  

even_counter = 0    
odd_couter = 0  

for i in mylist : 

    if i % 2 == 0 : 
        even_counter += 1   
    
    else:   
        odd_couter += 1 

print("Even:", even_counter)
print("odd:", odd_couter)
'''  

# 5). Write a program to merge two lists and sort the final list.
'''
list1 = [2,1,0] 
list2 = [5,4,6] 

merged = list1 + list2  
# print(merged.sort())  # ❌ output : None. due to original list they can changes directly not returns anything.
merged.sort()   
print(merged)    # [0, 1, 2, 4, 5, 6] here's the output is returns due to we cannot use the method with print line in the one line.

# ALterrnative sorted function use they can returns the directly new list.
print(sorted(merged))   # [0, 1, 2, 4, 5, 6]


# | sort()          | sorted()        |
# | --------------- | --------------- |
# | original modify | new list return |
# | method          | function        |

'''  


# 6). Write a program to find the second largest element in a list.
'''
mylist = [4, 8, 1, 9, 2] 

largest = mylist[0]           # Largest track krne ke liye initially list ka first item hi hoga ye baad mai compare mai update hoga.
second_largest = mylist[0]    # Second largest track krne ke liye initially list ka first item hi hoga ye baad mai compare mai update hoga.
 
for i in mylist:       # Har element compare hoga.

    if i > largest:     # Agar current element largest se bada hai to.
        second_largest = largest     # purana largest(second_largest) ban jyega.
        largest = i                    # vo value largest mai assign krdi hai

    # Case 2 : largest se chota hai BUT second_largest se bada hai
    elif i > second_largest and i != largest:   
        second_largest = i                         # case 2: ki codition satisfy krne ke baad isme assign kr dengai hm.

print("Second Largest:", second_largest)


# Alternative Easier way.   
mylist.sort()   
print(f"Second Largest number: {mylist[-2]}")
'''

# 7). Write a program to sort a list of tuples based on tuple values.   
'''
data  = [(3,1), (1,5), (2,4)]   
data.sort() 
print(data)
'''