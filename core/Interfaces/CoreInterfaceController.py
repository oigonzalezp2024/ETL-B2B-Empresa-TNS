
from abc import ABCMeta, abstractmethod

class CoreInterfaceController(metaclass=ABCMeta):

    @abstractmethod
    def controller(self, idventa=""):
        pass

    @abstractmethod
    def setData(self):
        pass

    @abstractmethod
    def pushData(self):
        pass
