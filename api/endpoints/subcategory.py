from fastapi import APIRouter, HTTPException, status
from services.subcategory import SubcategoryService
from schemas.subcategory import SubcategoryResponse, SubcategoryCreate, SubcategoryUpdate

router = APIRouter(prefix="/subcategories", tags=["subcategories"])


@router.post("/", response_model=SubcategoryResponse, status_code=status.HTTP_201_CREATED)
def create_subcategory(subcategory_data: SubcategoryCreate):
    return SubcategoryService.create_subcategory(subcategory_data)


@router.get("/{subcategory_id}", response_model=SubcategoryResponse)
def get_subcategory(subcategory_id: int):
    return SubcategoryService.get_by_id(subcategory_id)


@router.get("/", response_model=SubcategoryResponse)
def get_all():
    return SubcategoryService.get_all()


@router.delete("/{subcategory_id}", response_model=SubcategoryResponse)
def delete_subcategory(subcategory_id: int):
    return SubcategoryService.delete_subcategory(subcategory_id)


@router.put("/{}", response_model=SubcategoryResponse)
def update_subcategory(subcategory_data: SubcategoryUpdate):
    return SubcategoryService.update_subcategory(subcategory_data)
