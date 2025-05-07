from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Mapped,relationship

from db.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from db.models import Announcement


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    announcements: Mapped[list["Announcement"]] = relationship(back_populates="user", lazy='subquery')
