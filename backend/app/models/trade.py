from pydantic import BaseModel
from typing import Optional

class Trade(BaseModel):
    id: Optional[str] = None
    user_id: str
    item_id: str
    amount: int = 0
    status: str = "pending"
