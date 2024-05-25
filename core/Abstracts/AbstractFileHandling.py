
from abc import abstractmethod
from core.Interfaces.CoreInterfaceFileHandling import CoreInterfaceFileHandling

class CoreAbstractFileHandling(CoreInterfaceFileHandling):
    """
    Posiblita trabajar con archivos dentro del proyecto.
    """
    @abstractmethod
    def readFile(self):
        """
        Con este método se lee el contenido de un archivo.
        """
        pass
