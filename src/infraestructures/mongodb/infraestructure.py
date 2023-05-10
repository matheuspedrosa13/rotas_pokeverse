import pymongo


class MongoDBInfra:

    __client = None
    __user = "Contas"                       # TODO pegar da env
    __password = "Ma65451884"               # TODO pegar da env
    __url = "cluster0.ls20ooj.mongodb.net"  # TODO pegar da env

    @classmethod
    def get_client(cls):
        if cls.__client is None:
            cls.__client = pymongo.MongoClient(f"mongodb+srv://{cls.__user}:{cls.__password}@{cls.__url}")
        return cls.__client
