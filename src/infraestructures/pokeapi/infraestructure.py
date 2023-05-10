import requests
from pydantic import BaseModel


class PokeapiInfra:

    __url: str = "https://pokeapi.co/api/v2/pokemon/"

    @classmethod
    def get_url(cls):
        return cls.__url

    @classmethod
    def get(cls, id: int):
        url = cls.get_url() + f"{id}"
        return requests.get(url, verify=False)

