# 1). Write a program to create a dictionary from two lists: one of keys and one of values.
'''
keys = ["name", "age", "city"]  
values = ["Alpha", 22, "Noida"] 

data = {}   

for i in range(len(keys)):  
    data[keys[i]] = values[i]   

print(data) 
'''

# 2). Merge two dictionaries into one.
'''
user1 = {
    "Name": "Alpha",
    "Age": 22
}

user2 = {
    "Name": "Beeta",
    "Age": 21
}   

merged = {
   "user1": user1,  
   "user2": user2
}   

print(merged)  # {'user1': {'Name': 'Alpha', 'Age': 22}, 'user2': {'Name': 'Beeta', 'Age': 21}}
'''

# With spread operator two dic combine in one.  
'''
user1 = {
    "Name1": "Alpha",
    "Age": 22
}   

user2 = {
    "Name2": "Beeta",   
    "Age": 21
}   

merged = {
    **user1,    
    **user2
}   

print(merged)     # {'Name1': 'Alpha', 'Age': 21, 'Name2': 'Beeta'}
'''

# 3). Write a program to sort a dictionary by its values.
'''
data = {
    "a": 3, 
    "b": 1,
    "c": 2
}   

values = list(data.values())    
values.sort() 

for value in values:      # sorted values
    for key in data:      # matching key find

       if data[key] == value:  
        print(key, value)
'''
