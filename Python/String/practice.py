# String = text data

# name = 'APlha'    # string

# In python String are immutable means once created --> directly cannot changed.
# Example:
# name[0] = "a"   
# print(name)       # error due to we can changed in the original string.

# Double Quotes
# name = "APlha"

# Triple Quotes --> Multi-line strings.
'''
bio = """
Hello
I am learning python
"""

print(bio)
'''

# String Indexing
'''
name = "alpha"

# Positive Index
print(name[0]) # a
print(name[1]) # l

# Negative Index --> here the indexing is starting from -1 to till the words from right to left.
print(name[-1])  # a
print(name[-2])  # h
'''

# String Slicing
'''
name = "Alpha"

# Syntax --> name[start:end] here the end cannot be included.
print(name[0:3])  # Alp
print(name[-2:2])  # empty due to left to right cannot processed.
print(name[2:-2]) # p --> due to moves right to left.
print(name[0:5:2]) # Apa due to here the first index start = 0, end = 5 and step = 2.
'''

# Reverse String
'''
name = "Alpha"  
print(name[::-1])   
print(len(name))    # to finds the length of the string.
'''

# Loops
'''
name = "Alpha"  
for char in name:   
    print(char)
'''

# Important String Methods
'''
# 1. lower()
name = "ALPHA"  
print(name.lower())

# 2. upper()
print(name.upper())

# 3. strip()  --> removing all unnecessary spaces in the strings presents.
text = "  Hello  "  
print(text.strip())

# 4. replace()  
text = "I love JS"  
print(text.replace("JS", "Python"))

# 5. split()    
text = "Apple Mango Banana" 
print(text.split(' '))

# 6. join() ----> Reverse of split.
words = ['I', 'Love', 'AI']  
print(" ".join(words))
'''

# String Formatting
# ❌ Old Way
'''
name = "alpha"  
age = 21    
print("My name is:", name)
print("My age is:", age)
'''

# ✅ Modern Python Way → f-string   
'''
name = "Alpha"  
print(f"My name is {name}")
'''

# Escape Characters
# print("Hello\nworld")

# Membership Operator
'''
text = "I love AI"  
print("AI" in text)
'''

# String Concatenation
'''
first = "Alpha"
last = "Beetaa"

print(first + " " + last)
'''
