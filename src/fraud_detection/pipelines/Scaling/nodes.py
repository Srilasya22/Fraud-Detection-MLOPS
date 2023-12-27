"""
This is a boilerplate pipeline 'Scaling'
generated using Kedro 0.19.1
"""

from sklearn.preprocessing import StandardScaler
import logging
def standard(x_train,x_test):
    '''
    This function performs standardization
    Args:training input,testing input
    Returns:Scaled training input,Scaled testing input
    '''
    try:
        sc = StandardScaler()
        x_train_sc = sc.fit_transform(x_train)
        x_test_sc = sc.transform(x_test)
        return x_train_sc,x_test_sc
    except Exception as e:
        logging.ERROR(f"Error occured while sacling data {e}")
        raise e