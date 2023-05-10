import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import UJSONResponse
from fastapi.middleware.cors import CORSMiddleware
from src.services.router.service import RouterService
from src.services.auth.service import AuthService

import src.routes.store.route
import src.routes.pokemon.route
import src.routes.user.route
router = RouterService.get_router()
app = FastAPI(title="Pokemon")

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
]

app.include_router(
    router
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_token_validation(request: Request, call_next):
    url: str = request.url.path
    if url.find("/docs") != -1 or url.find("/openapi") != -1:
        response = await call_next(request)
        return response

    access_token = None
    headers: list[tuple, ...] = request.headers.items()
    for key, value in headers:
        if key == "access-token":
            access_token = value
            break
    authorized = await AuthService.authorize_jwt(access_token)
    if authorized:
        response = await call_next(request)
        return response

    return UJSONResponse({
        "message": "Not authorized!",
        "code": 0
    })

if __name__ == "__main__":
    port = 8000
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        access_log=True,
        root_path="/"
    )
