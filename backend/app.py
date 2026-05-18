# Step 1: Import Libraries
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Step 2: Create FastAPI App
app = FastAPI()

# Step 3: Load Saved Files
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

# Step 4: Create Input Data Class
class Customer(BaseModel):
    gender: str
    age: float
    estimated_salary: float

# Step 5: Create Prediction API
@app.post("/predict")
def predict_purchase(data: Customer):

    # Convert Gender into Number
    gender_value = 1 if data.gender.lower() == "male" else 0

    # Create DataFrame
    input_data = pd.DataFrame([{
        "Gender": gender_value,
        "Age": data.age,
        "EstimatedSalary": data.estimated_salary
    }])

    # Arrange columns correctly
    input_data = input_data[columns]

    # Scale Input Data
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)[0]

    # Result
    result = "Purchased" if prediction == 1 else "Not Purchased"

    # Return Output
    return {
        "prediction": int(prediction),
        "result": result
    }