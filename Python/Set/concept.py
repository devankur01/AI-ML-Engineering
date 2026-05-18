# set : unique values stores only not duplicates values.    
# syntax Example : nums = {1,1,2,2,3,3,4,5}   
# output: {1,2,3,4,5}   Duplicates automatically remove.
# Important properties set unordered, mutable, unique values only, fast lookup.
# Unordered mean indexing nhi hoti hai Ye wrong hai nums[0] Error kyuki set ordered collection nhi hai index-based nhi h.
# Empty Set --> data = {} ye empty dictionaary banata hai correct ye hai data = set().

# Add Elements. 
'''
nums = {1,2}    
nums.add(3)     
print(nums)   # {1, 2, 3}.

# Remove Elements.
# remove()  
nums.remove(2)   # here the remove method we can pass an value we want to delete and if the value we want to delete in by the pass in remove function not exists in the set then error occur.
print(nums)      # {1, 3}


# discard().    
nums.discard(5)  # here we can pass the value not exists in the set item then they cannot gets error but in the case of remove they can gets error. 
print(nums) 
''' 

'''
# Loop Through Set.
nums = {1,2,3}  

for i in nums:  
    print(i)

# Membership checking.  
# Set are fast lookup because of sets are internally using hashing then the "in" operations very fast.
if 2 in nums:   
    print("Exists")    # set mai lookup bhut fast hota hai.
'''

# Remove Duplicates Using Set
'''
nums = [1,2,2,2,3,4,4]  
unique = set(nums)       # we can convert the list into the set they can automatically remove duplicates.
print(unique)
'''

# Set Operations 
'''
# 1). Union --> combine both sets.  
a = {1,2,3} 
b = {3,4,5} 
print(a | b)      # {1, 2, 3, 4, 5}.    

# 2). Intersection --> common elements. 
print(a & b)      # {3}.

# 3). Difference .    
print(a - b)     # {1, 2}   
print(b - a)     # 4, 5}

# 4). Symmetric Difference --> Non-common elements.  
print(a ^ b)    # {1, 2, 4, 5}. 
'''   

# 5). Subset.   
'''
a = {1,2}   
b = {1,2,3} 
print(a.issubset(b))    # True.

# 5). Superset  
print(b.issuperset(a))  # True. 
'''   

# Frozen Set normal set are "mutable" but the Forzen set are "immutable".
'''
nums = {1,2,3,4}    
nums.frozenset([1,2,3]) 
nums.add(87)    
print(nums)   # error.
'''

'''
List vs Set
| List               | Set         |
| ------------------ | ----------- |
| duplicates allowed | unique only |
| ordered            | unordered   |
| indexing           | no indexing |
| slower lookup      | fast lookup |
'''
