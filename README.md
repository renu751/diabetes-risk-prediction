# 🩺 Diabetes Risk Prediction – Full Stack Machine Learning Application

This project is an **end-to-end healthcare machine learning system** that predicts the risk of diabetes using patient medical data.  
It demonstrates **real-world ML engineering**, combining data preprocessing, model training, API development, frontend UI, Dockerization, and cloud deployment.

The system is designed with a strong emphasis on **medical correctness**, especially **reducing false negatives**, which is critical in healthcare screening applications.

---

## 📌 Problem Statement

Diabetes is a chronic disease that often remains undiagnosed until complications arise.  
Early identification of high-risk individuals can enable timely screening and intervention.

The objective of this project is to build a **clinical decision-support system** that predicts whether a patient is at high risk of diabetes based on routinely collected medical parameters.

---

## 📊 Dataset

- **Dataset:** Pima Indians Diabetes Dataset (Kaggle)
- **Total Records:** 768 patients
- **Features Include:**
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function
  - Age
- **Target Variable:**  
  - `Outcome` → 0 (No Diabetes), 1 (Diabetes)

### Medical Data Cleaning
Certain clinical features contain invalid zero values (e.g., Glucose = 0), which are **medically impossible**.  
These were treated as missing values and handled using **median imputation**, a robust and medically safe approach.

---

## 🧠 Machine Learning Approach

- Data preprocessing with medical domain awareness
- Median imputation for missing clinical values
- Feature scaling using `StandardScaler`
- Logistic Regression model
- Class imbalance handled using `class_weight="balanced"`
- Model evaluation focused on **Recall** to reduce missed diabetes cases

---

## 📈 Model Performance (Balanced Model)

- **Recall (Diabetes Class): ~70%**
- Significant reduction in false negatives
- Acceptable precision trade-off for screening use cases

This makes the model suitable for **early risk screening**, where missing a positive case is more dangerous than a false alert.

---

## 🧩 System Architecture

