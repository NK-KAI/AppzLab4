from fastapi import APIRouter, HTTPException, status
from services.subcategory import SubcategoryService
from schemas import SubcategorySchema

router = APIRouter(prefix="/subcategories", tags=["subcategories"])


@router.post("/", response_model=SubcategorySchema, status_code=status.HTTP_201_CREATED)
def create_subcategory(subcategory_data: SubcategorySchema):
    return SubcategoryService.create_subcategory(subcategory_data)


@router.get("/{subcategory_id}", response_model=SubcategorySchema)
def get_subcategory(subcategory_id: int):
    return SubcategoryService.get_by_id(subcategory_id)


@router.get("/", response_model=SubcategorySchema)
def get_all():
    return SubcategoryService.get_all()


@router.delete("/{subcategory_id}", response_model=SubcategorySchema)
def delete_subcategory(subcategory_id: int):
    return SubcategoryService.delete_subcategory(subcategory_id)


@router.put("/", response_model=SubcategorySchema)
def update_subcategory(subcategory_data: SubcategorySchema):
    return SubcategoryService.update_subcategory(subcategory_data)
