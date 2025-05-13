from pydantic import BaseModel, typing, Field
from typing import TYPE_CHECKING, Optional

from schemas.announcement import AnnouncementBase


class CategoryBase(BaseModel):
    name: str = Field(alias='name')

    class Config:
        from_attributes = True
        validate_by_name = True


class SubcategoryBase(BaseModel):
    name: str = Field(alias='name')
    category_id: int

    class Config:
        from_attributes = True
        validate_by_name = True


class CategorySchema(CategoryBase):
    id: int
    subcategories: list[SubcategoryBase] = Field(default_factory=list)
    announcements: Optional[list[AnnouncementBase]] = Field(default_factory=list)


class SubcategorySchema(SubcategoryBase):
    id: int
    category_id: int = Field(alias='category_id')
    category: CategoryBase = Field(alias='category')
