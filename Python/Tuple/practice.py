# Tuple = ordered collection of items, they are immutable but in list are mutable.

# List vs Tuple
# | Feature  | List          | Tuple      |
# | -------- | ------------- | ---------- |
# | Syntax   | `[]`          | `()`       |
# | Mutable  | ✅            | ❌        |
# | Faster   | ❌            | ✅        |
# | Hashable | ❌            | ✅ mostly |
# | Use Case | changing data | fixed data |

# Tuple syntax = nums = (1,2,3)
# Tuples ke elements:  1) ordered hote hain , 2) indexing support krta h, 3) slicing support krta hai , Bas modify nhi krta hai original tuple.

#  Indexing
'''
data = (10, 20, 30)   
data[0] = 100   # Type error due to immutable of tuple.
print(data[0])  # 10.

# Negative Indexing     
print(data[-1]) # 30.
'''


#  Slicing.
'''
data = (1,2,3,4,5)  
print(data[1:4])   # (2, 3, 4) , last parameter index not included.
print(data[::-1])   # (5, 4, 3, 2, 1), reverse tuple.
'''

# Tuple in between list(mutable) allowed.
'''
data = ([1,2,3],4,5)    
data[0].append(100)   # we can add simple append method in the list b/w set.
print(data) # whole set can print here.
print(data[0]) # here the set in b/w list whole list can assigns the list with the index 0 OUPUT : [1, 2, 3, 100].
'''

# Single Element Tuple.
'''
data = (5)  # ye tuple nhi h ye int hai wrong way to store the element in the tuple.
print(type(data))   # <class 'int'>

data1 = (5,)    # Correct way to store one element in the tuple with the comma.
print(type(data1))  # <class 'tuple'>
'''

# Tuple Packing & Unpacking
'''
# Packing
data = 1,2,3 # Automatically tuple ban gaya with the packing of the data.

# unpacking --> also called as destructuring in the JS.  
a,b,c = (1,2,3)     
print(a)    
print(b)    
print(c)    
'''

# Swapping variables.
'''
a = 10  
b = 20  
a,b = b,a
print(a)    # 20. 
print(b)    # 10.
'''

# Tuple Methods due to tuple immutable methods limited in the tuple.
# 1. count()
'''
nums = (1,1,1,1,2)  
print(nums.count(1))  # 4
'''

# 2. index()  
'''
nums = (10,20,30)   
print(nums.index(20))  # 1
'''  

# Looping Through Tuple
'''
nums = (1,2,3)  
for i in nums:  
    print(i)    
'''

# Membership Operator.
'''
nums = (1,2,3)  
print(2 in nums)   # True.
'''

# Convert List ↔ Tuple
# List to Tuple.
'''
nums = [1,2,3]  
t = tuple(nums) 
print(t)        # (1, 2, 3).
'''

# Tuple to List
'''
t = (1,2,3,4)   
list = list(t)  
print(list)    # [1, 2, 3, 4]
'''

'''
Tuple:

thoda faster
less memory

than lists.
'''

# Nested Tuples.
'''
data = (
    (1,2),
    (3,4)
)   
print(data[0][1])  # Output : 2  # Same nested list logic.
'''

# Returning Multiple Values
# Python function internally tuple return krte hai.
'''
def user(): 
    return "ALpha", 21  

data = user()   
print(data)     # ('ALpha', 21)
'''

# Tuples as Dictionary Keys
# Kyuki tuples immutable hote hain, to unhe dictionary keys bana skte hai.
'''
data = {
    (1,2): "Point A"
}   

print(data[(1,2)])     # Point A, List ye nahi kar sakti.
'''