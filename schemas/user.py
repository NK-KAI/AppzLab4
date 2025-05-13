from pydantic import BaseModel
from typing import List


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    id: int


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True
