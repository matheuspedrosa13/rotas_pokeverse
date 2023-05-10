from src.domain.models.items.model import ItemModel
from src.infraestructures.mongodb.infraestructure import MongoDBInfra


class UsersRepository:

    def __init__(self):
        self.client = MongoDBInfra.get_client()
        self.database = self.client.get_database("user_microservice")
        self.collection = self.database.get_collection("users")
        self.base_projection = {"_id": 0}

        # self.collection_users = self.data_base.get_collection("user")

    def buy_item_from_store(self, user_name, item):
        query_find_user = {"name": user_name}
        user__cur = self.collection.find(query_find_user, {"_id": 0})
        user = [users for users in user__cur][0]

        items_of_user = list(user["items"])

        if (user["money"] - item["price"]) > 0:
            if not items_of_user:
                items_of_user.append([item['name'], 1])
            else:
                not_in_items = True
                for items in items_of_user:
                    if item['name'] in items:
                        items[1] = items[1] + 1
                        not_in_items = False
                if not_in_items:
                    items_of_user.append([item['name'], 1])

            self.collection.update_one(query_find_user,
                                       {"$set":
                                           {
                                               "money": (user["money"] - item["price"])
                                           }
                                       })

            self.collection.update_one(query_find_user,
                                       {"$set":
                                           {
                                               "items": items_of_user
                                           }
                                       }
                                       )

            user_updated = self.collection.find_one(query_find_user, {"_id": 0})
            return [user_updated]
        else:
            return [{"Status": "Sem saldo amigão"}]

