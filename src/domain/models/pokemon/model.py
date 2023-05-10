from pydantic import BaseModel


class PokeModel(BaseModel):
    id: int
    name: str
    type: list
    speed: int
    xp: int
    imagem: str
    attacks: list = ['Soco', 'Aranhão', 'Mordida']
