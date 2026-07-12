import streamlit as st
from prediction import prediction

st.title("# Hello, welcome to the NLP app!")
st.write("This app allows you to perform various NLP tasks using the spaCy library\
            gggggggggg"
         )
st.write("If Spam, the email is like spam 🛑, else it's not spam.❎")

# 1. Create a multi-line text box for the client's email
email_content = st.text_area(
    "Paste Client Email:",
    height=200,
    placeholder="Type or paste the client's email here..."
)

# 2. Button to trigger the prediction
if st.button("Predict Email"):
    if email_content.strip() == "":
        st.warning("Please enter some email text before predicting.")
    else:
        # Placeholder for your actual machine learning model or API call
        # prediction = my_model.predict([email_content])
        prediction = prediction([email_content])
        st.success("Prediction complete!")
        st.write(f"Predicted Category: {prediction}")
        st.write("Display prediction results here...")
