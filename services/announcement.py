from fastapi import HTTPException

from db.database import SessionLocal
from db.repositories.announcement import AnnouncementRepository
from schemas.announcement import AnnouncementUpdate, AnnouncementCreate


class AnnouncementService:
    @staticmethod
    def create_announcement(announcement_data: AnnouncementCreate):
        db = SessionLocal()
        try:
            repo = AnnouncementRepository(db)
            return repo.create(announcement_data)
        finally:
            db.close()

    @staticmethod
    def delete_announcement(announcement_id: int):
        db = SessionLocal()
        try:
            repo = AnnouncementRepository(db)
            announcement = repo.get_by_id(announcement_id)
            if not announcement:
                raise HTTPException(status_code=404, detail="Announcement not found")
            return repo.delete(announcement_id)
        finally:
            db.close()

    @staticmethod
    def update_announcement(announcement: AnnouncementUpdate):
        db = SessionLocal()
        try:
            repo = AnnouncementRepository(db)
            announcement = repo.get_by_id(AnnouncementUpdate.id)
            if not announcement:
                raise HTTPException(status_code=404, detail="Announcement not found")
            return repo.update(announcement)
        finally:
            db.close()

    @staticmethod
    def get_by_id(announcement_id: int):
        db = SessionLocal()
        try:
            repo = AnnouncementRepository(db)
            announcement = repo.get_by_id(announcement_id)
            if not announcement:
                raise HTTPException(status_code=404, detail="Announcement not found")
            return announcement
        finally:
            db.close()

    @staticmethod
    def get_all():
        db = SessionLocal()
        try:
            repo = AnnouncementRepository(db)
            announcements = repo.get_all()
            if not announcements:
                raise HTTPException(status_code=404, detail="Announcements not found")
            return announcements
        finally:
            db.close()