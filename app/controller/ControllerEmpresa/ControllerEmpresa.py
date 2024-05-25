
import json
from core.Abstracts.AbstractController import CoreAbstractController
from app.model.ModelEmpresa.ModelEmpresa import ModelEmpresa

class ControllerEmpresa(
    CoreAbstractController,
    ModelEmpresa
    ):

    def controller(self, idVenta):

        self.response = []
        self.selectData(idVenta)

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