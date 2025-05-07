from typing import Type

from sqlalchemy.orm import Session
from db.models import Subcategory
from schemas.subcategory import SubcategoryUpdate, SubcategoryCreate


class SubcategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, category_id: int) -> Subcategory:
        return self.db.query(Subcategory).filter(Subcategory.id == category_id).first()

    def get_all(self) -> list[Type[Subcategory]]:
        return self.db.query(Subcategory).all()

    def create(self, category_data: SubcategoryCreate) -> Subcategory:
        subcategory = Subcategory(name=category_data.name)
        self.db.add(subcategory)
        self.db.commit()
        self.db.refresh(subcategory)
        return subcategory

    def delete(self, subcategory_id: int) -> None:
        self.db.query(Subcategory).filter_by(id=subcategory_id).delete()
        self.db.commit()

    def update(self, subcategory_new: Subcategory) -> Subcategory:
        self.db.query(User).filter(id=category_new.id).update(subcategory_new.__dict__)
        self.db.commit()
        return subcategory_new
