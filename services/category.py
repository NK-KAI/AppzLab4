from fastapi import HTTPException

from db.database import SessionLocal
from db.models import Category
from db.repositories.category import CategoryRepository
from schemas.category import CategoryUpdate, CategoryCreate


class CategoryService:
    @staticmethod
    def create_category(category_data: CategoryCreate):
        db = SessionLocal()
        try:
            repo = CategoryRepository(db)
            try:
                repo.create(category_data)
            except Exception as e:
                raise HTTPException(400, e.__str__())
        finally:
            db.close()

    @staticmethod
    def delete_category(category_id: int):
        db = SessionLocal()
        try:
            repo = CategoryRepository(db)
            category = repo.get_by_id(category_id)
            if not category:
                raise HTTPException(status_code=404, detail="Category not found")
            return repo.delete(category_id)
        finally:
            db.close()

    @staticmethod
    def update_category(category: CategoryUpdate):
        db = SessionLocal()
        try:
            repo = CategoryRepository(db)
            category = Category(name=CategoryUpdate.name,
                                subcategories=CategoryUpdate.subcategories,
                                announcements=CategoryUpdate.announcements,
                                )
            if not category:
                raise HTTPException(status_code=404, detail="Category not found")
            return repo.update(category)
        finally:
            db.close()

    @staticmethod
    def get_by_id(category_id: int):
        db = SessionLocal()
        try:
            repo = CategoryRepository(db)
            category = repo.get_by_id(category_id)
            if not category:
                raise HTTPException(status_code=404, detail="Category not found")
            return category
        finally:
            db.close()

    @staticmethod
    def get_all():
        db = SessionLocal()
        try:
            repo = CategoryRepository(db)
            categories = repo.get_all()
            if not categories:
                raise HTTPException(status_code=404, detail="Categories not found")
            return categories
        finally:
            db.close()
