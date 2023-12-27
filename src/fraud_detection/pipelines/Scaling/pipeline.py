"""
This is a boilerplate pipeline 'Scaling'
generated using Kedro 0.19.1
"""

from kedro.pipeline import Pipeline, pipeline,node

from .nodes import standard
def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([node(func=standard,inputs=["x_train","x_test"],outputs=["x_train_sc","x_test_sc"])])
