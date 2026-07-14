from typing import Optional, List, Any
from pydantic import BaseModel


class MarketplaceItem(BaseModel):
    id: str
    character_id: Optional[str] = None
    owner_id: Optional[str] = None
    price: float = 0
    coin: str = 'BKC'
    rarity: Optional[str] = None
    status: Optional[str] = 'active'
    attributes: List[Any] = []


class MarketplaceResponse(BaseModel):
    success: bool = True
    data: List[MarketplaceItem] = []
