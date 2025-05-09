from pydantic import BaseModel
from typing import List


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int


class UserUpdate(UserBase):
    id: int
