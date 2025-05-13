from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Mapped, relationship, mapped_column

from db.database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from db.models import Announcement


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    password: Mapped[str] = mapped_column()

    announcements: Mapped[list["Announcement"]] = relationship(back_populates="user", lazy='subquery')
