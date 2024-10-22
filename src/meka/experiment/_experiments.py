from typing import List, Optional
from jpype import JClass
from weka.core.classes import OptionHandler
from meka.classifiers import MultiLabelClassifier
from ._datasetproviders import DatasetProvider
from ._evaluators import Evaluator
from ._evaluationstatisticshandlers import EvaluationStatisticsHandler
from ._evaluationstatistics import EvaluationStatistics


class Experiment(OptionHandler):
    """
    Interface for experiments.
    """

    def __init__(self, jobject=None, classname: str = "meka.experiment.DefaultExperiment", options: List[str] = None):
        """
        Initializes the experiment.

        :param jobject: the experiment object to wrap, ignores classname/options when not None
        :param classname: the class name of the experiment class to instantiate
        :type classname: str
        :param options: the options for the experiment
        :type options:  list
        """
        if classname is not None:
            jobject = JClass(classname)()
        if jobject is not None:
            self.enforce_type(jobject, "meka.experiment.Experiment")
        super().__init__(jobject, options=options)

    @property
    def notes(self) -> str:
        """
        Returns the stored notes.

        :return: the stored notes, if any
        :rtype: str
        """
        return self.jobject.getNotes()

    @notes.setter
    def notes(self, value):
        """
        Sets the notes to store.

        :param value: the notes to store
        :type value: str
        """
        self.jobject.setNotes(value)

    @property
    def classifiers(self) -> List[MultiLabelClassifier]:
        """
        Returns the classifiers to be evaluated.

        :return: the list of classifiers
        :rtype: list
        """
        jobj = self.jobject.getClassifiers()
        return [MultiLabelClassifier(jobject=x) for x in jobj]

    @classifiers.setter
    def classifiers(self, classifiers: List[MultiLabelClassifier]):
        """
        Sets the classifiers to be evaluated.

        :param classifiers: the classifiers to evaluate
        :type classifiers: list
        """
        items = [x.jobject for x in classifiers]
        self.jobject.setClassifiers(items)

    @property
    def datasetprovider(self) -> DatasetProvider:
        """
        Returns the dataset provider in use.

        :return: the dataset provider
        :rtype: DatasetProvider
        """
        return DatasetProvider(self.jobject.getDatasetProvider())

    @datasetprovider.setter
    def datasetprovider(self, provider: DatasetProvider):
        """
        Sets the dataset provider to use.

        :param provider: the dataset provider to use
        :type provider: DatasetProvider
        """
        self.jobject.setDatasetProvider(provider.jobject)

    @property
    def evaluator(self) -> Evaluator:
        """
        Returns the evaluator in use.

        :return: the evaluator object
        :rtype: Evaluator
        """
        return Evaluator(self.jobject.getEvaluator())

    @evaluator.setter
    def evaluator(self, evaluator: Evaluator):
        """
        Sets the evaluator to use.

        :param evaluator: the evaluator to use
        :type evaluator: Evaluator
        """
        self.jobject.setEvaluator(evaluator.jobject)

    @property
    def statisticshandler(self) -> EvaluationStatisticsHandler:
        """
        Returns the statistics handler in use.

        :return: the statistics handler
        :rtype: EvaluationStatisticsHandler
        """
        return EvaluationStatisticsHandler(self.jobject.getStatisticsHandler())

    @statisticshandler.setter
    def statisticshandler(self, handler: EvaluationStatisticsHandler):
        """
        Sets the statistics handler to use.

        :param handler: the statistics handler to use
        :type handler: EvaluationStatisticsHandler
        """
        self.jobject.setStatisticsHandler(handler.jobject)

    def initialize(self) -> Optional[str]:
        """
        Initializes the experiment.

        :return: None if successfully initialized, otherwise error message
        :rtype: str
        """
        return self.jobject.initialize()

    @property
    def is_initializing(self) -> bool:
        """
        Returns whether the experiment is initializing.

        :return: True if initializing
        :rtype: bool
        """
        return self.jobject.isInitializing()

    def run(self) -> Optional[str]:
        """
        Runs the experiment.

        :return: None if successfully run, otherwise error message
        :rtype: str
        """
        return self.jobject.run()

    @property
    def is_running(self) -> bool:
        """
        Returns whether the experiment is running.

        :return: True if running
        :rtype: bool
        """
        return self.jobject.isRunning()

    def stop(self):
        """
        Stops the experiment.
        """
        self.jobject.stop()

    @property
    def is_stopping(self) -> bool:
        """
        Returns whether the experiment is stopping.

        :return: True if stopping
        :rtype: bool
        """
        return self.jobject.isStopping()

    def finish(self) -> Optional[str]:
        """
        Finishes the run.

        :return: None if successful, otherwise error message
        :rtype: str
        """
        return self.jobject.finish()

    @property
    def statistics(self) -> List[EvaluationStatistics]:
        """
        Returns the current statistics.

        :return: the statistics
        :rtype: list
        """
        jobj = self.jobject.getStatistics()
        return [EvaluationStatistics(jobject=x) for x in jobj]
