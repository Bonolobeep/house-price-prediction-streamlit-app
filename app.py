
import streamlit as st
import joblib
import numpy as np

# Load trained machine learning model
model = joblib.load("house_model.pkl")

# Improved Title
st.title("🏠 House Price Prediction System")
st.write("Enter the house details below to estimate the property price.")

# Numeric Inputs
area = st.number_input("Area")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
stories = st.number_input("Stories")
parking = st.number_input("Parking")

# Categorical Inputs
mainroad = st.selectbox("Main Road", ["yes","no"])
guestroom = st.selectbox("Guest Room", ["yes","no"])
basement = st.selectbox("Basement", ["yes","no"])
airconditioning = st.selectbox("Air Conditioning", ["yes","no"])

# Added extra feature (your improvement)
prefarea = st.selectbox("Preferred Area", ["yes","no"])

# Prediction Button
if st.button("Predict Price"):

    features = np.array([[area, bedrooms, bathrooms, stories,
                          1 if mainroad=="yes" else 0,
                          1 if guestroom=="yes" else 0,
                          1 if basement=="yes" else 0,
                          0,
                          1 if airconditioning=="yes" else 0,
                          parking,
                          1 if prefarea=="yes" else 0,
                          1]])

    prediction = model.predict(features)

    st.success(f"Estimated Price: {prediction[0]}")
