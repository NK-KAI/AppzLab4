from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session

from db.database import SessionLocal, get_db
from db.models import Category
from db.repositories.category import CategoryRepository
from schemas import CategorySchema


class CategoryService:
    @staticmethod
    def create_category(category_data: CategorySchema, db: Session):
        print(db)
        repo = CategoryRepository(db)
        try:
            repo.create(category_data)
        except Exception as e:
            raise HTTPException(400, e.__str__())

    @staticmethod
    def delete_category(category_id: int, db: Session):
        repo = CategoryRepository(db)
        category = repo.get_by_id(category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return repo.delete(category_id)

    @staticmethod
    def update_category(category: CategorySchema, db: Session):
        repo = CategoryRepository(db)
        category = Category(id=category.id,
                            name=category.name,
                            subcategories=category.subcategories,
                            announcements=category.announcements,
                            )
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return repo.update(category)

    @staticmethod
    def get_by_id(category_id: int, db: Session):
        repo = CategoryRepository(db)
        category = repo.get_by_id(category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return category

    @staticmethod
    def get_all(db):
        repo = CategoryRepository(db)
        categories = repo.get_all()
        if not categories:
            raise HTTPException(status_code=404, detail="Categories not found")
        return categories
