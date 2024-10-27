from pydantic import BaseModel


class PlayerSchema(BaseModel):
    id: int
    name: str
    balance: int
    behavior_type: str
