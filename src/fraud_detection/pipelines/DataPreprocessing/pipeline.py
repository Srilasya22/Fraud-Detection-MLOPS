"""
This is a boilerplate pipeline 'DatPreprocessing'
generated using Kedro 0.19.1
"""

from kedro.pipeline import Pipeline, pipeline,node
from .nodes import preprocess

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([node(
        func=preprocess,
        inputs="raw_data",
        outputs=["processed_data","x_resampled","y_resampled"]
    )])
