from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from services.tag import TagService
from schemas.tag import TagResponse, TagCreate, TagUpdate

router = APIRouter(prefix="/tag", tags=["tag"])


@router.post("/", response_model=TagResponse, status_code=status.HTTP_201_CREATED)
def create_tag(tag_data: TagCreate, db: Session = Depends(get_db)):
    return TagService.create_tag(tag_data, db)


@router.delete("/{tag_id}", response_model=TagResponse)
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    return TagService.delete_tag(tag_id, db)


@router.get("/{tag_id}", response_model=TagResponse)
def get_tag(tag_id: int, db: Session = Depends(get_db)):
    return TagService.get_by_id(tag_id, db)


@router.get("/", response_model=list[TagResponse])
def get_tags(db: Session = Depends(get_db)):
    return TagService.get_all(db)


@router.put("/", response_model=TagResponse)
def update_tag(tag_data: TagUpdate, db: Session = Depends(get_db)):
    return TagService.update_tag(tag_data, db)
