from fastapi import HTTPException

from db.database import SessionLocal
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
            subcategory = repo.get_by_id(SubcategoryUpdate.id)
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
