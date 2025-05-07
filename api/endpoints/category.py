from fastapi import APIRouter, HTTPException, status
from services.category import CategoryService
from schemas.category import CategoryResponse, CategoryCreate, CategoryUpdate

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(category_data: CategoryCreate):
    return CategoryService.create_category(category_data)


@router.delete("/{category_id}", response_model=CategoryResponse)
def delete_category(category_id: int):
    return CategoryService.delete_category(category_id)


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int):
    return CategoryService.get_by_id(category_id)


@router.get("/", response_model=list[CategoryResponse])
def get_all_categories():
    return CategoryService.get_all()


@router.delete("/{category_id}", response_model=CategoryResponse)
def delete_category_by_id(category_id: int):
    return CategoryService.delete_category(category_id)


@router.put("/", response_model=CategoryResponse)
def update_category(category_data: CategoryUpdate):
    return CategoryService.update_category(category_data)
