from pydantic import BaseModel

from src.domain.enums.places_names.enum import LocalName


class PlaceModel(BaseModel):
    place_map: dict = {
        LocalName.MOGI: "flying",
        LocalName.CONSOLACAO: "steel",
        LocalName.BRAS: "",
        LocalName.ANA_ROSA: "grass",
        LocalName.PIRITUBA: "normal",
        LocalName.LUZ: "electric",
        LocalName.AGUA_BRANCA: "water",
        LocalName.JARDIM_ROMANO: "fighting",
        LocalName.JUNDIAI: "ground",
        LocalName.CAPAO_REDONDO: "fairy",
        LocalName.SACOMA: "bug",
        LocalName.TABOAO: "fire",
        LocalName.SOCORRO: "ghost",
        LocalName.JURUBATUBA: "dark",
        LocalName.TATUAPE: "poison",
        LocalName.SE: "rock",
        LocalName.VILA_MADALENA: "psychic",
        LocalName.JARAGUA: "dragon",
        LocalName.JABAQUARA: "ice"
    }
