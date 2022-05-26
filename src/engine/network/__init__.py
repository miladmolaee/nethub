from abc import ABC, abstractclassmethod

class Network(ABC):
    """_summary_

    Returns:
        _description_
    """

    # constants --------------------------------------------------------------------------------------------------------
    INPUT_LAYER: str = 'input-layer'
    OUTPUT_LAYER: str = 'output-layer'
    HIDDEN_LAYER: str = 'hidden-layer'

    # data -------------------------------------------------------------------------------------------------------------
    data: object

    input_training_data: object
    output_training_data: object

    input_validation_data: object
    output_validation_data: object

    input_dimension: int
    output_dimension: int

    batch_size: int

    # network structure ------------------------------------------------------------------------------------------------
    layers: list

    # execution --------------------------------------------------------------------------------------------------------
    max_epoch: int

    # result -----------------------------------------------------------------------------------------------------------
    predictions: object
    
    def __str__(self):
        return 'this is a neural network'

