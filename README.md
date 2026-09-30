# Machine Learning Prediction of Tensile Strength in Carbon-Fiber/Polysulfone Thermoplastic Composites

## Project Overview

This project develops a machine-learning model for predicting the tensile
strength of carbon-fiber/thermoplastic composite specimens using
experimental data.

The material system investigated is carbon-fiber-reinforced polysulfone
(PSU), a high-performance thermoplastic polymer.

## Dataset

The experimental dataset contains tensile-test results for more than
600 composite specimens.

The analysis uses five pre-test variables:

- PSU solution concentration group
- Carbon fiber concentration
- Specimen length
- Specimen mass
- Composite diameter

Post-test variables such as maximum force, Young's modulus, elongation,
and failure classification were excluded from the predictive model to
avoid using information obtained during or after tensile testing.

## Machine Learning

Three regression models were evaluated:

- Random Forest
- Gradient Boosting
- XGBoost

Five-fold cross-validation was used to compare model performance.

XGBoost showed the strongest average cross-validation performance among
the evaluated models.

## Final Model

The final XGBoost model achieved approximately:

- Test MAE: 218 MPa
- Test RMSE: 276 MPa
- Test R²: 0.162

The model is intended as a predictive screening tool rather than a
replacement for experimental tensile testing.

## Application

A Streamlit application provides a simple interface for entering
specimen characteristics and obtaining a predicted tensile strength.

## Project Structure

```text
carbon_fiber_ml_project/
├── data/
│   └── raw/
├── notebooks/
│   └── cf_thermoplastic_composite.ipynb
├── models/
│   └── xgboost_tensile_strength_model.joblib
├── app.py
├── README.md
└── requirements.txt
