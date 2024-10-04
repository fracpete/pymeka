from jpype import JClass
from meka.core import Result


class IncrementalEvaluation:
    """
    Wrapper around the multi-label/target IncrementalEvaluation class.
    """

    def __init__(self):
        """
        Initializes the object.
        """
        self.jclass = JClass("meka.classifiers.IncrementalEvaluation")
