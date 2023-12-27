"""
This is a boilerplate pipeline 'TrainTestSplit'
generated using Kedro 0.19.1
"""

from kedro.pipeline import Pipeline, pipeline,node
from .nodes import split


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([node(func=split,inputs=["x_resampled","y_resampled"],outputs=["x_train","y_train","x_test","y_test"])])
