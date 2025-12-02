import streamlit as st
import pandas as pd
import pickle

# Load the trained model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

# Streamlit app title
st.title("💰 Gold Price Prediction App")

st.write("Enter the following values to predict the Gold Price (GLD):")

# User inputs for predictors
spx = st.number_input('S&P 500 Index (SPX):', value=6840.200195)
slv = st.number_input('Silver Price (SLV):', value=44.009998)
uso = st.number_input('Oil Price (USO):', value=72.559998)
eur_usd = st.number_input('EUR/USD Exchange Rate:', value=1.157247)

# Create input DataFrame
input_data = {
    'SPX': [spx],
    'SLV': [slv],
    'USO': [uso],
    'EUR/USD': [eur_usd]
}
input_df = pd.DataFrame(input_data)

# Match the column order with training
input_df = input_df[scaler.feature_names_in_]

# Add a Predict button
if st.button("🔮 Predict Gold Price"):
    # Scale the input data
    scaled_input = scaler.transform(input_df)

    # Make prediction
    prediction = model.predict(scaled_input)

    # Display the result
    st.success(f"Predicted Gold Price (GLD): **{prediction[0]:.2f}** USD")

