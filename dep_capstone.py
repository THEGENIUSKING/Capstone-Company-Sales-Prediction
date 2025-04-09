

import streamlit as st
import pandas as pd
import joblib

# Load your trained model
capstone = joblib.load("capstone.pkl")  # Make sure your model file is in the same directory

st.title("📊 Capstone Company Sales Prediction App")

st.markdown("Enter your budget and select categories (they'll be auto-encoded):")

# Dropdown mappings for encoded values
tv_options = {'TV_A': 0, 'TV_B': 1, 'TV_C': 2, 'TV_D': 3}
influencer_options = {'Micro': 0, 'Macro': 1, 'Mega': 2, 'Nano': 3}

# Feature inputs
radio = st.number_input("Radio Budget", min_value=0.0)
social_media = st.number_input("Social Media Budget", min_value=0.0)

tv_choice = st.selectbox("TV Channel", list(tv_options.keys()))
influencer_choice = st.selectbox("Influencer Type", list(influencer_options.keys()))

# Encode selected values
tv_encoded = tv_options[tv_choice]
influencer_encoded = influencer_options[influencer_choice]

# Prepare input for prediction
input_data = pd.DataFrame([{
    'Radio': radio,
    'Social Media': social_media,
    'TV': tv_encoded,
    'Influencer': influencer_encoded
}])

# Prediction
if st.button("Predict Sales"):
    prediction = capstone.predict(input_data)
    st.success(f"📈 Predicted Sales: {prediction[0]:.2f}")