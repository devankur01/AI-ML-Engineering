# Write a program to check whether an element exists in a tuple.
'''
data = (10, 20, 30, 40) 
print(f"Element exists: {20 in data}")

# Dynamic User Input
data = (223,845,5697,7834)  
num = int(input("Enter number: "))  

if num in data: 
    print("Element exists") 

else:   
    print("Element does not exist")
'''

# Write a program to count the occurrence of an element in a tuple.
'''
data = (1, 2, 3, 2, 4, 2, 5)    
num = int(input("Enter element: ")) 

count = 0   

for i in data:  

    if i == num:    
        count += 1

print("Occurrance:", count)
'''

# Write a program to convert a tuple into a list and a list into a tuple.
'''
# Tuple to List

data = (1, 2, 3)
new_list = list(data)
print("Tuple converted to List:")
print(new_list)

# List to Tuple

nums = [4, 5, 6]
new_tuple = tuple(nums)
print("List converted to Tuple:")
print(new_tuple)
'''   