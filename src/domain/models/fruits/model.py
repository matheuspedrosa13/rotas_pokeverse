from pydantic import BaseModel

from src.domain.enums.fruit_name.enum import FruitName


class FruitModel(BaseModel):
    fruit_map: dict = {
        FruitName.NONE: 20,
        FruitName.BANANA: 21,
        FruitName.UVA: 21.5,
        FruitName.ABACAXI: 22,
        FruitName.UPGRADED_BANANA: 23,
        FruitName.UPGRADED_UVA: 24,
        FruitName.UPGRADED_ABACAXI: 25
    }
