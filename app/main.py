from fastapi import FastAPI
from app.routes.product import router as product_router
from app.routes.order import router as order_router

app = FastAPI()

app.include_router(product_router)
app.include_router(order_router)

