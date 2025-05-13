from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from db.database import SessionLocal, get_db
from db.models import TokenData
from db.repositories.user import UserRepository
from schemas.user import UserUpdate, UserCreate


class UserService:
    @staticmethod
    def create_user(user: UserCreate, db: Session):
        repo = UserRepository(db)
        user = repo.get_by_name(user.name)
        if not user:
            return False
        return user

    @staticmethod
    def delete_user(user_id: int, db: Session):
        repo = UserRepository(db)
        user = repo.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return repo.delete(user_id)

    @staticmethod
    def update_user(user: UserUpdate, db: Session):
        repo = UserRepository(db)
        user_old = repo.get_by_id(user.id)
        if not user_old:
            raise HTTPException(status_code=404, detail="User not found")
        return repo.update(user)

    @staticmethod
    def get_by_id(user_id: int, db: Session):
        repo = UserRepository(db)
        user = repo.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @staticmethod
    def get_by_name(username: str, db: Session):
        repo = UserRepository(db)
        user = repo.get_by_name(username)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @staticmethod
    def get_all(db: Session):
        repo = UserRepository(db)
        categories = repo.get_all()
        if not categories:
            raise HTTPException(status_code=404, detail="Users not found")
        return categories
