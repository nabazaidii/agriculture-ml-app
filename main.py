import streamlit as st
import pandas as pd
import numpy as np
import pickle  # or joblib depending on your model

# Load your trained model
model = pickle.load(open('model.pkl', 'rb'))  # Make sure model.pkl exists

# UI layout
st.title("🌾 Crop Recommendation System")
st.write("Enter soil and weather conditions below to get crop suggestions.")

# Input fields
N = st.number_input("Nitrogen (N)", min_value=0)
P = st.number_input("Phosphorus (P)", min_value=0)
K = st.number_input("Potassium (K)", min_value=0)
temperature = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")

ph = st.number_input("pH value")
rainfall = st.number_input("Rainfall (mm)")

# Predict button
if st.button("Predict Crop"):
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    st.success(f"🌱 Recommended Crop: **{prediction[0].capitalize()}**")

