from fastapi import APIRouter, HTTPException, status
from services.category import CategoryService
from schemas import CategorySchema
router = APIRouter(prefix="/categories", tags=["categories"])


@router.post("/", response_model=CategorySchema, status_code=status.HTTP_201_CREATED)
def create_category(category_data: CategorySchema):
    return CategoryService.create_category(category_data)


@router.delete("/{category_id}", response_model=CategorySchema)
def delete_category(category_id: int):
    return CategoryService.delete_category(category_id)


@router.get("/{category_id}", response_model=CategorySchema)
def get_category(category_id: int):
    return CategoryService.get_by_id(category_id)


@router.get("/", response_model=list[CategorySchema])
def get_all_categories():
    return CategoryService.get_all()


@router.delete("/{category_id}", response_model=CategorySchema)
def delete_category_by_id(category_id: int):
    return CategoryService.delete_category(category_id)


@router.put("/", response_model=CategorySchema)
def update_category(category_data: CategorySchema):
    return CategoryService.update_category(category_data)
