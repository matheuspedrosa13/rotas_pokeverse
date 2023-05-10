from src.services.pokemon.service import PokeService


class PokeController:
    poke_service = PokeService()

    @classmethod
    def registrar_poke(cls, id: int):
        return cls.poke_service.registrar_poke(id)
