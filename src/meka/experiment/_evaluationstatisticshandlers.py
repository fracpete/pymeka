from typing import Optional, List

from weka.core.classes import OptionHandler

from ._evaluationstatistics import EvaluationStatistics


class EvaluationStatisticsHandler(OptionHandler):

    def is_thread_safe(self) -> bool:
        """
        Returns whether the handler is threadsafe.

        :return: True when thread safe
        :rtype: bool
        """
        return self.jobject.isThreadSafe()

    def initialize(self) -> Optional[str]:
        """
        Initializes the handler.


        :return: None if successfully initialized, otherwise error message
        :rtype: str
        """
        return self.jobject.initialize()

    def read(self) -> List[EvaluationStatistics]:
        """
        Reads the statistics.

        :return: the statistics that were read
        :rtype: list
        """
        result = []
        items = self.jobject.read()
        if items is not None:
            for item in items:
                result.append(EvaluationStatistics(jobject=item))
        return result

    def write(self, statistics: List[EvaluationStatistics]) -> Optional[str]:
        """
        Stores the given statistics.

        :param statistics: the statistics to store
        :type statistics: list
        :return: None if successfully stored, otherwise error message
        :rtype: str
        """
        items = [x.jobject for x in statistics]
        return self.jobject.write(items)

    def finish(self) -> Optional[str]:
        """
        Gets called after the experiment finished.

        :return: None if successfully finished, otherwise error message
        :rtype: str
        """
        return self.jobject.finish()
