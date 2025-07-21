from fastapi import APIRouter, status
from app.database import db
from app.schemas.order import OrderCreate
from bson import ObjectId

router = APIRouter()

@router.post("/orders", status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderCreate):
    order_dict = order.dict()
    result = await db.orders.insert_one(order_dict)
    return {"id": str(result.inserted_id)}

@router.get("/orders/{user_id}")
async def get_orders_by_user(
    user_id: str,
    limit: int = 10,
    offset: int = 0
):
    cursor = db.orders.find({"user_id": user_id}).skip(offset).limit(limit)
    orders = []

    async for order in cursor:
        order["id"] = str(order["_id"])
        del order["_id"]
        orders.append(order)

    return orders
