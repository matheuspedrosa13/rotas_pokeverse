# Standard Libraries
from typing import Any

# Third-party Libraries
from pydantic import BaseModel, validator

# Project
from src.domain.enums.response_code.enum import ResponseCode


class OverallResponse(BaseModel):

    message: Any
    code: int

    @validator('code')
    def validate_code(cls, value: int) -> int:
        response_codes = [enum.value for enum in ResponseCode]
        if value in response_codes:
            return value

        raise TypeError("Codigo de retorno invalido")


