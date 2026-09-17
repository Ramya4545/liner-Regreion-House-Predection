```python
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("house_price_model.pkl")

# Page title
st.title("🏠 House Price Prediction")

st.write("Enter the house area to predict the price.")

# User input
area = st.number_input(
    "House Area (sq.ft)",
    min_value=500,
    max_value=5000,
    value=1600,
    step=100
)

# Prediction button
if st.button("Predict Price"):

    # Create input DataFrame
    input_data = pd.DataFrame({
        "Area": [area]
    })

    # Predict
    prediction = model.predict(input_data)

    # Display result
    st.success(
        f"Predicted House Price: {prediction[0]:.2f}"
    )

    st.info("Price is based on the training data.")
```
