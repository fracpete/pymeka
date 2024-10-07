from typing import List
from jpype import JClass
from weka.core.dataset import Instances
from meka.core import Result
from meka.classifiers import MultiXClassifier


class IncrementalEvaluation:
    """
    Wrapper around the multi-label/target IncrementalEvaluation class.
    """

    @classmethod
    def run_experiment(cls, classifier: MultiXClassifier, options: List[str]):
        """
        Build and evaluate a model with command-line options.

        :param classifier: the classifier to evaluate
        :type classifier: MultiXClassifier
        :param options: the commandline options to use
        :type options: list
        """
        JClass("meka.classifiers.incremental.IncrementalEvaluation").runExperiment(classifier.jobject, options)

    @classmethod
    def evaluate_model(cls, classifier: MultiXClassifier, options: List[str]) -> Result:
        """
        Build and evaluate a model with command-line options.

        :param classifier: the classifier to evaluate
        :type classifier: MultiXClassifier
        :param options: the commandline options to use
        :type options: list
        :return: the generated results
        :rtype: Result
        """
        jobj = JClass("meka.classifiers.incremental.IncrementalEvaluation").runExperiment(classifier.jobject, options)
        return Result(jobject=jobj)

    @classmethod
    def evaluate_batch_window(cls, classifier: MultiXClassifier, data: Instances, num_windows: int = 20, r_labeled: float = 1.0, top: str = "PCut1", vop: str = "3") -> Result:
        """
         Evaluate a multi-label data-stream model over windows.

        :param classifier: the classifier to evaluate
        :type classifier: MultiXClassifier
        :param data: the data to use for the evaluation
        :type data: Instances
        :param num_windows: the number of windows
        :type num_windows: int
        :param r_labeled: labelled-ness (1.0 by default)
        :type r_labeled: float
        :param top: Threshold OPtion (pertains to multi-label data only)
        :type top: str
        :param vop: Verbosity OPtion (which measures do we want to calculate/output)
        :type vop: str
        :return: The Result on the final window (but it contains samples of all the other evaluated windows). The window is sampled every N/numWindows instances, for a total of numWindows windows.
        :rtype: Result
        """
        jobj = JClass("meka.classifiers.incremental.IncrementalEvaluation").evaluateModelBatchWindow(classifier.jobject, data.jobject, num_windows, r_labeled, top, vop)
        return Result(jobject=jobj)

    @classmethod
    def evaluate_prequential(cls, classifier: MultiXClassifier, data: Instances, window_size: int = 20, r_labeled: float = 1.0, top: str = "PCut1", vop: str = "3") -> Result:
        """
        Prequential Evaluation - Accuracy since the start of evaluation.

        :param classifier: the classifier to evaluate
        :type classifier: MultiXClassifier
        :param data: the data to use for the evaluation
        :type data: Instances
        :param window_size: sampling frequency (of evaluation statistics)
        :type window_size: int
        :param r_labeled: labelled-ness (1.0 by default)
        :type r_labeled: float
        :param top: Threshold OPtion (pertains to multi-label data only)
        :type top: str
        :param vop: Verbosity OPtion (which measures do we want to calculate/output)
        :type vop: str
        :return: the evaluation results
        :rtype: Result
        """
        jobj = JClass("meka.classifiers.incremental.IncrementalEvaluation").evaluateModelPrequentialBasic(classifier.jobject, data.jobject, window_size, r_labeled, top, vop)
        return Result(jobject=jobj)
