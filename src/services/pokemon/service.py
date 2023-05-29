from src.domain.dtos.list_store_items.dto import ListStoreItemsDto
from src.repositories.pokemon.repository import PokeRepo
from src.domain.enums.response_code.enum import ResponseCode
from src.repositories.store.repository import ItemsRepository
from src.services.auth.service import AuthService


class PokeService:
    item_repository = ItemsRepository()
    repository = PokeRepo()
    auth_service = AuthService

    @classmethod
    def search_poke(cls, id: int):
        message = []
        code = ResponseCode.NOK.value
        try:
            message.append(cls.repository.search_poke(id))
            code = ResponseCode.OK.value
        except Exception as error:
            print(f"Deu pau")
            print(f"{error=}")
        finally:
            dto = ListStoreItemsDto(message=message, code=code)
            return dto.__dict__

    @classmethod
    def pag_poke(cls, start_id, limit_page):
        message = []
        code = ResponseCode.NOK.value
        try:
            message = cls.repository.pag_poke(start_id, limit_page)
            code = ResponseCode.OK.value
        except Exception as error:
            print(f"Deu pau")
            print(f"{error=}")
        finally:
            dto = ListStoreItemsDto(message=message, code=code)
            return dto.__dict__

    @classmethod
    def capture_poke(cls, name_poke, nickname, owner_email, name_pokeball, experience, fruit):
        message = []
        code = ResponseCode.NOK.value
        try:
            item_pokeball = cls.item_repository.list_one_item(name_pokeball)
            item_fruit = cls.item_repository.list_one_item(fruit)
            message = cls.repository.capture_poke(name_poke, nickname, owner_email, name_pokeball, experience, fruit, item_pokeball, item_fruit)
            code = ResponseCode.OK.value
        except Exception as error:
            print(f"Deu pau")
            print(f"{error=}")
        finally:
            dto = ListStoreItemsDto(message=message, code=code)
            return dto.__dict__

    @classmethod
    def search_poke_caught(cls, owner_email):
        message = []
        code = ResponseCode.NOK.value
        try:
            message = cls.repository.search_poke_caught(owner_email)
            code = ResponseCode.OK.value
        except Exception as error:
            print(f"Deu pau")
            print(f"{error=}")
        finally:
            dto = ListStoreItemsDto(message=message, code=code)
            return dto.__dict__

    @classmethod
    def select_random_pokemon(cls):
        message = []
        code = ResponseCode.NOK.value
        try:
            message = cls.repository.random_pokemon()
            code = ResponseCode.OK.value
        except Exception as error:
            print(f"Deu pau")
            print(f"{error=}")
        finally:
            dto = ListStoreItemsDto(message=message, code=code)
            return dto.__dict__
