from pydantic import BaseModel
from typing import Optional

class Wallet(BaseModel):
    user_id: str
    balance: int = 0
    currency: str = "BKC"
