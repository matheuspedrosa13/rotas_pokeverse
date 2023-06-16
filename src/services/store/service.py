from src.domain.dtos.list_store_items.dto import ListStoreItemsDto
from src.domain.enums.response_code.enum import ResponseCode
from src.repositories.store.repository import ItemsRepository
from src.repositories.user.repository import UsersRepository


class StoreService:
    user_repository = UsersRepository()
    item_repository = ItemsRepository()


    # list store pokemon
    # list store items
    # get-store-current-money
    # get-store-current-place

    @classmethod
    def list_store_items(cls):
        message = []
        code = ResponseCode.NOK.value
        try:
            message = cls.item_repository.list_all_items()
            code = ResponseCode.OK.value
        except Exception as error:
            print("Deu pau")
            print(f"error = {error}")
        finally:
            dto = ListStoreItemsDto(message=message, code=code)
            return dto.__dict__

    @classmethod
    def buy_item_from_store(cls, user_name, item_name, quantity):
        message = []
        code = ResponseCode.NOK.value
        try:
            item = cls.item_repository.list_one_item(item_name)
            message = cls.user_repository.buy_item_from_store(user_name, item[0], quantity)
            code = ResponseCode.OK.value
        except Exception as error:
            print("Deu pau")
            print(f"error = {error}")
        finally:
            dto = ListStoreItemsDto(message=message, code=code)
            # print("Problema no Retorno")
            return dto.__dict__
