from fastapi import APIRouter, HTTPException, status
import httpx
from schemas import ProductList, Product
from config import settings

router = APIRouter(prefix="/api", tags=["Products"])

client = httpx.AsyncClient(base_url=settings.BACKEND_URL)


@router.get("/products", response_model=ProductList)
async def list_product(limit: int = None, page: int = None, name: str = None):
    try:
        params = {}
        if limit is not None:
            params["limit"] = limit
        if page is not None:
            params["page"] = page
        if name is not None:
            params["name"] = name

        response = await client.get("/products", params=params)
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


@router.get("/products/{product_id}", response_model=Product)
async def get_product_detail(product_id: str):
    try:
        response = await client.get(f"/products/{product_id}")
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
