from pydantic import BaseModel


class PurchaseRequest(BaseModel):
    buyer_id: str
    seller_id: str
    character_id: str
    amount: float
    coin: str = 'BKC'
