
from core.Abstracts.AbstractModel import CoreAbstractModel
from core.Statics.CoreStaticFileHandling import CoreStaticFileHandling
from app.model.Connector.Connector import Connector

class ModelItemsDescuentos(
    CoreStaticFileHandling,
    CoreAbstractModel,
    Connector
    ):

    def selectData(self):
        mydb = self.connectorDataBase('administracion')
        mycursor = mydb.cursor()
        sql = self.readFile('./querys/view_itemsdescuentos.sql')
        mycursor.execute(sql)
        self.data = mycursor.fetchall()
        mydb.commit()
