from fastapi import APIRouter, HTTPException, status, Query
from typing import Annotated
import httpx
from schemas import ProductList, Product
from config import settings

router = APIRouter(prefix="/api", tags=["Products"])

client = httpx.AsyncClient(base_url=settings.BACKEND_URL)


@router.get("/products", response_model=ProductList)
async def list_product(
    name: str | None = None,
    limit: Annotated[int, Query(gt=0)] = 100,
    page: Annotated[int, Query(gt=0)] = 1,
    sort_key: Annotated[str, Query(pattern="^(new_price|created_at|name|old_price|updated_at)$")] = "name",
    order_by: Annotated[str, Query(pattern="^(desc|asc)$")] = "desc",
):
    try:
        params = {
            "name": name,
            "limit": limit,
            "page": page,
            "sort_key": sort_key,
            "order_by": order_by,
        }
        if name is None:
            del params["name"]

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
