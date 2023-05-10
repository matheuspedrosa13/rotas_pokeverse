# Standard Libraries
from typing import List

<<<<<<< HEAD
import pymongo

=======
>>>>>>> 27c10acf01476f4b78fbb69ed015dc78d3ca4ce4
from src.domain.dtos.overall_response.dto import OverallResponse


class ListStoreItemsDto(OverallResponse):

    message: List[dict]
