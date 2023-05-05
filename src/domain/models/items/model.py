# Third-party Libraries
from pydantic import BaseModel, validator

from src.domain.enums.fruit_name.enum import FruitName
from src.domain.enums.pokeball_name.enum import PokeballName


class ItemModel(BaseModel):
    name: str
    price: int

    @validator('name')
    def validate_name(cls, value: str) -> str:
        fruits_names = [enum.value for enum in FruitName]
        pokeball_names = [enum.value for enum in PokeballName]
        valid_names = fruits_names + pokeball_names
        if value in valid_names:
            return value

        raise TypeError(f"Invalid item name! Received {value}, try one of {valid_names}")
