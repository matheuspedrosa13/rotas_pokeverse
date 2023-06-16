import requests

from src.domain.dtos.list_store_items.dto import ListStoreItemsDto
from src.domain.enums.response_code.enum import ResponseCode
from src.repositories.user.repository import UserRepo


class UserService:
    user_repository = UserRepo()

    @classmethod
    def change_place(cls, email, place):
        return cls.user_repository.change_place(email, place)

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
            print(message)
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

    @classmethod
    def sign_in(cls, name, email, password, gender):
        print(password)
        message = []
        code = ResponseCode.NOK.value
        password_encrypted_response = requests.get(f'https://auth-pokeverse.onrender.com/encrypted?password={password}')
        password_encrypted = password_encrypted_response.text.strip('"')
        infos = {
            "name": name,
            "email": email,
            "password": password_encrypted,
            "gender": gender,
            "items": [
                ['pokeball', 0],
                ['greatball', 0],
                ['ultraball', 0],
                ['banana', 0],
                ['abacaxi', 0],
                ['uva', 0],
                ['upgraded_banana', 0],
                ['upgraded_abacaxi', 0],
                ['upgraded_uva', 0]
            ],
            "money": 0,
            "place": "bras"
        }

        # password_decrypted_response = requests.get(f'http://localhost:9999/descrypting?password={password_encrypted}')
        # password_decrypted = password_decrypted_response.text.strip('()').strip('"')
        # jwt_token_response = requests.get(
        #     f'http://localhost:9999/create_jwt?pass_cripto={password_decrypted}&password={password}&email={email}')
        # jwt_token = jwt_token_response.text

        try:
            print("aaaaaaaaaaa")
            message = cls.user_repository.insert(infos)
            code = ResponseCode.OK.value
        except Exception as error:
            print("Deu pau")
            print(f"error: {error}")

        finally:
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

        password_encrypted_response = requests.get(f'https://auth-pokeverse.onrender.com/encrypted?password={password}').text

        password_decrypted_response = requests.get(
            f'https://auth-pokeverse.onrender.com/descrypting?password={password_encrypted_response}').text

        password_decrypted = password_decrypted_response.strip(')').strip('"').strip(')')

        jwt_token_response = requests.get(
            f'https://auth-pokeverse.onrender.com/create_jwt?pass_cripto={password_decrypted}&password={password}&email={email}')
        jwt_token = jwt_token_response.text

        try:
            message = cls.user_repository.login(email, password_encrypted_response, jwt_token)
            code = ResponseCode.OK.value
        except Exception as error:
            print(f"Deu pau")
            print(f"{error=}")
        finally:
            dto = ListStoreItemsDto(message=message, code=code)
            return dto.__dict__

    @classmethod
    def show_all_items(cls, email):
        message = []
        code = ResponseCode.NOK.value
        try:
            message = cls.user_repository.find({"email": email}, {"_id": 0, "items": 1})
            code = ResponseCode.OK.value
        except Exception as error:
            print(f"Deu pau")
            print(f"{error=}")
        finally:
            dto = ListStoreItemsDto(message=message, code=code)
            return dto.__dict__


# TODO trocar localHost para auth
# UserService().find_trainer_with_query("email", "guizz@gmail.com")
