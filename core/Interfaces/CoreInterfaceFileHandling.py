
from abc import ABCMeta, abstractmethod

class CoreInterfaceFileHandling(metaclass=ABCMeta):

    @abstractmethod
    def readFile(self):
        pass
