# Multi-Model Language Detection Pipeline with Ensemble Learning

A robust Natural Language Processing (NLP) system that automatically detects text languages. This project demonstrates an end-to-end Machine Learning workflow, implementing iterative model selection, hyperparameter tuning, and advanced ensemble methods to achieve high-accuracy language classification.

##  Key Features & Workflow
1. **Feature Extraction:** Implements `TfidfVectorizer` to convert raw text into high-quality numerical features.
2. **Automated Pipeline:** Utilizes Scikit-Learn `Pipeline` to chain preprocessing and model training cleanly, preventing data leakage.
3. **Iterative Model Selection:** Leverages `GridSearchCV` to optimize and evaluate **5 competing machine learning algorithms**:
   * Logistic Regression
   * Linear Support Vector Classification (LinearSVC)
   * Stochastic Gradient Descent Classifier (SGDClassifier)
   * Extra Trees Classifier
   * Complement Naive Bayes (ComplementNB)
4. **Ensemble Learning:** Passes the optimized individual models into a `VotingClassifier` to create a powerful, high-performance majority-vote ensemble system.

---

##  Core Skills Demonstrated

This project showcases production-level machine learning engineering and data science skills:

* **Advanced NLP Pipeline Architecture:** Expertise in text preprocessing, TF-IDF vectorization, and building leak-proof ML pipelines.
* **Hyperparameter Optimization:** Deep understanding of `GridSearchCV` for exhaustive search over specified parameter grids to maximize model performance.
* **Ensemble Modeling:** Proficiency in advanced model combining techniques (Voting/Stacking Classifiers) to reduce variance and boost prediction stability.
* **Algorithm Evaluation & Benchmarking:** Hands-on experience in comparing multiple diverse mathematical classifiers (linear, tree-based, and probabilistic models) under the same constraints.
* **Clean Code & Scalability:** Structured, modular engineering principles using Scikit-Learn best practices, making the codebase highly reusable.

---

##  Project Structure

```text
├── c-language_detector/
│   ├── models/                # Saved/Serialized model ( .joblib)
│   ├── src/
│   │   ├── train.py           # Pipeline, GridSearch, and VotingClassifier implementation
│   │   └── predict.py         # Inference script for testing new text input
├── .gitattributes             # Git LFS configuration for large model tracking
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

---

## ⚙️ Installation & Usage

### 1. Clone the Repository (With Git LFS)
Since this repository contains large pre-trained model binaries, ensure you have **Git LFS** installed before cloning:
```bash
git clone https://github.com
cd test_repo
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Training (GridSearch + Voting)
```bash
python c-language_detector/src/train.py
```
