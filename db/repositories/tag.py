from typing import List, Type

from sqlalchemy.orm import Session
from db.models import Tag
from schemas.tag import TagUpdate, TagCreate


class TagRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, tag_id: int) -> Tag:
        return self.db.query(Tag).filter(Tag.id == tag_id).first()

    def get_all(self) -> list[Type[Tag]]:
        return self.db.query(Tag).all()

    def create(self, tag_data: TagCreate) -> Tag:
        tag = Tag(name=tag_data.name)
        self.db.add(tag)
        self.db.commit()
        self.db.refresh(tag)
        return tag

    def delete(self, tag_id: int) -> None:
        self.db.query(Tag).filter_by(id=tag_id).delete()
        self.db.commit()

    def update(self, tag_new: Tag) -> Tag:
        self.db.query(Tag).filter_by(id=tag_new.id).update({'name': tag_new.name})
        self.db.commit()
        return tag_new
