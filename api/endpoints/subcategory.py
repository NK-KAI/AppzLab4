from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from services.subcategory import SubcategoryService
from schemas import SubcategorySchema

router = APIRouter(prefix="/subcategories", tags=["subcategories"])


@router.post("/", response_model=SubcategorySchema, status_code=status.HTTP_201_CREATED)
def create_subcategory(subcategory_data: SubcategorySchema, db: Session = Depends(get_db)):
    return SubcategoryService.create_subcategory(subcategory_data, db)


@router.get("/{subcategory_id}", response_model=SubcategorySchema)
def get_subcategory(subcategory_id: int, db: Session = Depends(get_db)):
    return SubcategoryService.get_by_id(subcategory_id, db)


@router.get("/", response_model=list[SubcategorySchema])
def get_all(db: Session = Depends(get_db)):
    return SubcategoryService.get_all(db)


@router.delete("/{subcategory_id}", response_model=SubcategorySchema)
def delete_subcategory(subcategory_id: int, db: Session = Depends(get_db)):
    return SubcategoryService.delete_subcategory(subcategory_id, db)


@router.put("/", response_model=SubcategorySchema)
def update_subcategory(subcategory_data: SubcategorySchema, db: Session = Depends(get_db)):
    return SubcategoryService.update_subcategory(subcategory_data, db)
