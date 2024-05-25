
from abc import ABCMeta, abstractmethod

class CoreInterfaceModel(metaclass=ABCMeta):

    @abstractmethod
    def selectData(self, idventa=""):
        pass