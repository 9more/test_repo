# Email Threat Detection

## Overview

Email Threat Detection is a machine learning application that classifies incoming emails into one of three categories:

- Ham
- Spam
- Phishing

The project demonstrates an end-to-end machine learning workflow, from model development and evaluation to deployment as an interactive web application.

---

## Technologies

- Python
- Scikit-learn
- Flask
- React
- Joblib
- Git

---

## Model Development

During model experimentation, several preprocessing approaches were evaluated, including spaCy-based text normalisation and tokenisation.

The final deployed model was retrained using a Scikit-learn Pipeline that encapsulates all required preprocessing and feature extraction within the model itself. This simplified deployment by removing the need for a separate preprocessing stage during inference while ensuring that the same transformations used during training are automatically applied to new inputs.

## Machine Learning Pipeline

The deployed model is built as a Scikit-learn Pipeline that combines text vectorisation and classification into a single reusable workflow.

Pipeline:

TF-IDF Vectorizer

↓

Linear Support Vector Classifier (LinearSVC)

Because preprocessing is embedded within the trained pipeline, the deployed application performs prediction using a single model object without requiring separate preprocessing logic.

---

## Features

- Three-class classification
- Ham detection
- Spam detection
- Phishing detection
- Real-time inference
- REST API deployment
- Interactive web interface

---

## Skills Demonstrated

- Natural Language Processing
- Text Classification
- Feature Engineering
- Machine Learning Pipelines
- Model Deployment
- Flask API Development
- Frontend/Backend Integration

---

## Future Improvements

- Confidence scores
- Explainable AI
- Transformer-based classifiers
- Larger multilingual datasets
