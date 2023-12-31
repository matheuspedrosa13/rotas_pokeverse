from fastapi import Header
from src.controllers.user.controller import UserController
from src.services.router.service import RouterService

app = RouterService.get_router()


@app.post("/sign_in", tags=["User"])
async def sign_in(name: str, email: str, password: str, gender: str):
    return UserController.sign_in(name, email, password, gender.lower())


@app.get("/login", tags=["User"])
async def login(email: str, password: str):
    return UserController.sign_up(email, password)


@app.get("/show_all_items_backpack", tags=["User"])
async def show_all_items(email: str, token_jwt: str = Header(...)):
    return UserController.show_all_items(email)


@app.put("/alter_trainer", tags=["User"])
async def alter_trainer(email: str, field: str, value, token_jwt: str = Header(...)):
    return UserController.alter_trainer(email, field, value)


@app.delete("/delete_trainer", tags=["User"])
async def deleter_trainer(email: str, token_jwt: str = Header(...)):
    return UserController.delete_trainer(email)


@app.get("/find_all_trainer", tags=["User"])
async def find_all_trainers(token_jwt: str = Header(...)):
    return UserController.find_all_trainers()


@app.put("/change_place", tags=["User"])
async def change_place(email: str, place: str, token_jwt: str = Header(...)):
    return UserController.change_place(email, place)


@app.get("/find_trainer_with_query", tags=["User"])
async def find_trainer_with_query(field: str, value, token_jwt: str = Header(...)):
    return UserController.find_trainer_with_query(field, value)


@app.get("/find_trainer_field", tags=["User"])
async def find_trainer_field(field: str, token_jwt: str = Header(...)):
    return UserController.find_trainer_field(field)
