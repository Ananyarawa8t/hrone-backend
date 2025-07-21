from fastapi import APIRouter, status , Query
from app.database import db
from app.schemas.product import ProductCreate, ProductOut
from bson import ObjectId
import re

router = APIRouter()

@router.post("/products", status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate):
    product_dict = product.dict()
    result = await db.products.insert_one(product_dict)
    return {"id": str(result.inserted_id)}

@router.get("/products")
async def list_products(
    name: str = Query(None),
    size: str = Query(None),
    limit: int = 10,
    offset: int = 0
):
    query = {}
    if name:
        query["name"] = {"$regex": re.escape(name), "$options": "i"}
    if size:
        query["sizes"] = size

    cursor = db.products.find(query).skip(offset).limit(limit)
    products = []
    async for product in cursor:
        product["id"] = str(product["_id"])
        del product["_id"]
        products.append(product)
    return products