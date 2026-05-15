# List = ordered collection of multiple values and list is ordered, Mutable, Dynamic, Mixed data types allowed.

# Mutable --> List change ho skti hai after creation.  
'''
numbers = [1,2,3,4,5]
numbers[0] = 555    
print(numbers)  # [555, 2, 3, 4, 5].
''' 

# String are immutable and list are mutable.

# Mixed Data Types --> Allowed in List.
'''
data = [1, "alpha", True, 99.5] 
print(data)
'''

# Indexing.
'''
nums = [10,20,30,40,50]   
print(nums[0], nums[1], nums[2], nums[3], nums[4]) # Same exactly String.
print(nums[-1], nums[-2]) # 50 40
'''

# Slicing
'''
nums = [1,2,3,4,5]  
print(nums[1:4])    

# Reverse List
print(nums[::-1])  # [5, 4, 3, 2, 1]
'''

# List Methods
# 1. append() --> ENd mai add krta hai new elements ko.
'''
nums = [1,2]    
nums.append(3)  
print(nums)   # [1, 2, 3]

# 2. insert() --> They can add the value according to their first parameter pass whose is index and second parameter is value so index = 1, value = 199.
nums.insert(1, 199) 
print(nums)    #[1, 199, 2, 3]
'''

# extend()  
'''
a = [1,2]   
b = [3,4]   
a.extend(b) 
print(a)   # [1, 2, 3, 4]


# Difference Between append vs extend
# append
a.append(b) 
print(a)   # [1, 2, [3, 4]] --> Nested List ban jyegai.

# extend
a.extend(b) 
print(a)  #[1, 2, 3, 4]   --> Elements individually add hue.
'''

# 4. remove() --> value gets removes by the pass of the value in the given list.
'''
nums = [1,2,3,4]    
nums.remove(2)
print(nums)   # [1, 3, 4]

# 5. pop() --> Index remove.
nums.pop()  
print(nums) # remove item by the last when we without pass any parameter in the pop() method Output : [1, 3].
nums.pop(0) 
print(nums) # before [1, 3] after Ouput : [3].

# 6. clear() --> Sab remove.
nums.clear()
print(nums)  # []
'''

# Searching
# index()
'''
nums = [10,20,30]   
print(nums.index(20))   # 1
'''

# count()
'''
nums = [1,1,1,2]    
print(nums.count(1))  # 3   
'''

# Sorting
# sort() 
'''
nums = [4,1,3]  
nums.sort() 
print(nums)  # [1, 3, 4]
  

# Reverse Sorting
nums.sort(reverse=True)  # [1, 3, 4]

# Difference Between sort() and sorted()
# sort() --> Original list change krta hai.
# sorted() --> New Sorted list return krta hai.
new_list = sorted(nums) 
print(new_list) # [1, 3, 4].
'''

# Looping Through Lists
# normal loop
'''
nums = [1,2,3]  

for i in nums:  
    print(i)

# Using range() 
for i in range(len(nums)):  
    print(nums[i])

# enumerate()
for index, value in enumerate(nums):        # 0 1
       print(index, value)                  # 1 2
                                            # 2 3
'''

# Membership Operator
'''
nums = [1,2,3]  
print(2 in nums)    # True
'''

# List Concatenation
'''
a = [1,2]   
b = [3,4]   
print(a + b)   # [1, 2, 3, 4].
'''

# Nested Lists
'''
matrix = [
    [1,2],
    [3,4]
]

print(matrix[0])     # [1, 2]
print(matrix[1])     # [3, 4]
print(matrix[0][1])  # 2
'''

# Explain of 2 output 
'''
[
   0 -> [1,2],
   1 -> [3,4]
]

Ab first ke andar:
[1,2]
indexes:
0 -> 1
1 -> 2
To:
matrix[0][1]
Meaning:

first row lo → [1,2]
uska second element lo → 2
'''


# List Comprehension
# Normal Way
'''
squares = []

for i in range(5):  
    squares.append(i*i)

print(squares)  # [0, 1, 4, 9, 16]
'''

# Pythonic Way
'''
squares = [i*i for i in range(5)]
print(squares) #[0, 1, 4, 9, 16]
'''

# With Condition
'''
even = [i for i in range(10) if i % 2 == 0] 
print(even)  # [0, 2, 4, 6, 8]
'''

# Copying Lists
'''
a = [1,2]   
b = a.copy()
print(b)    # [1, 2]

b = a[:]
print(b)  # [1, 2]
'''