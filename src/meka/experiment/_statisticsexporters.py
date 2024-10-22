from typing import List, Optional
from jpype import JClass
from weka.core.classes import OptionHandler
from ._evaluationstatistics import EvaluationStatistics


class EvaluationStatisticsExporter(OptionHandler):
    """
    Interface for classes that export statistics into other formats.
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
            self.enforce_type(jobject, "meka.experiment.statisticsexporters.EvaluationStatisticsExporter")
        super().__init__(jobject, options=options)

    def export(self, stats: List[EvaluationStatistics]) -> Optional[str]:
        """
        Exports the statistics.

        :param stats: the statistics to export
        :type stats: list
        :return: None if successfully exported, otherwise error message
        :rtype: str
        """
        items = [x.jobject for x in stats]
        return self.jobject.export(items)
