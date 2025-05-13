from typing import Type

from sqlalchemy.orm import Session
from db.models import Subcategory
from schemas.subcategory import SubcategoryUpdate, SubcategoryCreate


class SubcategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, category_id: int) -> Type[Subcategory] | None:
        return self.db.query(Subcategory).filter_by(id=category_id).first()

    def get_all(self) -> list[Type[Subcategory]]:
        return self.db.query(Subcategory).all()

    def create(self, subcategory: SubcategoryCreate) -> Subcategory:
        subcategory = Subcategory(name=subcategory.name,
                                  category_id=subcategory.category_id, )
        self.db.add(subcategory)
        self.db.commit()
        self.db.refresh(subcategory)
        return subcategory

    def delete(self, subcategory_id: int) -> None:
        self.db.query(Subcategory).filter_by(id=subcategory_id).delete()
        self.db.commit()

    def update(self, subcategory_new: Subcategory) -> Subcategory:
        self.db.query(User).filter_by(id=category_new.id).update({'name': subcategory_new.name,
                                                                  'category_id': subcategory_new.category_id,
                                                                  'category': subcategory_new.category})
        self.db.commit()
        return subcategory_new
