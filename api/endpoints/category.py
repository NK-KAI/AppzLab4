from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from services.category import CategoryService
from schemas import CategorySchema
router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("/", response_model=CategorySchema, status_code=status.HTTP_201_CREATED)
def create_category(category_data: CategorySchema, db: Session = Depends(get_db)):
    return CategoryService.create_category(category_data, db)


@router.delete("/{category_id}", response_model=CategorySchema)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    return CategoryService.delete_category(category_id, db)


@router.get("/{category_id}", response_model=CategorySchema)
def get_category(category_id: int, db: Session = Depends(get_db)):
    return CategoryService.get_by_id(category_id, db)


@router.get("/", response_model=list[CategorySchema])
def get_all_categories(db: Session = Depends(get_db)):
    return CategoryService.get_all(db)


@router.delete("/{category_id}", response_model=CategorySchema)
def delete_category_by_id(category_id: int, db: Session = Depends(get_db)):
    return CategoryService.delete_category(category_id, db)


@router.put("/", response_model=CategorySchema)
def update_category(category_data: CategorySchema, db: Session = Depends(get_db)):
    return CategoryService.update_category(category_data, db)
