# Mini-project IV: Loan Approval Model with Deployment

### [Assignment](assignment.md)

## Project/Goals
Create a model that accurately mimics loan application judgements and deploy it with flask.

## Hypothesis
If loan approval depends on an applicants ability to repay the loan then the most important features will be combined applicant income and credit history. 

## EDA 
EDA revealed a few important characteristics in the dataset:
- Target variable: 69% of loans were approved
- Income was low (7k) and was heavily right-skewed. 
- Loan amount was slightly right-skewed, but near-normal upon logorithmic transformation. 
- No features were highly correlated with the target variable or each other.  Only semi-urban property areas and having exactly 2 dependents were slightly positively correlated. 


## Process
1. Hypothesis Generation
2. EDA (explore, clean, and wrangle)
3. Build Predictive Models
4. Create a Pipeline for best model (RFC)
5. Deploy Model

## Results/Demo
A Random Forest Classifier hyperparameterized with gridsearch CV was put into a pipeline and performed as follows: 
77%  Accuracy
81%  Precision
68%  Recall
69%  F1



## Challanges 
Deploying the project was the largest challenge.  Followed by throttling my model to fit my CPU. 

## Future Goals
- Improve the API
- Improve feature engineering and class imbalance