from pydantic import BaseModel
from typing import List

class OrderItem(BaseModel):
    product_id: str
    quantity: int
    size: str

class OrderCreate(BaseModel):
    user_id: str
    items: List[OrderItem]

class OrderOut(OrderCreate):
    id: str
