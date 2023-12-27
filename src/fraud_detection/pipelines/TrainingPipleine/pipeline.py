"""
This is a boilerplate pipeline 'TrainingPipleine'
generated using Kedro 0.19.1
"""

from kedro.pipeline import Pipeline, pipeline,node
from .nodes import training

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([node(func=training,inputs=["x_train_sc","y_train","x_test_sc"],outputs=["model","y_pred"])])
