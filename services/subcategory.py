from fastapi import HTTPException
from sqlalchemy.orm import Session
from db.models import Subcategory
from db.repositories.subcategory import SubcategoryRepository
from schemas import SubcategorySchema


class SubcategoryService:
    @staticmethod
    def create_subcategory(subcategory_data: SubcategorySchema, db: Session):
        repo = SubcategoryRepository(db)
        return repo.create(subcategory_data)

    @staticmethod
    def delete_subcategory(subcategory_id: int, db: Session):
        repo = SubcategoryRepository(db)
        subcategory = repo.get_by_id(subcategory_id)
        if not subcategory:
            raise HTTPException(status_code=404, detail="Subcategory not found")
        return repo.delete(subcategory_id)

    @staticmethod
    def update_subcategory(subcategory: SubcategorySchema, db: Session):
        repo = SubcategoryRepository(db)
        subcategory = Subcategory(
            name=subcategory.name,
            category_id=subcategory.category_id,
            category=subcategory.category,)

        if not subcategory:
            raise HTTPException(status_code=404, detail="Subcategory not found")
        return repo.update(subcategory)

    @staticmethod
    def get_by_id(subcategory_id: int, db: Session):
        repo = SubcategoryRepository(db)
        subcategory = repo.get_by_id(subcategory_id)
        if not subcategory:
            raise HTTPException(status_code=404, detail="Subcategory not found")
        return subcategory

    @staticmethod
    def get_all(db: Session):
        repo = SubcategoryRepository(db)
        subcategories = repo.get_all()
        if not subcategories:
            raise HTTPException(status_code=404, detail="Subcategories not found")
        return subcategories
