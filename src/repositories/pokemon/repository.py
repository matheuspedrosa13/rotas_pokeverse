import requests
from src.infraestructures.mongodb.infraestructure import MongoDBInfra
from src.infraestructures.pokeapi.infraestructure import PokeapiInfra
from src.domain.models.pokemon.model import PokeModel



class PokeRepo:
    def __init__(self):
        self.infra = MongoDBInfra.get_client()
        self.dbPokemons = self.infra['Trainers']
        self.catch = self.dbPokemons['wild pokemons']

    def registrar_pokemon(self, id: int):
        if self.catch.find_one({'id': id}):
            info = self.catch.find_one({'id': id}, {'_id': 0})
            print("banco")
        else:
            request = PokeapiInfra.get(id).json()
            name = request['name']
            types = [x['type']['name'] for x in request['types']]
            speed = request['stats'][5]['base_stat']
            xp = request['base_experience']
            imagem = request['sprites']['front_default']
            info = {
                'name': name,
                'id': id,
                'type': types,
                'speed': speed,
                'xp': xp,
                'imagem': imagem
            }
            self.catch.insert_one(info.copy())
            print("api")
        return info
