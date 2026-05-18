# Dictionary is a key-value pair stores the data, mutable, unordered(old python) but in modern python dictionary are ordered, fast lookup.
# Dictionary exactly: JSON object jaisi hoti hai.

# Example : 

# | Key  | Value |
# | ---- | ----- |
# | name | Ankur |
# | age  | 20    |

# Example:
'''
user  = {
    "name": "Alpha",    
    "age": 22
}   
print(user)     # {'name': 'Alpha', 'age': 22}.
'''

'''
student = {
    "name": "ALpha",    
    "age": 23
}       

# Access with the help of key not indexing in list. 
print(student["name"])   # ALpha, hm yha key ka naam de rahe hai to uski value le paa rahe hai.
print(student["age"])    # 23


# Add New Key
student["city"] = "Noida"   
print(student)           # {'name': 'ALpha', 'age': 23, 'city': 'Noida'}.


# Update Value  
student["age"] = 21 
print(student["age"])     # 21

# Remove Values 
# pop()
# student.pop("age")  
# print(student)           # {'name': 'ALpha', 'city': 'Noida'}   

# del   
del student["age"]  
print(student)             # {'name': 'ALpha', 'city': 'Noida'}
'''

# Loop Through Dictionary.
'''
user  = {
    "name": "Alpha",    
    "age": 22
}   

# 1. Loop through keys.
for key in user: 
    print(key)                # name, age

# 2. Loop through values.
for values in user.values():    
    print(values)             # Alpha, 22

# 3. Loop through Both(key, value). 
for key, value in user.items(): 
    print(key, value)           # name Alpha, age 22
'''  

# Dictionary Methods.

# keys() 
'''
user = {
    "name": "ALpha",    
    "age": 23,  
    "phone": ""
}   

# keys()
print(user.keys())      # dict_keys(['name', 'age'])

# values()
print(user.values())    # dict_values(['ALpha', 23])

# items()
print(user.items())     # dict_items([('name', 'ALpha'), ('age', 23)])

# get()
print(user.get("age"))  # 23    

# Check Key Exists
if "name" in user:  
    print("Exists")
''' 

# Nested Dictionaries.
'''
user = {
    "name": "ALpha",
    "address": {
        "city": "Gr. Noida",    
        "pincode": 201334590
    }
}   

# Access Dictionary length.
print(user["address"]['pincode'])    # 201334590.

# Dictionary Length
print(len(user))            # 2.

# Copy Dictionary
new_user = user.copy()  
print(new_user)

# Clear Dictionary  
new_user.clear()    
print(new_user)      # {}
'''

# Dictionary Comprehension. 

# Normal.
'''
squares = {}    

for i in range(5):        # range(5) mean --> 0 1 2 3 4.     
     squares[i] = i*i   

print(squares)            # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
'''

# Pythonic. 
'''
squares = {i: i*i for i in range(5)}    
print(squares)             # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
'''

# Dictionary keys: are must be immutable like string, int, tuple not list.

