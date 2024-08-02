from fastapi import APIRouter, HTTPException, status
import httpx
from schemas import ListCategory, CategoryDetail
from config import settings

router = APIRouter(prefix="/api", tags=["Category"])
client = httpx.AsyncClient(base_url=settings.BACKEND_URL)


@router.get("/categories", response_model=ListCategory)
async def list_category():
    try:
        response = await client.get("/categories")
        return response.json()
    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
        )
    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=exc.response.status_code,
            detail=str(exc),
        )


@router.get("/categories/{category_id}", response_model=CategoryDetail)
async def get_category_detail(category_id: str):
    try:
        response = await client.get(f"/categories/{category_id}")
        return response.json()
    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
        )
    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=exc.response.status_code,
            detail=str(exc),
        )
