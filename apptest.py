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



pickle_in = open("zillowmodel.pkl","rb")
zillowmodel=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def ratio_prediction(zipcode,yearBuilt,livingArea,bathrooms,annualHomeownersInsurance,bedrooms,monthlyHoaFee):
    
    """Rent to Price Ratio Prediction Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: zipcode
        in: query
        type: number
        required: true
      - name: yearBuilt
        in: query
        type: number
        required: true
      - name: livingArea
        in: query
        type: number
        required: true
      - name: bathrooms
        in: query
        type: number
        required: true
      - name: annualHomeownersInsurance
        in: query
        type: number
        required: true
      - name: bedrooms
        in: query
        type: number
        required: true
      - name: monthlyHoaFee
        in: query
        type: number
        required: true
      
    responses:
        200:
            description: The output values
        
    """
   
    prediction=zillowmodel.predict([[zipcode,yearBuilt,livingArea,bathrooms,annualHomeownersInsurance,bedrooms,monthlyHoaFee]])
    print(prediction)
    return prediction



def main():
    st.title("Rent to Price Ratio Prediction in Baltimore County")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Rent to Price Prediction in Baltimore County ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    zipcode = st.text_input("zipcode","Type Here")
    yearBuilt = st.text_input("yearBuilt","Type Here")
    livingArea = st.text_input("livingArea","Type Here")
    bathrooms = st.text_input("bathrooms","Type Here")
    annualHomeownersInsurance = st.text_input("annualHomeownersInsurance","Type Here")
    bedrooms = st.text_input("bedrooms","Type Here")
    monthlyHoaFee = st.text_input("monthlyHoaFee","Type Here")
    result=""
    if st.button("Predict"):
        result=ratio_prediction(zipcode,yearBuilt,livingArea,bathrooms,annualHomeownersInsurance,bedrooms,monthlyHoaFee)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    