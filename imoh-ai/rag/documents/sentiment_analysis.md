# Sentiment Analysis

## Status

Complete

---

## Overview

The Sentiment Analysis project is a Natural Language Processing (NLP) application that classifies customer reviews as either positive or negative. The project demonstrates how unstructured text data can be transformed into meaningful numerical features and used to train a supervised machine learning model capable of accurately predicting sentiment.

The trained model is deployed through a Flask API and integrated into a React frontend, allowing users to submit reviews and receive sentiment predictions in real time.

---

## Objective

The objective of this project was to build a complete end-to-end machine learning solution for sentiment classification while demonstrating best practices in text preprocessing, feature engineering, model optimisation and deployment.

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
- Sentiment classification
- Hyperparameter optimisation using GridSearchCV
- Scikit-learn Pipeline
- REST API integration
- Interactive web interface

---

## Technical Implementation

Customer reviews were cleaned and preprocessed using spaCy to standardise the text before feature extraction. The preprocessing pipeline included tokenisation, lemmatization and removal of stop words to reduce noise while preserving meaningful information.

The processed text was transformed into numerical features using TF-IDF Vectorisation before being passed to a supervised machine learning classifier. Hyperparameter tuning was performed using GridSearchCV within a Scikit-learn Pipeline to optimise model performance while ensuring a reproducible workflow.

After training, the model was deployed through a Flask API and connected to a React frontend to provide real-time sentiment predictions.

---

## Challenges & Solutions

### Processing Unstructured Text

Customer reviews often contain inconsistent grammar, punctuation and vocabulary. A consistent preprocessing pipeline was implemented to improve feature quality before model training.

### Feature Engineering

TF-IDF Vectorisation was selected to convert textual information into numerical features that capture the relative importance of words across the dataset.

### Model Deployment

The preprocessing and prediction steps were encapsulated within a Scikit-learn Pipeline to ensure identical processing during both training and inference.

---

## Skills Demonstrated

- Natural Language Processing
- Sentiment Analysis
- Machine Learning
- Text Classification
- Feature Engineering
- Pipeline Development
- Model Optimisation
- Flask
- React
- Python
- Scikit-learn
- spaCy
- Git

---

## Outcome

The project demonstrates the complete machine learning lifecycle for text classification, including data preprocessing, feature engineering, model optimisation and deployment within a full-stack web application. It showcases practical experience in building scalable NLP solutions capable of analysing customer sentiment in real time.
