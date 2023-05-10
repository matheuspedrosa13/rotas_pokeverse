from src.transports.auth_poke.transport import AuthPokeTransport


class AuthService:

    __transport = AuthPokeTransport

    @classmethod
    async def treat_poke_response(cls, jwt: dict) -> bool:
        # overall_response = cls.make_request(cls.__url, headers=jwt)
        return True

    @classmethod
    async def authorize_jwt(cls, jwt: dict) -> bool:
        raw_response = await cls.__transport.ask_pedrosa(jwt)
        response = await cls.treat_poke_response(raw_response)
        return response


