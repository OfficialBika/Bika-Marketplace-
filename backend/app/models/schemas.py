from pydantic import BaseModel
from typing import Optional

class NFTCard(BaseModel):
    character_id: str
    name: str
    rarity: str
    catch_count: int = 0
    owner: str

class Auction(BaseModel):
    character_id: str
    seller_id: str
    current_bid: float
    coin: str = 'BKC'
    status: str = 'active'

class WalletTransaction(BaseModel):
    user_id: str
    title: str
    amount: float
    coin: str = 'BKC'
    type: str
