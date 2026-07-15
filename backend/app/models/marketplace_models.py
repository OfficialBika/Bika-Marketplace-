from pydantic import BaseModel
from typing import Optional

class CharacterModel(BaseModel):
    name: str
    image: Optional[str] = None
    rarity: str = "Supreme"
    price: float = 0

class PurchaseModel(BaseModel):
    user_id: str
    character_id: str
    amount: float

class BidModel(BaseModel):
    user_id: str
    auction_id: str
    amount: float
