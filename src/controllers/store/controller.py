from src.services.store.service import StoreService


class StoreController:
    store_service = StoreService()

    @classmethod
    def list_store_items(cls):
        return cls.store_service.list_store_items()

    @classmethod
    def buy_item_from_store(cls, user_name, item_name, quantity):
        return cls.store_service.buy_item_from_store(user_name, item_name, quantity)


# list store pokemon
# list store items
# get-store-current-money
# get-store-current-place
