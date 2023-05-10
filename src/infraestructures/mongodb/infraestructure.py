import pymongo

<<<<<<< HEAD
=======
# Project
from src.utils.env_config.util import config

>>>>>>> 27c10acf01476f4b78fbb69ed015dc78d3ca4ce4

class MongoDBInfra:

    __client = None
<<<<<<< HEAD
    __user = "Contas"                       # TODO pegar da env
    __password = "Ma65451884"               # TODO pegar da env
    __url = "cluster0.ls20ooj.mongodb.net"  # TODO pegar da env
=======
    __user = config("MONGO_USER")
    __password = config("MONGO_PASSWORD")
    __url = config("MONGO_URL")
>>>>>>> 27c10acf01476f4b78fbb69ed015dc78d3ca4ce4

    @classmethod
    def get_client(cls):
        if cls.__client is None:
            cls.__client = pymongo.MongoClient(f"mongodb+srv://{cls.__user}:{cls.__password}@{cls.__url}")
        return cls.__client
