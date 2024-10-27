from pydantic import BaseModel


class PropertySchema(BaseModel):
    id: int
    cost: int
    rent: int
    owner_id: int
