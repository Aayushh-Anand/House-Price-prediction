# FASTAPI DEPLOYMENT + WEB INTERFACE

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import pandas as pd
import joblib


# PATH CONFIGURATION

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "final_house_price_model.pkl"
PREPROCESSOR_PATH = BASE_DIR / "models" / "final_preprocessor.pkl"

FRONTEND_DIR = BASE_DIR / "frontend"


# LOAD ML MODEL & PREPROCESSOR

model = joblib.load(MODEL_PATH)

preprocessor = joblib.load(PREPROCESSOR_PATH)


# FASTAPI APPLICATION

app = FastAPI(
    title="Delhi House Price Prediction API",
    description="ML API for predicting Delhi/Gurgaon house prices",
    version="1.0"
)


# FRONTEND STATIC FILES

app.mount(
    "/frontend",
    StaticFiles(directory=FRONTEND_DIR),
    name="frontend"
)


# HOME PAGE

@app.get("/")
def home():
    return FileResponse(
        FRONTEND_DIR / "index.html"
    )


# INPUT DATA SCHEMA

class HouseInput(BaseModel):

    Area: float
    BHK: float
    Bathroom: float

    Furnishing: str
    Locality: str
    Parking: str
    Status: str
    Transaction: str
    Type: str


# PRICE PREDICTION

@app.post("/predict")
def predict_price(house: HouseInput):

    # Convert input into DataFrame
    data = pd.DataFrame([
        house.model_dump()
    ])


    # Feature Engineering

    data["Total_Rooms"] = (
        data["BHK"] +
        data["Bathroom"]
    )

    data["Area_per_BHK"] = (
        data["Area"] /
        data["BHK"]
    )


    # Convert categorical columns to string

    categorical_columns = [
        "Furnishing",
        "Locality",
        "Parking",
        "Status",
        "Transaction",
        "Type"
    ]

    for column in categorical_columns:
        data[column] = data[column].astype(str)


    # Feature Order

    features = [
        "Area",
        "BHK",
        "Bathroom",
        "Furnishing",
        "Locality",
        "Parking",
        "Status",
        "Transaction",
        "Type",
        "Total_Rooms",
        "Area_per_BHK"
    ]

    data = data[features]


    # Preprocessing

    processed_data = preprocessor.transform(data)


    # Prediction

    prediction = model.predict(
        processed_data
    )[0]


    # API Response

    return {
        "predicted_price": round(
            float(prediction),
            2
        )
    }