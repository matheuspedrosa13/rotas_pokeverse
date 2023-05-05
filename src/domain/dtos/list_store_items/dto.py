# Standard Libraries
from typing import List

from src.domain.dtos.overall_response.dto import OverallResponse


class ListStoreItemsDto(OverallResponse):

    message: List[dict]
