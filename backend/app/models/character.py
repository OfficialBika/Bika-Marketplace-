from pydantic import BaseModel
from typing import Optional

class Character(BaseModel):
    id: Optional[str] = None
    name: str
    rarity: Optional[str] = None
    owner_id: Optional[str] = None
