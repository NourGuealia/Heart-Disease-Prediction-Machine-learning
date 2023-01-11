import streamlit as st
import pandas as pd
import numpy as np
import pickle



st.set_page_config(  # Alternate names: setup_page, page, layout
	layout="centered",  # Can be "centered" or "wide". In the future also "dashboard", etc.
	initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
	page_title=None,  # String or None. Strings get appended with "• Streamlit". 
	page_icon=None,  # String, anything supported by st.image, or None.
)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



# import the model :
model = pickle.load(open('./code/model.sav', 'rb'))

st.title("Heart Disease Prediction using")
st.text("Heart Disease Prediction using application Machine Learning model")
result = st.text("")
col1 , col2 , col3 = st.columns(3)

with col1 : 
  age = st.number_input('Age' , min_value=1 , step=1)
 

with col2:
  sex = st.radio(
    "Sex",
    ('M', 'F'))
  if sex == 'M':
    sex=1
  else:
    sex=0
with col3 : 
  cp = st.number_input('Chest Pain types' , min_value=0 , max_value=3 , step=1)

with col1 : 
  trestbps = st.number_input('Resting Blood Pressure' , min_value=50 , max_value=200 , step=50)

with col2:
    chol = st.number_input('Serum Cholestoral in mg/dl' , min_value=20 , max_value=300 , step=5)

with col3 : 
  fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl' , min_value=50 , max_value=200 , step=5)

with col1:
  restecg = st.number_input('Resting Electrocardiographic results')

with col2:
  thalach = st.number_input('Maximum Heart Rate achieved')

with col3:
  exang = st.number_input('Exercise Induced Angina')

with col1:
  oldpeak = st.number_input('ST depression induced by exercise')

with col2:
  slope = st.number_input('Slope of the peak exercise ST segment')

with col3:
  ca = st.number_input('Major vessels colored by flourosopy')

with col1:
  thal = st.selectbox(
    'Thalassemia',
    ('normal', 'fixed', 'defect'))
  if thal :
    if thal== 'normal' : 
      thal = 0
    if thal == 'fixed':
      thal = 1
    if thal == 'defect' : 
      thal = 2

  #thal = st.text_input('thal: 0  : normal; 1 : fixed defect; 2 : reversable defect')

# text for Prediction
diagnosis = ''

## [63,1,3,145,233,1,0,150,0,2.3,0,0,1] ==> 1 : The person is having heart disease
## [57,0,0,140,241,0,1,123,1,0.2,1,0,3] ==> 0 : The person does not have any heart disease
if st.button('Get the diagnosis') : 
  prediction = model.predict([[57,0,0,140,241,0,1,123,1,0.2,1,0,3]])
  if (prediction[0] == 1):
    diagnosis = 'The person is having heart disease'
  else:
    diagnosis = 'The person does not have any heart disease'
  result.success(diagnosis)
  #st.success(diagnosis)

 
