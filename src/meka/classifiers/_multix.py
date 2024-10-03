from weka.classifiers import Classifier


class MultiXClassifier(Classifier):
    """
    Common interface for multi-label and multi-target classifiers.
    """

    @property
    def model(self) -> str:
        """
        Returns the model as string.

        :return: the string representation of the model
        :rtype: str
        """
        return self.jobject.getModel()
