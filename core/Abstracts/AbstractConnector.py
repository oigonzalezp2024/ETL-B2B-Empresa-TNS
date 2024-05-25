
from abc import abstractmethod
from core.Interfaces.CoreInterfaceConnector import CoreInterfaceConnector

class CoreAbstractConnector(CoreInterfaceConnector):
    """
    ```
    # Ejemplo de implementación.
    import mysql.connector
    from core.abstracts.coreAbstractConnector import CoreAbstractConnector

    class Connector(CoreAbstractConnector):

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
    ```
    """
    @abstractmethod
    def __init__(self):
        """
        Esta clase siempre debera tener un constructor.  
        ```
        def __init__(self):
        self.__host=""
        self.__user=""
        self.__password=""
        self.last_insert_id=""
        ```
        Como buena práctica se aconseja siempre crear un método secreto  
        para gestionar las credenciales de acceso al servidor.
        ```
        def __secret(self):
            self.__host="localhost"
            self.__user="root"
            self.__password="myPassword"
        ```
        """
        pass

    @abstractmethod
    def connectorServer(self):
        """
        Establece una conexión al servidor sin declarar una base de datos.
        """
        pass

    @abstractmethod
    def connectorDataBase(self, database:str):
        """
        Establece una conexión concreta a una base de datos.
        """
        pass
