import pandas as pd
import numpy as np
import streamlit as st
from utils.models.model import getprediction
from utils.models.scalar import input_scalar

st.set_page_config(page_title="University Admission Check App",
                   page_icon="🚧", layout="wide")

options_Research = [0,1]

with st.form('prediction_form'):
    
    st.subheader("Enter the input for following features:")
        
    Gre_score = st.number_input(label = "GRE_Score:",min_value=0.00, max_value=340.00, step=1.0, value=0.00)
    Toefl_score = st.number_input(label = "Toefl_Score:",min_value=0.00, max_value=120.00, step=1.0, value=0.00)
    University_Rating = st.slider(label = "University_Rating:",min_value=0.00, max_value=5.0, step=1.0, value=0.00)
    SOP_score = st.slider(label = "SOP_score:",min_value=0.00, max_value=5.0, step=1.0, value=0.00)
    LOR_score = st.slider(label = "LOR_score:",min_value=0.00, max_value=5.0, step=0.10, value=0.00)
    CGPA_score = st.number_input(label = "CGPA_score:",min_value=0.00, max_value=10.0, step=0.01, value=0.00)
    Research_score = st.selectbox("Select Score: ",options=options_Research)
        
        
    submit = st.form_submit_button("Predict")
    
    
if submit:
    
    input_dict = {
    
    "Gre_score" : Gre_score,
    "Toefl_Score" : Toefl_score,
    "University_Rating" : University_Rating,
    "SOP_score" : SOP_score,
    "LOR_score" : LOR_score,
    "CGPA_score" : CGPA_score,
    "Research_score" : Research_score}
    
    
    attr_df = pd.DataFrame(input_dict, index=[1])
    input_scaled = input_scalar(attr_df)
    
    pred = getprediction(data=input_scaled, model=model)
    
    st.write(f"The predicted Possibility is:{pred}")
    
        

        
        
  

 