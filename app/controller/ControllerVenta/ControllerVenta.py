
import json
from core.Abstracts.AbstractController import CoreAbstractController
from app.model.ModelVenta.ModelVenta import ModelVenta

class ControllerVenta(
    CoreAbstractController,
    ModelVenta
    ):

    def controller(self, idVenta=""):

        self.response = []
        self.selectData(idVenta)

        for res in self.data:
            self.res = res
            self.setData()
            self.pushData()

        response = json.dumps(self.response)

        self.writeFile('./data/venta.json', response)

        return response

    def setData(self):

        res = self.res

        self.id_venta = str(res[0])
        self.codPrefijo = str(res[1])
        self.numero = str(res[2])
        self.fecha = str(res[3])
        self.codTercero = str(res[4])
        self.codVendedor = str(res[5])
        self.codDespachar = str(res[6])
        self.codFormaPago = str(res[7])
        self.codBanco = str(res[8])
        self.fechaVence = str(res[9])
        self.plazoDias = str(res[10])
        self.observacion = str(res[11])
        self.empresa_id = str(res[12])

    def pushData(self):

        self.data = {}
        self.data['id_venta'] = self.id_venta
        self.data['codPrefijo'] = self.codPrefijo
        self.data['numero'] = self.numero
        self.data['fecha'] = self.fecha
        self.data['codTercero'] = self.codTercero
        self.data['codVendedor'] = self.codVendedor
        self.data['codDespachar'] = self.codDespachar
        self.data['codFormaPago'] = self.codFormaPago
        self.data['codBanco'] = self.codBanco
        self.data['fechaVence'] = self.fechaVence
        self.data['plazoDias'] = self.plazoDias
        self.data['observacion'] = self.observacion
        self.data['empresa_id'] = self.empresa_id

        self.response.append(self.data)