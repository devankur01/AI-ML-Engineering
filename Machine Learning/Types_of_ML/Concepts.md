# Types of Machine Learning 

``` 
                         MACHINE LEARNING
                                │
       ┌────────────────────────┼────────────────────────┐
       │                        │                        │
   Supervised              Unsupervised            Reinforcement
       │                        │                        │
       │                 ┌──────┼──────┐               │
       │                 │      │      │               │
       │              Clustering  DR   Anomaly       Agent
       │                                             │
       │                                             ▼
       │                                         Environment
       │
       ├── Regression
       └── Classification

       PLUS modern learning paradigms
       │
       ├── Semi-Supervised Learning
       ├── Self-Supervised Learning
       ├── Weakly-Supervised Learning
       ├── Transfer Learning
       ├── Online / Incremental Learning
       ├── Active Learning
       ├── Federated Learning
       ├── Contrastive Learning
       └── Few-shot / Zero-shot learning    
``` 

**THis is all not mutually-exclusive list. One model/system can be lies or uses different categories simultaneously.**

A foundation model can be **self-supervised + deep Learning + transfer learning.**      

Example:    

``` 
GPT-like Model

How does it learn?
→ Self-Supervised Learning

What architecture does it use?
→ Deep Learning (Transformer)

How is pretrained knowledge reused?
→ Transfer Learning 
``` 

this is modern perspective. 

### 1. Supervised Learning - COre ML    

**Basic Idea :**    

Training data input + correct output(label/target) we can puts. 

``` 
Input X + Target Y
       ↓
   ML Algorithm
       ↓
   Learned Model
       ↓
New X → Prediction Ŷ    
``` 

Example:    

| Area | Bedrooms | Price |
| ---: | -------: | ----: |
| 1000 |        2 |   50L |
| 1500 |        3 |   75L |
| 2000 |        4 |  100L |

MOdel knows that:   

``` 
X = Area, Bedrooms
Y = Price   
``` 

That's why model X → Y relationship learns data.    

**Supervised Learning 2 major problems**    

**Regression**  

Output **continuous numerical value.**  

```
House → ₹85 lakh
Temperature → 32.5°C
Sales → ₹12.4M  
``` 

**Algorithms:** 

``` 
Linear Regression
Ridge
Lasso
Decision Tree
Random Forest
XGBoost
LightGBM
CatBoost    
``` 

**Classification**  

Output **class/category.**  

``` 
Email → Spam
Transaction → Fraud
Customer → Churn
Image → Cat 
``` 

Algorithms: 

``` 
Logistic Regression
KNN
Naive Bayes
SVM
Decision Tree
Random Forest
XGBoost
LightGBM
CatBoost
Neural Networks 
``` 

**SUpervised learning = labeled examples through input-output relationship learns data.**   

### 2. Unsupervised Learning    

Here **target are not available.**  

```
Data X
 ↓
Algorithm
 ↓
Hidden structure / patterns 
``` 

Example:    

Comany have customers.  

``` 
Age
Income
Spending
Frequency   
``` 

But not anyone customer have manually segement label.   

Model ourselves group discover: 

``` 
Group 1 → High-value customers
Group 2 → Occasional customers
Group 3 → Low-engagement customers
``` 

**Main Unsupervised Tasks** 

**Clustering**  

``` 
K-Means
DBSCAN
Hierarchical Clustering
Gaussian Mixture Models 
``` 

**Dimensionality Reduction**    

``` 
PCA
t-SNE
UMAP    
``` 

**Anomaly Detection**   

``` 
Isolation Forest
One-Class SVM
LOF 
``` 

**Density / Distribution Modeling** 

Conceptually:   

``` 
Gaussian Mixture Models
Kernel Density Estimation   
``` 

**Unsupervised Learning = Labels without inside data structure/pattern discover.**  


### 3. Semi-Supervised Learning 

Supppose we have:   

``` 
1,000,000 images    
``` 

But manually labeled:   

```
10,000 images   
``` 

Only.   

Others: 

``` 
990,000 → Unlabeled 
``` 

Semi-supervised learning labeled + unlabeled data combine.  

``` 
Small labeled dataset
          +
Large unlabeled dataset
          ↓
      ML system 
``` 

Useful when labeling expensive. 

Examples:   

``` 
Medical images
Speech
Document classification
Image classification    
``` 

### 4. Self-Supervised Learning 

In Self-supervised learning manually human labels not be requirement.   

**Model oursleves works into data constructs training signal/targets. oR Model data ke andar se training signal/targets construct krta h.** 

Example:    

Model Input:      

``` 
"The capital of India is ____"  
``` 

Model next token predict or Target automatically finds in the data.   

``` 
Delhi   
```   

So basically:     

**Data itself → creates the question and answer → model learns from it.**


Training signal makes by the data.    

Modern language-model pretraining core idea belongs these family.   

``` 
Huge raw data
      ↓
Self-supervised objective
      ↓
Neural Network
      ↓
Learn representations
      ↓
Foundation Model    
``` 

Examples of Objectives: 

``` 
Next-token prediction
Masked-token prediction
Contrastive objectives
Denoising objectives    
``` 

**Important distinction:**  

**Self-supervised ≠ unsupervised in every technical detail,** although it is often discussed under the broader unsupervised-learning umbrella.  

In modern deep learning self-supervised learning extremely important.   


### Unsupervised learning vs Self-Supervised Learning 

**Unsupervised Learning and  Self-supervised learning boths don't have output/label so, what is the main difference in boths?**     

ANswer:     

**In Unsupervised Learning they can discover into data hidden structure, Instead in Self-Supervised Learning is a method where the model creates its own learning targets from the data and learns by solving prediction tasks. or In self-Supervised Learning, the model learns from the data itself without needing manually created labels.**      

#### **Unsupervised Learning**     

Suppose we have customer data:      

| Age | Income | Spending |
| --- | ------ | -------- |
| 22  | 30k    | 15k      |
| 25  | 35k    | 20k      |
| 45  | 90k    | 80k      |
| 48  | 95k    | 85k      |

Our self donot have any target column:    

```   
Customer → ?      
```   

We can says to algorithm basically: 

**"this is a data. sees here data inside any natural structure/pattern/group exists.**    

What to do by K-Means algorithm?    

```   
Customer Data
      ↓
K-Means
      ↓
Group 1
Group 2
Group 3     
```   

Important:  

❌ We cannot here give any kind of correct answer.    

❌ We cannot says:      

```   
Customer 1 → Group A
Customer 2 → Group B    
```   

Algorithm ourselves according on the basis of Similarity/distance finds structure discovers.    

**Unsupervised Learning goal:**     

**Data understand/discover/explore.**     

#### **Self-Supervised Learning**  

Now same concepts we can sees by the LLM. 

Oursleves Sentence:     

```
I love Machine Learning 
```   

Human cannot put label maually.     

But we can ourselves after data transfer training example we can makes.    

For example:      

**Input:**  

```   
I love Machine    
```   

**Target:** 

```
Learning    
```   

Now sees that Original raw data:    

```   
I love Machine Learning 
```   

that data one part we make input and second part we makes target: 

```   
Input                 Target
--------------------------------
I                     love
I love                Machine
I love Machine        Learning      
```   

THis is self-supervised learning.   

Human cannot give any label.  

But:  

**Inside the data input-target paris automatically  creates.**    

DIfference: 

Unsupervised Learning   

```   
Input Data
    ↓
Algorithm
    ↓
Discover Structure      
```   

Example:    

```   
Customers
    ↓
K-Means
    ↓
Clusters    
```   

here is no any target.  

Self-Supervised Learning      

```   
Raw Data
    ↓
Automatically create target
    ↓
Input → Target
    ↓
Train predictive model  
```   
Example:    

```   
I love Machine Learning 
```   

Automatically:    

```   
I love Machine → Learning     
```   

Here target exist but target cannot gives by human data can automatically makes that.     

**Modern AI pipeline role**   

MOdern LLM training:    

```   
                INTERNET SCALE DATA
                        │
                        ▼
                 Raw Text / Code
                        │
                        ▼
              SELF-SUPERVISED LEARNING
                        │
                        ▼
                Next Token Prediction
                        │
                        ▼
                  FOUNDATION MODEL
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
         Fine-tuning        Preference Alignment
              │                   │
              └─────────┬─────────┘
                        ▼
                  AI Assistant      
```   

**Unsupervised Learning purpose primarily hidden patterns/structure discovers.**    

Whereas:          

**Self-Supervised Learning purpose raw unlabeled data use intelligently makes supervised-style training signal and powerful representation/models learns.**`


### 5. Reinforcement Learning - RL  

here model traditional dataset with each example cannot gives correct answer. 

Instead:    

```   
Agent
 ↓
Action
 ↓
Environment
 ↓
Reward / Penalty
 ↓
New State
 ↓
Next Action 
```   

Example:    

Game-playing AI:  

```   
Move
 ↓
Win → +Reward
Lose → -Reward    
```   

Agent goal: 

**Long-term cumulative reward maximumed.**      

COre Concepts:    

```   
State
Action
Reward
Policy
Value
Environment
Episode     
```   

Modern RL important families: 

```   
Value-based
Policy-based
Actor-Critic
Model-based RL    
```   

Algorithms: 

```   
Q-Learning
DQN
Policy Gradient
PPO
SAC   
```   

### 6. Offline Reinforcement Learning     

Modern production/Research perspective useful.  

Normal RL:  

```   
Agent
 ↕
Environment 
```   

Offline RL: 

```   
Existing historical interaction data
              ↓
          RL training   
```   


Here Agent cannot continuously experimnet do in environment.      

Useful where live epxerimentation expensive/risky:    

```   
Robotics    
Healthcare  
Recommendation    
Industrial system 
```   


### Self-Supervised + Supervised + RL - in one AI system    

MOdern AI this paradigms combines.  

Exampel Conceptual LLM training pipeline: 

```   
Massive data
   ↓
Self-Supervised Pretraining
   ↓
Foundation Model
   ↓
Supervised / instruction-style tuning
   ↓
Preference / reinforcement-based optimization
   ↓
Useful assistant model  
```   

that's why modern AI only:    

```   
Supervised  
Unsupervised      
RL    
```   

three boxes insufficent.      


### 8. Transfer Learning      

this is mostly reuse strategy as compare to learning paradigm.    

One model firstly on the huge dataset knowledge/representation learns.  

after the learning knowledge others related tasks uses.     

```   
Large Dataset
     ↓
Pretrained Model
     ↓
Transfer
     ↓
Your Dataset
     ↓
Fine-tuning / adaptation      
```   

Example:    

```   
General image model
       ↓
Medical image dataset
       ↓
Adapt
       ↓
Disease classifier      
```   

In Modern AI:     

 **Pretrained foundation model → downstream task**    


### 9. Fine-Tuning      

**Transfer learning practical form.**

OR    

**FIne tuning = ALready trained model according to their specific works we can trains our pretrained model to works our desires more effectively.**

Pretrained model: 

```   
Already learned         
```   

Then domain/task-specific data:     

```   
Your data
 ↓
Fine-tuning
 ↓
Specialized model 
```   

In LLM ecosystem: 

```   
Pretrained model
      ↓
Instruction tuning
      ↓
Domain adaptation
      ↓
Task-specific behavior  
```   

ML Example  

Suppose we have one model those trained on the millions of images.      

```   
Cats
Dogs
Cars
People
Buildings
Nature
Objects
...   
```   

Now model already:      

on the basic patterns/features images well knows.     

Our task:   

Cancer detection from X-ray images. 

Now we cannot train the model from zero point.  

```   
Pretrained Model  
(general image knowledge)     

 ↓    

Your X-ray Dataset     

  ↓   

Further Training  

 ↓    

Specialized Medical Model     
```   

This is **FIne-Tuning.**      

**LLM Example**   

One base LLM model already train from data to internet-scale:     

```   
Books
Articles
Code
Web data
Language
Knowledge   
```   

Model broadly language patterns learn.    

Now we have company dataset:  

```   
Legal documnets   
Company policies  
Customer support conversations      
```   

We can Futher train the LLM model:  

```   
Base LLM
    ↓
Your specialized dataset
    ↓
Further training
    ↓
Specialized LLM   
```   

Now the model specific domain better behaivour develops.    

##### What is Instruction Tuning?  

This is fine tuning important part. 

Base model have capability to predict the text. 

Example base training:  

```
"The capital of India is ...."      
↓
Next token prediction   
```   

BUt builds chatbots not only enough to predicts next words only.  

We can provides model to example:   

```   
Instruction:
Explain Machine Learning simply.

Good Response:
Machine Learning is...  
```   

In big amount:    

```   
Instruction → High-quality Answer   
```   

ON Example we can further training performs:    

```   
Base Model
     ↓
Instruction-response data
     ↓
Fine-Tuning
     ↓
Instruction-following Model   
```   

This is **Instruction FIne-Tuning.**      

##### Transfer Learning vs Fine-Tuning    

**Transfer Learning**   

Broad Concept / strategy      

```   
Knowledge learned in Task A
        ↓
Use in Task B     
```   

**FIne-Tuning**   

Transfer Learning is a method to implement is called FIne-tuning. 

```   
Pretrained Model
       ↓
Further training on new data
       ↓
Specialized Model 
```   

Relationship:     

```   
Transfer Learning
       │
       └── Fine-Tuning
             (one practical approach)     
```   

```   
FROM SCRATCH:

No Knowledge
    ↓
Huge Dataset
    ↓
Long Training
    ↓
Model


FINE-TUNING:

Already Trained Model
       ↓
Existing Knowledge
       +
Your Specific Data
       ↓
Small Further Training
       ↓
Specialized Model 
```   

### 10. Few-Shot & Zero-Shot Learning     

**Zero-shot**     

Model without specific examples provides tasks performs.    

```   
Model
 ↓
Instruction
 ↓
Task  
```   

**Few-shot**      

Model can provides few examples.    

```   
Example 1
Example 2
Example 3
   ↓
New input
   ↓
Prediction  
```   

In LLMs commonly **in-context learning** context discuss.   

Important:  

Few-shot/zero-shot are cannot be a separate algorithm family from traditional ML.   

this is **generalization/adaption bhevior** describe. 

### 11. Active Learning 

Suppose:    

```   
1 million unlabeled samples   
```   

Or labeling are expensive.    

Model ourselfs decides: 

"Me in 1 million which are examples doing labels by human?"       

```         
Unlabeled Data
      ↓
Model
      ↓
Most informative samples
      ↓
Human labeling
      ↓
Training    
```   

Useful when expert labeling expensive.

Examples:   

```   
Medical diagnosis
Legal documents
Scientific datasets
Computer vision   
```   

### 12. Weakly Supervised Learning        

Labels available, but:    
- Noisy dataset     
- Incomplete dataset      
- automatically generated dataset    
- approximate dataset   

Example:    

```   
Web data
 ↓
Automatically generated labels
 ↓
Noisy training signal   
```   

Useful when perfect human labels are expensive. 


### ONline/Incremental Learning     

Traditional batch ML:   

```   
Dataset
 ↓
Train
 ↓
Model 
```   

ONline Learning:  

```   
Data Stream
 ↓
Sample
 ↓
Update model
 ↓
New sample
 ↓
Update
 ↓
...   
```   

Useful for changing/streaming environments:     

```   
Fraud
Recommendations
IoT
Real-time systems 
```   

**MOdel cannot be static, incoming data with incrementally updates.**   

### 14. Federated Learning    

Instead of data collection in central server:   

```   
Device 1 ─┐
Device 2 ─┤
Device 3 ─┼→ Local Training
Device 4 ─┤
Device 5 ─┘
              ↓
       Model Updates
              ↓
       Central Aggregation    
```   

Raw data persists in devices. 

Useful where:     

```   
Privacy
Data locality
Distributed data  
```   

### 15. Contrastive Learning        

Modern representation learning in important.    

Baisc idea: 

Similar things in space we can gets close and dissimilar things we can far apart.   

Example:    

```   
Same image + augmented version
        ↓
      CLOSE

Different images
        ↓
       FAR
```   

This representation learn approach are powerful.      

Applications:     

```   
Computer Vision
Multimodal Learning
Text Embeddings
Image-Text Models
Retrieval Systems 
```   

### 16. Generative Learning   

MOdern AI context one more important distinction.     

Traditional Predictive ML:    

```   
Input → Prediction      
```   

Generative Models:      

```   
Learn data distribution
       ↓
Generate new samples    
```   

Examples:   

```   
LLMs
Diffusion models
Generative audio models
Generative video models 
```

So:   

**Generative AI, ML/DL use new content/data generates application/model family belongs.** 

```   
                    MACHINE LEARNING
                           │
       ┌───────────────────┼───────────────────┐
       │                   │                   │
   SUPERVISED          UNSUPERVISED       REINFORCEMENT
       │                   │                   │
   ┌───┴────┐        ┌─────┼──────┐       Agent
   │        │        │     │      │          ↓
Regression Classification  Clustering  Environment
                          Dimensionality      ↓
                          Reduction         Reward
                          Anomaly
       │
       └──────────────┐
                      │
              MODERN LEARNING
                      │
       ┌──────────────┼──────────────┐
       │              │              │
 Semi-Supervised  Self-Supervised  Weak-Supervised
       │
       ├── Transfer Learning
       ├── Fine-Tuning
       ├── Active Learning
       ├── Online Learning
       ├── Federated Learning
       └── Contrastive Learning     
```   


```   
Supervised Learning
    ↓
Regression
Classification

Unsupervised Learning
    ↓
Clustering
Dimensionality Reduction
Anomaly Detection

Self-Supervised Learning
    ↓
Concept + modern AI relevance

Reinforcement Learning
    ↓
Core concepts + major algorithms    
```   
```   
                    WE HAVE DATA WHICH TYPE?
                              │
             ┌────────────────┼─────────────────┐
             ↓                ↓                 ↓
        Labels exists?     Labels not?      Environment
             │                │                 │
             ↓                ↓                 ↓
        SUPERVISED       UNSUPERVISED           RL
             │                │                 │
       ┌─────┴─────┐     ┌────┼────┐            │
       ↓           ↓     ↓    ↓    ↓            ↓
 Regression  Classification Cluster  PCA      Reward
                                                ↓
                                              Policy  
```