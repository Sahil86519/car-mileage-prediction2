import streamlit as st
import pandas as pd
import numpy as np
import pickle

# 1. App Title and UI Setup
st.title("🚗 Car Mileage (MPG) Prediction App")
st.write("Enter the vehicle specifications below to predict its fuel efficiency (MPG):")

# 2. Creating Input Fields for User Data
cylinders = st.number_input("Cylinders", min_value=3, max_value=8, value=4, step=1)
displacement = st.number_input("Displacement (cc)", min_value=60.0, max_value=500.0, value=150.0)
horsepower = st.number_input("Horsepower (hp)", min_value=40.0, max_value=300.0, value=90.0)
weight = st.number_input("Weight (lbs)", min_value=1500.0, max_value=5000.0, value=2500.0)
acceleration = st.number_input("Acceleration", min_value=8.0, max_value=25.0, value=15.0)

# 3. Prediction Logic when Button is Clicked
if st.button("Predict Mileage"):
    try:
        # Loading the saved machine learning model from GitHub
        with open("car milage pred..", "rb") as file:
            model = pickle.load(file)
        
        # Converting inputs into a proper numpy array for the model
        input_data = np.array([[cylinders, displacement, horsepower, weight, acceleration]])
        
        # Making the prediction
        prediction = model.predict(input_data)
        
        # Displaying the final result in a green success box
        st.success(f"The predicted mileage for this car is: {prediction[0]:.2f} MPG")
        
    except FileNotFoundError:
        st.error("Error: Model file 'car milage pred..' not found on GitHub. Please check the file name.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
