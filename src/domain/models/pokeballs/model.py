from pydantic import BaseModel

from src.domain.enums.pokeball_name.enum import PokeballName


class PokeballModel(BaseModel):
    pokeball_map: dict = {
        PokeballName.POKEBALL: 85,
        PokeballName.GREATBALL: 65,
        PokeballName.ULTRABALL: 45
    }
