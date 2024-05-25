
from core.Abstracts.AbstractModel import CoreAbstractModel
from core.Statics.CoreStaticFileHandling import CoreStaticFileHandling
from app.model.Connector.Connector import Connector

class ModelItemsformapago(
    CoreStaticFileHandling,
    CoreAbstractModel,
    Connector
    ):

    def selectData(self, idVenta=""):
        mydb = self.connectorDataBase('administracion')
        mycursor = mydb.cursor()
        sql = self.readFile('./querys/view_itemsformapago.sql')
        mycursor.execute(sql.replace("xxxx",idVenta))
        self.data = mycursor.fetchall()
        mydb.commit()
