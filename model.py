from typing import List

from pydantic import BaseModel


class Recipe(BaseModel):
    name: str
    steps: List[str]
    ingredients: List[str]
    type: str
