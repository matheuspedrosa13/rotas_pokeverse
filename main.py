from fastapi.responses import UJSONResponse
from src.services.router.service import RouterService
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.requests import Request
import requests
from starlette.responses import PlainTextResponse
from starlette.status import HTTP_403_FORBIDDEN

app = FastAPI(title='pokemon')


# Middleware to intercept incoming requests
@app.middleware("http")
async def inteceptacao(request: Request, call_next):
    if "/docs" in request.url.path or "/openapi.json" in request.url.path:
        response = await call_next(request)
        return response

    jwt = request.headers.get("token-jwt")
    rota = str(request.url.path).replace("/", "")

    print(f"Requested route: {request.url.path}")

    if rota == "login" or rota == 'sign_in' or rota == 'select_random_pokemon':
        response = await call_next(request)
        return response

    else:
        # Call next middleware or route handler
        response = requests.get(f'http://localhost:9999/confirm_jwt?jwt={jwt}&rota={rota}')
        print(jwt)

        print(rota)
        print(response.json())
        if response.json():
            response = await call_next(request)
            return response

        return PlainTextResponse("Não tem permissão", status_code=HTTP_403_FORBIDDEN)


import src.routes.store.route
import src.routes.pokemon.route
import src.routes.user.route

router = RouterService.get_router()

app.include_router(router)

# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8000",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    port = 8000
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        access_log=True,
        root_path="/"
    )
