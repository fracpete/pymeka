from jpype import JClass
from weka.classifiers import Classifier


class MultiXClassifier(Classifier):
    """
    Common interface for multi-label and multi-target classifiers.
    """

    def __init__(self, classname="weka.classifiers.rules.ZeroR", jobject=None, options=None):
        """
        Initializes the specified classifier using either the classname or the supplied JPype object.

        :param classname: the classname of the classifier
        :type classname: str
        :param jobject: the JPype object to use
        :type jobject: JPype object
        :param options: the list of commandline options to set
        :type options: list
        """
        super().__init__(classname=classname, jobject=jobject, options=options)
        if not self.is_updateable:
            self.is_updateable = isinstance(self.jobject, JClass("weka.classifiers.UpdateableClassifier"))
        if not self.is_drawable:
            self.is_drawable = isinstance(self.jobject, JClass("weka.core.Drawable"))
        if not self.is_additional_measure_producer:
            self.is_additional_measure_producer = isinstance(self.jobject, JClass("weka.core.AdditionalMeasureProducer"))
        if not self.is_batchpredictor:
            self.is_batchpredictor = isinstance(self.jobject, JClass("weka.core.BatchPredictor"))

    @property
    def model(self) -> str:
        """
        Returns the model as string.

        :return: the string representation of the model
        :rtype: str
        """
        return self.jobject.getModel()
