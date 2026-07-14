from typing import Optional
from pydantic import BaseModel


class CharacterPurchaseRequest(BaseModel):
    buyer_id: str
    seller_id: str
    character_id: str
    amount: float
    coin: str = 'BKC'


class TransactionResponse(BaseModel):
    success: bool = True
    transaction_id: Optional[str] = None
    message: Optional[str] = None
