# 1. Create a Function to Check Whether Two Strings are Anagrams Problem 
#  Write a function that accepts two strings and returns True if both are anagrams, otherwise False.
'''  Concept
Agr dono strings ke letter same hain or same number of times hain too : Sorted string equal hongi.  

Example:    
listen  

Sort:   
['e', 'i', 'l', 'n', 's', 't']  

silent  

Sort: by the help of sorted() Function string ko: sorted character list me convert krta hai.   
['e', 'i', 'l', 'n', 's', 't']  

same
'''

'''
def is_anagram(str1, str2): 

    str1 = str1.lower() 
    str2 = str2.lower() 

    if sorted(str1) == sorted(str2):    
        return True 

    else:   
        return False    
    
print(is_anagram("listen", "silent"))
''' 

# Alternative  
'''
def is_Anagram(str1, str2):

    return sorted(str1.lower()) == sorted(str2.lower()) 

result = is_Anagram("listen", "silent")     
print(result)
''' 

# 2. Create a Function to Find Second Largest Number in a List Problem 
# Write a function that accepts a list and returns the second largest number.

'''
def Second_largest_Number(nums):    
    largest = max(nums)      # phle sabse largest number liya.
    nums.remove(largest)     # fir uss largest number ko remove kr diya uss list mai se or jo fir ab jo largest number tha usse nums mai store kr liya. 
    return max(nums)         # fir usse hi return kr diya.

numbers = [10, 20, 5, 40, 30]   

print(Second_largest_Number(numbers))
''' 


# 3. Create a Function to Count Vowels in a Sentence Problem 
# Write a function that accepts a sentence and returns the count of each vowel.
'''
def count_vowels(str):  
    str = str.lower()    # safe check of vowels

    vowels = {           # vowels dictionary 
        "a":0,  
        "e":0,  
        "i":0,
        "o":0,
        "u":0
    }   

    for char in str:        # loop through whole string
        if char in vowels:  # check vowel in the char of each in the contains string.
            vowels[char] += 1   # if the vowels matches their string character then increses in the vowels dictionary.

    return vowels        # then finally the vowel dictionary returns.

print(count_vowels("hello world"))     # {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0}.
'''
 
# 4. Create a Function to Check Whether a Number is an Armstrong Number Problem 
# Write a function that returns True if a number is an Armstrong number.
'''
Armstrong Number if the final number like 153 then their each digits in the number in the whole number we find the each digit cube then their add summ is output is equal to the whole digit is Amstrong number like 153 = 1^3 + 5^3 + 3^3 = 153 then its Amstrong number.

def is_armstrong(num):

    original = num        # original number save due to compare later.

    digits = len(str(num))    # digits count in num convert in the string.

    total = 0

    while num > 0:          # loop on number while the number is greater then the 0.

        digit = num % 10    # ye hme last digit nikal kr deta hai example: 153 mod 10 = 3 then digit = 3.

        total += digit ** digits    # now the 3 = digit is cubed now 3^3 = 27 now total = 27.

        num = num // 10            # //10 ye last digit remove krta hai 153 // 10 --> 15 now num = 15 again loop chalega fir 15 mai se digit = num % 10 ye code chalega fir vo ek value nikl kr uspr cube krega fir usse total maai add krega fir again and again num > 0 tk ye chalega code. 

    return total == original


print(is_armstrong(153))    # True
'''

'''
# Alternative
def is_armstrong(num):

    digits = len(str(num))

    total = sum(int(i) ** digits for i in str(num))

    return total == num


print(is_armstrong(153))    # True
'''

'''
| Operation | Meaning            |
| --------- | ------------------ |
| `% 10`    | total number mai se sirf last digit nikaalo |
| `// 10`   | total number mai se sirf last digit hatao   |
'''

# 5. Create a Function to Find Common Elements Between Multiple Lists Problem 
# Write a function that accepts three lists and returns common elements.
'''
def common_element(list1, list2, list3):    

    return set(list1) & set(list2) & set(list3)     # we can simply converts these listses into the set then find common element use to & intertion in the list.

print(                   # Output : {2, 3}

    common_element(
        [1,2,3,4],
        [2,3,5],
        [2,3,7]
    )
)
''' 