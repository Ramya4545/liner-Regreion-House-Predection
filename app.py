

import streamlit as st
import pandas as pd
import joblib




model = joblib.load("house_price_model.pkl")


=

st.title("House Price Prediction")

st.write("Enter the house details to predict the price.")




area = st.number_input(
    "Area (Sq. Ft)",
    min_value=300,
    max_value=5000,
    value=2000,
    step=50
)




floors = st.number_input(
    "Total Floors",
    min_value=1,
    max_value=20,
    value=4,
    step=1
)




bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    max_value=10,
    value=3,
    step=1
)




if st.button("Predict Price"):


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




    prediction = model.predict(input_data)


  

    st.success(
        "Predicted House Price: "
        + str(round(prediction[0], 2))
        + " Lakhs"
    )



