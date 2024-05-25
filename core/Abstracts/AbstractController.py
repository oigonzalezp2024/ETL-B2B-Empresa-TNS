
from abc import abstractmethod
from core.Interfaces.CoreInterfaceController import CoreInterfaceController

class CoreAbstractController(CoreInterfaceController):
    """
    Establece una forma de trabajo eficiente para todo el proyecto.
    ```
    # Ejemplo de implementación.

    import json
    from core.Abstracts.AbstractController import CoreAbstractController
    from app.model.ModelEmpresa.ModelEmpresa import ModelEmpresa

    class ControllerEmpresa(
        CoreAbstractController,
        ModelEmpresa
        ):

        def controller(self):

            self.response = []
            self.selectData()

            for res in self.data:
                self.res = res
                self.setData()
                self.pushData()

            response = json.dumps(self.response)

            self.writeFile('./data/empresa.json', response)

            return response

        def setData(self):

            res = self.res

            self.id_empresa = str(res[0])
            self.empresa = str(res[1])
            self.usuario = str(res[2])
            self.passw = str(res[3])
            self.tnsapitoken = str(res[4])
            self.codsucursal = str(res[5])

        def pushData(self):

            self.data = {}
            self.data['id_empresa'] = self.id_empresa
            self.data['empresa'] = self.empresa
            self.data['usuario'] = self.usuario
            self.data['password'] = self.passw
            self.data['tnsapitoken'] = self.tnsapitoken
            self.data['codsucursal'] = self.codsucursal

            self.response.append(self.data)
    ```
    """
    @abstractmethod
    def controller(self, idVenta=""):
        """
        Toda la lógica de extracción debe quedar clara aquí.
        """
        pass

    @abstractmethod
    def setData(self):
        """
        Define los valores del diccionario con la data recibida.
        """
        pass

    @abstractmethod
    def pushData(self):
        """
        Toma los diccionarios y los almacena dentro de una lista.
        """
        pass
