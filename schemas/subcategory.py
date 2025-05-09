from pydantic import BaseModel, typing
from typing import TYPE_CHECKING

from pydantic.fields import FieldInfo

from schemas import category

if TYPE_CHECKING:
    from category import CategoryBase


class SubcategoryBase(BaseModel):
    name: str
    category_id: int


class SubcategoryCreate(SubcategoryBase):
    pass


class SubcategoryResponse(SubcategoryBase):
    id: int
    category: category.CategoryBase


class SubcategoryUpdate(SubcategoryBase):
    pass
