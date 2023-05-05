from src.domain.dtos.list_store_items.dto import ListStoreItemsDto
from src.domain.enums.response_code.enum import ResponseCode
from src.repositories.user.repository import ItemsRepository
from src.services.auth.service import AuthService


class StoreService:
    user_repository = ItemsRepository()
    auth_service = AuthService

    # list store pokemon
    # list store items
    # get-store-current-money
    # get-store-current-place

    @classmethod
    async def authorize(cls, jwt) -> bool:
        authorized = await cls.auth_service.authorize_jwt(jwt)
        return authorized

    @classmethod
    def list_store_items(cls):
        message = []
        code = ResponseCode.NOK.value
        try:
            message = cls.user_repository.list_all_items()
            code = ResponseCode.OK.value
        except Exception as error:
            print(f"Deu pau")
            print(f"{error=}")
        finally:
            dto = ListStoreItemsDto(message=message, code=code)
            return dto.__dict__

    # @classmethod
    # def buy_item_from_store(cls, user_name, item_name):
    #     result = cls.user_repository.buy_item_from_store(user_name, item_name)
    #     return result
