from typing import Optional, Iterator, List
from jpype import JClass
from weka.core.classes import OptionHandler
from weka.core.dataset import Instances


class DatasetProvider(OptionHandler, Iterator[Instances]):

    def __init__(self, jobject=None, classname: str = None, options: List[str] = None):
        """
        Initializes the provider.

        :param jobject: the provider object to wrap, ignores classname/options when not None
        :param classname: the class name of the provider class to instantiate
        :type classname: str
        :param options: the options for the provider
        :type options:  list
        """
        if classname is not None:
            jobject = JClass(classname)()
        if jobject is not None:
            self.enforce_type(jobject, "meka.experiment.datasetproviders.DatasetProvider")
        super().__init__(jobject=jobject, optons=options)

    def initialize(self) -> Optional[str]:
        """
        Initializes the provider to start providing datasets from scratch.

        :return: None if successful, otherwise error message
        :rtype: str
        """
        return self.jobject.initialize()

    def __iter__(self) -> Iterator[Instances]:
        """
        Returns the iterator object itself.

        :return: the iterator object
        """
        return self

    def __next__(self) -> Instances:
        """
        Returns the next item of the iterator object.

        :return: the next item
        """
        if self.jobject.hasNext():
            return Instances(jobject=self.jobject.next())
        else:
            raise StopIteration()

    def finish(self) -> Optional[str]:
        """
        Gets called after the experiment finishes.

        :return: None if successful, otherwise error message
        :rtype: str
        """
        return self.jobject.finish()


class LocalDatasetProvider(DatasetProvider):

    def __init__(self, jobject=None, options: List[str] = None):
        """
        Initializes the provider.

        :param jobject: the provider to wrap
        :param options: the options for the provider
        :type options: list
        """
        classname = "meka.experiment.datasetproviders.LocalDatasetProvider"
        if jobject is not None:
            self.enforce_type(jobject, classname)
        super().__init__(jobject=jobject, classname=classname, options=options)

    @property
    def datasets(self) -> List[str]:
        """
        Returns the datasets.

        :return: the datasets
        :rtype: list
        """
        items = self.jobject.getDatasets()
        return [str(x) for x in items]

    @datasets.setter
    def datasets(self, paths: List[str]):
        """
        Sets the datasets.

        :param paths: the datasets to use
        :type paths: list
        """
        items = []
        for path in paths:
            items.append(JClass("java.io.File")(path))
        self.jobject.setDatasets(items)


class MultiDatasetProvider(DatasetProvider):

    def __init__(self, jobject=None, options: List[str] = None):
        """
        Initializes the provider.

        :param jobject: the provider to wrap
        :param options: the options for the provider
        :type options: list
        """
        classname = "meka.experiment.datasetproviders.MultiDatasetProvider"
        if jobject is not None:
            self.enforce_type(jobject, classname)
        super().__init__(jobject=jobject, classname=classname, options=options)

    @property
    def providers(self) -> List[DatasetProvider]:
        """
        Returns the providers.

        :return: the providers
        :rtype: list
        """
        items = self.jobject.getProviders()
        return [DatasetProvider(jobject=x) for x in items]

    @providers.setter
    def providers(self, providers: List[DatasetProvider]):
        """
        Sets the providers.

        :param providers: the providers to use
        :type providers: list
        """
        items = [x.jobject for x in providers]
        self.jobject.setProviders(items)
