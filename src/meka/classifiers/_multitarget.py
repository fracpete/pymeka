from typing import List
from jpype import JClass
from weka.core.classes import JavaArray
from ._multix import MultiXClassifier


class MultiTargetClassifier(MultiXClassifier):
    """
    Super class for multi-target classifiers.
    """

    def __init__(self, classname="meka.classifiers.multitarget.CC", jobject=None, options=None):
        """
        Initializes the specified classifier using either the classname or the supplied JPype object.

        :param classname: the classname of the classifier
        :type classname: str
        :param jobject: the JPype object to use
        :type jobject: JPype object
        :param options: the list of commandline options to set
        :type options: list
        """
        if jobject is None:
            jobject = MultiTargetClassifier.new_instance(classname)
        self.enforce_type(jobject, "meka.classifiers.multitarget.MultiTargetClassifier")
        super().__init__(jobject=jobject, options=options)

    @classmethod
    def make_copies(cls, classifier: 'MultiTargetClassifier', num: int) -> List['MultiTargetClassifier']:
        """
        Creates the specified number of copies of the supplied classifier.

        :param classifier: the classifier to copy
        :type classifier: MultiLabelClassifier
        :param num: the number of copies to create
        :type num: int
        """
        obj = JClass("meka.classifiers.multilabel.AbstractMultiLabelClassifier").makeCopies(classifier.jobject, num)
        jarray = JavaArray(obj)
        result = []
        for item in jarray:
            result.append(MultiTargetClassifier(jobject=item.jobject))
        return result

    @classmethod
    def run_classifier(cls, classifier: 'MultiTargetClassifier', args: List[str]):
        """
        Executes the classifier with the specified command-line options.

        :param classifier: the classifier to use
        :type classifier: MultiLabelClassifier
        :param args: the command-line options to use
        :type args: list
        """
        JClass("meka.classifiers.multilabel.AbstractMultiLabelClassifier").runClassifier(classifier.jobject, args)
