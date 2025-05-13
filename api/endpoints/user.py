from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from services.user import UserService
from schemas.user import UserResponse, UserCreate, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService
    registered_error = HTTPException(status_code=400, detail="Username already registered")
    try:
        db_user = user_service.get_by_name(username=user.name, db=db)
        if db_user:
            raise HTTPException(status_code=400, detail="Username already registered")
    except HTTPException as e:
        if e.status_code == 404:
            db_user = User(name=user.name, password=user.password)
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user
    raise registered_error


@router.delete("/{user_id}", response_model=UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return UserService.delete_user(user_id, db)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return UserService.get_by_id(user_id, db)


@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return UserService.get_all(db)


@router.put("/", response_model=UserResponse)
def update_user(user_data: UserUpdate, db: Session = Depends(get_db)):
    return UserService.update_user(user_data, db)
