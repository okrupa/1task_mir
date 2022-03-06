import streamlit as st
import pandas as pd
import numpy as np
import re

import datetime

from models.get_prediction import get_model_prediction, get_date
from data import get_data
from models.get_model_type import get_model_type


st.title("Delivery data prediction")

st.markdown('''This application was created to approximate the delivery time of an order.
The application returns information about the delivery time of the order with the accuracy of the day and time.

The service makes predictions based on the data provided:
* City
* Delivery company
* Purchase time
* Model type

The app allows you to predict delivery times for 3 courier companies, in any city by specifying the date of purchase. 
The user can choose the model which will be used to calculate the prediction
''')


form = st.form(key="submit-form")
input_text = re.sub("\s+", " ", form.text_input("City"))
first_company = 360
second_company = 516
third_company = 620
d_company = form.selectbox("Choose delivery company", [first_company, second_company, third_company])
p_data = form.date_input("Purchase date")
p_time = form.time_input('Purchase time')
simple_model = "Simple model"
random_forest = "Random forest"
model_type = form.selectbox("Choose model type", [simple_model, random_forest])
generate = form.form_submit_button("Predict delivery time")

if generate:
    purchase_timestamp = datetime.datetime.combine(p_data,p_time)
    if model_type =="Simple model":
        model_t = 0
    else:
        model_t = 1
    data = {"city": input_text, "delivery_company": d_company, "purchase_timestamp": purchase_timestamp, "model": model_t}
    df = get_data(data)
    model = data["model"]
    model = get_model_type(data["model"])
    p = get_model_prediction(model, df)

    pred_date = get_date(data, p)

    new_title = f'<p style="font-family:serif; color:Black; font-size: 22px;">Date of purchase: {purchase_timestamp}</p>'
    st.markdown(new_title, unsafe_allow_html=True)

    mess = "Expected delivery time: " + pred_date
    new_title = f'<p style="font-family:serif; color:Black; font-size: 32px;">Expected delivery time: </p> <p style="font-family:sans-serif; color:Green; font-size: 38px;">{pred_date}</p>'
    st.markdown(new_title, unsafe_allow_html=True)