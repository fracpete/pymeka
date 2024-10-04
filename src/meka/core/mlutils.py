from jpype import JClass
from weka.core.dataset import Instances


def prepare_data(data: Instances):
    """
    Prepares the class index of the data (in-place).

    :param data: the data to prepare
    :type data: Instances
    """
    JClass("meka.core.MLUtils").prepareData(data.jobject)
