# Standard Libraries
from typing import List

import pymongo

from src.domain.dtos.overall_response.dto import OverallResponse


class ListStoreItemsDto(OverallResponse):

    message: List[dict]
