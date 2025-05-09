from pydantic import BaseModel, Field
from typing import List
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from schemas.subcategory import SubcategoryCreate


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int
    subcategories: List["SubcategoryCreate"]


class CategoryUpdate(CategoryBase):
    id: int


class CategoryRead(BaseModel):
    id: int
    subcategories: List["SubcategoryCreate"]

    class Config:
        from_attributes = True
