from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[int]
    name: str
    email: str

class Item(BaseModel):
    id: Optional[int]
    name: str
    owner_id: int
