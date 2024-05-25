
import json
from core.Abstracts.AbstractController import CoreAbstractController
from app.model.ModelItemspedido.ModelItemspedido import ModelItemspedido

class ControllerItemsPedido(
    CoreAbstractController,
    ModelItemspedido
    ):

    def controller(self, idVenta):

        self.response = []
        self.selectData(idVenta)

        for res in self.data:
            self.res = res
            self.setData()
            self.pushData()

        response = json.dumps(self.response)

        self.writeFile('./data/itemsPedido.json', response)

        return response

    def setData(self):

        res = self.res

        #self.id_itemspedido = str(res[0])
        self.codMat = str(res[1])
        self.codBodega = str(res[2])
        self.codTalla = str(res[3])
        self.codColor = str(res[4])
        self.cantidad = str(res[5])
        self.tipoUnidad = str(res[6])
        self.descuento = str(res[7])
        self.centrosCostos = str(res[8])
        self.porcIva = str(res[9])
        self.valor = str(res[10])
        self.impConsumo = str(res[11])
        self.observacion = str(res[12])
        #self.venta_id = str(res[13])

    def pushData(self):

        self.data = {}
        #self.data['id_itemspedido'] = self.id_itemspedido
        self.data['codMat'] = self.codMat
        self.data['codBodega'] = self.codBodega
        self.data['codTalla'] = self.codTalla
        self.data['codColor'] = self.codColor
        self.data['cantidad'] = self.cantidad
        self.data['tipoUnidad'] = self.tipoUnidad
        self.data['descuento'] = self.descuento
        self.data['centrosCostos'] = self.centrosCostos
        self.data['porcIva'] = self.porcIva
        self.data['valor'] = self.valor
        self.data['impConsumo'] = self.impConsumo
        self.data['observacion'] = self.observacion
        #self.data['venta_id'] = self.venta_id

        self.response.append(self.data)