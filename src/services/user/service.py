from src.domain.dtos.list_store_items.dto import ListStoreItemsDto
from src.domain.enums.response_code.enum import ResponseCode
from src.repositories.user.repository import UserRepo
from src.services.auth.service import AuthService


class UserService:
    user_repository = UserRepo()
    auth_service = AuthService
    @classmethod
    async def authorize(cls, jwt) -> bool:
        authorized = await cls.auth_service.authorize_jwt(jwt)
        return authorized

    @classmethod
    def find_all_trainers(cls):
        message = []
        code = ResponseCode.NOK.value
        try:
            message = cls.user_repository.list_all_trainer()
            code = ResponseCode.OK.value
        except Exception as error:
            print(f"Deu pau")
            print(f"{error=}")
        finally:
            dto = ListStoreItemsDto(message=message, code=code)
            return dto.__dict__

    @classmethod
    def find_trainer_with_query(cls, field: str, value: str | int):
        message = []
        code = ResponseCode.NOK.value
        try:
            message = cls.user_repository.find({field: value})
            code = ResponseCode.OK.value
        except Exception as error:
            print(f"Deu pau")
            print(f"{error=}")
        finally:
            dto = ListStoreItemsDto(message=message, code=code)
            return dto.__dict__

    @classmethod
    def find_trainer_field(cls, field: str):
        message = []
        code = ResponseCode.NOK.value
        try:
            message = cls.user_repository.find({}, {field: 1, "_id": 0})
            code = ResponseCode.OK.value
        except Exception as error:
            print(f"Deu pau")
            print(f"{error=}")
        finally:
            dto = ListStoreItemsDto(message=message, code=code)
            return dto.__dict__

#só pro commite
    @classmethod
    def sign_in(cls, name, email, password, gender):
        message = []
        code = ResponseCode.NOK.value
        infos = {
            "name": name,
            "email": email,
            "password": password,
            "gender": gender,
            "pokemon": [],
            "items": [],
            "money": 0,
            "place": "bras"
        }
        try:
            message = (cls.user_repository.insert(infos))
            code = ResponseCode.OK.value
        except Exception as error:
            print(f"Deu pau")
            print(f"{error=}")
        finally:
            print(message)
            dto = ListStoreItemsDto(message=message, code=code)
            return dto.__dict__

    @classmethod
    def alter_trainer(cls, email, field, value):
        message = []
        code = ResponseCode.NOK.value
        value = {field: value}
        try:
            message = cls.user_repository.update(value, email)
            code = ResponseCode.OK.value
        except Exception as error:
            print(f"Deu pau")
            print(f"{error=}")
        finally:
            dto = ListStoreItemsDto(message=message, code=code)
            return dto.__dict__

    @classmethod
    def delete_trainer(cls, email):
        message = []
        code = ResponseCode.NOK.value
        try:
            message = cls.user_repository.delete(email)
            code = ResponseCode.OK.value
        except Exception as error:
            print(f"Deu pau")
            print(f"{error=}")
        finally:
            dto = ListStoreItemsDto(message=message, code=code)
            return dto.__dict__


    @classmethod
    def login(cls, email, password):
        message = []
        code = ResponseCode.NOK.value
        try:
            message = cls.user_repository.login(email, password)
            code = ResponseCode.OK.value
        except Exception as error:
            print(f"Deu pau")
            print(f"{error=}")
        finally:
            dto = ListStoreItemsDto(message=message, code=code)
            return dto.__dict__
