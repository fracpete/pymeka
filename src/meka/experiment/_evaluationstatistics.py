from collections.abc import Mapping
from typing import Optional, Any, Iterator

from jpype import JClass
from weka.classifiers import Classifier
from weka.core.classes import JavaObject
from weka.core.dataset import Instances

from meka.core import Result


class EvaluationStatistics(JavaObject, Mapping):
    """
    Stores evaluation statistics.
    """

    def __init__(self, jobject=None, classifier: Classifier = None, result: Result = None,
                 relation: str = None, dataset: Instances = None):
        """
        Initializes the container.

        :param jobject: the Java object to wrap
        :param classifier: the classifier to store
        :type classifier: Classifier
        :param result: the result to store
        :type result: Result
        :param relation: the relation name to store (if no dataset provided)
        :type relation: str
        :param dataset: the dataset to obtain the relation name from (if not provided directly)
        :type dataset: Instances
        """
        if jobject is None:
            if classifier is not None:
                _commandline = classifier.to_commandline()
                _relation = None
                if relation is not None:
                    _relation = relation
                elif dataset is not None:
                    _relation = dataset.relationname
                jobject = JClass("meka.experiment.evaluationstatistics.EvaluationStatistics")(
                    classifier.jobject, _relation, result.jobject)
            else:
                jobject = JClass("meka.experiment.evaluationstatistics.EvaluationStatistics")()
        super().__init__(jobject=jobject)

    @property
    def classifier(self) -> Optional[Classifier]:
        """
        Returns the stored classifier object.

        :return: the classifier object
        :rtype: Classifier
        """
        jobj = self.jobject.getClassifier()
        if jobj is not None:
            return Classifier(jobject=jobj)
        else:
            return None

    @property
    def command_line(self) -> Optional[str]:
        """
        Returns the stored command-line of the classifier.


        :return: the command-line
        :rtype: str
        """
        return self.jobject.getCommandLine()

    @property
    def relation(self) -> Optional[str]:
        """
        Returns the stored name of the dataset.


        :return: the relation name
        :rtype: str
        """
        return self.jobject.getRelation()

    def __getitem__(self, key) -> Any:
        """
        Returns the item specified by the key.

        :param key: the key to get the associated value for
        :return: the associated value
        """
        self.jobject.get(key)

    def __iter__(self) -> Iterator:
        """
        Returns an iterator over the stored keys.

        :return: the iterator over the keys
        :rtype: Iterator
        """
        return iter(self.jobject.keySet())

    def __len__(self) -> int:
        """
        Returns the number of stored evaluation statistics.

        :return: the number of statistics
        :rtype: int
        """
        return self.jobject.size()
