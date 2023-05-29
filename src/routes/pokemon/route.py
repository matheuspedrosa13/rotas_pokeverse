from fastapi import Header
from src.controllers.pokemon.controller import PokeController
from src.services.router.service import RouterService

app = RouterService.get_router()


@app.get("/search_pokemon", tags=["Pokemon"])
async def search_pokemon(id: int, access_token: str = Header(...)):
    return PokeController.search_poke(id)


@app.get("/pagination_of_pokemons", tags=["Pokemon"])
async def pag_pokemon(start_id='0', limit_page='20'):
    return PokeController.pag_poke(start_id, limit_page)


@app.put("/capture_pokemons", tags=["Pokemon"])
async def capture_pokemon(name_poke: str, nickname: str, owner_email: str, name_pokeball: str, experience: str, fruit: str = ""):
    experience = int(experience)
    return PokeController.capture_poke(name_poke, nickname, owner_email, name_pokeball, experience, fruit)


@app.get("/search_all_captured_pokemons", tags=["Pokemon"])
async def search_pokemon_caught(owner_id: str):
    return PokeController.search_poke_caught(owner_id)
