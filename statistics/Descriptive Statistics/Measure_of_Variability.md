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

# Measure of Variability    

Suppose we have two companies.  

**Company A**   

``` 
50
51
50
52
51  
``` 

**Company B**   

``` 
20
50
80
90
34  
``` 

Now, we can finds the Mean of these data is :   

Company A Mean ≈ 50 

Company B Mean ≈ 54 

Both of the Mean alomst same.   

Question : Both of the Companies data are same or not?  

Answer : ❌ Absolutely Not. 

Company A data close at one point(50).

But, Company B data are spread each side like 20, 34, 50, 80, 90 etc.   

that's difference tells us **Measure of Variability.**  

### What is Variability?    

*Defination*  

  **Measure of Variability tells us how much the data is spread around its center(Mean or Median).**  

- It tells us how close or how far the values are from each other.  

### What does "Spread" Mean?  

Suppose we two classes. 

**Class A Marks** 

``` 
48
49
50
51
52  
``` 

Graphs imagine  

``` 
48 49 50 51 52
█████ 
``` 

each marks are related/around each to the other.  

Spread

↓

Very Small  

**Class B Marks** 

``` 
10
35
50
75
100 
``` 

Graph 

``` 
10          50          100
█     █     █     █      █  
``` 

here the spread value are far with each other.

Spread

↓

Very Large  

Simple Rule

Close Values

↓

Small Spread

Far Values

↓

Large Spread  

### Why Do We Need Variability? 

Suppose Company Sees in the whole data is mean. 

Employee Salary 

``` 
30000
31000
32000
33000
34000 
``` 

Mean  

``` 
32000 
``` 

Now, second company 

``` 
10000
20000
32000
45000
83000 
``` 

Mean  

Almost same.  

but reality?  

First company employees salary are stable.  

but, second company employees salary are different. 

that's why only mean sees we cannot decide their variability. 

### Why is important in AI/ML?  

Machine Learning cannot only takes Average. 

They can understand whole data. 

Question  

Data  

Is stable?  

ya  

Or Is Random? 

If the data is Random then  

↓ 

Model cannot understand the patterns of the data. 

Precdiction accuracy also dropdown. 

### Real AI Pipeline  

``` 
Collect Data
      ↓
Clean Data
      ↓
Find Mean
      ↓
Find Variability
      ↓
Check Outliers
      ↓
Scale Features
      ↓
Train Model 
``` 

That's Why Variability In ML preprocessing is important.  

### Components of Measure of Variability  

``` 
Measure of Variability
│
├── Range
├── Variance
├── Standard Deviation
└── IQR 
``` 

each purpose has different. 

1. **Range**  

Formula   

**Range = Maximum - Minimum** 

Example     

```   
20

25

30

40

60    
```   

Maximum     

```   
60    
```   

Minimum     

```   
20    
```   

Range 

```
60 - 20     

= 40  
```   

**Purpose** 

They Says Overall spread.     

Only Use of Highest and lowest value.     

**Limitation**    

If have an outlier in our data.     

```   
20

22

25

28

500   
```   

Range 

```   
500 - 20    

= 480 
```   

In Reality, only one value can changes here range cannot reliable.      


2. **Variance**   

This is the heart of Statistics.    

**They can tell us each of the value how to far by the Mean of the average**  

**Har value Mean se average me kitni door hai.**      

**Formula (Population)**

$$
\sigma^2=\frac{\sum (x-\mu)^2}{N}
$$    

**For Sample**    

$$
s^2=\frac{\sum (x-\bar{x})^2}{n-1}
$$    

**Why Square**    

Question    

Example     

```   
Mean  

50    
```   

Values      

```   
40    

60    
```   

Difference  

```   
-10

+10   
```   

if we can direct add these then,    

```   
-10+10=0    
```   

Wrong 

Doesnot spread is Zero  

That's why we can do square.  

```   
(-10)²

100

(+10)²

100
```   

Now, we can take the average and Correct the spread.  

**In AI/ML Use**     

Variance tells us Feature informative or not.   

if the feature variance almost zero then. 

Example     

```   
Age

25

25

25

25

25    
```   

Model cannot takes any information. 

That's why **Low Variance Features** some time removes.     

that process is called as the **Variance Threshold Feature Selection.** 

3. **Standard Deviation**     

Standard Deviation is a sqaure root of Variance.      

Formula     

$$
\sigma=\sqrt{\sigma^2}
$$    

Question    

WHy we can use the Variance?  

Example     

Salary in Rupees that's why Variance Ruppes^2 that is not looks practical.

Standard Deviation takes Square then again it can converted into the rupees that's why company use the SD.  

**Interpretation**

Small SD

↓

Data stable.

Large SD

↓

Data highly scattered.  

Means we here in the standard devation also finds the Means so the Mean of by find the standard devation formula is give if is small then the data is stable means Values each other closes but the Mean is Big in number of standard deviation then Data is highly scattered values each other is highly far.    

**AI/ML Uses**    

- Outlier Detection.    
- Feature Scaling.      
- Z-score Normalization.      
- Model Evaluation.
- Risk Analysis.  

Finance Companies daily calculate the Standard Devation.    

4. **Interquartile Range (IQR)**    

IQR Says    

Middle 50%  data how the spread.    

Formula :   

IQR = Q3 - Q1     

Question    

Why Middle 50%?   

Because, Extreme Values ignores.    

Example:    

```   
20

22

24

25

26

500   
```   

Range 

Huge. 

IOR   

Normal.     

That's why Box plot use the IOR.    

**AI/ML Uses of IQR**   

✔ Outlier Detection

✔ Data Cleaning

✔ Box Plot

✔ Robust Statistics    

if the outlier can removes then we can use the IOR method or Z-score Method.  


**Complete Flow** 

```   
Raw Data
      ↓
Find Mean
      ↓
Check Spread
      ↓
Range
      ↓
Variance
      ↓
Standard Deviation
      ↓
IQR
      ↓
Outlier Detection
      ↓
Feature Scaling
      ↓
Machine Learning Model  
```   

Range
→ Overall spread using Max − Min

Variance
→ Average squared distance from Mean

Standard Deviation
→ Actual spread in the original unit

IQR
→ Spread of the middle 50% data     


| Measure                | What it tells                          | Best Use                                                            |
| ---------------------- | -------------------------------------- | ------------------------------------------------------------------- |
| **Range**              | Total spread from minimum to maximum   | Quick overview of spread                                            |
| **Variance**           | Average squared distance from the Mean | Measure how scattered the data is and analyze feature variability   |
| **Standard Deviation** | Average spread in the original unit    | Outlier detection, feature scaling, risk analysis, model evaluation |
| **IQR**                | Spread of the middle 50% of the data   | Detect outliers while ignoring extreme values                       |
