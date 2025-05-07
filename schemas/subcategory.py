from pydantic import BaseModel
from typing import List


class SubcategoryBase(BaseModel):
    name: str


class SubcategoryCreate(SubcategoryBase):
    pass


class SubcategoryResponse(SubcategoryBase):
    id: int


class SubcategoryUpdate(SubcategoryBase):
    pass

