from typing import List, Type

from sqlalchemy.orm import Session
from db.models import Category
from schemas.category import CategoryUpdate, CategoryCreate, CategoryResponse


class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, category_id: int) -> CategoryResponse:
        return self.db.query(Category).filter(Category.id == category_id).first()

    def create(self, category_data: CategoryCreate) -> CategoryResponse:
        category = Category(name=category_data.name)
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return category

    def delete(self, category_id: int) -> None:
        self.db.query(Category).filter_by(id=category_id).delete()
        self.db.commit()

    def update(self, category_new: Category) -> CategoryResponse:
        self.db.query(Category).filter(Category.id==category_new.id).update(category_new.__dict__)
        self.db.commit()
        return category_new

    def get_all(self) -> list[Type[CategoryResponse]]:
        return self.db.query(Category).all()
