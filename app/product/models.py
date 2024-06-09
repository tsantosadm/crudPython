from pydantic import BaseModel, Field
from typing import Literal


class ProductsQuery(BaseModel):
    name: str | None = Field(None, description='Name of the product')
    page: int = Field(1, description='The page number', gt=0)
    per_page: int = Field(10, description='The page list size', gt=0)


class ProductRequest(BaseModel):
    name: str = Field(..., description='Name of the product')
    price: float = Field(..., description='Price of the product')
    description: str = Field(None, description="Description of the product")


class ProductResponse(ProductRequest):
    id: int = Field(..., description='The product id')


class ProductsResponse(BaseModel):
    products: list[ProductResponse] = Field([], description='List of products')
    total_pages: int = Field(1, description='Total of pages', ge=1)


class ProductIdPath(BaseModel):
    product_id: int


class ProductNotFound(BaseModel):
    error_type: Literal['ID_NOT_FOUND'] = 'ID_NOT_FOUND'
