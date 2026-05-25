import streamlit as st
import pandas as pd
import numpy as np
import pickle

# App Title
st.title("🚗 Car Mileage (MPG) Prediction App")
st.write("Enter the vehicle specifications below to predict its fuel efficiency (MPG):")

# Input Fields
cylinders = st.number_input("Cylinders", min_value=3, max_value=8, value=4, step=1)
displacement = st.number_input("Displacement (cc)", min_value=60.0, max_value=500.0, value=150.0)
horsepower = st.number_input("Horsepower (hp)", min_value=40.0, max_value=300.0, value=90.0)
weight = st.number_input("Weight (lbs)", min_value=1500.0, max_value=5000.0, value=2500.0)
acceleration = st.number_input("Acceleration", min_value=8.0, max_value=25.0, value=15.0)

# Prediction Logic
if st.button("Predict Mileage"):
    try:
        # अब यह सही फाइल 'model.pkl' को लोड करेगा
        with open("model.pkl", "rb") as file:
            model = pickle.load(file)
        
        input_data = np.array([[cylinders, displacement, horsepower, weight, acceleration]])
        prediction = model.predict(input_data)
        
        st.success(f"The predicted mileage for this car is: {prediction[0]:.2f} MPG")
        
    except FileNotFoundError:
        st.error("Error: 'model.pkl' file not found on GitHub. Please make sure the file is uploaded with this exact name.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
