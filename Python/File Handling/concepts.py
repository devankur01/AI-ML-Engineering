# File Handling means files read/write/managed like .txt, .csv, .json, .py, etc.    
# Opening a File --> file = open("data.txt") and we also assign some mode in the open() function with the separate by , and these mode decides the what can do by the file like 'r' read only 'w' write only mention below to all mode.
# Modes and thier purpose.      
'''
| Mode   | Main Purpose  |
| ------ | ------------- |
| `"r"`  | read          |
| `"w"`  | overwrite     |
| `"a"`  | append        |
| `"x"`  | create        |
| `"r+"` | read + write  |
| `"w+"` | write + read  |
| `"a+"` | append + read |
''' 


'''  1. read()
f = open("data.txt", 'r')   
print(f)        # <_io.TextIOWrapper name='data.txt' mode='r' encoding='cp1252'> print(f) mean file object print not their content.
print(f.read())   # file inner content view write in the file access by the help of read() the code this and the output --> Hello Alpha. Python file handling. Some operation we can performs here.   
f.close()  # after the work done by the file close.
''' 

'''
Why close() Important?  
- Memory release hoti h.    
- File lock remove hota h.  
- Safe practice h.
''' 

# Best Modern Way → with because of automatic close no need here to write code manully close file like f.close().
'''
with open("data.txt") as file:  
    print(file.read())         # output --> Hello Alpha. Python file handling. Some operation we can performs here.     
    print(f.readline())        # read only single line
    print(f.readlines())       # read whole the data into the file exists.
'''    

# 2). "w" --> Write Mode purpose Write only here one catch puri file ka old content delete kr deta hai fir jo hm dete hai vo deta hai hmne vo.  
'''
f = open("data.txt", 'w')       
f.write("new Data by the write function")   
f.close()
'''     

# New Method.
'''
with open("data.txt", 'w') as file: 
    file.write("new Data by the write function by the help of new modern syntax")
'''     

# 3. "a" --> Append Mode purpose new content end mai add krne ke liye or append mai sirf read nhi hota hai iske liye hme a+ krna padega jisme read with append hota h or file.seek(0) isliye kyuki cursor problem solve krta hai cursor ko start mai lane ke liye.  
'''
with open("data.txt", 'a+') as file: 
    file.write("New content added by the help of append function")  

    file.seek(0)    

    print(file.read())
'''   

'''
| Mode   | Read | Write |
| ------ | ---- | ----- |
| `'a'`  | ❌    | ✅     |
| `'a+'` | ✅    | ✅     |
'''

# 4. "x" → CREATE MODE purpose: new file create already exist file error.   
'''
with open("new.txt", 'x') as file:  
    file.write("New content added by the help of new create file mode of use 'x'")  
'''   

# 5. "r+" → READ + WRITE can read and write but file already exist honi chiye. 
'''
with open("data.txt", 'r+') as file:    
    print(file.read())  
    file.write("\nAdded")
'''     

# 6. "w+" → WRITE + READ can write and read old content delete kr deta hai. 
'''
with open("data.txt", "w+") as file:

    file.write("Hello")

    file.seek(0)

    print(file.read())
''' 

# WHY seek(0)? kyuki write ke baad cursor end pe chala gya tha so we read content from starting that's why the cursor we would replace from end to start.   

# Reset Cursor  
# file.seek(0)

# Current Position  --> cursor kis point pr hai.
# file.tell()   

# Example  
'''
with open("data.txt") as file:

    print(file.tell())

    print(file.read(5))

    print(file.tell())
''' 

# File Exists Check
'''
import os   
print(os.path.exists("data.txt"))  # True
'''

# Delete File   
'''
import os

os.remove("data.txt")
''' 

# Rename File   
'''
os.rename("new.txt", "old.txt")
''' 

# Exception Handling    
'''
try:

    with open("data.txt") as file:

        print(file.read())

except FileNotFoundError:

    print("File not found")
'''