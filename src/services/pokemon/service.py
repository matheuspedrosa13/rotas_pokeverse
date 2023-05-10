from src.domain.dtos.list_store_items.dto import ListStoreItemsDto
from src.repositories.pokemon.repository import PokeRepo
from src.domain.enums.response_code.enum import ResponseCode
from src.services.auth.service import AuthService



class PokeService:
    repository = PokeRepo()
    auth_service = AuthService


    @classmethod
    def registrar_poke(cls, id: int):
        message = []
        code = ResponseCode.NOK.value
        try:
            message.append(cls.repository.registrar_pokemon(id))
            code = ResponseCode.OK.value
        except Exception as error:
            print(f"Deu pau")
            print(f"{error=}")
        finally:
            dto = ListStoreItemsDto(message=message, code=code)
            return dto.__dict__



