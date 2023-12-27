"""
This is a boilerplate pipeline 'Evaluation'
generated using Kedro 0.19.1
"""
from sklearn.metrics import average_precision_score
import logging
def evaluate(y_test,y_pred):
    '''
    Evaluates the perfomance of model on unseen data
    args:actual output,predicted output
    returns:Average precision score
    '''
    try:
        #To evaluate the perfomance of the model
        auprc = average_precision_score(y_test, y_pred)
        print("The Area under Precision Recall Curve Score is", auprc)
        return {"Average precision score": auprc}
    except Exception as e:
        logging.ERROR(f"Error occured while evaluating the model {e}")
        raise e