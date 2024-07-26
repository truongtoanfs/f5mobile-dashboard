from fastapi import APIRouter
import httpx
from schemas import ListCategory, Category, CategoryDetail

router = APIRouter(prefix="/api", tags=["Category"])


@router.get("/categories", response_model=ListCategory)
async def list_category():
    api_url = "http://127.0.0.1:8000/api/categories"
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
        return response.json()


@router.get("/categories/{category_id}", response_model=CategoryDetail)
async def get_category_detail(category_id: str):
    api_url = f"http://127.0.0.1:8000/api/categories/{category_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(api_url)
        return response.json()
