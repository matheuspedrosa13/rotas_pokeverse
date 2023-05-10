from fastapi import Header
from src.controllers.pokemon.controller import PokeController
from src.services.router.service import RouterService

app = RouterService.get_router()


@app.get("/registrar_poke", tags=["pokemon"])
async def registrar_poke(id: int, access_token: str = Header(...)):
    return PokeController.registrar_poke(id)
