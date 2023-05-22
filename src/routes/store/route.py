# Third-party Libraries
from fastapi import Header

# Project
from src.controllers.store.controller import StoreController
from src.services.router.service import RouterService


app = RouterService.get_router()


# list store pokemon
# list store items
# get-store-current-money
# get-store-current-place

@app.get("/list_store_items", tags=["store"])
async def list_store_items(access_token: str = Header(...)):
    return StoreController.list_store_items()
@app.put("/buy_item_from_store", tags=["store"])
async def buy_item_from_store(user_name: str, item_name: str, quantity: int, access_token: str = Header(...)):
    return StoreController.buy_item_from_store(user_name, item_name, quantity)


# /list-places
# /capture-pokemon
# /which-pokemon-to-capture?
# /get-pokemon-info?
# /update-store
# /deactivate-store
# /edit-pokemon
# /delete-pokemon