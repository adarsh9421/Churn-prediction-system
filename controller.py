import joblib
import numpy as np
import pandas as pd
from sqlalchemy.orm import Session
from model import ChurnPrediction
from dtos import ChurnPredictionInput, ChurnPredictionOutput

# load model and encoders once when server starts
# not inside function — so it loads only one time
loaded_model = joblib.load("model.pkl")
label_encoders = joblib.load("label_encoders.pkl")

def predict_churn(input_data: ChurnPredictionInput, db: Session):

    # step 1 — convert input to model data
    input_dict = input_data.model_dump()

    

    # step 2 — convert to dataframe
    input_df = pd.DataFrame([input_dict])

    # step 3 — encode categorical columns
    for col in input_df.select_dtypes(include='object').columns:
        input_df[col] = label_encoders[col].transform(input_df[col])

    # step 4 — get prediction (0 or 1)
    prediction = loaded_model.predict(input_df)[0]

    # step 5 — get probability
    churn_probability = loaded_model.predict_proba(input_df)[0][1]

    # step 6 — convert prediction to human readable label
    if prediction == 1:
        prediction_label = "Will Churn"
    else:
        prediction_label = "Will Not Churn"

    # step 7 — save everything to postgresql database
    db_record = ChurnPrediction(
        # save all input columns
        
        gender = input_data.gender,
        SeniorCitizen = input_data.SeniorCitizen,
        Partner = input_data.Partner,
        Dependents = input_data.Dependents,
        tenure = input_data.tenure,
        PhoneService = input_data.PhoneService,
        MultipleLines = input_data.MultipleLines,
        InternetService = input_data.InternetService,
        OnlineSecurity = input_data.OnlineSecurity,
        OnlineBackup = input_data.OnlineBackup,
        DeviceProtection = input_data.DeviceProtection,
        TechSupport = input_data.TechSupport,
        StreamingTV = input_data.StreamingTV,
        StreamingMovies = input_data.StreamingMovies,
        Contract = input_data.Contract,
        PaperlessBilling = input_data.PaperlessBilling,
        PaymentMethod = input_data.PaymentMethod,
        MonthlyCharges = input_data.MonthlyCharges,
        TotalCharges = input_data.TotalCharges,

        # save output columns
        prediction = int(prediction),
        prediction_label = prediction_label,
        churn_probability = float(churn_probability)
    )

    # step 8 — add record to database session
    db.add(db_record)

    # step 9 — commit to actually save in postgresql
    db.commit()

    # step 10 — refresh to get updated record with id and timestamp
    db.refresh(db_record)

    # step 11 — return output
    return ChurnPredictionOutput(
        prediction = int(prediction),
        prediction_label = prediction_label,
        churn_probability = round(float(churn_probability), 2)
    )