# Medical Insurance Cost Predictor

## Status

Complete

---

## Overview

The Medical Insurance Cost Predictor is a supervised machine learning application that estimates an individual's medical insurance charges based on demographic and lifestyle information. The project demonstrates an end-to-end regression workflow, including data preprocessing, feature engineering, model training, evaluation and deployment within a full-stack web application.

The trained model is deployed through a Flask API and integrated into a React frontend, allowing users to enter their information and receive estimated insurance charges in real time.

---

## Objective

The objective of this project was to develop a robust regression model capable of predicting medical insurance costs while demonstrating best practices in data preprocessing, machine learning pipeline development and model deployment.

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
- Missing value handling
- Feature scaling
- One-Hot Encoding
- ColumnTransformer pipeline
- Random Forest Regression
- Target transformation
- Real-time predictions
- REST API integration
- Interactive web interface

---

## Technical Implementation

The project uses demographic and lifestyle variables including age, sex, body mass index (BMI), number of children, smoking status and geographical region to estimate medical insurance charges.

Categorical variables are transformed using One-Hot Encoding, while numerical variables are standardised using feature scaling. These preprocessing steps are combined using a Scikit-learn ColumnTransformer to ensure consistent processing during both training and prediction.

The transformed features are used to train a Random Forest Regressor. To improve prediction performance and reduce the impact of the skewed target distribution, the model is wrapped within a TransformedTargetRegressor using a QuantileTransformer.

After training, the complete pipeline is deployed through a Flask API and connected to a React frontend, allowing users to receive instant insurance cost estimates.

---

## Challenges & Solutions

### Mixed Data Types

The dataset contains both numerical and categorical variables. A ColumnTransformer was implemented to apply the appropriate preprocessing technique to each feature type within a single reusable pipeline.

### Skewed Target Variable

Medical insurance charges exhibit a highly skewed distribution. A QuantileTransformer was applied to the target variable using a TransformedTargetRegressor to improve model performance and produce more stable predictions.

### Consistent Deployment

The preprocessing pipeline and regression model were packaged together to ensure that new user inputs are transformed in exactly the same way as the training data.

---

## Skills Demonstrated

- Regression Modelling
- Feature Engineering
- Data Preprocessing
- ColumnTransformer
- Random Forest Regression
- Target Transformation
- Scikit-learn Pipelines
- Flask API Development
- React Integration
- Python
- Model Deployment
- Git

---

## Outcome

The project successfully demonstrates the complete supervised machine learning workflow for a regression problem, from data preparation and feature engineering to deployment within a full-stack web application. It showcases practical experience in building maintainable machine learning pipelines capable of generating real-time predictions.

---

## Why This Project Matters

This project demonstrates my ability to work with structured tabular data and develop regression models for real-world prediction tasks. It highlights my understanding of preprocessing mixed data types, building reusable machine learning pipelines and deploying predictive models as interactive web applications. Together with my NLP projects, it showcases experience across multiple machine learning problem domains.
