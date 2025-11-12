import pandas as pd
import streamlit as st 
import joblib

# Load the model
model = joblib.load('xgb_model.jb')

st.title("🏠 House Price Prediction")
st.write("Enter the details below to predict the house price:")

# Define input features
inputs = ['OverallQual', 'GrLivArea', 'GarageArea', '1stFlrSF',
          'FullBath', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'Fireplaces',
          'BsmtFinSF1', 'LotFrontage', 'WoodDeckSF', 'OpenPorchSF', 'LotArea',
          'CentralAir']

# Collect user input
input_data = {}
for feature in inputs:
    if feature == 'CentralAir':
        input_data[feature] = st.selectbox(f"{feature}", options=['Yes', 'No'], index=0)
    else:
        input_data[feature] = st.number_input(
            f"{feature}",
            value=0.0,
            step=1.0 if feature in ['OverallQual', 'FullBath', 'Fireplaces'] else 0.1
        )

# Predict when button is clicked
if st.button("Predict Price"):
    # Convert 'CentralAir' to numeric
    input_data['CentralAir'] = 1 if input_data['CentralAir'] == "Yes" else 0

    # Create DataFrame
    input_df = pd.DataFrame([input_data], columns=inputs)

    # Make prediction
    predictions = model.predict(input_df)

    # Display result
    st.success(f"Predicted House Price: ${predictions[0]:,.2f}")
