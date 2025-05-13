from fastapi import HTTPException
from sqlalchemy.orm import Session

from db.database import SessionLocal
from db.repositories.tag import TagRepository
from schemas.tag import TagUpdate, TagCreate


class TagService:
    @staticmethod
    def create_tag(tag_data: TagCreate, db: Session):
        repo = TagRepository(db)
        return repo.create(tag_data)

    @staticmethod
    def delete_tag(tag_id: int, db: Session):
        repo = TagRepository(db)
        tag = repo.get_by_id(tag_id)
        if not tag:
            raise HTTPException(status_code=404, detail="Tag not found")
        return repo.delete(tag_id)

    @staticmethod
    def update_tag(new_tag: TagUpdate, db: Session):
        repo = TagRepository(db)
        tag = repo.get_by_id(new_tag.id)
        if not tag:
            raise HTTPException(status_code=404, detail="Tag not found")
        return repo.update(new_tag)

    @staticmethod
    def get_by_id(tag_id: int, db: Session):
        repo = TagRepository(db)
        tag = repo.get_by_id(tag_id)
        if not tag:
            raise HTTPException(status_code=404, detail="Tag not found")
        return tag

    @staticmethod
    def get_all(db: Session):
        repo = TagRepository(db)
        categories = repo.get_all()
        if not categories:
            raise HTTPException(status_code=404, detail="Tags not found")
        return categories
