from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from services.announcement import AnnouncementService
from schemas.announcement import AnnouncementResponse, AnnouncementCreate, AnnouncementUpdate

router = APIRouter(prefix="/announcements", tags=["announcements"])


@router.post("/", response_model=AnnouncementResponse, status_code=status.HTTP_201_CREATED)
def create_announcement(announcement_data: AnnouncementCreate, db: Session = Depends(get_db)):
    return AnnouncementService.create_announcement(announcement_data, db)


@router.delete("/{announcement_id}", status_code=status.HTTP_200_OK)
def delete_announcement(announcement_id: int, user_id: int, db: Session = Depends(get_db)):
    return AnnouncementService.delete_announcement(announcement_id, user_id, db)


@router.get("/{announcement_id}", response_model=AnnouncementResponse)
def get_announcement(announcement_id: int, db: Session = Depends(get_db)):
    return AnnouncementService.get_by_id(announcement_id, db)


@router.get("/", response_model=list[AnnouncementResponse])
def get_all_announcements(db: Session = Depends(get_db)):
    return AnnouncementService.get_all(db)


@router.put("/{}", response_model=AnnouncementResponse)
def update_announcement(announcement: AnnouncementUpdate, db: Session = Depends(get_db)):
    return AnnouncementService.update_announcement(announcement, db)
