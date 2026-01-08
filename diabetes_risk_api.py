from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import numpy as np

app = FastAPI(title="Diabetes Risk Prediction API")

# Load trained balanced model
model = joblib.load("diabetes_risk_model_balanced.pkl")


# -------------------------
# Input Schema (Clean & Easy)
# -------------------------
class DiabetesInput(BaseModel):
    pregnancies: int = Field(..., example=4)
    glucose: float = Field(..., example=145)
    blood_pressure: float = Field(..., example=82)
    skin_thickness: float = Field(..., example=30)
    insulin: float = Field(..., example=130)
    bmi: float = Field(..., example=33.6)
    diabetes_pedigree_function: float = Field(..., example=0.627)
    age: int = Field(..., example=52)


@app.get("/")
def home():
    return {"message": "Diabetes Risk Prediction API is running"}


@app.post("/predict")
def predict_diabetes(data: DiabetesInput):
    """
    Predict diabetes risk (0 = low risk, 1 = high risk)
    """
    input_array = np.array([[  
        data.pregnancies,
        data.glucose,
        data.blood_pressure,
        data.skin_thickness,
        data.insulin,
        data.bmi,
        data.diabetes_pedigree_function,
        data.age
    ]])

    prediction = model.predict(input_array)[0]
    probability = model.predict_proba(input_array)[0][1]

    return {
        "diabetes_risk": int(prediction),
        "risk_probability": round(float(probability), 2)
    }
