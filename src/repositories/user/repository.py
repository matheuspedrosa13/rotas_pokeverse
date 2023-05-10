from src.domain.models.items.model import ItemModel
from src.infraestructures.mongodb.infraestructure import MongoDBInfra
from src.domain.models.user.model import UserModel


class UserRepo:

    def __init__(self):
        self.client = MongoDBInfra.get_client()
        self.database = self.client.get_database("Trainers")
        self.collection = self.database.get_collection("registered trainers")
        self.base_projection = {"_id": 0}

    def find(self, query: dict, projection: dict | None = None):
        if projection is None:
            projection = self.base_projection
        query = self.collection.find(query, projection)
        return [i for i in query]

    def list_all_trainer(self):
        query = {}
        trainers = self.find(query)
        return trainers

    def insert(self, info: dict):
        if self.collection.find_one({"email": info['email']}):
            return [{"Erro": "Email em uso"}]
        else:
            if UserModel(**info):
                self.collection.insert_one(info.copy())
                return [info]
            else:
                return [{}]

    def update(self, changed: dict, email: str):
        self.collection.update_one({"email": email}, {"$set": changed})
        return [self.collection.find_one({"email": email}, {"_id": 0})]

    def delete(self, email: str):
        try:
            if self.collection.find_one({"email": email}):
                self.collection.delete_one({"email": email})
                return [{"Status": "Deletado com sucesso"}]
            else:
                return [{"Status": "Email não existe"}]
        except:
            return [{"Status": "Num funfou"}]


    def login(self, email: str, password: str):
        user = self.collection.find_one({"$and": [{"email": email}, {"password": password}]}, {"_id": 0})
        if user:
            return [{"Usuario logado": user}]
        else:
            return [{"Erro": "Credenciais invalidas"}]


class ItemsRepository:
    def __init__(self):
        self.client = MongoDBInfra.get_client()
        self.database = self.client.get_database("user_microservice")
        self.collection = self.database.get_collection("items")
        self.base_projection = {"_id": 0}

    # self.collection_users = self.data_base.get_collection("user")

    def list_all_items(self):
        query = {}
        items = self.collection.find(query)
        return [ItemModel(**item).__dict__ for item in items]

    def list_one_item(self, item_name):
        query = {"name": item_name}
        items = self.collection.find(query, {"_id": 0})
        return [ItemModel(**item).__dict__ for item in items]
