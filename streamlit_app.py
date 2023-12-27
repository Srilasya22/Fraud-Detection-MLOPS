import streamlit as st
import pandas as pd
import joblib
import numpy as np 

st.sidebar.header("Model Prediction or Report")

selection = st.sidebar.selectbox("Select anyone from below", ["Model Prediction","Data Integrity","Feature Drift", "Label Drift"])

if selection == "Model Prediction":
        st.header("Fraud Detection Model")
        def predict(step,amount,isFlaggedFraud,errorBalanceOrig,errorBalanceDest, type_mapping):
            if type_mapping == 'CASH_OUT':
                type_mapping=0
            elif type_mapping == 'PAYMENT':
                 type_mapping=1
            elif type_mapping == 'CASH_IN':
                 type_mapping=2
            elif type_mapping == 'TRANSFER':
                 type_mapping=3
            else:
                type_mapping=4

            if isFlaggedFraud == 'NOT FRAUD':
                 isFlaggedFraud=0
            else:
                 isFlaggedFraud=1
            step = int(step)
            isFlaggedFraud = int(isFlaggedFraud)
            type_mapping = int(type_mapping)
            errorBalanceOrig = float(errorBalanceOrig)
            errorBalanceDest = float(errorBalanceDest)
            input=np.array([[step,amount,isFlaggedFraud,errorBalanceOrig,errorBalanceDest,type_mapping]]).astype(np.float64)
    
        
            model = joblib.load('models/model.pkl')
    # Make prediction
            prediction = model.predict(input)
            prediction= np.round(prediction)
    # Return the predicted value for isFraud
            return prediction
        
        step = st.number_input('Enter the step',min_value = 0)
        amount = st.number_input('Enter the amount',min_value = 0)
        isFlaggedFraud = st.radio("isFlaggedFraud",('NOT FRAUD','FRAUD'))
      
        errorBalanceOrig = st.number_input('Enter the amount which is difference between actual balance and new balance of person after initiating transaction',min_value =-100000.0)   
        errorBalanceDest = st.number_input('Enter the amount which is difference between actual balance and new balance of receiver after completion of transaction',min_value = 0.0)
        type_encoded = st.radio("Type",('CASH_IN','PAYMENT','CASH_OUT','DEBIT','TRANSFER'))

        if st.button("Predicted Output"): 
             output = predict(step,amount,isFlaggedFraud,errorBalanceOrig,errorBalanceDest, type_encoded)
             if output==0:
                  output1="Not Fraud"
             else:
                  output1="Fraud"  
             st.success("The transaction is: {}".format(output1)) 
else:
    st.header("Fraud Detection Monitoring Report")
    report_file_name = "report/"+ selection.replace(" ", "") + ".html"
    HtmlFile = open(report_file_name, 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    st.components.v1.html(source_code, width=1200, height=1500, scrolling=True)
