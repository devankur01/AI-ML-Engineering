'''
All About Pandas.

- Pandas is a Python library that works with data in table form.

What is a Python Library?

- Python itself is a basic programming language.

But things like:

- Excel work
- AI
- Machine Learning
- Web Development
- Game Development

are done using different libraries/tools.

Example:

| Work         | Library       |
| ------------ | ------------- |
| Maths        | NumPy         |
| Tables/Data  | Pandas        |
| Graphs       | Matplotlib    |
| AI/ML        | Scikit-learn  |

Why Was Pandas Made?

Using normal Python lists and dictionaries,
handling large data was difficult.

Example:

students = [
    ["Alpha", 20, 85],
    ["Beta", 21, 90]
]

Now tasks like:

- filtering
- finding averages
- reading CSV files
- sorting

became messy in normal Python.

Then Pandas came.

Pandas made table handling easy,
just like Excel.

How Is Real-World Data?

Mostly data comes from:

- Excel files
- CSV files
- Databases
- APIs

And almost all data is in:

- rows
- columns

Example:

| name  | age | salary |
| ----- | --- | ------ |
| Alpha | 20  | 50000  |
| Gamma | 21  | 60000  |

What Does Pandas Do?

Pandas can:

- load data
- clean data
- filter data
- analyze data
- save data

Flow:

CSV/Excel
   ↓
Pandas
   ↓
Cleaning
   ↓
Analysis
   ↓
Graphs / ML / Reports

Without Pandas:

- many loops
- many conditions
- nested lists
- manual calculations

had to be written.

With Pandas:

many tasks can be done in one line.

Example:

Average Salary:

df["salary"].mean()

Most Important Thing About Pandas:

Pandas works with tabular data,
which means:

- rows
- columns

Main 2 Structures In Pandas:

| Structure | Meaning        |
| --------- | -------------- |
| Series    | Single column  |
| DataFrame | Full table     |
'''

'''
1). What Is a Series?

Series = Single Column Data Structure.

Meaning:
- data in one line
- one single column
- every value has an index

Main Purpose of Series:

Series stores ordered data of the same type.

Examples:
- Marks
- Salary
- Names
- Temperature

2). Structure of a Series 

A Series has 2 main parts:  

| Part   | Meaning        |
| ------ | -------------- |
| Index  | label/position |
| Values | actual data    |

Example:   

import pandas as pd  
s = pd.Series([90, 85, 95])   
print(s)

Output:

0 1 2 left side are indexes(are the identifiers of the values here the Default index) and the right side are their values 90 85 95 and then last one was the int64 is Data type(dtype).

0    90
1    85
2    95
dtype: int64


# Custom Index 
import pandas as pd  
s = pd.Series(
    [90, 85, 95], 
    index=["ALpha", "Beeta", "Gamma"]
)  
print(s) 

OutPut:     

here the indexes are the now decides by the our-selves like here we use the names of random.

ALpha    90
Beeta    85
Gamma    95
dtype: int64   
'''   

'''
import pandas as pd  
s = pd.Series(
    [90, 85, 95], 
    index=["ALpha", "Beeta", "Gamma"]
)  
# print(s)    

# Access Karna 
# By index Label. 
print(s["ALpha"])    # 90. 

# By Position they can only applicable when the indexes is same as we can access that or default indexes. 
print(s[0])            # 90.  

# In Series Labels and position boths we can access their values.  
# But Internally series is the optimized array structure.   
'''

# 3. Series Data Type   
'''
import pandas as pd  

# Integer Series. 
s = pd.Series([1,2,3,4]) 
print(s)                  # dtype: int64. 

# String Series.
s1 = pd.Series(["A", "B", "C", "D"])   
print(s1)                 # dtype: str. 

# Float Series.
s2 = pd.Series([1.2, 4.5]) 
print(s2)                # dtype: float64.   

# Boolean Series.
s3 = pd.Series([True, False]) 
print(s3)                # dtype: bool.   
'''

# Series Operations (Vectorized Operations). 
'''
import pandas as pd  
s = pd.Series([1,2,3,4])   
print(s*2)   # Every values gets Multiply by the 2 Automatically without this we can multiply by the 2 by the loop operation but in pandas is automatically.   

print(s + 10) 

Ouput :  

0    2
1    4
2    6
3    8
dtype: int64
0    11
1    12
2    13
3    14
dtype: int64
'''

# Filtering.  
'''
import pandas as pd  

s = pd.Series([10,20,30,40,50])  

print(s[s > 20])

Output:  
2    30
3    40
4    50
dtype: int64
'''   


'''
import pandas as pd  
s = pd.Series(
    [90, 85, 95], 
    index=["ALpha", "Beeta", "Gamma"]
) 

# Series Properties. 

# s.index
print(s.index)   # Index(['ALpha', 'Beeta', 'Gamma'], dtype='str')

# s.values  
print(s.values)    # [90 85 95]  

# s.dtype   
print(s.dtype)     # int64 

# s.shape   
print(s.shape)     # (3,)  

# some function of series. 

# Sum 
print(s.sum())       # 270 

# Mean   
print(s.mean())     # 90.0 

# Max 
print(s.max())      # 95   

# Min 
print(s.min())      # 85   

# Count  
print(s.count())     # 3   

# Unique 
print(s.unique())   # [90 85 95] unique values. 

# Value Counts 
print(s.value_counts())


Output of value count: 
90    1
85    1
95    1
Name: count, dtype: int64   
'''

# Missing Values 
'''
import pandas as pd  

s = pd.Series([10, None, 30]) 

print(s)

Output :
0    10.0
1     NaN
2    30.0
dtype: float64  

# Check missing Values. 

print(s.isnull())

OutPut :     
0    False
1     True
2    False
dtype: bool  

# Fill Missing Values   

print(s.fillna(20))  

Output :  
0    10.0
1    20.0
2    30.0
dtype: float64  

# Remove Missing Values 
print(s.dropna()) 

 OutPut : 
0    10.0
2    30.0
dtype: float64
''' 