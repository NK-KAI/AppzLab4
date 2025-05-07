from fastapi import HTTPException

from db.database import SessionLocal
from db.repositories.user import UserRepository
from schemas.user import UserUpdate, UserCreate


class UserService:
    @staticmethod
    def create_user(user_data: UserCreate):
        db = SessionLocal()
        try:
            repo = UserRepository(db)
            return repo.create(user_data)
        finally:
            db.close()

    @staticmethod
    def delete_user(user_id: int):
        db = SessionLocal()
        try:
            repo = UserRepository(db)
            user = repo.get_by_id(user_id)
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            return repo.delete(user_id)
        finally:
            db.close()

    @staticmethod
    def update_user(user: UserUpdate):
        db = SessionLocal()
        try:
            repo = UserRepository(db)
            user = repo.get_by_id(UserUpdate.id)
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            return repo.update(user)
        finally:
            db.close()

    @staticmethod
    def get_by_id(user_id: int):
        db = SessionLocal()
        try:
            repo = UserRepository(db)
            user = repo.get_by_id(user_id)
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            return user
        finally:
            db.close()

    @staticmethod
    def get_all():
        db = SessionLocal()
        try:
            repo = UserRepository(db)
            categories = repo.get_all()
            if not categories:
                raise HTTPException(status_code=404, detail="Users not found")
            return categories
        finally:
            db.close()
