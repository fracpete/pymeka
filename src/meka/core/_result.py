from typing import List, Set
from jpype import JClass
from weka.core.classes import JavaObject
from weka.core.dataset import Instance


class Result(JavaObject):
    """
    Wrapper for evaluation results.
    """

    def __init__(self, jobject=None, N: int = None, L: int = None):
        """
        Initializes the wrapper with the specified Java object.
        If L or N and L are supplied, a new Result object is instantiated rather than
        wrapping an existing one

        :param jobject: the Java object to wrap
        :type jobject: JPype object
        :param N: capacity
        :type N: int
        :param L: cardinality
        :type L: int
        """
        if (N is not None) and (L is not None):
            jobject = JClass("meka.core.Result")(N, L)
        elif N is not None:
            jobject = JClass("meka.core.Result")(N)
        super().__init__(jobject=jobject)

    def __len__(self):
        """
        Returns the number of value-prediction pairs stared in this Result.

        :return: the number or pairs
        :rtype: innt
        """
        return self.jobject.size()

    def add_result(self, pred: List[float], real: Instance):
        """
        Adds an entry.

        :param pred: the prediction list
        :type pred: list
        :param real: the Instance with the ground truth
        :type real: Instance
        """
        self.jobject.addResult(pred, real.jobject)

    def row_true(self, i: int) -> List[int]:
        """
        Retrieve the true values for the i-th instance.

        :param i: the row index
        :type i: int
        :return: the true values
        :rtype: list
        """
        return self.jobject.rowTrue(i)

    def row_confidence(self, i: int) -> List[float]:
        """
        Retrieve the prediction confidences for the i-th instance.

        :param i: the row index
        :type i: int
        :return: the confidence values
        :rtype: list
        """
        return self.jobject.rowConfidence(i)

    def row_prediction(self, i: int, t: float = None) -> List[int]:
        """
        Retrieve the predicted values for the i-th instance according to threshold t.

        :param i: the row index
        :type i: int
        :param t: the threshold to use, if None, uses the threshold stored under "Threshold"
        :type t: float
        :return: the predicted values
        :rtype: list
        """
        if t is None:
            return self.jobject.rowPrediction(i)
        else:
            return self.jobject.rowPrediction(i, t)

    def col_confidence(self, j: int) -> List[float]:
        """
        Retrieve the prediction confidences for the j-th label (column).

        :param j: the column index
        :type j: int
        :return: the prediction confidences
        :rtype: list
        """
        return self.jobject.colConfidence(j)

    def all_predictions(self, t: float = None):
        # TODO
        return None

    def all_true_values(self):
        # TODO
        return None

    def available_metrics(self) -> Set[str]:
        """
        Return the set of metrics for which measurements are available.

        :return: the metrics
        :rtype: set
        """
        return self.jobject.availableMetrics()

