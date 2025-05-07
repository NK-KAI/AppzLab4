from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db.database import Base
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from db.models import Announcement, Subcategory


class Category(Base):
    __tablename__ = 'categories'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    subcategories: Mapped[Optional[list["Subcategory"]]] = relationship(back_populates='category', lazy='subquery')
    announcements: Mapped[Optional[list["Announcement"]]] = relationship(back_populates='category', lazy='subquery')
