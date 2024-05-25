
from abc import abstractmethod
from core.Interfaces.CoreInterfaceModel import CoreInterfaceModel

class CoreAbstractModel(CoreInterfaceModel):
    """
    Establece una forma de trabajo eficiente para todo el proyecto.
    ```
    # Ejemplo de implementación.

    from core.Abstracts.AbstractModel import CoreAbstractModel
    from core.Statics.CoreStaticFileHandling import CoreStaticFileHandling
    from app.model.Connector.Connector import Connector

    class ModelEmpresa(
        CoreStaticFileHandling,
        CoreAbstractModel,
        Connector
        ):

        def selectData(self, idVenta=""):
            mydb = self.connectorDataBase('administracion')
            mycursor = mydb.cursor()
            sql = self.readFile('./querys/view_empresa.sql')
            mycursor.execute(sql.replace("xxxx",idVenta))
            self.data = mycursor.fetchall()
            mydb.commit()

    ```
    """
    @abstractmethod
    def selectData(self, idVenta=""):
        """
        Lista los datos de la consulta a una tabla o vista de una base de datos.
        """
        pass
