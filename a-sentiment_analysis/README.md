# Amazon Reviews Sentiment Analysis with NLP and Machine Learning

Link to my repo containing other data science projects:

https://github.com/9more/Spam-Filtering
https://github.com/9more/Diabetes-Detection-
https://github.com/9more/test_repo
# Project Overview
This project analyses customer reviews from the Kaggle Amazon Reviews dataset to predict sentiment using Natural Language Processing (NLP) and machine learning. The objective is to transform unstructured text into meaningful numerical features and build an optimised classification pipeline for accurate sentiment prediction.

The project demonstrates expertise in data preprocessing, NLP, feature engineering, machine learning, and pipeline automation.

## Dataset

The dataset contains customer review text, sentiment labels, review ratings, and product metadata where available.

## Technical Stack

Python
Pandas
NumPy
Scikit-learn
Jupyter Notebook
Workflow

## Data Ingestion and Preprocessing

Raw CSV files were processed and cleaned using Pandas to ensure data quality. Key steps included:

Handling malformed records and inconsistent formatting
Removing duplicates
Managing missing values
Standardising text encoding
Cleaning and normalising review text
Natural Language Processing

Text preprocessing included:

** Lowercasing
** Removing punctuation and special characters
** Stop-word removal
** Tokenisation
** Text normalisation
** Feature Engineering

Review text was transformed into machine-readable features using:

CountVectorizer for token frequency extraction
TF-IDF to weight terms by importance across the corpus
Machine Learning Pipeline

An end-to-end Scikit-learn pipeline automated preprocessing, feature extraction, model training, and evaluation.

Models evaluated:

Random Forest Classifier
Support Vector Machine (SVM)
K-Nearest Neighbours (KNN)
Hyperparameter Optimisation

GridSearchCV was used to optimise vectorisation settings and model hyperparameters, with model performance assessed using cross-validation, F1-score, and confusion matrices.

## Key Skills Demonstrated

Natural Language Processing (NLP)
Text Classification
CountVectorizer and TF-IDF
Scikit-learn Pipelines
GridSearchCV
Feature Engineering
Data Cleaning and Preprocessing
Model Evaluation
Future Improvements

Implement Word2Vec, GloVe, or transformer models such as BERT
Deploy the model as an API
Build an interactive sentiment analysis dashboard
Add experiment tracking and model versioning
Author

Developed as a portfolio project focused on extracting actionable insights from customer feedback at scale.
