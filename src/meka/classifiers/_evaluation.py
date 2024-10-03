from jpype import JClass
from meka.core import Result


class Evaluation:
    """
    Wrapper around the multi-label/target Evaluation class.
    """

    def __init__(self):
        """
        Initializes the object.
        """
        self.jclass = JClass("meka.classifiers.Evaluation")
