from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, get_db, Base
from dtos import ChurnPredictionInput, ChurnPredictionOutput
from controller import predict_churn
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# create all tables in postgresql automatically
Base.metadata.create_all(bind=engine)

# create fastapi app
app = FastAPI(
    title="Churn Prediction API",
    description="API to predict customer churn using machine learning",
    version="1.0.0"
)

# health check route
@app.get("/")
def root():
    return {"message": "Churn Prediction API is running "}

# prediction route
@app.post("/predict", response_model=ChurnPredictionOutput)
def predict(input_data: ChurnPredictionInput, db: Session = Depends(get_db)):
    return predict_churn(input_data, db)