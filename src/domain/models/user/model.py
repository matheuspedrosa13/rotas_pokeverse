<<<<<<< HEAD
from pydantic import BaseModel, validator
from src.domain.enums.places_names.enum import LocalName
from src.domain.enums.gender_options.enum import GenderOptions
=======
from pydantic import BaseModel
>>>>>>> 27c10acf01476f4b78fbb69ed015dc78d3ca4ce4


class UserModel(BaseModel):
    name: str
    email: str
    password: str
    gender: str
    pokemon: list
    items: list
    money: int
<<<<<<< HEAD
    place: str

    @validator('place')
    def validate_place(cls, value: str) -> str:
        locals_name = [enum.value for enum in LocalName]
        if value in locals_name:
            return value

        raise TypeError(f"Invalid item name! Received {value}, try one of {locals_name}")

    @validator('gender')
    def validate_gender(cls, value: str) -> str:
        gender_options = [enum.value for enum in GenderOptions]
        if value in gender_options:
            return value

        raise TypeError(f"Invalid item name! Received {value}, try one of {gender_options}")
=======
    place: int
>>>>>>> 27c10acf01476f4b78fbb69ed015dc78d3ca4ce4
