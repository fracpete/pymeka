from typing import Optional, List
from jpype import JClass
from weka.core.classes import OptionHandler
from weka.core.dataset import Instances
from meka.classifiers import MultiLabelClassifier
from  ._evaluationstatistics import EvaluationStatistics


class Evaluator(OptionHandler):
    """
    Interface for classes that evaluate on a dataset.
    """

    def __init__(self, jobject=None, classname: str = None, options: List[str] = None):
        """
        Initializes the experiment.

        :param jobject: the evaluator object to wrap, ignores classname/options when not None
        :param classname: the class name of the evaluator class to instantiate
        :type classname: str
        :param options: the options for the evaluator
        :type options:  list
        """
        if classname is not None:
            jobject = JClass(classname)()
        if jobject is not None:
            self.enforce_type(jobject, "meka.experiment.evaluators.Evaluator")
        super().__init__(jobject, options=options)

    def initialize(self) -> Optional[str]:
        """
        Initializes the evaluator.

        :return: None if successful, otherwise error message
        :rtype: str
        """
        return self.jobject.initialize()

    def evaluate(self, classifier: MultiLabelClassifier, dataset: Instances) -> List[EvaluationStatistics]:
        """
        Returns the evaluation statistics generated for the dataset.

        :param classifier: the classifier to evaluate
        :type classifier: MultiLabelClassifier
        :param dataset: the dataset to evaluate on
        :type dataset: Instances
        :return: the list of generated statistics
        :rtype: list
        """
        items = self.jobject.evaluate(classifier.jobject, dataset.jobject)
        return [EvaluationStatistics(jobject=x) for x in items]

    def stop(self):
        """
        Stops the evaluation, if possible.
        """
        self.jobject.stop()
