
import mysql.connector
from core.Abstracts.AbstractConnector import CoreAbstractConnector

class Connector(CoreAbstractConnector):
    """
    Posibilita la conexión con la base de datos.
    """
    def __init__(self):

        self.__host=""
        self.__user=""
        self.__password=""
        self.last_insert_id=""

    def __secret(self):
        # Como buena práctica se aconseja siempre crear un método secreto para gestionar las credenciales de acceso al servidor.
        self.__host="localhost"
        self.__user="root"
        self.__password=""

    def connectorServer(self):
        self.__secret()
        mydb = mysql.connector.connect(
            host=self.__host,
            user=self.__user,
            password=self.__password
        )
        return mydb

    def connectorDataBase(self, database:str):
        self.__secret()
        mydb = mysql.connector.connect(
            host = self.__host,
            user = self.__user,
            password = self.__password,
            database = database
        )
        return mydb