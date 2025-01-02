# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 17:39:07 2025

@author: KARTHIK
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav','rb'))

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System', ['Diabetes Prediction',
                                                                 'Heart Disease Prediction',
                                                                 'Parkinsons Prediction'],
                           icons=['activity','heart','person'], default_index=0)
    

if(selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')
    
    Pregnancies = st.text_input('Number of pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin thickness value')
    Insulin = st.text_input('insulin level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the person')
    
    diabetes_diagnosis=''
    
    if st.button('Diabetes Test Result'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if(diabetes_prediction[0] == 1):
            diabetes_diagnosis = 'The person is diabetic'
        else:
            diabetes_diagnosis = 'The person is not diabetic'
            
    st.success(diabetes_diagnosis)
    
    
# Heart Disease prediction

if(selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML')
    
    age = st.text_input('age')
    sex = st.text_input('sex')
    cp = st.text_input('cp')
    trestbps = st.text_input('trestbps')
    chol = st.text_input('chol')
    fbs = st.text_input('fbsl')
    restecg = st.text_input('restecg')
    thalach = st.text_input('thalach')
    exang = st.text_input('exang')
    oldpeak = st.text_input('oldpeak')
    slope = st.text_input('slope')
    ca = st.text_input('ca')
    thal = st.text_input('thal')
    
    heart_disease_diagnosis=''
    
    if st.button('Heart Disease Test Result'):
        heart_disease_prediction = heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if(heart_disease_prediction[0] == 1):
            heart_disease_diagnosis = 'The person is having heart disease'
        else:
            heart_disease_diagnosis = 'The person not have any heart disease'
            
    st.success(heart_disease_diagnosis)

