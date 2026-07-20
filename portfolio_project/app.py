from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="ML Portfolio | Imoh Ekpenyong",
    page_icon="🧠",
    layout="wide",
)

MODELS_DIR = Path(__file__).parent / "models"


@st.cache_resource
def load_models():
    return {
        "spam": joblib.load(MODELS_DIR / "spam_model.joblib"),
        "sentiment": joblib.load(MODELS_DIR / "sentiment_model.joblib"),
        "insurance_cost": joblib.load(MODELS_DIR / "insurance_cost_model.joblib"),
        "insurance_risk": joblib.load(MODELS_DIR / "insurance_risk_model.joblib"),
    }


st.markdown(
    """
    <style>
        .stApp {
            background: #0b1020;
            color: #e5e7eb;
        }

        .block-container {
            max-width: 1120px;
            padding-top: 3rem;
            padding-bottom: 4rem;
        }

        .hero {
            text-align: center;
            padding: 2rem 1rem;
        }

        .hero h1 {
            color: #f8fafc;
            font-size: 3rem;
            margin-bottom: 0.4rem;
        }

        .hero p {
            color: #cbd5e1;
            font-size: 1.1rem;
            max-width: 760px;
            margin: auto;
        }

        .section-title {
            color: #f8fafc;
            margin-top: 2.5rem;
        }

        .card {
            background: #151c33;
            border: 1px solid #293452;
            border-radius: 14px;
            padding: 1.2rem;
            min-height: 110px;
        }

        .card h3 {
            color: #a78bfa;
            margin-top: 0;
        }

        .card p {
            color: #cbd5e1;
        }

        label, .stMarkdown, .stCaption {
            color: #e5e7eb !important;
        }
        

         html, body {
            background-color: #0b1020;
        }

        [data-testid="stAppViewContainer"] {
            background-color: #0b1020;
        }

        [data-testid="stHeader"] {
            background-color: #0b1020;
        }

        .stApp {
            background-color: #0b1020;
        }

        /* Keep your existing CSS below */
    </style>
    """,
    unsafe_allow_html=True,
)

try:
    models = load_models()
except Exception as error:
    st.error(f"Unable to load model files: {error}")
    st.stop()

st.markdown(
    """
    <div class="hero">
        <h1>Hi, I’m Imoh Ekpenyong 👋</h1>
        <p>
            <strong>Data Scientist / ML Engineer</strong><br><br>
            I deliver end-to-end machine-learning projects — from data
            collection and analysis to model development, deployment,
            and interactive web applications.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

link_one, link_two, link_three = st.columns(3)
link_one.link_button("View Projects", "#projects", use_container_width=True)
link_two.link_button(
    "GitHub",
    "https://github.com/9more/test_repo",
    use_container_width=True,
)
link_three.link_button(
    "LinkedIn",
    "https://www.linkedin.com/in/imoh-ekpenyong-95983045",
    use_container_width=True,
)

st.markdown("<h2 class='section-title'>Technical Skills</h2>", unsafe_allow_html=True)

skills = [
    ("Programming & Data", "Python · SQL · Pandas · NumPy"),
    ("Machine Learning & NLP", "Scikit-learn · NLP · TF-IDF · Text Classification"),
    ("Deployment & MLOps", "Streamlit · Flask · Docker · Git · CI/CD"),
    ("Web & Data Collection", "React · REST APIs · Web Scraping · Beautiful Soup"),
    ("Visualisation", "Power BI · Tableau · Matplotlib · Seaborn"),
]

skill_columns = st.columns(3)

for index, (title, content) in enumerate(skills):
    with skill_columns[index % 3]:
        st.markdown(
            f"<div class='card'><h3>{title}</h3><p>{content}</p></div>",
            unsafe_allow_html=True,
        )

st.markdown(
    "<h2 id='projects' class='section-title'>Interactive NLP Projects</h2>",
    unsafe_allow_html=True,
)

spam_column, sentiment_column = st.columns(2, gap="large")

with spam_column:
    st.markdown(
        "<div class='card'><h3>📨 Spam Detector</h3>"
        "<p>Classify an email or message as Spam or Not Spam.</p></div>",
        unsafe_allow_html=True,
    )

    spam_text = st.text_area(
        "Enter a message",
        placeholder="Paste an email or message here...",
        height=150,
        key="spam_text",
    )

    if st.button("Analyse Message", key="spam_button", use_container_width=True):
        if not spam_text.strip():
            st.warning("Enter a message first.")
        else:
            prediction = models["spam"].predict([spam_text])[0]
            st.success(f"Prediction: **{prediction}**")

with sentiment_column:
    st.markdown(
        "<div class='card'><h3>💬 Sentiment Analysis</h3>"
        "<p>Classify text as Positive or Negative.</p></div>",
        unsafe_allow_html=True,
    )

    sentiment_text = st.text_area(
        "Enter a review or comment",
        placeholder="For example: The service was excellent and very fast!",
        height=150,
        key="sentiment_text",
    )

    if st.button("Analyse Sentiment", key="sentiment_button", use_container_width=True):
        if not sentiment_text.strip():
            st.warning("Enter text first.")
        else:
            prediction = models["sentiment"].predict([sentiment_text])[0]

            if prediction == "Positive":
                st.success(f"Sentiment: **{prediction} 😊**")
            else:
                st.error(f"Sentiment: **{prediction} 😟**")

st.markdown(
    "<h2 class='section-title'>Insurance Machine Learning</h2>",
    unsafe_allow_html=True,
)

cost_column, risk_column = st.columns(2, gap="large")

with cost_column:
    st.markdown(
        "<div class='card'><h3>🛡️ Insurance Cost Predictor</h3>"
        "<p>Estimate annual insurance cost using profile information.</p></div>",
        unsafe_allow_html=True,
    )

    with st.form("insurance_cost_form"):
        first, second = st.columns(2)

        with first:
            cost_age = st.number_input(
                "Age",
                min_value=18,
                max_value=100,
                value=30,
                key="cost_age",
            )
            cost_bmi = st.number_input(
                "BMI",
                min_value=15.0,
                max_value=55.0,
                value=27.5,
                step=0.1,
                key="cost_bmi",
            )
            cost_children = st.number_input(
                "Children",
                min_value=0,
                max_value=10,
                value=0,
                key="cost_children",
            )

        with second:
            cost_sex = st.selectbox(
                "Sex",
                ["female", "male"],
                key="cost_sex",
            )
            cost_smoker = st.selectbox(
                "Smoker",
                ["no", "yes"],
                key="cost_smoker",
            )
            cost_region = st.selectbox(
                "Region",
                ["northeast", "northwest", "southeast", "southwest"],
                key="cost_region",
            )

        cost_submit = st.form_submit_button(
            "Estimate Annual Cost",
            use_container_width=True,
        )

    if cost_submit:
        cost_input = pd.DataFrame(
            [{
                "age": cost_age,
                "sex": cost_sex,
                "bmi": cost_bmi,
                "children": cost_children,
                "smoker": cost_smoker,
                "region": cost_region,
            }]
        )

        prediction = models["insurance_cost"].predict(cost_input)[0]
        st.success(f"Estimated annual cost: **${prediction:,.2f}**")
        st.caption("Portfolio demonstration only — not an insurance quote.")

with risk_column:
    st.markdown(
        "<div class='card'><h3>📊 Insurance Risk Classifier</h3>"
        "<p>Classify a profile as low risk or high risk.</p></div>",
        unsafe_allow_html=True,
    )

    with st.form("insurance_risk_form"):
        first, second = st.columns(2)

        with first:
            risk_age = st.number_input(
                "Age",
                min_value=18,
                max_value=100,
                value=30,
                key="risk_age",
            )
            risk_bmi = st.number_input(
                "BMI",
                min_value=15.0,
                max_value=55.0,
                value=27.5,
                step=0.1,
                key="risk_bmi",
            )
            risk_children = st.number_input(
                "Children",
                min_value=0,
                max_value=10,
                value=0,
                key="risk_children",
            )

        with second:
            risk_sex = st.selectbox(
                "Sex",
                ["female", "male"],
                key="risk_sex",
            )
            risk_smoker = st.selectbox(
                "Smoker",
                ["no", "yes"],
                key="risk_smoker",
            )
            risk_region = st.selectbox(
                "Region",
                ["northeast", "northwest", "southeast", "southwest"],
                key="risk_region",
            )

        risk_submit = st.form_submit_button(
            "Classify Risk",
            use_container_width=True,
        )

    if risk_submit:
        risk_input = pd.DataFrame(
            [{
                "age": risk_age,
                "sex": risk_sex,
                "bmi": risk_bmi,
                "children": risk_children,
                "smoker": risk_smoker,
                "region": risk_region,
            }]
        )

        prediction = models["insurance_risk"].predict(risk_input)[0]

        if prediction == "HIGH RISK":
            st.error(f"Risk classification: **{prediction}**")
        else:
            st.success(f"Risk classification: **{prediction}**")

        st.caption(
            "Educational portfolio demo only — not for insurance eligibility or underwriting decisions."
        )

st.divider()
st.markdown(
    "<p style='text-align: center; color: #64748b;'>"
    "© 2026 Imoh Ekpenyong · Built with Streamlit"
    "</p>",
    unsafe_allow_html=True,
)