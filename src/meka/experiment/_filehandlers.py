from typing import List, Optional

from jpype import JClass
from weka.core.classes import OptionHandler
from ._experiments import Experiment


class ExperimentFileHandler(OptionHandler):

    def __init__(self, jobject=None, classname: str = None, options: List[str] = None):
        """
        Initializes the experiment.

        :param jobject: the file handler object to wrap, ignores classname/options when not None
        :param classname: the class name of the file handler class to instantiate
        :type classname: str
        :param options: the options for the file handler
        :type options:  list
        """
        if classname is not None:
            jobject = JClass(classname)()
        if jobject is not None:
            self.enforce_type(jobject, "meka.experiment.filehandlers.ExperimentFileHandler")
        super().__init__(jobject, options=options)

    @property
    def format_description(self) -> str:
        """
        Returns the description of the file formatt.

        :return: the description
        :rtype: str
        """
        return self.jobject.getFormatDescription()

    @property
    def format_extensions(self) -> List[str]:
        """
        Returns the extensions of the file formatt.

        :return: the extensions
        :rtype: list
        """
        return list(self.jobject.getFormatExtensions())

    def read(self, path: str) -> Experiment:
        """
        Reads the experiment from disk.

        :param path: the path to the experiment file
        :type path: str
        :return: the experiment object
        :rtype: Experiment
        """
        jobj = self.jobject.read(JClass("java.io.File")(path))
        return Experiment(jobject=jobj)

    def write(self, exp: Experiment, path: str) -> Optional[str]:
        """
        Writes an experiment to disk.

        :param exp: the experiment to save
        :type exp: Experiment
        :param path: the filename to store the experiment under
        :type path: str
        :return: None if successful, otherwise error message
        :rtype: str
        """
        return self.jobject.write(exp.jobject, JClass("java.io.File")(path))
