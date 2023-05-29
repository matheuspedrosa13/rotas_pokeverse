from src.domain.models.items.model import ItemModel
from src.infraestructures.mongodb.infraestructure import MongoDBInfra


class ItemsRepository:
    def __init__(self):
        self.client = MongoDBInfra.get_client()
        self.database = self.client.get_database("Trainers")
        self.collection = self.database.get_collection("store")
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
