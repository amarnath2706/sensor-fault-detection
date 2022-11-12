import pymongo
from sensor.constant.database import DATABASE_NAME
import certifi
import os
ca = certifi.where()

class MongoDBClient:
    client = None
    def __init__(self,database_name = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
            
                #MongoDBClient.client = pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)
                MongoDBClient.client = pymongo.MongoClient(os.getenv('MONGO_DB_URL'),tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e
