from src.domain.models.items.model import ItemModel
from src.infraestructures.mongodb.infraestructure import MongoDBInfra
from src.domain.models.user.model import BaseModel


class ItemsRepository:

    def __init__(self):
        self.client = MongoDBInfra.get_client()
        self.database = self.client.get_database("user_microservice")
        self.collection = self.database.get_collection("items")
        self.base_projection = {"_id": 0}

        # self.collection_users = self.data_base.get_collection("user")

    def find(self, query: dict, projection: dict | None = None):
        if projection is None:
            projection = self.base_projection
        return self.collection.find(query, projection)

    def list_all_items(self):
        query = {}
        items = self.find(query)
        return [ItemModel(**item).__dict__ for item in items]


    # def buy_item_from_store(self, user_name, item_name):
    #     user = self.collection_users.find_one({"name": user_name}, {"_id": 0})
    #     item = self.collection_items.find_one({"name": item_name}, {"_id": 0})
    #     money_spent = user["money"] - item
    #     self.collection_users.update_one({"name": user["name"]}, {"money": user})

# pegar o store e o item para que possa comprar o item( tirar os mangos do store )
# ver se na mochila jpa tiver este item if tem: item quantidade += 1 else: adicionar este item
