from src.services.user.service import UserService


class UserController:
    user_service = UserService()

    @classmethod
    def find_all_trainers(cls):
        return cls.user_service.find_all_trainers()

    @classmethod
    def login(cls, email, password):
        return cls.user_service.login(email, password)

    @classmethod
    def find_trainer_with_query(cls, field: str, value: str | int):
        return cls.user_service.find_trainer_with_query(field, value)

    @classmethod
    def find_trainer_field(cls, field: str):
        return cls.user_service.find_trainer_field(field)

    @classmethod
    def sign_in(cls, name: str, email: str, password: str, gender: str):
        return cls.user_service.sign_in(name, email, password, gender)

    @classmethod
    def alter_trainer(cls, email: str, field: str, value: str | int):
        return cls.user_service.alter_trainer(email, field, value)

    @classmethod
    def delete_trainer(cls, email: str):
        return cls.user_service.delete_trainer(email)


    @classmethod
    def sign_up(cls, email: str, password: str):
        return cls.user_service.login(email, password)
