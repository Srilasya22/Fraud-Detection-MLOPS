"""
This is a boilerplate pipeline 'Evaluation'
generated using Kedro 0.19.1
"""

from kedro.pipeline import Pipeline, pipeline,node

from .nodes import evaluate
def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([node(func=evaluate,inputs=["y_test","y_pred"],outputs="metrics")])
