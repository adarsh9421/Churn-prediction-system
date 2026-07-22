from pydantic import BaseModel

# input schema — what customer data comes into the API , basically what request model handle by api 
class ChurnPredictionInput(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

# output schema — what the API sends back after prediction response model what api will provide 

class ChurnPredictionOutput(BaseModel):
    prediction: int
    prediction_label: str
    churn_probability: float