# 📊 Customer Churn Prediction System

A Machine Learning-based web application that predicts whether a customer is likely to **leave (churn)** or **stay** with a telecom company based on customer demographics, account information, and subscribed services.

The project uses the **Random Forest Classifier**, a powerful ensemble learning algorithm, to analyze customer behavior and predict churn with high accuracy.

---

## 🚀 Features

- Predict customer churn in real-time
- User-friendly interface
- Machine Learning model powered by Random Forest
- Fast and accurate predictions
- Preprocessed categorical and numerical data
- Easy deployment using FastAPI/Flask (if applicable)

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Random Forest Classifier
- Joblib
- FastAPI / Flask (Optional)
- HTML
- CSS
- JavaScript

---

## 📂 Dataset Features

The model is trained using the following customer information:

| Feature | Description |
|----------|-------------|
| customerID | Unique customer identifier |
| gender | Male or Female |
| SeniorCitizen | Whether customer is a senior citizen |
| Partner | Has a partner or not |
| Dependents | Has dependents or not |
| tenure | Number of months with the company |
| PhoneService | Phone service subscription |
| MultipleLines | Multiple phone lines |
| InternetService | Internet service provider |
| OnlineSecurity | Online security subscription |
| OnlineBackup | Online backup service |
| DeviceProtection | Device protection plan |
| TechSupport | Technical support subscription |
| StreamingTV | Streaming TV service |
| StreamingMovies | Streaming movie service |
| Contract | Contract type |
| PaperlessBilling | Paperless billing enabled |
| PaymentMethod | Payment method |
| MonthlyCharges | Monthly bill amount |
| TotalCharges | Total amount charged |

---

## 🎯 Target Variable

```
Churn
```

- Yes → Customer will leave the company
- No → Customer will stay

---

## 🧠 Machine Learning Algorithm

### Random Forest Classifier

Random Forest is an ensemble learning algorithm that builds multiple decision trees and combines their predictions.

### Advantages

- High prediction accuracy
- Handles missing values effectively
- Reduces overfitting
- Works well with categorical and numerical data
- Robust against noisy datasets

---

## 📁 Project Structure

```
Customer-Churn-Prediction/
│
├── data/
│   └── customer_churn.csv
│
├── models/
│   └── churn_model.pkl
│
├── app.py
├── model.py
├── requirements.txt
├── README.md
└── templates/
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/adarsh9421/customer-churn-prediction.git
```

### Move into the project

```bash
cd customer-churn-prediction
```

### Create Virtual Environment

Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

If using FastAPI:

```bash
uvicorn app:app --reload
```

If using Flask:

```bash
python app.py
```

---

## 📈 Model Training

1. Load dataset
2. Clean missing values
3. Encode categorical variables
4. Split dataset into training and testing sets
5. Train Random Forest Classifier
6. Evaluate model
7. Save trained model using Joblib

---

## 📊 Evaluation Metrics

The model performance can be evaluated using:

- Accuracy Score
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

---

## 📌 Workflow

```
Customer Data
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Encoding
        │
        ▼
Train/Test Split
        │
        ▼
Random Forest Classifier
        │
        ▼
Prediction
        │
        ▼
Customer Will Churn?
```

---

## 💡 Future Improvements

- Deploy on Render or Railway
- Docker support
- SHAP explainability
- Feature importance visualization
- Model comparison (XGBoost, CatBoost, LightGBM)
- Customer churn probability score
- Dashboard with analytics

---


---

## 📚 Libraries Used

```text
pandas
numpy
scikit-learn
joblib
fastapi 
uvicorn 
jinja2 
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 👨‍💻 Author

**Adarsh Gusain (adarsh9421)**
**Saarthak Sajwan (saarthak911)**


## ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub.