# house-price-prediction-streamlit-app
A small data science project where I built a machine learning model to predict house prices and turned it into a web app using Streamlit.

# 🏠 House Price Prediction System

## Project Overview
This project demonstrates the development and deployment of a machine learning model that predicts house prices based on property features.

The system is built using **Python, Scikit-learn, and Streamlit**, allowing users to input housing characteristics and receive a predicted house price through a web application.

---

## Dataset

The dataset used in this project is **Housing.csv**, which contains 545 records and 13 features describing different house attributes.

### Key Features in the Dataset

- Area
- Bedrooms
- Bathrooms
- Stories
- Parking
- Main Road Access
- Guest Room
- Basement
- Air Conditioning
- Preferred Area
- Furnishing Status

The target variable is:

**Price** – the house price to be predicted.

---

## Machine Learning Workflow

The project follows a typical machine learning pipeline:

1. Load and explore the dataset
2. Data preprocessing and encoding categorical variables
3. Splitting the dataset into training and testing sets
4. Training a Linear Regression model
5. Evaluating the model using Mean Absolute Error (MAE)
6. Saving the trained model using Joblib
7. Building a web application using Streamlit
8. Deploying the application on Streamlit Community Cloud

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

---

## Project Files
