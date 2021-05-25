import streamlit as st
import math
import sys
import pickle
import numpy as np 
from matplotlib import pyplot as plt

st.markdown("<h1 align='center'> FAMER'S AMIGO </h1>",unsafe_allow_html=True)

st.title('Crop Prediction')
Nitrogen = st.selectbox('Nitrogen',(range(0,141)))
Phosphorous = st.selectbox('Phosphorous',(range(5,146)))
potasium = st.selectbox('potassium',(range(5,205)))
temperature = st.selectbox('temperature',(range(9,44)))
Ph = st.selectbox('Ph',(range(0,100)))
humidity = st.selectbox('Humidity',(range(15,99)))
Rainfall = st.selectbox('rainfall',(range(20,298)))

Soil_composition_list = [Nitrogen,Phosphorous,potasium,temperature,humidity,Ph,Rainfall]

col1, col2, col3 = st.beta_columns(3)
if col2.button('Click to konow suitabe crop'):

        loaded_model = pickle.load(open('Crop_recommendation_model.sav', 'rb'))
        result = loaded_model.predict(np.array(Soil_composition_list).reshape(1,7))
        st.markdown(f"<h1 align='center'> Predicted crop is {result[0]} </h1>",unsafe_allow_html=True)
        if result[0] != 'rice' or result[0] != 'maize':
            st.markdown(f"<h2 align='center'> Due to lack of data for the crop {result[0]} cant get the forcasting prices . Forcasting prices for rice and maize are shown below </h2>",unsafe_allow_html=True)
            st.markdown('<h3>Price forcasting for Maize crop</h3>',unsafe_allow_html=True)
            rice_forcasting = pickle.load(open('Rice_forcasting.sav', 'rb'))
            forcast = rice_forcasting.predict()
            fig, ax = plt.subplots()
            ax.plot(forcast['ds'],forcast['yhat'])
            st.pyplot(fig)
            st.markdown('<h3>Price forcasting for Maize crop</h3>',unsafe_allow_html=True)
            rice_forcasting = pickle.load(open('Maize_forcasting.sav', 'rb'))
            forcast = rice_forcasting.predict()
            fig, ax = plt.subplots()
            ax.plot(forcast['ds'],forcast['yhat'])
            st.pyplot(fig)
        elif result[0] == 'rice':
            st.markdown('<h3>Price forcasting for Maize crop</h3>',unsafe_allow_html=True)
            rice_forcasting = pickle.load(open('Rice_forcasting.sav', 'rb'))
            forcast = rice_forcasting.predict()
            fig, ax = plt.subplots()
            ax.plot(forcast['ds'],forcast['yhat'])
            st.pyplot(fig)
        else:
            st.markdown('<h3>Price forcasting for Maize crop</h3>',unsafe_allow_html=True)
            rice_forcasting = pickle.load(open('Maize_forcasting.sav', 'rb'))
            forcast = rice_forcasting.predict()
            fig, ax = plt.subplots()
            ax.plot(forcast['ds'],forcast['yhat'])
            st.pyplot(fig)


