from pathlib import Path

readme = """# 🏠 Delhi House Price Prediction

An end-to-end Machine Learning project for predicting residential property prices using Delhi and Gurgaon house data.

The project covers the complete ML lifecycle — from data cleaning and exploratory analysis to feature engineering, model comparison, hyperparameter tuning, error analysis, final model training, FastAPI deployment, and an interactive web interface.

---

## 🎯 Project Objective

The objective of this project is to build a Machine Learning model that can estimate the price of a residential property based on its characteristics.

The model uses features such as:

- Area
- BHK
- Bathroom
- Furnishing
- Locality
- Parking
- Property Status
- Transaction Type
- Property Type

---

## 🧠 Machine Learning Workflow

```text
Raw Dataset
     ↓
Data Understanding
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Feature Engineering
     ↓
Train/Test Split
     ↓
Data Preprocessing
     ↓
Multiple Regression Models
     ↓
Cross Validation
     ↓
Advanced Regression
     ↓
Hyperparameter Tuning
     ↓
Error & Residual Analysis
     ↓
Final Model Selection
     ↓
Prediction Pipeline
     ↓
FastAPI Deployment
     ↓
Web Interface
```

---

## 📊 Dataset

The project uses residential property data from Delhi and Gurgaon.

### Target Variable

```text
Price
```

### Main Features

```text
Area
BHK
Bathroom
Furnishing
Locality
Parking
Status
Transaction
Type
```

### Data Quality

During EDA, missing values and duplicate records were identified and handled as part of the data-cleaning process.

---

## 🔍 Exploratory Data Analysis

EDA was performed to understand:

- Dataset structure
- Numerical feature distributions
- Categorical feature distributions
- Missing values
- Duplicate records
- Price distribution
- Relationships between property features and price
- Potential outliers
- Correlations between numerical variables

The analysis was used to make decisions for feature engineering and preprocessing.

---

## ⚠️ Target Leakage Detection

The dataset contained a `Per_Sqft` feature.

Since price per square foot is directly derived from:

```text
Price / Area
```

using it as an input feature could introduce **target leakage** because it contains information derived from the target variable.

Therefore:

```text
Per_Sqft
```

was excluded from model training.

This helps ensure that the model learns from genuine property characteristics rather than information derived from the target.

---

## ⚙️ Feature Engineering

Two additional features were created.

### Total Rooms

```text
Total_Rooms = BHK + Bathroom
```

This provides the model with a combined representation of the property's room and bathroom count.

### Area per BHK

```text
Area_per_BHK = Area / BHK
```

This represents the approximate area available per bedroom.

---

## 🔄 Data Preprocessing

A preprocessing pipeline was created using Scikit-learn.

### Numerical Features

The numerical features were handled using:

- Missing-value imputation
- StandardScaler

### Categorical Features

The categorical features were handled using:

- Missing-value imputation
- OneHotEncoder
- Unknown-category handling

A `ColumnTransformer` was used to apply the appropriate preprocessing to numerical and categorical features.

This same preprocessing pipeline is used during prediction to ensure consistency between training and inference.

---

## 🤖 Machine Learning Models

Multiple regression algorithms were experimented with.

### Baseline Regression Models

- Linear Regression
- Ridge Regression
- Lasso Regression
- Elastic Net
- KNN Regression
- Support Vector Regression
- Decision Tree Regression

### Advanced Regression Models

- Huber Regression
- Bayesian Ridge
- Extra Trees Regression
- Histogram Gradient Boosting

This allowed the project to compare different types of regression approaches instead of relying on a single algorithm.

---

## 📈 Model Evaluation

Models were evaluated using three primary regression metrics.

### R² Score

Measures how much of the variation in house prices is explained by the model.

```text
Higher R² = Better
```

### MAE — Mean Absolute Error

Measures the average absolute difference between actual and predicted prices.

```text
Lower MAE = Better
```

### RMSE — Root Mean Squared Error

Penalizes larger prediction errors more strongly than MAE.

```text
Lower RMSE = Better
```

---

## 🔁 Cross Validation

5-Fold Cross Validation was used to evaluate model stability.

```text
Dataset
   ↓
 ┌─────┬─────┬─────┬─────┬─────┐
 │ F1  │ F2  │ F3  │ F4  │ F5  │
 └─────┴─────┴─────┴─────┴─────┘
    ↓
5 different validation runs
    ↓
Mean performance
    +
Performance stability
```

Cross-validation helped determine whether a model's performance was consistent across different subsets of the training data.

---

## 🎯 Hyperparameter Tuning

The strongest candidate models were selected using cross-validation.

Hyperparameter optimization was performed using:

```text
RandomizedSearchCV
```

The tuning process explored different combinations of model parameters and selected configurations that produced stronger cross-validation performance.

Models considered for tuning included:

- Extra Trees
- Histogram Gradient Boosting
- KNN Regression

---

## 🔬 Error & Residual Analysis

After model selection, detailed error analysis was performed.

The following were analyzed:

- Actual vs Predicted prices
- Residual distribution
- Residuals vs predicted values
- Largest prediction errors
- Absolute prediction errors

### Residual

```text
Residual = Actual Price - Predicted Price
```

Residual analysis helped understand where the model performs well and where larger prediction errors occur.

---

## 🏆 Final Model

After comparing the baseline models, advanced models, cross-validation results, and tuned models, the best-performing tuned model was selected as the final model.

The final model was retrained using the complete available dataset so that it could learn from the maximum amount of training information.

Saved model files:

```text
final_house_price_model.pkl
final_preprocessor.pkl
```

---

## 🔮 Prediction Pipeline

The project includes a complete prediction pipeline.

```text
New Property Details
        ↓
Feature Engineering
        ↓
Saved Preprocessor
        ↓
Encoded & Transformed Features
        ↓
Final ML Model
        ↓
Predicted House Price
```

The prediction pipeline ensures that new input data goes through the same feature engineering and preprocessing logic used during model training.

---

## 🌐 Web Application

The trained ML model was integrated with **FastAPI** and connected to a custom web interface.

The application allows users to enter property information such as:

- Area
- BHK
- Bathroom
- Furnishing
- Locality
- Parking
- Status
- Transaction
- Property Type

The backend processes the input and returns the estimated property price.

### Application Architecture

```text
                    USER
                      │
                      ↓
              ┌───────────────┐
              │ Web Interface │
              │ HTML/CSS/JS   │
              └───────┬───────┘
                      │
                 POST /predict
                      │
                      ↓
              ┌───────────────┐
              │    FastAPI    │
              └───────┬───────┘
                      │
                      ↓
             Feature Engineering
                      │
                      ↓
              ML Preprocessor
                      │
                      ↓
               Final ML Model
                      │
                      ↓
              Predicted Price
```

---

## 🏗️ Project Structure

```text
house-price-prediction/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── data/
│   ├── Delhi_House_Data.csv
│   └── processed/
│
├── models/
│   ├── final_house_price_model.pkl
│   └── final_preprocessor.pkl
│
├── notebooks/
│   └── House_Price_Prediction.ipynb
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

### Programming

- Python

### Data Analysis

- Pandas
- NumPy
- Matplotlib
- Seaborn

### Machine Learning

- Scikit-learn
- Regression
- Feature Engineering
- Cross Validation
- Hyperparameter Tuning

### Backend

- FastAPI
- Uvicorn

### Frontend

- HTML
- CSS
- JavaScript

### Development Tools

- Jupyter Notebook
- VS Code
- Git
- GitHub

---

## 💡 Key Learning Outcomes

Through this project, the following Machine Learning concepts were implemented practically:

- Data cleaning
- Missing-value analysis
- Duplicate detection
- Exploratory Data Analysis
- Outlier analysis
- Target leakage detection
- Feature engineering
- Train/test splitting
- Numerical preprocessing
- Categorical encoding
- Feature scaling
- Regression algorithms
- Model comparison
- Cross-validation
- Model stability analysis
- Hyperparameter tuning
- Residual analysis
- Error analysis
- Model serialization
- Prediction pipelines
- FastAPI deployment
- REST API development
- ML web application development

---

## 👨‍💻 Author

### AYUSH ANAND

B.Tech — Artificial Intelligence & Machine Learning

---