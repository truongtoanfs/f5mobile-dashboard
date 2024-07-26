from pydantic import BaseModel
from datetime import datetime


class Product(BaseModel):
    id: str
    name: str
    old_price: int | None = None
    new_price: int
    avatar_url: str
    description: str | None = None
    category_id: str
    subcategory_id: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None


class ProductList(BaseModel):
    data: list[Product]
    total: int


class SubCategory(BaseModel):
    id: str
    name: str
    category_id: str


class Category(BaseModel):
    id: str
    name: str
    subcategories: list[SubCategory]


class CategoryDetail(Category):
    products: list[Product]


class ListCategory(BaseModel):
    data: list[Category]
    total: int
