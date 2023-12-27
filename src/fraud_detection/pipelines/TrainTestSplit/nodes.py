"""
This is a boilerplate pipeline 'TrainTestSplit'
generated using Kedro 0.19.1
"""

from sklearn.model_selection import train_test_split
import logging
def split(x_resampled,y_resampled):
    '''
    The function splits the data into training set and testing set
    args:The balanced data
    Returns:
    x_train:Training input data
    y_train:Training target variable
    x_test:Testing output data
    y_test:Testing target variable
    '''
    try:
        x_train, x_test, y_train, y_test = train_test_split(x_resampled, y_resampled, test_size = 0.2, random_state = 42)

        # checking the new shapes
        print("Shape of x_train: ", x_train.shape)
        print("Shape of x_test: ", x_test.shape)
        print("Shape of y_train: ", y_train.shape)
        print("Shape of y_test: ", y_test.shape)
        return x_train,y_train,x_test,y_test
    except Exception as e:
        logging.ERROR(f"Error occured while spplitting the data {e}")
        raise e