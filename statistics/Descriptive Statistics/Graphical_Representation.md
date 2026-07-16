# All About Graphical Representation.   

### What is Graphical Representation?  

**Defination**  

Graphical Representation is the process of displaying statistical data using charts or graphs to make it easier to understand, analyze, and communicate.    

Simple English words    

**It converts numbers into visuals so that patterns become easy to understand.**    

### Why Do We Need Graphs?  

Suppose company has sales data. 

``` 
120
130
140
145
150
155
160 
``` 

if they are numbers only.   

So, the questions to that we cannot get's answer in easy way without using graphs?   

like,   

- Sales are increasing or not?  
- Is it stable or not?  
- their present any unsual data/Outlier?    
- How the distribution of data? 

but when we sees the graphs we can answers of all of the question easily

That's why graphs are uses. 

### Statistics + Graphs.    

Statistics concepts 

``` 
Mean    
Median  
Mode    
Variance    
Standard Deviation  
IQR 
``` 
These all are only calculations.    

Graphs in calculation visually explained.   

Example 

Mean    

↓   

Center of Data  

Histogram   

↓   

Distribution    

Box Plot    

↓   

Median + IQR + Outliers 

KDE 

↓   

Denstiy     

all are connected.  

### Why AI/ML Uses Graphical Representation?    

Machine Learning first step is  

``` 
Understand the Data 
``` 

before the model trained Data Scientist draw the graph. 

Why?    

Because Graph says  

- Distribution. 
- Outliers. 
- Skewness. 
- Missing Pattern.  
- Realtionships.    
- Correlation.  

If we cannot understand these, then  

↓   

Model weak as a train.    

### AI/ML Workflow  

``` 
Raw Dataset
      ↓
Data Cleaning
      ↓
Descriptive Statistics
      ↓
Graphical Representation
      ↓
EDA
      ↓
Feature Engineering
      ↓
Feature Selection
      ↓
Model Training  
``` 

that Grpahical Representation is important for the EDA. 


### Types of Grapha     

``` 
Graphical Representation
│
├── Histogram
├── Box Plot
└── Pie Chart   
``` 

these are the three basic.  

1. **Histogram**    

**Purpose** 

Histogram says how the range of data repeated to the data.  

Example 

Employee Salary 

``` 
20k
25k
28k
30k
30k
31k
32k
35k
80k 
``` 

Histogram answer that question  

- Most employees lies in the salary range?  
- distribution is normal or not?    
- Data is Left skew?    
- Data is Right skew?   
- How the data is spread?   

**Statistics Connection**   

In Histogram    

✔ Mean

✔ Median

✔ Mode

✔ Distribution

✔ Skewness

✔ Spread   

All of the indirectly understand.   

**AI/ML Uses**

- Distribution check
- Normality check
- Feature understanding
- Data preprocessing    

2. **Box Plot**   

**Putpose** 

Box plot is statistical Summary graph.    

these things written in below show in one graph.      

✔ Minimum

✔ Q1

✔ Median

✔ Q3

✔ Maximum

✔ IQR

✔ Outliers 

**Statistics Connection**     

Box plot directly use   
- Median.   
- Quartiles.      
- IOR.      

**AI/ML Uses**

✔ Outlier Detection

✔ Data Cleaning

✔ Feature Comparison

✔ Distribution Summary

✔ Robust Analysis      

3. **Pie Chart**  

**Purpose** 

Pie chart says how each category percentage and proportion. 

Example     

Departments 

```   
IT      50%
HR      20%
Sales   30% 
```   

Pie chart instantly sees IT department is biggest of others.      

**Statistics Connection**     

Pie Chart mainly use    

- Frequency.      
- Percentange.    

Means categorical summarizes the data.    

**AI/ML uses**

pie Chart directly not using in ML training this is mostly use in:      

- EDA 
- Dashboard 
- Business Reports.     
- Presentation.   
- Customer Analysis.    

```   
Raw Data
      │
      ▼
Central Tendency
(Mean, Median, Mode)
      │
      ▼
Measure of Variability
(Range, Variance, SD, IQR)
      │
      ▼
Graphical Representation
      │
      ├── Histogram
      ├── Box Plot
      └── Pie Chart
      │
      ▼
EDA
      │
      ▼
Feature Engineering
      │
      ▼
Machine Learning Model  
```   

```   
Mean
↓
Center

Variance / SD
↓
Spread

Histogram
↓
Distribution

Box Plot
↓
Median + IQR + Outliers

Pie Chart
↓
Category Percentage     
```   

| Graph         | Main Purpose                                 | Statistics Used            | AI/ML Use                                                     |
| ------------- | -------------------------------------------- | -------------------------- | ------------------------------------------------------------- |
| **Histogram** | Show data distribution                       | Mean, Median, Mode, Spread | Distribution analysis, normality check, feature understanding |
| **Box Plot**  | Show statistical summary and detect outliers | Median, Quartiles, IQR     | Outlier detection, data cleaning, robust analysis             |
| **Pie Chart** | Show category percentages                    | Frequency, Percentage      | Business reports, dashboards, categorical data analysis       |

```         
Statistics
│
├── Descriptive Statistics
│      │
│      ├── Mean, Median, Mode
│      │        ↓
│      │   Find the Center
│      │
│      ├── Range, Variance, SD, IQR
│      │        ↓
│      │   Measure the Spread
│      │
│      └── Graphical Representation
│               ↓
│      Convert Statistics into Visuals
│
└───────────────▼────────────────
                EDA
                 ↓
        Understand the Dataset
                 ↓
       Feature Engineering
                 ↓
         Machine Learning     
```   
