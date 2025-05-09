from fastapi import APIRouter, HTTPException, status
from services.user import UserService
from schemas.user import UserResponse, UserCreate, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate):
    return UserService.create_user(user_data)


@router.delete("/{user_id}", response_model=UserResponse)
def delete_user(user_id: int):
    return UserService.delete_user(user_id)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return UserService.get_by_id(user_id)


@router.get("/", response_model=list[UserResponse])
def get_users():
    return UserService.get_all()


@router.put("/", response_model=UserResponse)
def update_user(user_data: UserUpdate):
    return UserService.update_user(user_data)
