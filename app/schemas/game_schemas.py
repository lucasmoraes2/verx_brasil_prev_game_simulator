from pydantic import BaseModel
from typing import List


class GameSchema(BaseModel):
    winner: str
    players: List[str]
