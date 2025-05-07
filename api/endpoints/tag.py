from fastapi import APIRouter, HTTPException, status
from services.tag import TagService
from schemas.tag import TagResponse, TagCreate, TagUpdate

router = APIRouter(prefix="/tag", tags=["tag"])


@router.post("/", response_model=TagResponse, status_code=status.HTTP_201_CREATED)
def create_tag(tag_data: TagCreate):
    return TagService.create_tag(tag_data)


@router.delete("/{tag_id}", response_model=TagResponse)
def delete_tag(tag_id: int):
    return TagService.delete_tag(tag_id)


@router.get("/{tag_id}", response_model=TagResponse)
def get_tag(tag_id: int):
    return TagService.get_by_id(tag_id)


@router.get("/", response_model=list[TagResponse])
def get_tags():
    return TagService.get_all()


@router.put("/", response_model=TagResponse)
def update_tag(tag_data: TagUpdate):
    return TagService.update_tag(tag_data)