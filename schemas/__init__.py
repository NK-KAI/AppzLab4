from pydantic import BaseModel, typing, Field
from typing import TYPE_CHECKING, Optional

from schemas.announcement import AnnouncementBase


class CategoryBase(BaseModel):
    name: str = Field(alias='name')

    class Config:
        from_attributes = True
        allow_population_by_field_name = True


class SubcategoryBase(BaseModel):
    name: str = Field(alias='name')
    category_id: int

    class Config:
        from_attributes = True
        allow_population_by_field_name = True


class CategorySchema(CategoryBase):
    subcategories: list[SubcategoryBase] = Field(default_factory=list)
    announcements: Optional[list[AnnouncementBase]] = Field(default_factory=list)


class SubcategorySchema(SubcategoryBase):
    category_id: int = Field(alias='category_id')
