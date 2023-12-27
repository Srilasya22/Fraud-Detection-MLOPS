"""
This is a boilerplate pipeline 'TrainingPipleine'
generated using Kedro 0.19.1
"""
import xgboost as xgb
from xgboost.sklearn import XGBClassifier
import logging
def training(x_train_sc,y_train,x_test_sc):
    '''
    Train the model
    args:Scaled training input,training output,Scaled testing input
    Returns:trained model,predicted output for test data
    '''
    try:
        model = XGBClassifier()
        model.fit(x_train_sc, y_train)
        y_pred = model.predict(x_test_sc)
        return model,y_pred
    except Exception as e:
        logging.ERROR(f"Error occured in data training {e}")
        raise e