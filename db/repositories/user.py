from sqlalchemy.orm import Session
from db.models import User
from schemas.user import UserUpdate, UserCreate


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()

    def create(self, user_data: UserCreate) -> User:
        user = User(name=user_data.name)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user_id: int) -> None:
        self.db.query(User).filter_by(id=user_id).delete()
        self.db.commit()

    def update(self, user_new: User) -> User:
        self.db.query(User).filter(id=user_new.id).update(user_new.__dict__)
        self.db.commit()
        return user_new
