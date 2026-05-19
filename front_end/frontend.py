import streamlit as st
import requests

st.set_page_config(
    page_title="Social Network Ads Prediction",
    page_icon="🛒",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #141E30, #243B55);
}

.main-box {
    background: rgba(255, 255, 255, 0.95);
    padding: 30px;
    border-radius: 25px;
    box-shadow: 0px 8px 30px rgba(0,0,0,0.4);
    text-align: center;
}

.title {
    color: #243B55;
    font-size: 38px;
    font-weight: bold;
}

.subtitle {
    color: #555;
    font-size: 18px;
}

.result-box {
    padding: 20px;
    border-radius: 18px;
    margin-top: 20px;
    font-size: 24px;
    font-weight: bold;
}

.success-box {
    background-color: #D4F8D4;
    color: #087A08;
}

.danger-box {
    background-color: #FFD6D6;
    color: #B00020;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-box">
    <div class="title">🛒 Social Network Ads Prediction</div>
    <p class="subtitle">Predict whether a customer will purchase a product based on gender, age and salary.</p>
    <h1>📊</h1>
</div>
""", unsafe_allow_html=True)

st.write("")

gender = st.selectbox("👤 Select Gender", ["Male", "Female"])

age = st.slider("🎂 Select Age", 18, 100, 30)

estimated_salary = st.number_input(
    "💰 Enter Estimated Salary",
    min_value=1000,
    max_value=200000,
    value=50000,
    step=1000
)

if st.button("🚀 Predict Purchase"):

    data = {
        "gender": gender,
        "age": age,
        "estimated_salary": estimated_salary
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        result = response.json()

        if result["prediction"] == 1:
            st.markdown("""
            <div class="result-box success-box">
                ✅ Customer Will Purchase
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="result-box danger-box">
                ❌ Customer Will Not Purchase
            </div>
            """, unsafe_allow_html=True)

    except:
        st.warning("⚠️ Backend Server Not Running. Start FastAPI first.")