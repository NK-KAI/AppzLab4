from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session

from db.database import SessionLocal, get_db
from db.repositories.announcement import AnnouncementRepository
from db.repositories.user import UserRepository
from schemas.announcement import AnnouncementUpdate, AnnouncementCreate


class AnnouncementService:
    @staticmethod
    def create_announcement(announcement_data: AnnouncementCreate, db: Session):
        repo = AnnouncementRepository(db)
        return repo.create(announcement_data)

    @staticmethod
    def delete_announcement(announcement_id: int, user_id: int, db: Session):
        ann_repo = AnnouncementRepository(db)
        announcement = ann_repo.get_by_id(announcement_id)
        if not announcement:
            raise HTTPException(status_code=404, detail="Announcement not found")
        if announcement.user_id != user_id:
            raise HTTPException(status_code=403, detail="You are not allowed to delete this announcement")
        return ann_repo.delete(announcement_id)

    @staticmethod
    def update_announcement(announcement: AnnouncementUpdate, db: Session):
        repo = AnnouncementRepository(db)
        announcement = repo.get_by_id(announcement.id)
        if not announcement:
            raise HTTPException(status_code=404, detail="Announcement not found")
        return repo.update(announcement)

    @staticmethod
    def get_by_id(announcement_id: int, db: Session):
        repo = AnnouncementRepository(db)
        announcement = repo.get_by_id(announcement_id)
        if not announcement:
            raise HTTPException(status_code=404, detail="Announcement not found")
        return announcement

    @staticmethod
    def get_all(db: Session):
        repo = AnnouncementRepository(db)
        announcements = repo.get_all()
        if not announcements:
            raise HTTPException(status_code=404, detail="Announcements not found")
        return announcements
