# All About Descriptive Statistics  

``` 
Descriptive Statistics
│
├── Measure of Central Tendency
│      ├── Mean
│      ├── Median
│      └── Mode
│
├── Measure of Variability
│      ├── Range
│      ├── Variance
│      ├── Standard Deviation
│      └── IQR
│
└── Graphical Representation
       ├── Histogram
       ├── Box Plot
       └── Pie Chart    
``` 

**What is Descriptive Statistics**  
- Descriptive Statistics is used to summarize, organize, and describe the existing data.    
- It helps us understand the data without making predictions.   
- they cannot predicts the future.  

they only tells us :    
- what kind of data?    
- How the data is spread?   
- What is the average?  
- Outliers present or not?  

**Example** 

Suppose Microsoft has the data of Employees 1,00,000 Employees. 

``` 
| Age | Salary | Experience |
| --- | ------ | ---------- |
| 22  | 30000  | 1          |
| 25  | 40000  | 3          |
| 31  | 70000  | 8          |
``` 

Company cannot predicts here.   

they only sees  
- Average Salary?   
- Highest Salary?   
- Lowest Salary?    
- Outliers? 

These finds by the Descriptive Statistics.  

## Measure of Central Tendency  

**Why is it call Central Tendency?**    

"Tendency"  

Means   

**Which kind of value the data is collected around most-likly** 

Suppose salaries    

``` 
30000
32000
31000
30500
29000
100000  
``` 
Question    

these employess generally how the salary they earns?    

each value of salary of each employee is finds to difficult?    

that's why we can finds the central value?  

and we call that **Central Tendency**   

**AIM** 

we can summarize the whole data with one value of the dataset.  

Instead of  
``` 
50000 numbers   
``` 

Company says    

Average Salary  
``` 
₹52,400 
``` 

So, the central tendency purpose is that only.  

**Why AI/ML Uses Central Tendency?**    

suppose dataset 

``` 
Age

22
23
24
25
26
NaN
27  
``` 

the missing value.  

ML model cannot accepts the missing value.  

**that's why company fill the missing value of whole dataset by the use of Mean and Median and that method is ***Data Imputation.***    

**AI/ML Uses**  

Central Tendency use of AI/ML   

✔ Missing Values  

✔ Data Cleaning   

✔ Features Engineering    

✔ Business Reporting  

✔ Dashborad   

✔ Summary Statistcs    

✔ Data Understanding   

### Components of Measure of Central tendency  

1. Mean(Arithmetic Mean)    

**What is Mean?**   

Mean means average of all values.   

this is the balancing point(center point).  

Formula 

Suppose dataset contains n values.  

```
x₁, x₂, x₃, x₄, .......... xₙ   
``` 

Then, the Mean formula is : 

$$
\bar{x}=\frac{\sum x}{n}
$$  

**Symbols Meaning** 

| Symbol      | Meaning                      |
| ----------- | ---------------------------- |
| ( \bar{x} ) | Mean                         |
| ( \sum x )  | Sum of all values            |
| ( n )       | Total number of observations |

**Example** 

Salary  

``` 
30000
35000
40000
45000
50000   
``` 

Step 1  

Sum     

```
30000 + 35000 + 40000 + 45000 + 50000

= 200000    
``` 

Step 2  

Number of values    

``` 
5   
``` 

Step 3  

Mean    

200000/5 = 40000    

Mean    

``` 
₹40,000 
``` 

**Mathematical Meaning**    

Mean is a **Balance point** 

Imagine we have one scale   

``` 
20      30      40      50      60

------------▲------------
           Mean 
``` 

Mean is the point where the whole data is balance.

that's why Variance and Standard Deviation is calculate around the Mean.    

Mean use only when the data is normally distributed, no Major outlier presents. 

Example:    

Marks, Height, Weight, Temperature etc. 

Mean avoid when outliers presents . 

Example of avoid outlier:   

``` 
25
26
24
27
300 
``` 

Mean ≈ 80   

All the students are 25 around but one outlier waste the Mean.  

2. Median   

What is Median? 

Median  

**Middle value after sorting the data** 

Median can divide the data into 2 equal parts.  

**Formula(Odd Number of Values)**   

if the Observations of **n** is **odd**    

Formula  :  

$$
\frac{\ n + 1}{2}
$$      

they says positive. 

Example 

``` 
10
15
20
25
30  
``` 

Total values    

```
5   
``` 

Formula : 5+1/2 = 3 

3rd value   

``` 
20  
``` 

Median = 20.    

**Formula (Even Number of Values)** 

if the Observations of **n** is **Even**    

Formula :       

$$
\text{Median Position}=\frac{\left(\frac{n}{2}\right)^{th}+\left(\frac{n}{2}+1\right)^{th}}{2}
$$  

Exmaple :   

``` 
10
15
20
25  
``` 

Middle values   

```
15 

20  
``` 

Median : 15 + 20 / 2 = 17.5 

**Mathematical Meaning**    

Median  

Data divide into    

50%

↓

50% 

```
10 20 30 | 40 | 50 60 70

          ↑
      Median    
``` 

when to use median ?    

✅ Outliers

✅ Income

✅ House Price

✅ Salary   

finance companies mostly median use.    

WHY?    

Example 

```
25000
26000
27000
28000
500000  
``` 

Mean Bad Median 27000 Reality better shows. 

3. Mode 

**What is Mode?**   

Mode    

   **Most frequently occuring value.**  

that values whose repeated mostly.  

**Formula** 

Mode cannot have any mathematical formula.  

we can only count the frequency.    

Example 

``` 
20

25

25

25

30

35  
``` 

Frequency   

| Value | Frequency |
| ----- | --------- |
| 20    | 1         |
| 25    | 3         |
| 30    | 1         |
| 35    | 1         |

Mode    
``` 
25  
```     

**Multiple Modes**  

Dataset 

``` 
10

10

20

20

30  
``` 

Mode    

``` 
10

20  
``` 

we can says that as a **Bimodal**   

if the no one value can repeat's    

``` 
10

20

30

40  
``` 

then    

we can **No Mode**  

**Mathematical Difference** 

| Mean                  | Median                        | Mode                  |
| --------------------- | ----------------------------- | --------------------- |
| Uses every value      | Uses only middle position     | Uses frequency        |
| Sensitive to outliers | Not affected much by outliers | Depends on repetition |
| Formula available     | Position formula              | No formula            |


**AI/ML Perspective**   

| Measure | AI/ML Use                                                |
| ------- | -------------------------------------------------------- |
| Mean    | Missing value imputation, feature scaling, normalization |
| Median  | Missing values with outliers, skewed data                |
| Mode    | Filling missing categorical values                       |

**Company Example** 

Suppose company ha employee salaries.   

``` 
25000
26000
27000
28000
900000  
``` 

Mean    

25000+26000+27000+28000+90000/5 = 201200    

❌ Misleading   

Median 

``` 
27000   
``` 

✅ Best 

Suppose Departments 

``` 
IT
HR
IT
IT
Sales   
``` 

Mode    

``` 
IT  
``` 

| Feature              | Mean                     | Median                                                      | Mode                           |
| -------------------- | ------------------------ | ----------------------------------------------------------- | ------------------------------ |
| Meaning              | Average value            | Middle value                                                | Most frequent value            |
| Formula              | Σx / n                   | (n+1)/2 position (odd), average of two middle values (even) | No formula                     |
| Uses All Values      | ✅ Yes                    | ❌ No                                                        | ❌ No                           |
| Affected by Outliers | ✅ Yes                    | ❌ No (or very little)                                       | ❌ No                           |
| Best For             | Normal data              | Skewed data & outliers                                      | Categorical or repeated values |
| AI/ML Use            | Mean imputation, scaling | Median imputation                                           | Categorical data imputation    |
