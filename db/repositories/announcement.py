from typing import List, Type

from sqlalchemy.orm import Session
from db.models import Announcement
from schemas.announcement import AnnouncementUpdate, AnnouncementCreate


class AnnouncementRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, announcement_id: int) -> Announcement:
        return self.db.query(Announcement).filter(Announcement.id == announcement_id).first()

    def get_all(self) -> list[Type[Announcement]]:
        return self.db.query(Announcement).all()

    def create(self, announcement_data: AnnouncementCreate) -> Announcement:
        announcement = Announcement(title=announcement_data.title,
                                    description=announcement_data.description,
                                    category_id=announcement_data.category_id,
                                    user_id=announcement_data.user_id
                                    )
        self.db.add(announcement)
        self.db.commit()
        self.db.refresh(announcement)
        return announcement

    def delete(self, announcement_id: int) -> None:
        self.db.query(Announcement).filter_by(id=announcement_id).delete()
        self.db.commit()
        return None

    def update(self, announcement_new: Announcement) -> Announcement:
        self.db.query(Announcement).filter(id=announcement_new.id).update(announcement_new.__dict__)
        self.db.commit()
        return announcement_new
