
import json
from core.Abstracts.AbstractFileHandling import CoreAbstractFileHandling

class CoreStaticFileHandling(CoreAbstractFileHandling):
    """
    Todo manejo de archivos se debe gestionar con esta clase.
    """
    @staticmethod
    def readFile(pathFile):
        f = open(pathFile,'r')
        content = f.read()
        f.close()
        return content
    
    """
    Crea archivos paravisualizar data y facilitar el análisis.
    """
    @staticmethod
    def writeFile(pathFile, content):
        data = json.loads(content)
        formatt = json.dumps(data, indent=4)
        f = open(pathFile,'w')
        f.write(formatt)
        f.close()
