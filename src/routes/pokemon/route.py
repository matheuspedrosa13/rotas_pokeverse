from fastapi import Header
from src.controllers.pokemon.controller import PokeController
from src.services.router.service import RouterService

app = RouterService.get_router()


@app.get("/search_pokemon", tags=["Pokemon"])
async def search_pokemon(id: int, token_jwt: str = Header(...)):
    return PokeController.search_poke(id)


@app.get("/pagination_of_pokemons", tags=["Pokemon"])
async def pag_pokemon(start_id='0', limit_page='20', token_jwt: str = Header(...)):
    return PokeController.pag_poke(start_id, limit_page)


@app.get("/search_all_captured_pokemons", tags=["Pokemon"])
async def search_pokemon_caught(owner_id: str, token_jwt: str = Header(...)):
    return PokeController.search_poke_caught(owner_id)


@app.get("/select_random_pokemon", tags=["Pokemon"])
async def search_pokemon_caught(email: str):
    return PokeController.select_random_pokemon(email)


@app.put("/capture_pokemons", tags=["Pokemon"])
async def capture_pokemon(name_poke: str, owner_email: str, name_pokeball: str, experience: str, fruit: str = "",
                          token_jwt: str = Header(...)):
    experience = int(experience)
    return PokeController.capture_poke(name_poke, owner_email, name_pokeball, experience, fruit)


@app.put("/change_nickname", tags=["Pokemon"])
async def change_nickname(nickname: str, owner_email: str, token_jwt: str = Header(...)):
    return PokeController.change_nickname(nickname, owner_email)
