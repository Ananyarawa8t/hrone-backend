# HROne Backend Task

###  Tech Stack
- FastAPI
- MongoDB (Atlas Free Tier)
- Motor (Async driver)
- Uvicorn

###  APIs

- `POST /products`: Create a product
- `GET /products`: List products with filters (name regex, size, limit, offset)
- `POST /orders`: Create order
- `GET /orders/{user_id}`: Get orders for a user

### Deployment

Deployed using [Render / Railway]

- Base URL: `https://<your-deployment-url>`
- MongoDB URL is loaded via `.env`
