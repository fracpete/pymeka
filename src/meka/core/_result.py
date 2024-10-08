import numpy as np
from typing import List, Set, Any, Dict
from jpype import JClass
from weka.core.classes import JavaObject
from weka.core.dataset import Instance, Instances


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

        :return: the number of pairs
        :rtype: int
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
        """
        Returns all prediction confidences in an L * N matrix (2d array). Optionally according to threshold t.

        :param t: the optional threshold
        :type t: float
        :return: the matrix
        :rtype: np.ndarray
        """
        if t is None:
            m = self.jobject.allPredictions()
        else:
            m = self.jobject.allPredictions(t)
        return np.asarray(m)

    def all_true_values(self):
        """
        Retrieve all true values in an L x N matrix.

        :return: the matrix
        :rtype: np.ndarray
        """
        return np.asarray(self.jobject.allTrueValues())

    def available_metrics(self) -> Set[str]:
        """
        Return the set of metrics for which measurements are available.

        :return: the metrics
        :rtype: set
        """
        return self.jobject.availableMetrics()

    def set_measurement(self, metric: str, stat: Any):
        """
        Sets the measurement for the specified metric.

        :param metric: the metric to set
        :type metric: str
        :param stat: the metric value
        """
        self.jobject.setMeasurement(metric, stat)

    def get_measurement(self, metric: str) -> Any:
        """
        Retrieves the measurement for the specified metric.

        :param metric: the metric to retrieve
        :type metric: str
        :return: the measurement
        """
        return self.jobject.getMeasurement(metric)

    def set_value(self, metric: str, value: float):
        """
        Sets the value for the specified metric.

        :param metric: the metric to set
        :type metric: str
        :param value: the value to set
        :type value: float
        """
        self.jobject.setValue(metric, value)

    def get_value(self, metric: str) -> float:
        """
        Retrieves the value for the specified metric.

        :param metric: the metric to retrieve
        :type metric: str
        :return: the associated value
        :rtype: float
        """
        return self.jobject.getValue(metric)

    def set_info(self, cat: str, val: str):
        """
        Sets the value in the information category.

        :param cat: the category to store under
        :type cat: str
        :param val: the value to set
        :type val: str
        """
        self.jobject.setInfo(cat, val)

    def get_info(self, cat: str) -> str:
        """
        Retrieves the value from the information category.

        :param cat: the category to retrieve
        :type cat: str
        :return: the value
        :rtype: str
        """
        return self.jobject.getValue(cat)

    def set_model(self, key: str, val: str):
        """
        Stores the model under the specified key.

        :param key: the key to store the model under
        :type key: str
        :type val: the model string
        :type val: str
        """
        self.jobject.setModel(key, val)

    def get_model(self, key: str) -> str:
        """
        Retrieves the specified model string.

        :param key: the key of the model to retrieve
        :type key: str
        :return: the model string
        :rtype: str
        """
        return self.jobject.getModel(key)

    @classmethod
    def stats(cls, r: 'Result', vop: str) -> Dict[str, Any]:
        """
        Return the evaluation statistics given predictions and real values stored in the result.
        In the multi-label case, a Threshold category must exist, containing a string
        defining the type of threshold we want to use/calibrate.

        :param r: the result object to use
        :type r: Result
        :param vop: the verbosity option
        :type vop: str
        :return: the stats
        :rtype: dict
        """
        return JClass("meka.core.Result").getStats(r.jobject, vop)

    @classmethod
    def result_as_string(cls, r: 'Result', num_decimals: int = 3) -> str:
        """
        Print out each prediction in a Result (to a certain number of decimal points) along with its true labelset.

        :param r: the Result to process
        :type r: Result
        :param num_decimals: the number of decimals to use
        :type num_decimals: int
        :return: the generated output
        :rtype: str
        """
        return JClass("meka.core.Result").getResultAsString(r.jobject, num_decimals)

    @classmethod
    def predictions_as_instances(cls, r: 'Result') -> Instances:
        """
        Convert predictions into Instances (and true values).
        The first L attributes (for L labels) hold the true values, and the next L attributes hold the predictions.

        :param r: the Result to process
        :type r: Result
        :return: the generated data
        :rtype: Instances
        """
        return Instances(jobject=JClass("meka.core.Result").getPredictionsAsInstances(r.jobject))

    @classmethod
    def results_as_instances(cls, metrics: List[Dict[str, Any]]) -> Instances:
        """
        Convert a list of Results into Instances.

        :param metrics: the results to convert
        :type metrics: list
        :return: the generated data
        :rtype: Instances
        """
        return Instances(JClass("meka.core.Result").getResultsAsInstances(metrics))
