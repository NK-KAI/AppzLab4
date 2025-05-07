from fastapi import APIRouter, HTTPException, status
from services.announcement import AnnouncementService
from schemas.announcement import AnnouncementResponse, AnnouncementCreate, AnnouncementUpdate

router = APIRouter(prefix="/announcements", tags=["announcements"])


@router.post("/", response_model=AnnouncementResponse, status_code=status.HTTP_201_CREATED)
def create_announcement(announcement_data: AnnouncementCreate):
    return AnnouncementService.create_announcement(announcement_data)


@router.delete("/{announcement_id}", response_model=AnnouncementResponse)
def delete_announcement(announcement_id: int):
    return AnnouncementService.delete_announcement(announcement_id)


@router.get("/{announcement_id}", response_model=AnnouncementResponse)
def get_announcement(announcement_id: int):
    return AnnouncementService.get_by_id(announcement_id)


@router.put("/{}", response_model=AnnouncementResponse)
def update_announcement(announcement: AnnouncementUpdate):
    return AnnouncementService.update_announcement(announcement)
