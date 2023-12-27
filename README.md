# FraudDetection
# Objective
Online payment is the most popular transaction method in the world today. However, with an increase in online payments also comes a rise in payment fraud.Fraud detection in online payments is a multifaceted approach aimed at protecting users, businesses, and the integrity of digital financial systems.The objective of the project is to develop machine learning model for identifying fraudulent and non-fraudulent payments. The dataset is collected from Kaggle, which contains historical information about fraudulent transactions which can be used to detect fraud in online payments.

# Data
The data used in this project is from kaggle website
1. step: Represents a unit of time where 1 step equals 1 hour
2. type: type of online transaction
3. amount: The amount of the transaction
4. nameOrig: Customer initiating the transaction
5. oldbalanceOrg: balance before the transaction of the customer initiating the transaction
6. newbalanceOrig: balance after the transaction of the customer initiating the transaction
7. nameDest: recipient of the transaction
8. oldbalanceDest: initial balance of recipient before the transaction
9. newbalanceDest: the new balance of recipient after the transaction
10. isFraud: It is used to define whether a transaction is fraud or not

# Deployment
Within the python environment of yout choice run:

git clone https://github.com/Srilasya22/FraudDetection.git

pip install -r requirements.txt

# Kedro
Kedro is an open-source tool.It has the following features:

1. Handles Complexity: It provide a stucture to test data which can be pushed to production after successful testing.
 
2. Standardisation: It provides standard template for project. Making it earrlier to understand for others.
   
3. Production-Ready: Code can be easily pushed to production with exploratory code that you can transition to reproducible, maintainable, and modular experiments.

#Installing kedro

pip install kedro

#Installing kedro-viz

pip install kedro-viz

#To create new project

kedro new

#To create new pipeline

kedro pipeline create <pipeline-name>

#To run kedro

kedro run

#Visualizing pipeline

kedro viz run

# Solution
Once model is build, it can be deployed in production to track the model. Deepchecks can be used to track model performance. Using Kedro we can monitor the logs in real-time as well as old logs can also be checked.

# Training pipeline
Our standard training pipeline consists of several steps:

1. data_preprocessing: We will take the raw data and process it to standard polished data for model training.

2. train_test_split: This pipeline will split the dataset into two part. On first part the model will be trained and on second set model will be tested.

3. Scaling: Standardizing the training input and testing input
  
4. model_training: This pipeline is used to train model on dataset using hyperparameter.

5. model_evaluation: This pipeline is used to evaluate the model performance.

Below is the pipeline workflow which we will implement in this project:

![WhatsApp Image 2023-12-27 at 17 27 55](https://github.com/Srilasya22/FraudDetection/assets/113256681/b5a40593-4d25-4d00-b03a-961ab946b4aa)

# Log Analysis
Kedro can be used for log analysis as well.Here the log analysis of the project:
![WhatsApp Image 2023-12-27 at 17 59 01](https://github.com/Srilasya22/FraudDetection/assets/113256681/4f8b888d-03a7-4577-98cd-2995013f3777)


# Demo Streamlit app

There is a live demo of this project using Streamlit which you can find here. It takes some input features for the transaction and predicts whether the transaction is fraudlent or not. If you want to run this Streamlit app in your local system, you can run the following command to access the app locally:

streamlit run streamlit_app.py

![WhatsApp Image 2023-12-27 at 17 59 37](https://github.com/Srilasya22/FraudDetection/assets/113256681/f6d58368-2734-4724-a30d-be0d258d84f9)


# Model Monitoring

Model monitoring is done using DeepChecks.It is a machine learning tool for data analysis.It is used to generate reports for DataInetgrityDrift,Feature Drift and TargetDrift
