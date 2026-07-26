# Spam Email Detection

## Status

Complete

---

## Overview

The Spam Email Detection project is a machine learning application that classifies emails as either spam or legitimate (ham) using Natural Language Processing (NLP) techniques. The project demonstrates the complete machine learning lifecycle, from data preprocessing and feature engineering to model training, evaluation and deployment through a web application.

The trained model is integrated into a Flask backend and can be accessed through a React frontend, allowing users to classify email messages in real time.

---

## Objective

The objective of this project was to develop an accurate and reusable machine learning pipeline capable of automatically detecting spam emails while demonstrating best practices in text preprocessing, feature engineering, model optimisation and deployment.

---

## Technologies

### Programming

- Python

### Machine Learning

- Scikit-learn
- spaCy

### Deployment

- Flask
- React

### Development Tools

- Git
- Jupyter Notebook

---

## Key Features

- Text preprocessing
- Tokenisation
- Lemmatization
- Stop-word removal
- TF-IDF Vectorisation
- Linear Support Vector Classifier (LinearSVC)
- Hyperparameter optimisation using GridSearchCV
- Scikit-learn Pipeline
- Real-time prediction
- REST API integration
- Interactive web interface

---

## Technical Implementation

The project begins by cleaning and preprocessing raw email text using spaCy. The preprocessing pipeline removes unnecessary characters, tokenises text, performs lemmatization and removes stop words to improve the quality of the extracted features.

The processed text is transformed into numerical representations using TF-IDF Vectorisation before being passed to a Linear Support Vector Classifier. Hyperparameters were optimised using GridSearchCV within a Scikit-learn Pipeline to ensure preprocessing and model training remained reproducible and efficient.

Once trained, the model was saved and deployed through a Flask API, enabling predictions from a React-based web interface.

---

## Challenges & Solutions

### Text Preprocessing

Selecting appropriate preprocessing techniques required balancing simplicity with predictive performance. spaCy was used to create a consistent preprocessing workflow that could be reused during both training and prediction.

### Model Optimisation

Different model configurations were evaluated using GridSearchCV to identify the combination of parameters that produced the best classification performance.

### Deployment

To ensure predictions remained consistent between development and production, the preprocessing and classification steps were combined into a single Scikit-learn Pipeline before deployment.

---

## Skills Demonstrated

- Natural Language Processing
- Machine Learning
- Text Classification
- Feature Engineering
- Pipeline Development
- Model Optimisation
- API Development
- Flask
- React
- Python
- Scikit-learn
- spaCy
- Git

---

## Outcome

The project successfully demonstrates an end-to-end machine learning workflow, covering data preparation, feature extraction, model training, optimisation and deployment within a full-stack application. It highlights the ability to develop production-ready machine learning solutions using reusable and maintainable workflows.
