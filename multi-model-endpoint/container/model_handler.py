# custom service file

# model_handler.py

"""
ModelHandler defines a base model handler.
"""
import logging


class ModelHandler(object):
    """
    A base Model handler implementation.
    """

    def __init__(self):
        self.error = None
        self._context = None
        self._batch_size = 0
        self.initialized = False

    def initialize(self, context):
        """
        Initialize model. This will be called during model loading time
        :param context: Initial context contains model server system properties.
        :return:
        """
        
        logging.info("GGGGGG - enter initialize")
        self._context = context
        self._batch_size = context.system_properties["batch_size"]
        self.initialized = True
        logging.info("GGGGGG - exit initialize")

    def preprocess(self, batch):
        
        """
        Transform raw input into model input data.
        :param batch: list of raw requests, should match batch size
        :return: list of preprocessed model input data
        """
        # Take the input data and pre-process it make it inference ready
        logging.info("GGGGGG - enter preprocess")
        assert self._batch_size == len(batch), "Invalid input batch size: {}".format(len(batch))
        logging.info("GGGGGG - exit preprocess")
        return None

    def inference(self, model_input):
        """
        Internal inference methods
        :param model_input: transformed model input data
        :return: list of inference output in NDArray
        """
        # Do some inference call to engine here and return output
        logging.info("GGGGGG - enter inference")
        logging.info("GGGGGG - exit inference")
        return None

    def postprocess(self, inference_output):
        """
        Return predict result in batch.
        :param inference_output: list of inference output
        :return: list of predict results
        """
        # Take output from network and post-process to desired format
        logging.info("GGGGGG - enter postprocess")
        logging.info("GGGGGG - exit postprocess")
        return ["OK"] * self._batch_size
        
    def handle(self, data, context):
        """
        Call preprocess, inference and post-process functions
        :param data: input data
        :param context: mms context
        """
        
        logging.info("GGGGGG - enter handle")
        
        model_input = self.preprocess(data)
        model_out = self.inference(model_input)
        logging.info("GGGGGG - exiting handle")
        return self.postprocess(model_out)

_service = ModelHandler()


def handle(data, context):
    if not _service.initialized:
        _service.initialize(context)

    if data is None:
        return None

    return _service.handle(data, context)