from typing import Type

from sqlalchemy.orm import Session
from db.models import User
from schemas.user import UserUpdate, UserCreate, UserResponse


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: int) -> UserResponse:
        return self.db.query(User).filter(User.id == user_id).first()

    def get_all(self) -> list[Type[User]]:
        return self.db.query(User).all()

    def create(self, user_data: UserCreate) -> UserResponse:
        user = User(name=user_data.name)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user_id: int) -> None:
        self.db.query(User).filter_by(User.id==user_id).delete()
        self.db.commit()

    def update(self, user_new: User) -> UserResponse:
        self.db.query(User).filter(User.id==user_new.id).update({'id': user_new.id, 'name': user_new.name})
        self.db.commit()
        return user_new
