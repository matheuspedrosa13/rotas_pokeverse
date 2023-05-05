from pydantic import BaseModel


class UserModel(BaseModel):
    name: str
    email: str
    password: str
    gender: str
    pokemon: list
    items: list
    money: int
    place: int
