from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

# database table structure
class ChurnPrediction(Base):
    __tablename__ = "churn_predictions"

    # primary key
    id = Column(Integer, primary_key=True, index=True)

    # input columns
    gender = Column(String)
    SeniorCitizen = Column(Integer)
    Partner = Column(String)
    Dependents = Column(String)
    tenure = Column(Integer)
    PhoneService = Column(String)
    MultipleLines = Column(String)
    InternetService = Column(String)
    OnlineSecurity = Column(String)
    OnlineBackup = Column(String)
    DeviceProtection = Column(String)
    TechSupport = Column(String)
    StreamingTV = Column(String)
    StreamingMovies = Column(String)
    Contract = Column(String)
    PaperlessBilling = Column(String)
    PaymentMethod = Column(String)
    MonthlyCharges = Column(Float)
    TotalCharges = Column(Float)

    # output columns
    prediction = Column(Integer)
    prediction_label = Column(String)
    churn_probability = Column(Float)

    # timestamp — automatically saves when prediction was made
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())