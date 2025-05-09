from fastapi import HTTPException

from db.database import SessionLocal
from db.models import Subcategory
from db.repositories.subcategory import SubcategoryRepository
from schemas.subcategory import SubcategoryUpdate, SubcategoryCreate


class SubcategoryService:
    @staticmethod
    def create_subcategory(subcategory_data: SubcategoryCreate):
        db = SessionLocal()
        try:
            repo = SubcategoryRepository(db)
            return repo.create(subcategory_data)
        finally:
            db.close()

    @staticmethod
    def delete_subcategory(subcategory_id: int):
        db = SessionLocal()
        try:
            repo = SubcategoryRepository(db)
            subcategory = repo.get_by_id(subcategory_id)
            if not subcategory:
                raise HTTPException(status_code=404, detail="Subcategory not found")
            return repo.delete(subcategory_id)
        finally:
            db.close()

    @staticmethod
    def update_subcategory(subcategory: SubcategoryUpdate):
        db = SessionLocal()
        try:
            repo = SubcategoryRepository(db)
            subcategory = Subcategory(
                name=subcategory.name,
                category_id=subcategory.category_id,
                category=subcategory.category,)

            if not subcategory:
                raise HTTPException(status_code=404, detail="Subcategory not found")
            return repo.update(subcategory)
        finally:
            db.close()

    @staticmethod
    def get_by_id(subcategory_id: int):
        db = SessionLocal()
        try:
            repo = SubcategoryRepository(db)
            subcategory = repo.get_by_id(subcategory_id)
            if not subcategory:
                raise HTTPException(status_code=404, detail="Subcategory not found")
            return subcategory
        finally:
            db.close()

    @staticmethod
    def get_all():
        db = SessionLocal()
        try:
            repo = SubcategoryRepository(db)
            subcategories = repo.get_all()
            if not subcategories:
                raise HTTPException(status_code=404, detail="Subcategories not found")
            return subcategories
        finally:
            db.close()
