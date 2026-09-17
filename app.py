import streamlit as st
import pandas as pd
import joblib


# Load trained model
model = joblib.load("house_price_model.pkl")


# Title
st.title("House Price Prediction")

st.write("Enter the house details to predict the price.")


# Area input
area = st.number_input(
    "Area (Sq. Ft)",
    min_value=300,
    max_value=5000,
    value=2000,
    step=50
)


# Total Floors input
floors = st.number_input(
    "Total Floors",
    min_value=1,
    max_value=20,
    value=4,
    step=1
)


# Bedrooms input
bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    max_value=10,
    value=3,
    step=1
)


# Predict button
if st.button("Predict Price"):

    # Create input data
    input_data = pd.DataFrame(
        [
            [
                area,
                floors,
                bedrooms
            ]
        ],
        columns=[
            "Area_Sq_Ft",
            "Total_Floors",
            "Bedrooms"
        ]
    )

    # Make prediction
    prediction = model.predict(input_data)

    # Display prediction
    st.success(
        "Predicted House Price: "
        + str(round(prediction[0], 2))
        + " Lakhs"
    )
