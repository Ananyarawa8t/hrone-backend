from pydantic import BaseModel
from typing import List

class Size(BaseModel):
    size: str
    quantity: int

class ProductBase(BaseModel):
    name: str
    price: float

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: str
