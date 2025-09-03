from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError  
from dotenv import load_dotenv
import os

load_dotenv()

class Database_conversation:
    def __init__(self,):
        """
        Inicializa el gestor de conexión a MongoDB.
        """
        self.host = os.getenv('DB_MONGO_HOST')
        self.db_name = os.getenv('DB_MONGO_NAME')
        self.user = os.getenv('DB_MONGO_USER')
        self.password = os.getenv('DB_MONGO_PASS')
        self.client = None
        self.db = None
        # NOTA IMPORTANTE: Si cambias usuario o contraseña de MongoDB en el archivo .env o docker-compose.yml,
        # debes eliminar el volumen de datos de MongoDB para que los cambios tengan efecto.
        # Usa: docker-compose down -v && docker-compose up -d --build
        # IMPORTANTE: El usuario root de MongoDB se autentica en la base de datos 'admin' por defecto.
        # Por eso se agrega '?authSource=admin' a la URI de conexión.
        self.uri = f"mongodb://{self.user}:{self.password}@{self.host}:27017/{self.db_name}?authSource=admin"

    def connect(self):
        """
        Conecta a la base de datos de MongoDB especificada.
        """
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.db_name]
        except ServerSelectionTimeoutError  as e:
            print(f"[ERROR_DATABASE_CONVERSATION]: Error al conectar a MongoDB: {e}")
            raise

    def close_connection(self):
        """
        Cierra la conexión a la base de datos de MongoDB.
        """
        if self.client:
            self.client.close()
        else:
            print("[DATABASE_CONVERSATION]: No hay conexión activa a MongoDB.")

    def get_collection(self, collection_name: str):
        """
        Obtiene una colección de la base de datos.
        
        :param collection_name: Nombre de la colección.
        :return: Colección de MongoDB.
        """
        if self.db is not None:
            return self.db[collection_name]
        else:
            raise RuntimeError("[ERROR_DATABASE_CONVERSATION]: No hay conexión activa a la base de datos. Conéctese primero.")

