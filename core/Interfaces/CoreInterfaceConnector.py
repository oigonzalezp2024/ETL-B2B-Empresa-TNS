
from abc import abstractmethod
from abc import ABCMeta

class CoreInterfaceConnector(metaclass=ABCMeta):  

    @abstractmethod
    def __init__(self):
        """
        Obligatorio.
        Se requiere un constructor.
        """
        pass

    @abstractmethod
    def connectorServer(self):
        """
        Obligatorio.
        Posibilitar el acceso a un servidor de base de datos.
        """
        pass
    
    @abstractmethod
    def connectorDataBase(self, database:str):
        """
        Obligatorio.
        Posibilitar el acceso a una base de datos.
        """
        pass
