# Machine Learning Fundamentals 

### What is Machine Learning?   

Machine Learning are approach where we cannot in computer explicit rules in every situation defines instead of this we can do patterns learns, our model must be unseen/new data prediction or takes decision.  

Traditional Programming:    

```     
Rules + Data
    ↓
 Program
    ↓
 Output
``` 

Machine Learning:   

```
Data + Correct Answers
        ↓
      ML Algorithm
        ↓
       Model
        ↓
      New Data
        ↓
    Prediction  
``` 

Example — Spam Detection    

In Traditional Programming: 

``` 
if message contains "free money":   
   spam 
``` 

Just like this we can defines manually hundreds/thousands rules.    

But in ML:  

``` 
Old Emails  
    ↓   
Spam / Not Spam labels  
    ↓   
ML Algorithm    
    ↓   
Trained Model   
    ↓   
New Email   
    ↓   
Spam Probability = 0.94 
``` 

model ourselves data useful patterns learns.    

### Algorithm vs Model  

**Algorithm**   

Learning method/process.    

Examples:   

``` 
Linear Regression   
Decision Tree   
Random Forest   
Logistic Regression 
XGBoost 
``` 

**Model**   

After the learned model by the help of ALgorithm training data we gets learned parameters/patterns that's called as trained model.  

Example:    

``` 
Linear Regression ALgorithm 
          +
     Training Data  
          ↓
    Learned Model   
``` 

If Same algorithm different dataset we can trained, so different learned model can we gets. 

### ML Core Flow    

``` 
Data
 ↓
Patterns
 ↓
Parameters
 ↓
Prediction
 ↓
Error
 ↓
Optimization    
```

SOme Expands :  

``` 
Raw Data
   ↓
Data Preparation
   ↓
Features + Target
   ↓
Algorithm
   ↓
Parameters
   ↓
Prediction
   ↓
Loss / Error
   ↓
Optimization
   ↓
Updated Parameters
   ↓
Repeat
   ↓
Trained Model
   ↓
New / Unseen Data
   ↓
Prediction  
``` 

### Data    

Model have information. 

Suppose we do house price prediction.   

| Area | Bedrooms | Location | Price |
| ---: | -------: | -------- | ----: |
| 1000 |        2 | Delhi    |   50L |
| 1500 |        3 | Delhi    |   75L |
| 2000 |        4 | Delhi    |   1Cr |
| 2500 |        4 | Delhi    | 1.3Cr |

Here:   

**Features**    

``` 
Area    
Bedrooms    
Location    
``` 

**Target** 

``` 
Price   
``` 

Models uses features to predicts their target.  

``` 
Features
   ↓
 ML Model
   ↓
Predicted Price 
``` 

### Patterns    

Model in between dataset(Data) identify relationships/patterns. 

Example:    

``` 
Area ↑
   ↓
Price generally ↑   
``` 

Or: 

``` 
Bedrooms ↑
   ↓
Price generally ↑   
``` 

MOdel actually learns these things: 

**"INput and Output in between relationship?"** 

Important:  

Model cannot understand just like "human" they can learns by mathematical/statistical patterns. 

### Parameters  

In Model some values those learns data in during the process of training.   

Linear Regression example:  

y=β0​+β1​x  

Suppose after training: 

y=10+0.05x  

here:   

``` 
β₀ = 10
β₁ = 0.05   
``` 
 
these parameters β₀, β₁ model learns data from these values.    

Simple meaning: **Parameters = MOdel Learned values.**  

### Prediction  

NOw trained model we get new data.  

Suppose:    

``` 
Area = 2000 sq ft
``` 

Model:  

``` 
y = 10 + 0.05(2000)

y = 110 
``` 

Model predicted Price:  

``` 
110 
``` 

Actual price may be:    

``` 
105 
``` 

NOw the time predicted value and acutal value have difference.  

### Error / Loss    

Prediction: 

``` 
110
``` 

Actual: 

``` 
105 
``` 

Difference: 

``` 
110 - 105 = 5   
``` 

This is error.  

ML model objective broadly seems:   

**Prediction value gets more closes to actual values.** 

that time we can use the **Loss Function**  

Example:    

**Mean Squared Error**  

MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2  

Here:   

- $y_i$ = actual value
- $\hat{y}_i$ = predicted value  

### Optimization  

Model our parameters repeadtedly adjusts because of they gets reduce the loss.   

Example: 

```   
Initial parameter
      ↓
Prediction
      ↓
Loss = HIGH
      ↓
Parameter update
      ↓
Prediction
      ↓
Loss = LOWER
      ↓
Parameter update
      ↓
...
      ↓
Loss minimized 
```   

This learning process **optimzation** role occurs. 

In Linear models **Gradient Descent** very important optimization technique.  

Concept: 

```   
Loss
 ↑
 |\
 | \
 |  \
 |   \____
 |        \___
 +----------------→ Parameters   
 ```  


### SO, What actually learns Model? 

Machine learning model by training data parameters learns and those parameters input features and target relationship represents.   

Training:   

```   
Data
 ↓
Prediction
 ↓
Loss
 ↓
Optimization
 ↓
Parameter Update
 ↓
Prediction
 ↓
Loss
 ↓
...   
```   

this process repeatedly works.

Finally: 

```   
Learned Parameters
        ↓
   Trained Model  
```   

### Training vs Inference  

**Training**   

Model that learns from  data. 

```   
Training Data
     ↓
   Model
     ↓
Parameters Learn  
```   

**Inference**  

Already trained model through on new data predictions performs.   

```   
New Data
   ↓
Trained Model
   ↓
Prediction  
```   

Example: 

Fraud model trains:  

```   
1 million historical transactions
        ↓
       Train
        ↓
    Fraud Model
```   

NOw customer have new transaction:  

```   
New Transaction
      ↓
Trained Model
      ↓
Fraud Probability = 0.97   
```   

that is inference.   


### Generalization   

MOdel goal not only training data memoraized.   

Goal: 

**model performs also good at unseen data.** 

Example: 

Training data: 

```   
100,000 transactions 
```   

Model training accuracy:   

```   
99.9%
```   

But on new transactions:   

```   
65%   
```   

that time model not be great. 

Model training data can overfit. 

**Good ML model:**   

```   
Training Data
      ↓
Learning
      ↓
General Pattern
      ↓
Unseen Data
      ↓
Good Prediction   
```

that is **generalization**.   


### Overfitting vs Underfitting  

**Underfitting**  

Model pattern properly not be learns.

```   
Too Simple
   ↓
Poor Training Performance
   ↓
Poor Test Performance   
```   

**Overfitting**   

Model training data patterns/noise excessively fits.  

```   
Too Complex
   ↓
Excellent Training Performance
   ↓
Poor Test Performance   
```   

**Ideal**   

```   
Enough Complexity
       ↓
Good Training
       +
Good Generalization  
```   

### AI vs ML vs Deep Learning 

**Artifical Intelligence — AI**  

```   
                         ARTIFICIAL INTELLIGENCE
                                  │
             ┌────────────────────┼────────────────────┐
             │                    │                    │
       Classical AI          Machine Learning       Other AI
             │                    │
      ┌──────┼──────┐       ┌─────┼──────────┐
      │      │      │       │     │          │
    Rules  Search  Planning  Supervised  Unsupervised
                              │
                              └── Reinforcement Learning
                                     
                         Machine Learning
                              │
                              ▼
                       Deep Learning
                              │
                     Neural Networks
                              │
              ┌───────────────┼────────────────┐
              │               │                │
             CNN          Transformers       Other architectures
                              │
                    ┌─────────┴─────────┐
                    │                   │
                   NLP              Multimodal AI
                    │
                    ▼
             Language Models
                    │
                    ▼
              Foundation Models
                    │
          ┌─────────┴──────────┐
          │                    │
     Generative AI        Embodied/other AI
          │
     ┌────┴─────────┐
     │              │
   LLMs         Image/Audio/Video
     │
     ▼
   AI Systems / Applications
     │
     ├── RAG
     ├── Tool Calling
     ├── Workflows
     ├── Agents
     └── Agentic AI Systems   
```   

#### 1. AI - Artificial Intelligence   

**AI - broadest field.**   

Goal: 

Machines makes like systems those performs tasks like need traditionally human-like intelligence, reasoning, perception, learning, planing or decision-making. 

AI has differnet approaches : 

```   
AI
├── Rule-based reasoning
├── Search
├── Planning
├── Optimization
├── Machine Learning
└── Hybrid AI systems   
```   

Modern AI has ML/DL dominant approachs, but AI = ML not. 

#### 2. ML - Machine Learning 

ML AI data-driven learning approach.   

Instead of manually programming every rule:  

```   
Data
 ↓
Learning algorithm
 ↓
Learned model
 ↓
Prediction / decision   
```   

Examples:   

- Fraud detection.
- Credit risk. 
- Customer churn. 
- Recommendation. 
- Demand forecasting.   
- Price Prediction.  

IMportant algorithms:   

```   
Linear Regression
Logistic Regression
Decision Trees
Random Forest
XGBoost
LightGBM
CatBoost
SVM
K-Means
PCA   
```

Current time Classical ML not dead Especially structred/tabular business data in tree ensembles/boosting extremely relevent.  

#### 3. DL - Deep Learning  

Deep Learning = ML subset. 

```   
AI
 └── ML
      └── Deep Learning 
```   

Deep learning primarily muti-layer neural networks through complex representations learns data. 

Traditional ML:   

```   
Data
 ↓
Human-designed features
 ↓
ML model 
```   

Deep Learning often: 

```   
Raw / less-processed data
 ↓
Neural Network
 ↓
Learned representations
 ↓
Prediction / generation 
```   

Major architectures: 

```   
CNN
RNN / LSTM
Transformers
Autoencoders
Diffusion architectures 
```   

In modern time transformers particulary important. 


#### 4. NLP - Natural Language Processing 

**NLP cannot be ML algorithm.**  

NLP are application/research domain.   

GOal: 

Human language process, understand, analyze or generates.   

NLP problems:  

```  
Text classification
Sentiment analysis
Translation
Information extraction
Question answering
Summarization
Speech-language tasks
Text generation   
```   

NLP can do by traditionally classical ML: 

```   
TF-IDF
Naive Bayes
Logistic Regression
SVM   
```   

After by Deep Learning: 

```   
RNN
LSTM
CNN   
```   

After that Modern NLP:  

```   
Transformers
        ↓
Foundation Models
        ↓
LLMs  
```   

So:   

```   
NLP
  ├── Classical ML
  ├── Deep Learning
  └── Transformers / Foundation Models 
```   

#### 5. Foundation Model   

this is very important for understand modern AI.   

foundation model are large model that's on broad data pre-trained or that adapts or uses by different downstream tasks/applications.   

Examples of modalities: 

```
Text
Image
Audio
Video
Code
Multimodal  
```   

LLM foundation models are one important category, but **every foundation model is not an LLM.** 


#### 6. Generative AI   

Generative AI focus: 

**New content/data generates.**  

Examples:   

```   
Text
Images
Audio
Video
Code
Synthetic data 
```   

Traditional predictive ML: 

```   
Customer data
      ↓
Will customer churn?
      ↓
Prediction  
```   

Generative AI: 

```   
Prompt
 ↓
Model
 ↓
Generate new content 
```   

Modern GenAI major model families:  

```   
LLMs
Diffusion models
Generative multimodal models
Generative audio/video models 
```   

Therefore:  

```   
Generative AI ≠ LLM only   
```   

**LLM are one major part of generative AI.** 


#### 7. LLM - Large Language Model  

LLM = large language model trained on huge amounts of language/code and related data to model and generate language. 

MOdern LLMs mostly use **Transformer-based architectures.** 

Conceptually:  

```   
Text
 ↓
Tokens
 ↓
Embeddings
 ↓
Transformer
 ↓
Contextual representations
 ↓
Next-token / generation process
 ↓
Output   
```   

LLMs enable:   

```   
Chat
Reasoning
Coding
Summarization
Translation
Extraction
Question answering
Tool use 
```   

But:

**LLM ≠ complete AI application.**  

LLM only system model/component. 

#### 8. Tool Calling/Function Calling  

Modern AI Engineering important part.  

LLM external tools provides.  

```   
LLM
 │
 ├── Calculator
 ├── Database
 ├── Search
 ├── API
 ├── Code execution
 └── Business systems   
```  

Example: 

User: 

"What is My Account current balance."

LLM cannot be ourselfs balance invent. 

Instead: 

```   
User
 ↓
LLM
 ↓
Tool call
 ↓
Bank API
 ↓
Result
 ↓
LLM
 ↓
Answer   
```   

this is modern AI application fundamental pattern. 


#### 9. RAG - Retrieval-Augmented Generation 

this is also not LLM itself.  

problem: 

LLM cannot your private/latest information let be know ourself.   

RAG:  

```   
User Question
      ↓
Retriever
      ↓
Relevant Documents
      ↓
Context
      ↓
LLM
      ↓
Answer   
```   

Example: 

Company have 10,000 internal documents.   

```   
Question
   ↓
Search relevant chunks
   ↓
Give chunks to LLM
   ↓
Generate grounded answer   
```   

Typical components:  

```   
Documents
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector / hybrid retrieval
 ↓
Reranking
 ↓
Context
 ↓
LLM   
```   

Modern production in RAG only "vector DB + LLM" thinking is insufficient, retrieval quality, reranking, grounding or evaluation also important. 

#### 10. Agent 

Confusion:  

**Agent ≠ chatbot.** 

A simple LLM chatbot:   

```
User
 ↓
LLM
 ↓
Answer   
```   

Agent:   

```   
Goal
 ↓
LLM / reasoning model
 ↓
Decide next action
 ↓
Tool
 ↓
Observe result
 ↓
Decide next action
 ↓
Tool
 ↓
...
 ↓
Final result   
```   

Agent important components:   

```   
Model
+
Instructions
+
Tools
+
State / context
+
Decision / control loop
+
Possibly memory
+
Guardrails  
```   

Example: 

"For my trip to find Delhi to mumbai cheapest flight with suitable option."   

Agent potentially:   

```   
Understand goal
      ↓
Search flight API
      ↓
Compare results
      ↓
Check constraints
      ↓
Maybe search again
      ↓
Return recommendation   
```   

#### 11. Agentic AI  

Now Agent vs Agentic AI.   

**Agent**   

One particular system/component do: 

**To Achieve a goal by reasoning/decision + tools/actions use that things.**  

**Agentic AI** 

Broader system design/paradigm where AI systems goals purse to do, plan, act, observe or adapt greater autonomy.  

Simple Difference:   

```   
Agent
↓
Individual AI worker/system
↓
Agentic AI
↓
Autonomous goal-oriented AI system/design 
```   

In Agentic System have multiple agents:   

```   
                    Agentic System
                          │
             ┌────────────┼────────────┐
             ↓            ↓            ↓
          Planner       Researcher    Executor
             │            │            │
             └────────────┼────────────┘
                          ↓
                       Tools
                          ↓
                    Environment
                          ↓
                     Observation
                          ↓
                      Next Action   
```   

#### 12. Traditional ML vs DL vs GenAI vs Agents

| Technology           | Main Purpose                                                          | Example                            |
| -------------------- | --------------------------------------------------------------------- | ---------------------------------- |
| **AI**               | Making machines act intelligently                                     | Planning system                    |
| **ML**               | Learning patterns from data                                           | Fraud prediction                   |
| **DL**               | Learning complex patterns using neural networks                       | Image recognition                  |
| **NLP**              | Understanding and working with human language                         | Text classification                |
| **Foundation Model** | A large model trained on lots of data that can be used for many tasks | Large language or multimodal model |
| **Generative AI**    | Creating new content                                                  | Text, image, or video generation   |
| **LLM**              | Understanding and generating text and code                            | Chat or coding model               |
| **RAG**              | Getting information from external sources before generating an answer | Company document Q&A               |
| **Tool Calling**     | Allowing a model to use external tools or APIs                        | Calling a weather API              |
| **Agent**            | AI that uses reasoning and tools to complete a goal                   | Research agent                     |
| **Agentic AI**       | AI systems that can plan and perform multiple steps to achieve a goal | Automated business workflow        |


**AI → ML → DL → Foundation Models → GenAI/LLMs → RAG → Tool Calling → Agents → Agentic AI**    


#### Real modern AI architecture    

Suppose we are **AI Finance Assistant**   

User: 

"My last 6 months expenses analyze can explain me where is unnecesaary spending or suggests me saving plan" 

System:     

```
                         USER
                           │
                           ▼
                    AI APPLICATION
                           │
                           ▼
                     LLM / MODEL
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
           Database       RAG        Tools/APIs
              │            │            │
              └────────────┼────────────┘
                           ▼
                     Reason / Plan
                           │
                           ▼
                       Actions
                           │
                           ▼
                     Final Answer   
```   

Here in this :    

- **AI** = entire intelligent system.     
- **ML/DL** = MOdels underlying learning approaches.  
- **LLM** = Language/reasoning component. 
- **NLP** = Language processing capability/domain.    
- **GenAI** = generated explanation/content.    
- **RAG** = External knowledge retrieval. 
- **Tool calling** = database/API access. 
- **Agent** = Multi-step goal/action loop.      
- **Agentic AI** = broader autonomous workflow/system.