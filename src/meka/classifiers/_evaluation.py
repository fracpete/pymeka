from typing import List
from jpype import JClass
from weka.core.classes import is_instance_of
from weka.core.dataset import Instances
from meka.core import Result
from ._multix import MultiXClassifier
from ._multilabel import MultiLabelClassifier


class Evaluation:
    """
    Wrapper around the multi-label/target Evaluation class.
    """

    @classmethod
    def evaluate_model(cls, classifier: MultiXClassifier, train: Instances, test: Instances,
                       top: str = "PCut1", vop: str = "1") -> Result:
        """
        Builds the classifier on the training data and evaluates it on the test set.

        :param classifier: the classifier to train
        :type classifier: MultiXClassifier
        :param train: the training set
        :type train: Instances
        :param test: the test set
        :type test: Instances
        :param top: Threshold OPtion (pertains to multi-label data only)
        :type top: str
        :param vop: Verbosity OPtion (which measures do we want to calculate/output)
        :type vop: str
        :return: raw prediction data with evaluation statistics included.
        :rtype: Result
        """
        jobj = JClass("meka.classifiers.multilabel.Evaluation").evaluateModel(
            classifier.jobject, train.jobject, test.jobject, top, vop)
        return Result(jobject=jobj)

    @classmethod
    def cv_model(cls, classifier: MultiXClassifier, data: Instances, num_folds: int = 10,
                 top: str = "PCut1", vop: str = "1") -> Result:
        """
        Cross-validate the specified classifier on the supplied dataset and with the specified number of folds.

        :param classifier: the classifier to train
        :type classifier: MultiXClassifier
        :param data: the dataset set to use
        :type data: Instances
        :param num_folds: the number of folds to use for cross-validation (>= 2)
        :type num_folds: int
        :param top: Threshold OPtion (pertains to multi-label data only)
        :type top: str
        :param vop: Verbosity OPtion (which measures do we want to calculate/output)
        :type vop: str
        :return: raw prediction data with evaluation statistics included.
        :rtype: Result
        """
        jobj = JClass("meka.classifiers.multilabel.Evaluation").cvModel(
            classifier.jobject, data.jobject, num_folds, top, vop)
        return Result(jobject=jobj)

    @classmethod
    def test_classifier(cls, classifier: MultiXClassifier, test: Instances, multi_threaded: bool = False) -> Result:
        """
        Evaluates the trained classifier on the specified test set.

        :param classifier: the classifier to evaluate
        :type classifier: MultiXClassifier
        :param test: the test set to use for evaluation
        :type test: Instances
        :param multi_threaded: if the classifier implements MultiLabelClassifierThreaded, then evaluates it using multi-threading
        :type multi_threaded: bool
        :return: raw prediction data with evaluation statistics included.
        :rtype: Result
        """
        if multi_threaded and is_instance_of(
                classifier.jobject, "meka.classifiers.multilabel.MultiLabelClassifierThreaded"):
            jobj = JClass("meka.classifiers.multilabel.Evaluation").testClassifierM(classifier.jobject, test.jobject)
        else:
            jobj = JClass("meka.classifiers.multilabel.Evaluation").testClassifier(classifier.jobject, test.jobject)
        return Result(jobject=jobj)

    @classmethod
    def run_experiment(cls, classifier: MultiLabelClassifier, options: List[str]):
        """
        Build and evaluate a model with command-line options.

        :param classifier: the classifier to evaluate
        :type classifier: MultiLabelClassifier
        :param options: the commandline options to use
        :type options: list
        """
        JClass("meka.classifiers.multilabel.Evaluation").runExperiment(classifier.jobject, options)

    @classmethod
    def is_multi_target(cls, data: Instances) -> bool:
        """
        Checks whether the dataset is multi-target or just multi-label.

        :param data: the dataset to check
        :type data: Instances
        :return: True if multi-target
        :rtype: bool
        """
        return JClass("meka.classifiers.multilabel.Evaluation").isMT(data.jobject)
