from fastapi import HTTPException

from db.database import SessionLocal
from db.repositories.tag import TagRepository
from schemas.tag import TagUpdate, TagCreate


class TagService:
    @staticmethod
    def create_tag(tag_data: TagCreate):
        db = SessionLocal()
        try:
            repo = TagRepository(db)
            return repo.create(tag_data)
        finally:
            db.close()

    @staticmethod
    def delete_tag(tag_id: int):
        db = SessionLocal()
        try:
            repo = TagRepository(db)
            tag = repo.get_by_id(tag_id)
            if not tag:
                raise HTTPException(status_code=404, detail="Tag not found")
            return repo.delete(tag_id)
        finally:
            db.close()

    @staticmethod
    def update_tag(tag: TagUpdate):
        db = SessionLocal()
        try:
            repo = TagRepository(db)
            tag = repo.get_by_id(TagUpdate.id)
            if not tag:
                raise HTTPException(status_code=404, detail="Tag not found")
            return repo.update(tag)
        finally:
            db.close()

    @staticmethod
    def get_by_id(tag_id: int):
        db = SessionLocal()
        try:
            repo = TagRepository(db)
            tag = repo.get_by_id(tag_id)
            if not tag:
                raise HTTPException(status_code=404, detail="Tag not found")
            return tag
        finally:
            db.close()
