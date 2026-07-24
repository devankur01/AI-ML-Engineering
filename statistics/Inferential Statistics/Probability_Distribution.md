# All About Probability Distribution    

Probability Means how possibility an event can occurs.  

Probability value   

``` 
0 ≤ P ≤ 1   
``` 
- 0 → Impossible    
- 1 → Certain   
- 0.5% → 50% Chance 

Example 

Coin Toss   

``` 
Head = 0.5

Tail = 0.5  
```

### What is Distribution?   

Distribution means  

**How the spread of value to the Data with also pattern of spread** 

We can learns about in Variability data are spread and Distribution that spreaded data graphical and mathematical representation.   

Example 

Marks   

``` 
40
42
44
45
46
47
48
49
50
90  
``` 

these data cannot be evenly spreaded.   

Distribution tells us   
- Maximum values.   
- Minimum values.   
- Where is Mean.    
- Outlier present or not.   
- how the shape of the data in graph.   

Variability only provides the number how the data is spreaded means spread of data is more or less variability tells these thing only.  

Distribution tells us spread are their in the data but how to spread the data just like spread is high or low, Shape are wide or narrow, what is center value, outlier present or not, how the patterns of the data means distribution provides more information.   

### What is Probability Distribution?   

Probability we knows about that part and Distribution also knows so we can easily combine both of that. 

Probability

.

Distribution

= Probability Distribution. 

### Defination  

probability Distribution is mathematical function that tells us random variable each possible value of probability. 

Simple words, how the time and ways random value can occurs, that complete map probability distribution.    

### Real world Example  

Suppose we have one call center Average 4 calls per minutes can comes Question Next time how the calls can occurs?  

``` 
0

1

2

3

4

5

6

7   
``` 

Each value of probability are different.    

Example 

``` 
0 Calls → 2%

1 Call → 8%

2 Calls → 18%

3 Calls → 25%

4 Calls → 30%

5 Calls → 10%

6 Calls → 5%

7 Calls → 2%    
``` 

this full table is probability distribution.    

### What is random variable?    

Random variable means such a value that can be decided after the experiment.    

Example 

Coin Toss   

Result  

``` 
Head

Tail    
``` 

We cannot knows about before the toss random.   

Examples    

Dice    

Possible values 

``` 
1

2

3

4

5

6   
``` 

Which one can occurs?   

Random. 

Customer Purchase   

Today customer  

``` 
₹500

₹1000

₹1500

₹0  
``` 

how to spends?  

Random  

**Machine Learning**    

tomorrow user movie views or not Random Variable.   

### Probability Distribution Purpose?   

Probability distribution says   
- Which value chances can occurs more.  
- Which value chances can occurs less.  
- what is average.  
- What is Variance. 
- How to predicts the future.   

### Why in AI/ML important? 

Machine Learning cannot works on certainty they can predicts only.  

Example 

**SPam Detection** 

Model says  

``` 
Spam

97% 
``` 

this is probability.    

**Disease Prediction**

``` 
Cancer

82%
```

Probability.    

**Face Recognition**    

``` 
Person A

95% 
``` 

Probability.    

**Recommendation System**

Netflix

```
Movie Like

91%
``` 

Probability.    

Each case Probability Distribution indirectly uses. 

### Probability Distribution Workflow   
``` 
Random Experiment

↓

Possible Outcomes

↓

Probability Assign

↓

Probability Distribution

↓

Prediction

↓

Decision    
``` 

### Types of Probability Distribution   

their are two major categories. 

``` 
Probability Distribution

│

├── Discrete Probability Distribution

└── Continuous Probability Distribution 
``` 

1. **Discrete Probability Distribution**    

Discrete means we can count the values. 

Example 

Dice    

``` 
1

2

3

4

5

6   
``` 

Coin    

``` 
0

1   
``` 

Students    
``` 
20

21

22  
``` 

Cars    
``` 
100

101

102 
``` 

All are countable that's why Discrete.  

Real Examples
- Number of calls
- Number of Customers   
- Number of Emails
- Number of Bugs
- Number of Goals
- Number of Transactions    

2. **Continuous Probability Distribution**  

Continuous means Infinte possible values.   

Example 

**Height**  

``` 
170.1

170.12

170.123

170.1234    
```     

Never finish.   

**Weight**  

``` 
65.12

65.125

65.1257 
``` 

**Temperature** 

``` 
28.23

28.2345

28.234567   
``` 

Continuous. 

### Difference 
  
| Discrete     | Continuous       |
| ------------ | ---------------- |
| Countable    | Measurable       |
| Fixed values | Infinite values  |
| Coin Toss    | Height           |
| Dice         | Weight           |
| Calls        | Temperature      |
| Customers    | Salary (approx.) |


| Type       | Distribution   | When to use that           |
| ---------- | -------------- | -------------------------- |
| Discrete   | Binomial       | Success/Failure Count      |
| Discrete   | Poisson        | Event Count in Time        |
| Continuous | Normal         | Natural Data               |
| Continuous | t-Distribution | Small Sample Statistics    |
| Continuous | Chi-Square     | Variance & Feature Testing |

### 1. BINOMIAL DISTRIBUTION    

Question:   

5 times a coin tossed, what is the probability of Exactly 3 Head?   

Here each tossed have only 2 possibilities: 

- Head  
- Tail  

that is  Binomial use case. 

**Conditions**  

Binomial only use when: 

1. **Fixed Trails** 

5 tosses    

n = 5   

2. **Two Outcomes** 

Head/Tail   

3. **Independent**  

When the tossed coin gives us one outcomes it doesn't relation or dependent to other outcomes.    

4. **Same Probability** 

Each toss outcomes has probability p = 0.5  

**Binomial Formula**    

$$
P(X = k) = \binom{n}{k} \, p^k (1 - p)^{\,n-k}
$$  

**Formula Meaning** 

**n**   

Total Trials    

Examole: 5 tosses   

n = 5.  

**k**   

Required Successes or this is also probability distribution time.

3 heads 

k = 3   

**p**   

success Probability     
Head    
p = 0.5 

**(1-p)** 

Failure Probability 
Tail    
0.5 

**nCk** 

combination

How the way 3 heads are comes   

$$
{}^nC_k = \frac{n!}{k!(n-k)!}
$$  

**Question Solve**  

5 Toss Exactly 3 Heads? 

n = 5, k = 3, p = 0.3   

Step 1  

**Combination**     
            
$$
\binom{5}{3}=\frac{5!}{3!(5-3)!}=10
$$

Step 2  

**Binomial Formula**     

$$
P(X=3)=10\times(0.5)^3\times(0.5)^2
$$

$$
=
10\times(0.5)^5
$$ 

$$
=
10\times\frac{1}{32}
$$  

$$
\frac{10}{32}
=\frac{5}{16}
=0.3125
$$

$$
P(X=3)=0.3125
$$  

**Mean Formula**    

$$
\mu=np
$$

$$
\mu=5\times0.5=2.5
$$  

**Variance Formula**    

$$
\sigma^2=np(1-p)
$$  

$$
\sigma^2
=
5\times0.5\times(1-0.5)
$$  

$$
=
5\times0.5\times0.5
$$ 

$$
=
1.25
$$  

**Standard Deviation Formula**  

$$
\sigma=\sqrt{np(1-p)}
$$  

$$
\sigma
=
\sqrt{5\times0.5\times(1-0.5)}
$$ 

$$
=
\sqrt{5\times0.5\times0.5}
$$ 

$$
\sqrt{1.25}\approx1.118
$$

### AI/ML UseCase of Binomial   

**Email Spam Detection**    

Spam = Success 

Not Spam = Failure  

**Loan Approval**   

Approved

Rejected    

**Disease Prediction**

Disease

No Disease

**Customer Churn**

Leave

Stay    

### 2. POISSON DISTRIBUTION 

Question:   

4 calls per hours an average can comes from anywhere?   

So, What is the probabililty Exactly 6 calls comes from anywhere?

Binomial count Successes Poission counts the Events?

Examples:   
- Calls 
- Accidents 
- Website Cicks.    
- Orders.   
- Defects.  

Formula :   

$$
P(X=k)=\frac{e^{-\lambda}\lambda^{k}}{k!}
$$  

**Symbols** 

**Lambda (λ)**  

Average number of events in a fixed interval.   

Example :   

Average calls per hour = 4  

$$
\lambda = 4
$$  


**k**   

Required number of events.  

Example:    

Exactly 6 calls 

$$
k = 6
$$  

**Euler's Number**  

A Mathematical constant used in exponential growth and probability. 

$$
e \approx 2.71828
$$  

**Example** 

A call center receives an average of **4 calls per hour.**  

Find the probability of receiving **exactly 6 calls.**  

**Given**   

$$
\lambda = 4,\qquad k = 6
$$  

**Formula** 

$$
P(X=6)=\frac{e^{-4}\times4^{6}}{6!}
$$  
   

$$
4^{6}=4096
$$  

$$
6!=720
$$  

$$
e^{-4}\approx0.018315
$$  

$$
P(X=6)=\frac{0.018315\times4096}{720}
$$  

$$
P(X=6)\approx0.1043
$$  

**Probability in Percentage**   

$$
0.1043\times100=10.43\%
$$

**Mean of Poisson Distribution**    

The expected(average) number of events. 

$$
\mu=\lambda
$$  

$$
\mu=4
$$  

**Variance of Poisson Distribution**    

In a Poission distribution, the variance is equal to the mean.  

$$
\sigma^2=\lambda
$$  

$$
\sigma^2=4
$$  

**Standard Deviation of Poisson Distribution**  

the standard deviation is the square root of the variance.  

$$
\sigma=\sqrt{\lambda}
$$  

$$
\sigma=\sqrt{4}=2
$$  

| Quantity           | Formula                                       |
| ------------------ | --------------------------------------------- |
| Probability        | $$P(X=k)=\frac{e^{-\lambda}\lambda^{k}}{k!}$$ |
| Mean               | $$\mu=\lambda$$                               |
| Variance           | $$\sigma^2=\lambda$$                          |
| Standard Deviation | $$\sigma=\sqrt{\lambda}$$                     |

### AI/ML UseCase of Poission Distribution

**Website Traffic Prediction**

Per minute visitors

**Fraud Detection**

Transactions per minute

**Network Monitoring**

Errors per second

**E-commerce**

Orders per hour

**Manufacturing**

Defective products count    

### BINOMIAL VS POISSON 

| Feature           | Binomial  | Poisson      |
| ----------------- | --------- | ------------ |
| Count What?       | Success finite  | Events infinite     |
| Outcomes          | 2         | Many         |
| Probability Fixed | Yes       | Average Rate |
| Example           | Head/Tail | Calls/Hour   |
| Mean              | np        | λ            |
| Variance          | np(1-p)   | λ            |


### 3. NORMAL DISTRIBUTION      

His graph is like 🔔 Bell Shape.   

Examples :  
- Height.   
- Weigth.   
- IQ.
- Marks.    
- Salary.   

Mostly real world data normal closed of that.   

**Properties**  

**Symmetric**   

Left = Rigth    

Mean = Median = Mode    

these all three's are in the centered.  

**Area = 1**    

Total probability = 100%    

Formula :   

$$
f(x)=\frac{1}{\sigma\sqrt{2\pi}}\,e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$  

**68-95-99.7 Rule** 

Mean ± 1 SD

68% 

Mean ± 2 SD

95% 

Mean ± 3 SD

99.7%   

### AI/ML use-Case  

**Feature Scaling** 

**Outlier Detection**   

**Anomaly Detection**   

**Statistical Testing** 

**Guassain Navie Bayes**    

Probability Density (PDF)   
```

 ^
 |                                μ (Mean)
 |                                │
 |                                │
 |                           .-''''''-.
 |                        .-'          '-.
 |                      .'                '.
 |                    .'                    '.
 |                  .'                        '.
 |                .'                            '.
 |______________.'______________________________  '.______________> X

          μ-3σ     μ-2σ     μ-σ      μ      μ+σ    μ+2σ    μ+3σ


                          |-------68%----------|
                    |--------------95%----------------|
            |--------------------99.7%--------------------|
```

- first standard deviation μ(Mean) between to  μ-σ left to μ-σ right data can holds 68%.    
- second standard devaiton μ(Mean) in between to μ-2σ left to μ-2σ right data can holds 95%.   
- Thrid standard devation μ(Mean) in between to μ-3σ left to μ-3σ right data can holds 99.7%.
- Symmetric means left or right side under the curve data are equal from left to right.

```
                      Mean
                       │
                    Median
                       │
                      Mode
                       │

                  .-''''''-.
               .-'          '-.
             .'                '.
            /                    \
___________/______________________\___________
```

Normal Distribution = Mean = Median = Mode. 

these all three in the center of graph. 


``` 

                  .-''''''-.
               .-'##########'-.
             .'################'.
____________/####################\_____________
``` 

Shaded Area = probability = 1.  

Means 100%. 

probability cannot increases at the value of 1. 

**Continuous Variable** 

``` 

Height

170.1

170.11

170.111

170.1115

170.11152

170.111521

170.1115217

....

Infinite Values
``` 

that's why  

``` 
P(X =170)

=

0   
``` 

But     

``` 
P(169<X<171)

possible this.  
``` 

**Gaussian Noise**  

``` 

Original Signal

───────────────

Noise Added

───~─────~~──~───~~────
``` 

Noise ≈ Normal Distribution.    

that's why in gaussian noise use in the AI. 

**Gaussian Distribution Formula**

$$
f(x)=\frac{1}{\sigma\sqrt{2\pi}}
e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$  

| Symbol           | Simple Meaning                                                                       |
| ---------------- | ------------------------------------------------------------------------------------ |
| $x$              | The value you want to check (Example: Height = 170 cm)                               |
| $\mu$ (Mu)       | Average value (Center of the data)                                                   |
| $\sigma$ (Sigma) | Standard Deviation (Shows how much the data is spread)                               |
| $\sigma^2$       | Variance (Square of the Standard Deviation)                                          |
| $e$              | Euler's Number (≈ 2.71828), a mathematical constant used in exponential calculations |
| $\pi$            | Pi (≈ 3.14159), a mathematical constant                                              |
| $f(x)$           | Probability Density (Shows how likely the value is around that point)                |

**Understanding the Formula**   

the normal distribution formula has two main parts. 

1. **Scaling part** 

**Formula** 


$$
\frac{1}{\sigma\sqrt{2\pi}}
$$  
 

This part controls the height of the bell curve.

It also makes sure that the total area under the curve is always equal to 1 (100%). 

Important Points    
- If Standard Deviation ($\sigma$) increases, the curve becomes wider and shorter.  
- If Standard Deviation ($\sigma$) decreases, the curve becomes narrower and taller.    
- This part keeps the curve properly scaled.    

2. **Exponential part** 

**Formula** 


$$
e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$  
 

This part checks how far the value ($x$) is from the mean ($\mu$).  

Important points    
- If $x$ is very close to the mean, the curve has a high density (high point).
- If $x$ is far from the mean, the curve becomes lower.
- The farther the value moves from the mean, the smaller the density becomes.   

``` 
Normal Distribution Formula

        f(x)

          =
   Scaling Part
          ×
 Exponential Part   
 ```    
    
``` 
                Normal Distribution Formula

                        f(x)
                          │
          ┌───────────────┴───────────────┐
          │                               │
          ▼                               ▼

    Scaling Part                 Exponential Part

   1 / (σ√2π)              e^(-(x-μ)² / 2σ²)

 Controls the              Checks how far x
 height of the             is from the mean

 Makes total               Near Mean → High Density
 area = 1                  Far from Mean → Low Density

 σ ↑ → Wide Curve          Controls the Bell Shape
 σ ↓ → Tall Curve   
 ```    

- **Scaling Part** → Controls the size (height and width) of the curve.
- **Exponential Part** → Controls the shape of the curve based on the distance from the mean.   

**Example** 

Suppose the average height of students is   

``` 
Mean (μ) = 170 cm
Standard Deviation (σ) = 5 cm   
``` 

Now check three students:   

| Height ($x$) | Distance from Mean | Density   |
| ------------ | ------------------ | --------- |
| 170 cm       | Exactly at Mean    | Very High |
| 172 cm       | Very Close         | High      |
| 180 cm       | Far from Mean      | Low       |
| 190 cm       | Very Far           | Very Low  |

**Conclusion:** 
- Values near the average are more common.  
- Values far from the average are rare. 

``` 
Scaling Part
↓

Controls the Size of the Curve

Exponential Part
↓

Controls the Shape of the Curve

Whole Formula
↓

Calculates the Probability Density of any Value (x) 
``` 

f(x) = Probability Density Function (PDF)   

$f(x)$ = The density (height of the curve) at a particular value $x$. It is NOT the probability itself. Probability is found by calculating the area under the curve over a range of values.  

### 4. t-DISTRIBUTION 

**Why do we need t-Distribution?**  

Suppose Google HR Finds employees average salary? 

Google Employees : ```10,00,000 Employees```  

So, we can collect the each of the employee salary ❌ Impossible so, what we can do instead of collecting each of employee salary?  

Takes Random sample Example ```30 Employees``` or ```20 Employees``` this is we can knowns as the inferential statistics but problem starts when we takes sample of whole population we cannot finds the exacts average that will we finds by the whole population average that uncertainty can handled by the **t-Distribution.**  

**Main Idea** 

Normal Distribution says we have alot's of data.  

**t-distribution**  

we have less data as compare to normal distribution, that's why we can consider also uncertainty. 

#### Graph Comparison.  

``` 
Probability Density
^

|                         Normal Distribution
|                            .-''''''-.
|                         .-'          '-.
|                       .'                '.
|                     .'                    '.
|___________________.'________________________'.____________________

|                    t-Distribution
|                 .--''''''''''''--.
|              .-'                  '-.
|            .'                        '.
|__________.'____________________________'._________________________> X
``` 

✅ Center almost same.  

✅ t-Distribution ha less than normal distribution. 

✅ Tails has thicker in size. 

#### Normal vs t Distribution 

```
               Normal

                    /\
                  /    \
                /        \
______________/___________\________________


             t Distribution

                 ______
               /        \
             /            \
___________/________________\____________
``` 

Observe 

**Normal**  
- Peak High.  
- Tail Thin.  

**t-Distribution**  
- Peak Low. 
- Tail thick. 

#### Why Thick Tails? 

Suppose we have only ```10 Students``` marks only collected this data is lucky sample or unlucky sample that's why uncertainty has been increases Graph says Extreme values also can inside the data that's why tails has thicker.  

``` 
Less Data

↓

More Uncertainty

↓

More Chance of Extreme Values

↓

Thick Tails

↓

t Distribution  
``` 

#### Formula  

**t-score** 

$$
t=\frac{\bar{x}-\mu}{\frac{s}{\sqrt{n}}}
$$  

#### Formula Meaning  

| Symbol    | Meaning                   |
| --------- | ------------------------- |
| $\bar{x}$ | Sample Mean               |
| $\mu$     | Population Mean           |
| $s$       | Sample Standard Deviation |
| $n$       | Sample Size               |
| $t$       | t-score                   |

#### Degree of Freedom(df)  

**Formula** 

$$
df=n-1
$$  

Example 

Sample  
``` 
10 Students 
``` 

Then  

``` 
df = 9  
``` 

#### Why n-1? 

If we have 10 values 9 values gets fixed firstly last value automatically decide that's why independent values only 9 we can call it Degree of Freedom. 

#### Graph with Degrees of Freedom? 

``` 
Probability Density
^

|

|          df = 3
|       .-------------.
|    .-'               '-.

|          df = 10
|       .-----------.
|    .-'             '-.

|          df = 30
|      .---------.
|    .'           '.

|          Normal
|       .-------.
|     .'         '.

+----------------------------------------------------->
``` 

Observe Means --> df, then --> sample size, t-Distribution --> Normal distribution. 

### AI/ML Example 

Suppose we have ```18 customers``` we can sees that average spending 1000 yes or not Population SD(Standard deviation) are unknown to Hyothesis Testing --> t-Distribution. 

#### AI/ML Uses

✔ Small Dataset Analysis

✔ Hypothesis Testing

✔ A/B Testing

✔ Confidence Interval

✔ Medical Research

✔ Startup Analytics

✔ Survey Analysis

✔ Model Evaluation (Small Sample)  

#### Normal vs t Distribution 

| Normal Distribution                  | t Distribution             |
| ------------------------------------ | -------------------------- |
| Large Sample                         | Small Sample               |
| Population SD Known                  | Population SD Unknown      |
| Thin Tails                           | Thick Tails                |
| Less Uncertainty                     | More Uncertainty           |
| Uses Z-score                         | Uses t-score               |
| Becomes inaccurate for small samples | Designed for small samples |

``` 
                    Dataset
                       │
             Is Sample Large?
                 /          \
               Yes          No
                │            │
      Population SD      Population SD
          Known?             Unknown
            │                  │
            Yes                Yes
             │                  │
   Normal Distribution     t Distribution 
``` 

``` 
Normal Distribution

Large Sample
+
Population SD Known

↓

Use Z-score


t Distribution

Small Sample
+
Population SD Unknown

↓

Use t-score 
```

**Sample Mean**

$$
\bar{x}=\frac{\sum x}{n}
$$

Where

- $\bar{x}$ = Sample Mean
- $\sum x$ = Sum of all sample values
- $n$ = Sample Size 

**Population Mean** 

$$
\mu=\frac{\sum x}{N}
$$  

Where   

- $\mu$ = Population Mean
- $N$ = Population Size 

**Sample Variance** 

$$
s^2=\frac{\sum (x_i-\bar{x})^2}{n-1}
$$  

Where

- $s^2$ = Sample Variance
- $x_i$ = Each Sample Value
- $\bar{x}$ = Sample Mean
- $n$ = Sample Size

**Sample Standard Deviation** 

$$
s=\sqrt{\frac{\sum (x_i-\bar{x})^2}{n-1}}
$$  

Where 

- $s$ = Sample Standard Deviation.  

**Population Standard Deviation** 

$$
\sigma=\sqrt{\frac{\sum (x_i-\mu)^2}{N}}
$$  

Where 

- $\sigma$ = Population Standard Deviation. 

**Standard Error (SE)** 

$$
SE=\frac{s}{\sqrt{n}}
$$  

Where 

- $SE$ = Standard Error
- $s$ = Sample Standard Deviation
- $n$ = Sample Size 

Meaning

They tell us Sample Mean actual Population Mean how the average can fluctuate.  

**t-Score Formula** 

$$
t=\frac{\bar{x}-\mu}{\frac{s}{\sqrt{n}}}
$$  

or  

$$
t=\frac{\bar{x}-\mu}{SE}
$$  

Where 

| Symbol    | Meaning                   |
| --------- | ------------------------- |
| $t$       | t-score                   |
| $\bar{x}$ | Sample Mean               |
| $\mu$     | Population Mean           |
| $s$       | Sample Standard Deviation |
| $n$       | Sample Size               |
| $SE$      | Standard Error            |

**Degrees of Freedom (df)** 

$$
df=n-1
$$  

Example 

``` 
Sample Size = 20

df = 19 
```
**Confidence Interval (Using t-Distribution)**  

$$
\bar{x}\pm t\left(\frac{s}{\sqrt{n}}\right)
$$  

this formula can calculates/estimates the acutal population mean lies which ranges has been probability.  

``` 
Sample Size (n)

          n < 30
              │
              ▼
     Use t-Distribution
     (Population SD Unknown)

────────────────────────────────

          n ≥ 30
              │
              ▼
     Normal Distribution
     (or t ≈ Normal for large n)  
``` 

| Feature                 | Normal Distribution      | t-Distribution      |
| ----------------------- | ------------------------ | ------------------- |
| Sample Size             | Usually $n \ge 30$       | Usually $n < 30$    |
| Population SD           | Known ($\sigma$)         | Unknown             |
| Standard Deviation Used | Population SD ($\sigma$) | Sample SD ($s$)     |
| Score Used              | Z-score                  | t-score             |
| Shape                   | Thin Tails               | Thick Tails         |
| Uncertainty             | Low                      | Higher              |
| Degrees of Freedom      | Not Required             | Required ($df=n-1$) |

``` 
Population Known
        ↓
      Use Z

Population Unknown
        ↓
      Use t

Small Sample
        ↓
More Uncertainty
        ↓
Thicker Tails
        ↓
t-Distribution  
```

**Normal Distribution assumes that you already have enough data and know the population variability. t-Distribution is used when you have only a small sample and must account for extra uncertainty.** 

One-Line Summary

- Normal Distribution = **More data → More confidence → Thin tails**
- t-Distribution = **Less data → Less confidence → Thick tails**  

### 5. CHI-SQUARE DISTRIBUTION  

**Chi-Square Distribution measures how much the observed data differs from the expected data.** 

they can compare the :
``` 
Reality

VS

Expectation 
``` 

**Real Life Example** 

Suppose HR says   

``` 
In Each department Contains only 25 Employees. 
``` 

**Expected**  

| Department | Employees |
| ---------- | --------- |
| HR         | 25        |
| IT         | 25        |
| Sales      | 25        |
| Finance    | 25        |

**but in Acutal**

| Department | Employees |
| ---------- | --------- |
| HR         | 15        |
| IT         | 40        |
| Sales      | 20        |
| Finance    | 25        |

Question  

``` 
The Difference are Normal or Big difference?  
``` 

that's answer can given by the **Chi-Square.**  

**Main Idea** 

If the Observed ≈ Expected then,  

``` 
Chi-Square Value

Small 
``` 

If the Observed ≠ Expected then,  

``` 
Chi-Square Value

Large 
``` 

that concepts made up by Chi-Square.  

**Why Name "Chi-Square"?**  

Greek letter  
``` 
χ 
``` 

Read as 
``` 
Chi 
``` 

Or Why we can difference squared that is  

``` 
χ²

Chi Square  
``` 

**Formula** 

$$
\chi^2=\sum\frac{(O-E)^2}{E}
$$

**Formula Meaning** 

| Symbol   | Meaning                        |
| -------- | ------------------------------ |
| $\chi^2$ | Chi-Square Statistic           |
| $O$      | Observed Value (Actual Data)   |
| $E$      | Expected Value (Expected Data) |
| $\sum$   | Add all categories             |

**Formula Logic** 

Suppose 

Expected  

``` 
50  
``` 

Observed  

``` 
60  
``` 

Difference  

``` 
60−50

=

10  
``` 

Square  

``` 
100 
``` 

Divide by expected

``` 
100/50

=

2 
``` 

This is only one category contribution. 

All categories add then it will converted into --> Final Chi-Square Value.  

**Why Square and Divide by Expected?**  

If we cannot do square  

``` 
+10

-10

cancel ho jate. 
``` 

Square can do then, 

``` 
100

100 
``` 

Now, cancellation not performs. 


**Expected Value**  

Example 1 Difference are small  

Suppose one company expect website  
``` 
1000 Visitors 
```

But actual comes in website   
``` 
1020 Visitors 
``` 

Difference  
``` 
1020 - 1000 = 20  
``` 

Now, we can think that only 20 Visitors are  extra comes into website.  

percentage  

``` 
20 / 1000 = 0.02

= 2%  
``` 

only 2% difference this is very normal.


Example 2 Difference are big  

Expected  

``` 
25 Visitors 
``` 

Actual  

``` 
45 Visitors 
``` 

Difference  

``` 
45 - 25 = 20  
``` 

Now, we can think that Difference aree 20 only but in Percentage we can sees, 

```
20 / 25 = 0.80  

= 80% 
``` 

Now, the difference are very big this are very big difference.  

**Compare Both Cases :**  

| Expected | Observed | Difference | Percentage Difference |
| -------: | -------: | ---------: | --------------------: |
|     1000 |     1020 |         20 |                    2% |
|       25 |       45 |         20 |                   80% |

Sees? both are differenced is = 20 but impact are not samee in both that's why Expected we can divide.  

``` 
Difference = 20

↓

Is 20 is bigger?

↓

Depends on Expected Value

Expected = 1000

20 is Small ✅

Expected = 25

20 is Huge ✅ 
```

**Graph** 

``` 
Probability

^

|

|\
| \
|  \
|   \
|     \
|       \
|         \______
|______________________________> χ²

0 
``` 

Observe 

✔ Starts from left side 

✔ Not in Negative values

✔ Right Skewed

✔ Long Tail  

**Why Right Skewed?** 

Chi square cannot be negative Reason. 

``` 
(O-E)²  
``` 

Square cannot be negative That's why graph starts with 0. 

**Degrees of Freedom**  

Formula 

$$
df=n-1
$$  

how the times df gets increases graph are Normal distribution looks like. 

**What is Non-Parametric Variable?**  

what is **parametric test**?    

they can assume the they can follows Normal distribution. 

Example   
- Z-test  
- t-test  

**Non-Parametric**  

``` 
We cannot needs of Normal distribution. 
``` 

We can works only on the Categorical data that's why Chi-Square are **Non-Parametric Test.**  

**Example** 

Gender  

``` 
Male

Female  
``` 

Or  

Payment Method  

``` 
Cash

UPI

Card  
``` 

they are not numbers they are categories that's why Chi-Square. 

#### AI/ML Actual Use 

**1. Feature Selection** 

Suppose Columns   
```
Age

Salary

Gender

Purchased 
``` 

Question  

``` 
Gender

Purchased

they are related? 

``` 

Now Chi Square check that If Realtion strong --> Feature important If realtion weak --> Drop Feature that's why ```SelectKBest(chi2)``` famous in scikit-learn. 

**2. Spam Detection** 

Features  

``` 
Free

Offer

Win

Lottery 
``` 

Target Spam Not Spam Chi-Square Best words selected.  

**3. Recommendation System**

Product Category

Purchase

They both are realted or not.

**4. Medical AI**

Smoking

Cancer

They both are realted or not. 

**5. Fraud Detection**

Card Type

Fraud

related?  

#### Types of Chi-Square Tests  

**1. Goodness of Fit**  

Question  

``` 
Expected Distribution

Matched or not? 
``` 

Example 

Dice Fair or not? 

**2. Test of Independence** 

Question  

``` 
Their are two variables they are related or not?  
``` 

Example 

```
Gender

Purchase
```

**Difference**  

| Goodness of Fit      | Test of Independence        |
| -------------------- | --------------------------- |
| One Variable         | Two Variables               |
| Expected vs Observed | Relationship Check          |
| Example: Dice        | Example: Gender vs Purchase |

``` 
Observed

↓

Expected

↓

Difference

↓

Square

↓

Divide by Expected

↓

Add

↓

Chi-Square  
``` 

**AI/ML Flow**  

``` 
Raw Dataset
      │
      ▼

Categorical Features
      │
      ▼

Chi-Square Test
      │
      ▼

Important Features
      │
      ▼

Model Training  
``` 

**Chi-Square Distribution is used to measure how different the observed data is from the expected data. In AI/ML, it is mainly used for feature selection, testing relationships between categorical variables, and checking whether observed frequencies differ significantly from expected frequencies.** 

