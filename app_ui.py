import streamlit as st
import requests

API_URL = "https://diabetes-risk-prediction-2.onrender.com/predict"
  # local for now

st.title("🩺 Diabetes Risk Prediction")
st.write("Enter patient details to assess diabetes risk")

pregnancies = st.number_input("Number of Pregnancies", 0, 20, 2)
glucose = st.slider("Glucose Level", 50, 200, 120)
blood_pressure = st.slider("Blood Pressure", 40, 130, 70)
skin_thickness = st.slider("Skin Thickness", 0, 100, 20)
insulin = st.slider("Insulin Level", 0, 300, 80)
bmi = st.slider("BMI", 10.0, 60.0, 25.0)
dpf = st.slider("Diabetes Pedigree Function", 0.0, 2.5, 0.5)
age = st.number_input("Age", 10, 100, 30)

if st.button("Predict Diabetes Risk"):
    payload = {
        "pregnancies": pregnancies,
        "glucose": glucose,
        "blood_pressure": blood_pressure,
        "skin_thickness": skin_thickness,
        "insulin": insulin,
        "bmi": bmi,
        "diabetes_pedigree_function": dpf,
        "age": age
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:
        result = response.json()
        risk = result["diabetes_risk"]
        prob = result["risk_probability"]

        if prob < 0.4:
            st.success(f"🟢 Low Risk (Probability: {prob})")
        elif prob < 0.7:
            st.warning(f"🟡 Medium Risk (Probability: {prob})")
        else:
            st.error(f"🔴 High Risk (Probability: {prob})")
    else:
        st.error("API error. Please check backend.")
