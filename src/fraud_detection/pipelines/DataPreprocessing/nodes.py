"""
This is a boilerplate pipeline 'DatPreprocessing'
generated using Kedro 0.19.1
"""
import pandas as pd 
from imblearn.over_sampling import SMOTE
import logging
def preprocess(raw):
    '''
        This function cleans the data by performing categorical encoding,removing unnecessary columns,feature engineering,handling imbalanced target variable
        Args:raw data in csv format
        Returns:cleaned data frame,resampled train data,resampled test data
    '''
    try:
        df=pd.DataFrame(raw)
  
        #Removing unwanted columns
        df = df.drop(['nameDest','nameOrig'], axis = 1)

        #Feature Engineering
        df['errorBalanceOrig'] = df.newbalanceOrig + df.amount - df.oldbalanceOrg
        df['errorBalanceDest'] = df.oldbalanceDest + df.amount - df.newbalanceDest
        df=df.drop(['newbalanceOrig','oldbalanceOrg','oldbalanceDest','newbalanceDest'],axis=1)

        type_mapping = {'CASH_OUT':0,'PAYMENT':1,'CASH_IN':2,'TRANSFER':3,'DEBIT':4}

        # Use the map function to encode the 'type' column
        df['type_encoded'] = df['type'].map(type_mapping)   
        df=df.drop('type',axis=1)

        x=df.drop('isFraud',axis=1)
        y=df['isFraud']
        x_resample, y_resample = SMOTE().fit_resample(x, y.values.ravel())

        # getting the shapes of x and y after resampling
        print("Shape of x: ", x_resample.shape)
        print("Shape of y:", y_resample.shape)

        return df,x_resample,y_resample
    except Exception as e:
        logging.ERROR(f"Error occured in data preprocessing {e}")
        raise e
