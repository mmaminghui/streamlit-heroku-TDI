#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 16:30:31 2022

@author: minghuima
"""

import streamlit as st
import pickle
import numpy as np
import pandas as pd


pickle_in = open("renttopricemodel.pkl","rb")
renttopricemodel=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def ratio_prediction(zipcode,longitude,latitude,yearbuilt,livingarea,bathrooms,annualhomeownersinsurance,bedrooms,monthlyhoafee):
    
    """Rent to Price Ratio Prediction Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: zipcode
        in: query
        type: number
        required: true
      - name: longitude
        in: query
        type: number
        required: true
      - name: latitude
        in: query
        type: number
        required: true
      - name: yearbuilt
        in: query
        type: number
        required: true
      - name: livingarea
        in: query
        type: number
        required: true
      - name: bathrooms
        in: query
        type: number
        required: true
      - name: annualhomeownersinsurance
        in: query
        type: number
        required: true
      - name: bedrooms
        in: query
        type: number
        required: true
      - name: monthlyhoafee
        in: query
        type: number
        required: true
      
    responses:
        200:
            description: The output values
        
    """
   
    prediction=renttopricemodel.predict([[zipcode,longitude,latitude,yearbuilt,livingarea,bathrooms,annualhomeownersinsurance,bedrooms,monthlyhoafee]])
    print(prediction)
    return prediction



def main():
    st.title("Rent to Price Ratio Prediction App for Rental Property Investors")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Does your target house meet the 1% rule? 
    Note: Investopedia suggests that monthly rent is greater than 1% of the purchase price </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    zipcode = st.text_input("zipcode","Type Here")
    longitude = st.text_input("longitude","Type Here")
    latitude = st.text_input("latitude","Type Here")
    yearbuilt = st.text_input("yearbuilt","Type Here")
    livingarea = st.text_input("livingarea","Type Here")
    bathrooms = st.text_input("bathrooms","Type Here")
    annualhomeownersinsurance = st.text_input("annualhomeownersinsurance","Type Here")
    bedrooms = st.text_input("bedrooms","Type Here")
    monthlyhoafee = st.text_input("monthlyhoafee","Type Here")
    result=""
    if st.button("Predict"):
        result=ratio_prediction(zipcode,longitude,latitude,yearbuilt,livingarea,bathrooms,annualhomeownersinsurance,bedrooms,monthlyhoafee)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("This app is based on the transaction data (2022.1-2022.6) in Baltimore County")
        st.text("This app can be customized for your local area")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    