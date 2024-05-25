
import json
from core.Abstracts.AbstractController import CoreAbstractController
from app.model.ModelItemsformapago.ModelItemsformapago import ModelItemsformapago

class ControllerItemsFormaPago(
    CoreAbstractController,
    ModelItemsformapago
    ):

    def controller(self, idVenta=""):

        self.response = []
        self.selectData(idVenta)

        for res in self.data:
            self.res = res
            self.setData()
            self.pushData()

        response = json.dumps(self.response)

        self.writeFile('./data/itemsformapago.json', response)

        return response

    def setData(self):

        res = self.res

        #self.id_itemsformapago = str(res[0])
        self.codFormaPago = str(res[1])
        self.plazoDias = str(res[2])
        self.fechaVencimiento = str(res[3])
        self.valor = str(res[4])
        #self.venta_id = str(res[5])

    def pushData(self):

        self.data = {}
        #self.data['id_itemsformapago'] = self.id_itemsformapago
        self.data['codFormaPago'] = self.codFormaPago
        self.data['plazoDias'] = self.plazoDias
        self.data['fechaVencimiento'] = self.fechaVencimiento
        self.data['valor'] = self.valor
        #self.data['venta_id'] = self.venta_id

        self.response.append(self.data)