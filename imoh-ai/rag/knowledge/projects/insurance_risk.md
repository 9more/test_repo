# Insurance Risk Classifier

## Status

Complete

---

## Overview

The Insurance Risk Classifier is a supervised machine learning application that predicts an individual's insurance risk category using demographic and lifestyle information. The project demonstrates the complete workflow for a classification problem, including data preprocessing, feature engineering, model development and deployment within a full-stack application.

The trained model is deployed through a Flask API and integrated into a React frontend, allowing users to submit their information and receive an instant insurance risk assessment.

---

## Objective

The objective of this project was to develop a reliable classification model capable of predicting insurance risk while demonstrating best practices in structured data preprocessing, machine learning pipeline development and deployment.

---

## Technologies

### Programming

- Python

### Machine Learning

- Scikit-learn

### Deployment

- Flask
- React

### Development Tools

- Git
- Jupyter Notebook

---

## Key Features

- Data preprocessing
- Feature scaling
- One-Hot Encoding
- ColumnTransformer pipeline
- Logistic Regression
- Probability prediction
- Real-time classification
- REST API integration
- Interactive web interface

---

## Technical Implementation

The application uses demographic and lifestyle information, including age, sex, body mass index (BMI), number of children, smoking status and geographical region, to classify individuals into insurance risk categories.

Categorical variables are transformed using One-Hot Encoding, while numerical variables are standardised using feature scaling. These preprocessing steps are managed using a Scikit-learn ColumnTransformer to ensure consistent feature preparation during both training and prediction.

A Logistic Regression classifier was trained using the processed features to predict the appropriate insurance risk category. The complete preprocessing and modelling workflow was encapsulated within a Scikit-learn Pipeline before deployment.

The trained model was integrated into a Flask API and connected to a React frontend, enabling users to obtain real-time insurance risk predictions through a simple web interface.

---

## Challenges & Solutions

### Mixed Feature Types

The dataset contains both categorical and numerical variables. A ColumnTransformer was used to apply the correct preprocessing technique to each feature while maintaining a single reusable workflow.

### Consistent Predictions

To eliminate differences between training and production data, preprocessing and classification were combined into a single Scikit-learn Pipeline.

### Model Deployment

The trained pipeline was serialised and deployed through a Flask API, ensuring efficient and reliable prediction within the web application.

---

## Skills Demonstrated

- Classification Modelling
- Logistic Regression
- Feature Engineering
- Data Preprocessing
- ColumnTransformer
- Scikit-learn Pipelines
- Machine Learning
- Flask API Development
- React Integration
- Python
- Model Deployment
- Git

---

## Outcome

The project successfully demonstrates the complete machine learning lifecycle for a structured data classification problem, from preprocessing and model development to deployment within a full-stack application. It highlights the ability to build maintainable and reusable machine learning solutions capable of supporting real-time decision making.

---

## Why This Project Matters

This project demonstrates my ability to solve classification problems using structured data and complements my regression and NLP projects. It highlights my understanding of feature engineering, reusable machine learning pipelines and full-stack deployment, showcasing versatility across multiple machine learning domains.
