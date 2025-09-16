# 🏠 House Prices Prediction - Kaggle Challenge

> A machine learning project to predict house prices using real estate data from Kaggle’s House Prices: Advanced Regression Techniques competition.

## 📌 Project Overview

This project aims to build predictive models that estimate house sale prices based on features such as living area, number of rooms, quality ratings, and more. The project compares multiple regression models and tracks learning progress along the way.

- **Competition**: [House Prices - Advanced Regression Techniques (Kaggle)](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)
- **Duration**: 21/08/2025 → 28/08/2025
- **Author**: Vũ Quang Huy

---

## 🎯 Objectives

- Perform Exploratory Data Analysis (EDA)
- Preprocess and clean real-world data
- Build and evaluate multiple machine learning models:
  - Linear Regression (baseline)
  - Random Forest
  - XGBoost
- Track progress via a study log
- Identify the best model based on RMSE on validation/test sets

---

## 🗂️ Folder Structure
House_Prices_Predict/
├── house_prices/ # Raw and processed data
    ├── data_description.txt
    ├── sample_submission.csv
    ├── test.csv
    ├── train.csv
├── 01_EDA.ipynb # An overview through data
├── 02_Preprocessing.ipynb # Preprocessing
├── 03_Models.ipynb # models
├── 04_Predict.ipynb # use the best model to predict the test-price
├── preprocessiong.py # reusable code for preprocessing
├── README.md # This file
├── result.png # My first time in Kaggle leaderboard
└── submission.csv # The prediction of the best model to submit in the competition

---

## 🧪 Models & Performance

| Model              | Train RMSE | CV RMSE  | Test RMSE | Notes                 |
|--------------------|------------|----------|-----------|-----------------------|
| Linear Regression  | 16009.35   | 24152.73 | 25939.93  | Best model (lambda=30)|
| Random Forest      | 13359.81   | 29842.53 | 34197.30  | Overfitting           |
| XGBoost            |  2330.72   | 28676.99 | 29671.82  | Strong overfit        |

---

## 📊 Key Techniques Used

- Data visualization using `matplotlib` and `seaborn`
- Feature correlation analysis
- Polynomial features & regularization (L2)
- Train-validation-test split (manual)
- RMSE evaluation metric
- Hyperparameter tuning (lambda, degree, depth, etc.)
- Log-transforming target (`SalePrice`) for better learning

---

## 🧠 Study Log Highlights

- ✅ **Day 1** (21/08): Data loading, EDA, pandas basics  
- ✅ **Day 2** (22/08): Preprocessing, encoding, splitting data  
- ✅ **Day 3** (23/08): Baseline linear model + RMSE evaluation  
- ✅ **Day 4** (27/08): Model tuning with polynomial + regularization  
- ✅ **Day 5** (28/08): Added XGBoost, Random Forest — confirmed Linear still best, 
                        submitted the prediction to the competition

---
