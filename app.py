import streamlit as st
import pickle

st.set_page_config(
    page_title="Spam Email Classifier",
    page_icon="📧",
    layout="centered"
)

with open('models/spam_classifier.pkl', 'rb') as f:
    model = pickle.load(f)

with open('models/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

st.title("📧 Spam Email Classifier")

st.markdown("---")

message = st.text_area(
    "Enter Email Content",
    height=150
)

if st.button("Predict"):

    if message:

        transformed = vectorizer.transform([message])

        prediction = model.predict(transformed)

        if prediction[0] == 1:
            st.error("🚨 Spam Detected")
        else:
            st.success("✅ Safe Message")

st.markdown("---")
st.caption("Built using Python, Scikit-Learn and Streamlit")