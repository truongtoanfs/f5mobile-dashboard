from fastapi import APIRouter
import httpx
from schemas import ProductList, Product

router = APIRouter(prefix="/api", tags=["Products"])


@router.get("/products", response_model=ProductList)
async def list_product(limit: int = None, page: int = None, name: str = None):
    api_url = "http://127.0.0.1:8000/api/products"
    async with httpx.AsyncClient() as client:
        params = {}
        if limit is not None:
            params['limit'] = limit
        if page is not None:
            params['page'] = page
        if name is not None:
            params['name'] = name
        response = await client.get(api_url, params=params)
        return response.json()


@router.get("/products/{product_id}", response_model=Product)
async def get_product_detail(product_id: str):
    api_url = f"http://127.0.0.1:8000/api/products/{product_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
        return response.json()
