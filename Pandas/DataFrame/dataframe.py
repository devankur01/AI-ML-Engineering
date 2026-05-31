'''
All About DataFrame :   

DataFrame means rows and columns contains in the table is called dataframe or multiple Series togther.  

Real Example:   

| name  | age | marks |
| ----- | --- | ----- |
| Ankur | 20  | 90    |
| Rahul | 21  | 85    |

is Dataframe.   

we can also says that each column in the table is as Series or boths we can combines is DataFrame like in above table has three columns one is name and second one is age and last marks these separately called as the Series and these different Series uses same indexing like 0, 1, 2, 3, 4.

Why we use DataFrame?   

Real-world data:    
- Excel.    
- CSV.  
- databases.    
- APIs. 

mostly in table form and pandas has easy operates with table that's why dataframe is used.  

DataFrame Ka Structure? 

Dataframe has 3 parts:  
| Part    | Meaning         |
| ------- | --------------- |
| Rows    | horizontal data |
| Columns | vertical data   |
| Index   | row numbering   |

How to make dataframe?  

Mostly:     

- dictionary.   

data = {
  "name" : ["Alpha", "Beetaa"], 
  "age" : [20, 21]
}   

Here's the keys makes columns and lists has their columns values then   

pd.DataFrame(data)  

dictionary to table converts.   

''' 

'''
import pandas as pd 

data = {
    "name": ["Alpha", "Beeta"], 
    "age": [20, 23]
}   

df = pd.DataFrame(data) 

print(df)   

    name  age
0  Alpha   20
1  Beeta   23   

''' 

'''
# DataFrame properties. 

import pandas as pd 

data = {
    "name": ["Alpha", "Beeta"], 
    "age": [20, 23]
}   

df = pd.DataFrame(data)     

# Shape 
print(df.shape)    # Output : (rows, columns), Our code Output: (2, 2) means 2 rows and 2 columns. 

# Columns   
print(df.columns)  # Output : Index(['name', 'age'], dtype='str').  
    
# Data Types    
print(df.dtypes)   # Output : dtype: object.    

# Info  
print(df.info())   # Complete summary.  

Output of print(df.info()) :
<class 'pandas.DataFrame'>
RangeIndex: 2 entries, 0 to 1
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   name    2 non-null      str  
 1   age     2 non-null      int64
dtypes: int64(1), str(1)
memory usage: 164.0 bytes
None  

# Head  
print(df.head())    # Top 5 rows.

Ouput:    
    name  age
0  Alpha   20
1  Beeta   23 

# Tail      
print(df.tail())    # Last rows.    

Output :    
    name  age
0  Alpha   20
1  Beeta   23 

# Data Access   

# Single Column 
print(df["name"])   

Output :    
0    Alpha
1    Beeta
Name: name, dtype: str    

# Multiple Columns  
# print(df["name", "age"])  # ❌ error    
print(df[["name", "age"]])  # Dataframe 

output:
    name  age
0  Alpha   20
1  Beeta   23 

# Row Access    
# loc[] --> Label/index based.  
print(df.loc[0])    

Output :   
name    Alpha
age        20
Name: 0, dtype: object    

# iloc[] --> position based.    
print(df.iloc[0])   

Ouput :   
name    Alpha
age        20
Name: 0, dtype: object    

Difference
| Method | Works On  |
| ------ | --------- |
| loc    | labels    |
| iloc   | positions |
''' 

'''
# Filtering 
import pandas as pd 

data = {
    "name": ["Alpha", "Beeta"], 
    "age": [20, 23]
}   

df = pd.DataFrame(data) 

# Filter rows where age is greater than 20
filtered_df = df[df["age"] > 20]
print(filtered_df)

# New Column makes  
df["double_age"] = df["age"] * 2
print(df)

#     name  age  double_age
# 0  Alpha   20          40
# 1  Beeta   23          46 

# Sorting       
df.sort_values("age")
print(df)

''' 

'''
# GroupBy   

import pandas as pd 

data = {
    "name": ["Alpha", "Beeta", "Charlie", "Delta"], 
    "city": ["Delhi", "Mumbai", "Delhi", "Mumbai"],
    "salary": [5000000, 60000, 55000, 65000]
}   
df = pd.DataFrame(data) 
print(df.groupby("city")["salary"].mean())  # Group by city and calculate average salary.   \

# Output: 
# city
# Delhi     2527500.0
# Mumbai      62500.0
# Name: salary, dtype: float64

print(df.groupby("city")["salary"].agg(
    ["mean", "max", "min", "count"]
))  

# Output: 
#             mean      max    min  count
# city                                    
# Delhi   2527500.0  5000000  55000      2
# Mumbai    62500.0    65000  60000      2  
'''

# Merge 
'''
import pandas as pd 

employees = pd.DataFrame({
    "id": [1, 2, 3],    
    "name": ["Alpha", "Beeta", "Gamma"]
})  

salary = pd.DataFrame({
    "id": [1, 2, 3],    
    "salary": [50000, 60000, 70000]
})  

result = pd.merge(
    employees,  
    salary, 
    on="id"
)   

print(result)   

# Output : 
#    id   name  salary
# 0   1  Alpha   50000
# 1   2  Beeta   60000
# 2   3  Gamma   70000
''' 


'''
| Kaam             | Syntax                |
| ---------------- | --------------------- |
| Single Column    | `df["name"]`          |
| Multiple Columns | `df[["name", "age"]]` |
| Print            | `print()`             |

Example: of printing more then one column.    

print(
    df[
        ["name", "age"]
    ]
)
'''