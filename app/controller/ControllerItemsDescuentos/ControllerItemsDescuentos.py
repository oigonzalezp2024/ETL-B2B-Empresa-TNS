
import json
from core.Abstracts.AbstractController import CoreAbstractController
from app.model.ModelItemsDescuentos.ModelItemsDescuentos import ModelItemsDescuentos

class ControllerItemsDescuentos(
    CoreAbstractController,
    ModelItemsDescuentos
    ):

    def controller(self):

        self.response = []
        self.selectData()

        for res in self.data:
            self.res = res
            self.setData()
            self.pushData()

        response = json.dumps(self.response)

        self.writeFile('./data/itemsdescuentos.json', response)

        return response

    def setData(self):

        res = self.res

        self.id_itemsdescuentos = str(res[0])
        self.codconcepto = str(res[1])
        self.valordto = str(res[2])
        self.baseretd = str(res[3])
        self.porcretd = str(res[4])
        self.porivad = str(res[5])
        self.centrocostos = str(res[6])
        self.codarea = str(res[7])
        self.venta_id = str(res[8])

    def pushData(self):

        self.data = {}
        self.data['id_itemsdescuentos'] = self.id_itemsdescuentos
        self.data['codconcepto'] = self.codconcepto
        self.data['valordto'] = self.valordto
        self.data['baseretd'] = self.baseretd
        self.data['porcretd'] = self.porcretd
        self.data['porivad'] = self.porivad
        self.data['centrocostos'] = self.centrocostos
        self.data['codarea'] = self.codarea
        self.data['venta_id'] = self.venta_id

        self.response.append(self.data)