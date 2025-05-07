from pydantic import BaseModel, Field
from typing import List
from schemas.user import UserCreate


class AnnouncementBase(BaseModel):
    title: str
    description: str
    category_id: int
    user_id: int
    user: UserCreate
    tag_ids: list[int] = Field(default_factory=list)


class AnnouncementCreate(AnnouncementBase):
    pass


class AnnouncementResponse(AnnouncementBase):
    id: int
    is_active: bool


class AnnouncementUpdate(AnnouncementBase):
    id: int
    is_active: bool


class AnnouncementRead(BaseModel):
    id: int
    is_active: bool

    class Config:
        from_attributes = True
