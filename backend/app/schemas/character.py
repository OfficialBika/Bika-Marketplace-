from typing import Any, Optional, List
from pydantic import BaseModel


class CharacterResponse(BaseModel):
    id: str
    name: Optional[str] = None
    rarity: Optional[str] = None
    owner_id: Optional[str] = None
    image: Optional[str] = None
    attributes: List[Any] = []
    status: Optional[str] = None


class CharacterListResponse(BaseModel):
    success: bool = True
    data: List[CharacterResponse] = []
