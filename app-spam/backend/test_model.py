# import pickle

# with open("models/spam_model.pkl", "rb") as f:
#     model = pickle.load(f)

# sample = [
#     "Congratulations! You have won a free iPhone. Click here to claim your prize."
# ]

# prediction = model.predict(sample)

# print(prediction)

# print(model.best_estimator_)


# sample = "Congratulations! You have won a free iPhone."

# print(model.predict([sample]))

# tests/test_sentiment.py

import pickle
from utils.preprocessing import preprocess_text

with open(
    "models/model.pkl",
    "rb"
) as f:

    model = pickle.load(f)

text = "This product is absolutely amazing"

clean_text = preprocess_text(text)

print(model.predict([clean_text]))
y=lambda x: 'Postive Sentiment' if model.predict(x)==1 else 'Negative Sentiment'
print(y(["This product is absolutely amazing"]))



print(
    model.predict(
        ["This product is absolutely amazing"]
    )
)