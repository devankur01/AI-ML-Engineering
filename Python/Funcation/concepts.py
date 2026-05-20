# Function --> reusable block of code hota h, mtlb ek kaam ek jagah likho baar baar use kro by the invoke of the function code. 

# Basic Syntax:
'''
         def greet():   
              print("Hello")

    greet()    # function Call.    
'''

 # Understanding.   
'''
| Keyword | Meaning               |
| ------- | --------------------- |
| `def`   | function define karna |
| `greet` | function name         |
| `()`    | parameters area       |
| `:`     | block start           |
''' 

# Why Functions Important?  
# Without functions:
'''
print("Hello")
print("Hello")
print("Hello")

# Bad Practice.
''' 

# Better:   
'''
def greet():    
       print("Hello")   

greet()
greet()
greet()

# Reusable.
''' 

# Parameters --> Function ke inputs.    
'''
def greet(name):    
    print("Hello", name)    

greet("Alpha")     # here the Alpha is argument.

Output: 

Hello Alpha
''' 

'''
# Multiple Parameters.

def add(a, b):  
    print(a + b)    

add(10, 20)
''' 


'''
# Return Keyword --> Function value wapas bhj skte hai.
def add(a, b):  
    return a + b    

# Function Call
result = add(10, 20)    
print(result)      # Output ==> 30. 

# Print() sirf screen pe dikhata hai.
# return Value wapas deta hai.
''' 

'''
Why Return Important?
Kyuki:  
returned value ko:  
- Store.    
- reuse.    
- calculations. 
- chaining. 
kar skta hain.
'''

'''
# Default Parameters
def greet(name="Guest"):    
    print("Hello", name)    
 
greet()    # Output: Hello Guest.
''' 


# Keyword Arguments.  
'''
def student(name, age): 
     print(name, age)   

student(age=20, name="Alpha")     # Alpha 20
'''


# Variable Arguments
# *args --> Multiple values.  
'''
def total(*nums):   
    print(nums) 

total(1,2,3)    # OutPut: (1, 2, 3) Tuple milta hai.
'''

# **kwargs --> Dictionary arguments.    
'''
def user(**data):   
    print(data) 

user(name="Alpha", age=21)   # OutPut: {'name': 'Alpha', 'age': 21} Dicitonary milta hai.
'''    

# Scope
'''
# Local Variable --> Function ke andar define. 
def test(): 
    x = 10

# Bahaar use nhi hoga.

# Global Variable --> Function ke bahar define. 
x = 10
''' 

# Nested Functions. 
'''
def outer():    

    def inner():    
        print("Inner")  

    inner() 

outer()
''' 

# Lambda Functions --> short one-line functions.    
'''
square = lambda x: x*x  
print(square(5))      # output: 25.
'''   

# Recursion --> function khud ko call kare. 
'''
def countdown(n):   

    if n == 0:  
        return  
    
    print(n)    

    countdown(n-1)  

countdown(5)
'''     

# Built-in Functions --> python already deta hai.   
'''
len()   
sum()   
max()   
min()
type()
''' 

# function as Variable ----> pytyhon me function bhi object hai.    
'''
def greet():    
    print("hello")  

x = greet   
x()      # OutPut: hello
'''  


# List + Function Example   
'''
def square(num):   
    return num*num

nums = [1,2,3]  

for i in nums:  
    print(square(i))
'''