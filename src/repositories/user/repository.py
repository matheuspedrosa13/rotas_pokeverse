import requests
import base64
from typing import Union

from src.domain.enums.places_names.enum import LocalName
from src.domain.models.items.model import ItemModel
from src.infraestructures.mongodb.infraestructure import MongoDBInfra
from src.domain.models.user.model import UserModel


class UserRepo:

    def __init__(self):
        self.client = MongoDBInfra.get_client()
        self.database = self.client.get_database("Trainers")
        self.collection = self.database.get_collection("registered trainers")
        self.base_projection = {"_id": 0}

    def change_place(self, email, place):
        query_find_user = {"email": email}
        user = self.collection.find_one(query_find_user, {"_id": 0})
        place = place.lower()
        if user:
            for member in LocalName.__members__.values():
                if member.value == place:
                    self.collection.update_one(query_find_user, {"$set": {"place": place}})
                    user2 = self.collection.find_one(query_find_user, {"_id": 0})
                    return user2
            return "Lugar inválido"
        else:
            return [{"Status": "Usuário não encontrado"}]

    def find(self, query: dict, projection: Union[dict, None] = None):
        if projection is None:
            projection = self.base_projection
        query = self.collection.find(query, projection)
        user = [i for i in query]
        user[0]['password'] = (base64.b64encode(requests.get(f'https://auth-pokeverse.onrender.com/descrypting?password={user[0]["password"]}').text.replace('"', "").encode())).decode()
        return user

    def list_all_trainer(self):
        query = {}
        trainers = self.find(query)
        return trainers

    def insert(self, info: dict):
        if self.collection.find_one({"email": info['email']}):
            return [{"Erro": "Email em uso"}]
        else:
            user = UserModel(**info)
            if user:
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

    def login(self, email: str, password: str, jwt):
        user = self.collection.find_one({"$and": [{"email": email}, {"password": password.strip('"')}]}, {"_id": 0})
        if user:
            if jwt.strip('"').strip('/') == "senha incorreta":
                return [{'jwt': jwt.strip('"').strip('/')}]
            else:
                return [{"Usuario logado": user}, {'jwt': jwt.strip('"').strip('/')}]
        else:
            return [{"Erro": "Credenciais invalidas"}]


class UsersRepository:

    def __init__(self):
        self.client = MongoDBInfra.get_client()
        self.database = self.client.get_database("user_microservice")
        self.database2 = self.client.get_database("Trainers")
        self.collectionUser = self.database2.get_collection("registered trainers")
        self.item_collection = self.database.get_collection("items")
        self.base_projection = {"_id": 0}

        # self.collection_users = self.data_base.get_collection("user")

    def buy_item_from_store(self, user_name, item_name, quantity):
        query_find_user = {"email": user_name}
        user = self.collectionUser.find_one(query_find_user, {"_id": 0})
        if user:
            item = self.item_collection.find_one({"name": item_name['name']}, {"_id": 0})
            if item and item["price"] * int(quantity) <= user["money"]:
                items_of_user = list(user.get("items", []))
                not_in_items = True
                for items in items_of_user:
                    if item_name['name'] in items:
                        items[1] += int(quantity)
                        not_in_items = False
                        break
                if not_in_items:
                    items_of_user.append([item_name['name'], int(quantity)])
                self.collectionUser.update_one(query_find_user,
                                               {"$set": {"money": user["money"] - item["price"] * int(quantity)}})
                self.collectionUser.update_one(query_find_user, {"$set": {"items": items_of_user}})
                user_updated = self.collectionUser.find_one(query_find_user, {"_id": 0})
                return [user_updated]
            else:
                return [{"Status": "Sem saldo suficiente ou item não encontrado"}]
        else:
            return [{"Status": "Usuário não encontrado"}]
