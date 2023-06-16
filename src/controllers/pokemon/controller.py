from src.services.pokemon.service import PokeService


class PokeController:
    poke_service = PokeService()

    @classmethod
    def search_poke(cls, id: int):
        return cls.poke_service.search_poke(id)

    @classmethod
    def pag_poke(cls, start_id: str, limit_pag: str):
        return cls.poke_service.pag_poke(start_id, limit_pag)

    @classmethod
    def capture_poke(cls, name_poke: str, owner_email: str, name_pokeball: str, experience: int, fruit: str):
        return cls.poke_service.capture_poke(name_poke, owner_email, name_pokeball, experience, fruit)

    @classmethod
    def search_poke_caught(cls, owner_id: str):
        return cls.poke_service.search_poke_caught(owner_id)

    @classmethod
    def select_random_pokemon(cls, email):
        return cls.poke_service.select_random_pokemon(email)

    @classmethod
    def change_nickname(cls, nickname, owner_email):
        return cls.poke_service.change_nickname(nickname, owner_email)